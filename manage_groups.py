#!/usr/bin/env python3
"""
Florida Keys Facebook Groups - master database manager.

Single source of truth: data/groups.json
Everything else (README.md, ROUTING.md, exports/groups.csv) is GENERATED. Never hand-edit those.

Usage:
  python3 manage_groups.py generate            # rebuild README.md, ROUTING.md, exports/groups.csv
  python3 manage_groups.py validate            # sanity-check the master
  python3 manage_groups.py list [--joined] [--region X] [--identity Y] [--tier N]
  python3 manage_groups.py route --type business --region islamorada [--max 8] [--joined-only]
  python3 manage_groups.py set <slug> field=value [field=value ...]   # e.g. promo_policy=designated_days
  python3 manage_groups.py join-list           # groups worth joining, ranked by reach
"""
import csv, json, os, sys, datetime

MASTER = "data/groups.json"
README = "README.md"
ROUTING = "ROUTING.md"
CSV_OUT = "exports/groups.csv"
ACCOUNT = "dan_heart"

# --- helpers ---------------------------------------------------------------

def load():
    with open(MASTER, encoding="utf-8") as f:
        return json.load(f)

def save(d):
    d["version"] = datetime.date.today().isoformat()
    with open(MASTER, "w", encoding="utf-8") as f:
        json.dump(d, f, indent=2, ensure_ascii=False)

def esc(s):
    """Escape pipes so group names never break markdown tables."""
    return str(s).replace("|", "\\|")

def fmt_members(m):
    return f"{m:,}" if isinstance(m, int) else "unknown"

def joined(g):
    return g["membership"].get(ACCOUNT) == "joined"

def sort_key(g):
    return (g["tier"], -(g["members"] or 0))

# --- routing ---------------------------------------------------------------

# post type -> identities that fit, in priority order
POST_TYPES = {
    "business":      ["business_board", "community_hub"],
    "event":         ["events_board", "community_hub", "tourism_recreation"],
    "food_drink":    ["food_drink", "events_board", "community_hub"],
    "fishing":       ["fishing_marine", "tourism_recreation", "community_hub"],
    "boating":       ["fishing_marine", "tourism_recreation", "community_hub"],
    "boat_sale":     ["marketplace", "fishing_marine"],
    "vacation":      ["tourism_recreation", "housing_board", "events_board"],
    "tourism":       ["tourism_recreation", "events_board", "community_hub"],
    "jobs":          ["jobs_board"],
    "housing":       ["housing_board"],
    "product_deal":  ["marketplace", "business_board"],
    "environment":   ["environment_water", "community_cause", "fishing_marine"],
    "history":       ["history_culture", "community_hub"],
    "family_youth":  ["family_youth", "community_hub"],
    "community":     ["community_hub", "community_cause"],
}

# region -> regions that also apply (a post for Islamorada also fits upper_keys and keys_wide)
REGION_EXPANSION = {
    "keys_wide": ["keys_wide"],
    "upper_keys": ["upper_keys", "keys_wide"],
    "key_largo_tavernier": ["key_largo_tavernier", "upper_keys", "keys_wide"],
    "islamorada": ["islamorada", "upper_keys", "keys_wide"],
    "marathon_middle_keys": ["marathon_middle_keys", "keys_wide"],
    "lower_keys_key_west": ["lower_keys_key_west", "keys_wide"],
    # Miami is its own section: Keys posts never spill into Miami groups, and
    # Miami posts never spill into Keys locals groups.
    "miami": ["miami", "south_florida"],
    "south_florida": ["south_florida", "miami"],
    "statewide": ["statewide", "keys_wide"],
}

def route(d, post_type, region, max_groups=8, joined_only=False):
    idents = POST_TYPES[post_type]
    regions = REGION_EXPANSION[region]
    picks = []
    for g in d["groups"]:
        if g["identity"] not in idents or g["region"] not in regions:
            continue
        if g["promo_policy"] in ("no_promo", "community_only") and post_type in ("business", "product_deal"):
            continue
        if joined_only and not joined(g):
            continue
        # rank: tier first (reach), then identity fit, then region specificity, then raw size
        score = (g["tier"], idents.index(g["identity"]), regions.index(g["region"]), -(g["members"] or 0))
        picks.append((score, g))
    picks.sort(key=lambda x: x[0])
    chosen = [g for _, g in picks[:max_groups]]
    return chosen, [g for _, g in picks[max_groups:]]

def print_route(d, chosen, skipped, post_type, region):
    print(f"\nROUTE  type={post_type}  region={region}\n")
    print("Post in this order, 10-15 min apart:")
    t = datetime.datetime.now().replace(second=0, microsecond=0)
    for i, g in enumerate(chosen, 1):
        flag = "" if joined(g) else "  [NOT JOINED - join first]"
        priv = "" if g["privacy"] == "public" else "  [private]"
        when = (t + datetime.timedelta(minutes=12*(i-1))).strftime('%I:%M %p')
        print(f"  {i}. {when}  {g['name']}  ({fmt_members(g['members'])}, T{g['tier']}, {g['identity']}){priv}{flag}")
        print(f"       {g['url']}")
    if skipped:
        print("\nAlso fits, skipped for volume:")
        for g in skipped[:6]:
            print(f"  - {g['name']} ({fmt_members(g['members'])})")
    print("\nCopy notes: change the first sentence per bucket - community hubs get a local-news opener,"
          " business boards get the offer up front, niche groups get the niche hook.\n")

# --- generators ------------------------------------------------------------

def gen_readme(d):
    gs = d["groups"]
    total = sum(g["members"] or 0 for g in gs)
    j = [g for g in gs if joined(g)]
    md = []
    md.append("# 🌴 Florida Keys Facebook Groups Database")
    md.append("")
    md.append("a.i. STaRR's go-to database of real, verified Florida Keys Facebook groups, used to route and post client, a.i. STaRR, and FitKidz USA content quickly and safely.")
    md.append("")
    md.append("**Single source of truth:** `data/groups.json`. This README, `ROUTING.md`, and `exports/groups.csv` are generated - run `python3 manage_groups.py generate` after any edit.")
    md.append("")
    md.append("## 📊 At a glance")
    md.append("")
    md.append(f"- **Last verified on Facebook:** {d['version']}")
    md.append(f"- **Groups in database:** {len(gs)} ({sum(1 for g in gs if g['verification_status']=='verified')} verified, {sum(1 for g in gs if g['verification_status']=='candidate')} candidates to confirm)")
    md.append(f"- **Combined reach:** {total:,} members")
    md.append(f"- **Joined by Dan Heart:** {len(j)} groups / {sum(g['members'] or 0 for g in j):,} members")
    md.append(f"- **Legacy names that turned out not to exist:** {len(d['legacy_entries_not_found'])} (see bottom)")
    md.append("")
    md.append("### Reach by region")
    md.append("")
    md.append("| Region | Groups | Members | Joined |")
    md.append("| :--- | :---: | :---: | :---: |")
    for rk, rl in d["regions"].items():
        rg = [g for g in gs if g["region"] == rk]
        if not rg: continue
        md.append(f"| **{esc(rl)}** | {len(rg)} | {sum(g['members'] or 0 for g in rg):,} | {sum(1 for g in rg if joined(g))} |")
    md.append("")
    md.append("### Reach by identity")
    md.append("")
    md.append("| Identity | Groups | Members | What it's for |")
    md.append("| :--- | :---: | :---: | :--- |")
    for ik, il in d["identities"].items():
        ig = [g for g in gs if g["identity"] == ik]
        if not ig: continue
        md.append(f"| `{ik}` | {len(ig)} | {sum(g['members'] or 0 for g in ig):,} | {esc(il)} |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 📂 Groups by region")
    md.append("")
    md.append("Tier 1 = post first for reach. Tier 2 = town or niche match. Tier 3 = only when the content fits exactly. ✅ = Dan Heart is a member. 🔒 = private group. ⚠️ = candidate match, confirm before relying on it.")
    md.append("")
    for rk, rl in d["regions"].items():
        rg = sorted([g for g in gs if g["region"] == rk], key=sort_key)
        if not rg: continue
        md.append(f"### {rl}")
        md.append("")
        md.append("| Group | Members | Identity | Tier | Status | Link |")
        md.append("| :--- | :---: | :--- | :---: | :---: | :---: |")
        for g in rg:
            flags = ("✅" if joined(g) else "") + ("🔒" if g["privacy"] == "private" else "") + ("⚠️" if g["verification_status"] == "candidate" else "")
            md.append(f"| {esc(g['name'])} | {fmt_members(g['members'])} | `{g['identity']}` | {g['tier']} | {flags or '—'} | [Open ↗]({g['url']}) |")
        md.append("")
    md.append("---")
    md.append("")
    md.append("## 🧼 Posting rules")
    md.append("")
    pr = d["posting_rules"]
    md.append(f"- Normal post: {pr['normal_post_group_count']} groups. Strong Keys-wide announcement: {pr['keys_wide_post_group_count']}.")
    md.append(f"- Stagger {pr['stagger_minutes']} minutes apart; change the first sentence per group bucket; no identical link-only posts.")
    md.append(f"- Same client in the same group no more than once every {pr['max_posts_per_client_per_group_per_days']} days.")
    md.append("- Never post to a group we haven't joined, a group whose rules forbid promos, or a marketplace/yard-sale board unless it's a product offer.")
    md.append("- Read each group's rules before the first post there and record `promo_policy`, `allowed_post_days`, and `admin_post_approval` in the master.")
    md.append("- Automation: every group starts in `assist` mode (agent drafts, human approves). After 5 clean posts with no admin pushback it can be switched to `autopilot`.")
    md.append("")
    md.append("## ⚙️ How to use")
    md.append("")
    md.append("```bash")
    md.append("python3 manage_groups.py route --type business --region islamorada     # posting plan for a post")
    md.append("python3 manage_groups.py list --joined                                 # what we can post to today")
    md.append("python3 manage_groups.py join-list                                     # highest-reach groups to join next")
    md.append("python3 manage_groups.py set whats-up-florida-keys promo_policy=designated_days allowed_post_days=Tue")
    md.append("python3 manage_groups.py generate                                      # rebuild README / ROUTING / CSV")
    md.append("```")
    md.append("")
    md.append("Post types for `route`: " + ", ".join(f"`{k}`" for k in POST_TYPES) + ".")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 🗑️ Legacy names not found on Facebook")
    md.append("")
    md.append("The July 2026 list contained these names. On " + d["version"] + " none could be found as a Facebook group by that name, and several carried member counts that were far off. They are kept here so nobody re-adds them without verifying first.")
    md.append("")
    md.append("| Legacy name | Note |")
    md.append("| :--- | :--- |")
    for e in d["legacy_entries_not_found"]:
        md.append(f"| {esc(e['legacy_name'])} | {esc(e['note'])} |")
    md.append("")
    with open(README, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

def gen_routing(d):
    md = ["# Routing Guide", "",
          "Generated from `data/groups.json`. Route by post type first, then narrow by region. Groups marked ✅ are ones Dan Heart has joined and can post to today.", ""]
    for pt, idents in POST_TYPES.items():
        md.append(f"## `{pt}`")
        md.append("")
        md.append("Identities used, in priority order: " + ", ".join(f"`{i}`" for i in idents))
        md.append("")
        for rk, rl in d["regions"].items():
            rg = sorted([g for g in d["groups"] if g["region"] == rk and g["identity"] in idents], key=sort_key)
            if not rg: continue
            md.append(f"**{rl}:** " + "; ".join(
                f"{'✅ ' if joined(g) else ''}{esc(g['name'])} ({fmt_members(g['members'])}{', 🔒' if g['privacy']=='private' else ''})" for g in rg))
            md.append("")
    md.append("## Posting order template")
    md.append("")
    md.append("```text")
    md.append("Primary groups:   (tier 1 matches in the post's own region, then keys-wide tier 1)")
    md.append("Secondary groups: (tier 2 matches)")
    md.append("Skip:             (identity doesn't fit, not joined, or posted for this client < 7 days ago)")
    md.append("Posting order:    1... 2... 3...  (10-15 min apart)")
    md.append("Copy notes:       opener for locals / opener for business boards / opener for niche groups")
    md.append("```")
    md.append("")
    with open(ROUTING, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

def gen_csv(d):
    os.makedirs(os.path.dirname(CSV_OUT), exist_ok=True)
    cols = ["slug","name","fb_id","url","region","identity","tier","privacy","members","members_verified_on",
            "verification_status","joined_dan_heart","has_group_rules","promo_policy","allowed_post_days",
            "admin_post_approval","automation_mode","clean_posts","last_posted","notes"]
    with open(CSV_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f); w.writerow(cols)
        for g in sorted(d["groups"], key=lambda g: (g["region"], g["tier"], -(g["members"] or 0))):
            w.writerow([g["slug"], g["name"], g["fb_id"], g["url"], g["region"], g["identity"], g["tier"], g["privacy"],
                        g["members"] if g["members"] is not None else "", g["members_verified_on"] or "",
                        g["verification_status"], "yes" if joined(g) else "no",
                        "" if g["has_group_rules"] is None else ("yes" if g["has_group_rules"] else "no"),
                        g["promo_policy"], "|".join(g["allowed_post_days"]), g["admin_post_approval"],
                        g["automation_mode"], g["clean_posts"], g["last_posted"] or "", g["notes"]])

def validate(d):
    errs = []
    slugs = set(); ids = set()
    for g in d["groups"]:
        if g["slug"] in slugs: errs.append(f"duplicate slug {g['slug']}")
        if g["fb_id"] in ids: errs.append(f"duplicate fb_id {g['fb_id']} ({g['name']})")
        slugs.add(g["slug"]); ids.add(g["fb_id"])
        if g["region"] not in d["regions"]: errs.append(f"{g['slug']}: bad region {g['region']}")
        if g["identity"] not in d["identities"]: errs.append(f"{g['slug']}: bad identity {g['identity']}")
        if g["tier"] not in (1,2,3): errs.append(f"{g['slug']}: bad tier")
        if g["privacy"] not in ("public","private"): errs.append(f"{g['slug']}: bad privacy")
        if not g["url"].startswith("https://www.facebook.com/groups/"): errs.append(f"{g['slug']}: bad url")
    for e in errs: print("ERROR:", e)
    print(f"{len(d['groups'])} groups, {len(errs)} errors")
    return not errs

# --- CLI -------------------------------------------------------------------

def main(argv):
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__); return
    cmd, args = argv[0], argv[1:]
    d = load()
    if cmd == "generate":
        if not validate(d): sys.exit(1)
        gen_readme(d); gen_routing(d); gen_csv(d)
        print(f"generated {README}, {ROUTING}, {CSV_OUT}")
    elif cmd == "validate":
        sys.exit(0 if validate(d) else 1)
    elif cmd == "list":
        gs = d["groups"]
        if "--joined" in args: gs = [g for g in gs if joined(g)]
        for flag in ("--region", "--identity", "--tier"):
            if flag in args:
                v = args[args.index(flag)+1]
                gs = [g for g in gs if str(g[flag[2:]]) == v]
        for g in sorted(gs, key=sort_key):
            print(f"{'✅' if joined(g) else '  '} T{g['tier']} {fmt_members(g['members']):>9}  {g['region']:<22} {g['identity']:<20} {g['name']}")
        print(f"\n{len(gs)} groups")
    elif cmd == "route":
        pt = args[args.index("--type")+1]; rg = args[args.index("--region")+1]
        mx = int(args[args.index("--max")+1]) if "--max" in args else 8
        chosen, skipped = route(d, pt, rg, mx, "--joined-only" in args)
        print_route(d, chosen, skipped, pt, rg)
    elif cmd == "set":
        slug = args[0]
        g = next((g for g in d["groups"] if g["slug"] == slug), None)
        if not g: print("no such slug"); sys.exit(1)
        for kv in args[1:]:
            k, v = kv.split("=", 1)
            if k == "allowed_post_days": g[k] = [x for x in v.split(",") if x]
            elif k in ("members","clean_posts","tier"): g[k] = int(v)
            elif k == "joined": g["membership"][ACCOUNT] = "joined" if v.lower() in ("yes","true","1") else "not_joined"
            else: g[k] = v
        save(d); gen_readme(d); gen_routing(d); gen_csv(d)
        print(f"updated {slug} and regenerated docs")
    elif cmd == "join-list":
        gs = sorted([g for g in d["groups"] if not joined(g)], key=lambda g: -(g["members"] or 0))
        print("Highest-reach groups we have NOT joined yet:\n")
        for g in gs[:25]:
            print(f"  {fmt_members(g['members']):>9}  {'🔒' if g['privacy']=='private' else '  '} {g['name']:<60} {g['url']}")
    else:
        print(__doc__); sys.exit(1)

if __name__ == "__main__":
    main(sys.argv[1:])
