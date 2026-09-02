#!/usr/bin/env python3
"""One-time builder: creates data/groups.json (the master) from the Sept 2, 2026
Facebook verification pass. Safe to delete after the master exists; kept for audit."""
import json, datetime

TODAY = "2026-09-02"
J = "joined"; N = "not_joined"; U = "unknown"

# slug, name, fb_id, region, identity, tier, privacy, members, membership(dan_heart), has_rules, status, notes
# status: verified (ID confirmed on Facebook) | candidate (best real match for a legacy name, confirm before posting)
G = [
 # ---------- KEYS-WIDE ----------
 ("whats-up-florida-keys","What's Up Florida Keys? LOCALS ONLY","KeysGossip","keys_wide","community_hub",1,"public",38700,J,True,"verified","Main Keys-wide locals hub. Legacy DB said 52K."),
 ("fk-local-business-ads","Florida Keys Local Business information and advertising","211495939188593","keys_wide","business_board",1,"public",9600,J,True,"verified","Promo posts welcome by design."),
 ("keep-it-local-fk","Keep It Local Florida Keys","1514283075319977","keys_wide","business_board",1,"public",7600,J,False,"verified",""),
 ("fk-locals-only","Florida Keys - Locals Only","1478183676350897","keys_wide","community_hub",2,"public",4900,J,True,"verified","Local-first; write like news, not an ad."),
 ("keys-life","Keys Life (a place to share)","1112742373974472","keys_wide","community_hub",2,"public",4000,J,True,"verified","Soft community posts only."),
 ("fk-locals-respectful-visitors","What's up Florida Keys? LOCALS and Respectful Visitors ONLY!","1138209453245216","keys_wide","community_hub",3,"public",1300,N,None,"verified",""),
 ("the-real-florida-keys","The Real Florida Keys","therealfloridakeys","keys_wide","community_hub",2,"public",3200,N,None,"verified",""),
 ("florida-keys-4k","FLORIDA KEYS","579572661430932","keys_wide","community_hub",3,"public",4000,N,None,"verified",""),
 ("fl-keys-roll-call","Fl Keys ROLL CALL","2051579451744842","keys_wide","community_hub",3,"public",2800,N,None,"verified",""),
 ("keylife","KeyLife","1736804119872023","keys_wide","community_hub",2,"private",11000,N,None,"verified","Private; join first."),
 ("florida-keys-news","Florida Keys News","1446771849773677","keys_wide","community_hub",3,"public",1200,N,None,"verified",""),
 ("amigos-of-fk","Amigos of Florida Keys","1217461423478219","keys_wide","community_hub",3,"public",22,J,False,"verified","Tiny."),
 ("keys-yard-sale","Keys Yard Sale (FL KEYS )","406989962701110","keys_wide","marketplace",2,"public",30000,N,None,"verified","Yard-sale board; product/retail offers only, no service ads."),
 ("fk-fishing","Florida Keys Fishing","2972971759613211","keys_wide","fishing_marine",3,"public",2000,N,None,"verified","Legacy DB said 137,800 — real count is 2K."),
 ("fk-fishing-forum","Florida Keys Fishing Forum","1120911431585040","keys_wide","fishing_marine",2,"public",8700,N,None,"verified","Larger than 'Florida Keys Fishing'."),
 ("fk-history","Florida Keys History","1362248743967131","keys_wide","history_culture",2,"public",8400,N,None,"candidate","Legacy name 'Florida Keys History with Brad Bertelli' not found; this is the real history group."),
 ("kw-fk-sargassum","Key West and Florida Keys - Sargassum Seaweed Daily Updates","316100958070809","keys_wide","environment_water",3,"public",3100,N,None,"candidate","Replaces legacy 'Florida Sargassum Reports + Daily News' (not found)."),
 ("fkec","The Florida Keys Environmental Coalition","FKEC.org","keys_wide","environment_water",3,"public",3500,N,None,"verified",""),
 ("pirates-saving-paradise","Pirates Saving Paradise Group","1084161769664023","keys_wide","community_cause",3,"public",429,N,None,"verified",""),
 ("fk-for-rent","Florida Keys FOR RENT","FloridaKeysForRent","keys_wide","housing_board",2,"public",11000,N,None,"candidate","Replaces legacy 'Upper Fl Keys Rentals' (not found)."),
 ("fk-vacation-rentals","Florida Keys Vacation Rentals","FloridaKeysVacationRentals","keys_wide","housing_board",3,"public",3600,N,None,"verified",""),
 ("fk-art-music","Florida Keys Art & Music","1001370882105457","keys_wide","events_board",2,"public",4000,N,None,"verified",""),
 ("fk-live-music-report","Florida Keys LIVE Music Report","959038414890708","keys_wide","events_board",3,"public",1900,N,None,"verified",""),
 ("fk-restaurants-guide","Florida Keys Restaurants & Dining Guide: Key West to Key Largo","keysbeat","keys_wide","food_drink",3,"public",956,N,None,"verified",""),
 ("keys-beer-events","Beer, Liquor, Events in the Keys","keysbeerevents","keys_wide","food_drink",3,"public",269,N,None,"candidate","Nearest real match to legacy 'Upper Keys Wine Beer & Food Events'."),
 ("lost-found-pets-fk","Lost and Found Pets Florida Keys","LostandFoundPetsFloridaKeys","keys_wide","community_cause",3,"public",17000,N,None,"verified","Pets only; not a promo venue."),
 ("keys-to-peace","Keys To Peace","146688231023","keys_wide","community_cause",3,"public",1100,J,True,"verified",""),
 ("jobs-in-monroe","Jobs in Monroe Florida - Hiring in Key West, Marathon & Key Largo","jobs.monroe","keys_wide","jobs_board",1,"public",15000,N,None,"verified","Best Keys-wide jobs board. Replaces legacy Marathon jobs group (not found)."),
 ("captains-mates-fl","Captains and Mates for hire in Florida","713556279640347","statewide","jobs_board",3,"public",21000,N,None,"verified","Marine jobs only."),
 # ---------- FAMILY / YOUTH (FitKidz) ----------
 ("florida-keys-moms","Florida Keys Moms","2758892740893461","keys_wide","family_youth",1,"private",798,N,True,"verified","Private. Top FitKidz target; request to join."),
 ("little-conchs-playgroup","Little Conchs aka Florida Keys Kids Playgroup","255153098270822","keys_wide","family_youth",2,"private",476,N,None,"verified","Private."),
 ("key-west-for-kids","Key West for Kids","577019075821418","lower_keys_key_west","family_youth",2,"public",2700,N,None,"verified",""),
 ("keyskids4life","KeysKids 4Life","1552938855026561","keys_wide","family_youth",3,"public",2000,N,None,"verified",""),
 ("fk-kw-family-fun","Florida Keys and Key West Family Fun","1012857710387060","keys_wide","family_youth",3,"public",390,N,None,"verified",""),
 ("upper-keys-flag-football","Upper Keys Flag Football League","851347746623201","upper_keys","family_youth",2,"public",490,N,None,"verified","Youth sports; FitKidz partner candidate."),
 ("key-west-home-schoolers","Key West Home Schoolers","150642021701659","lower_keys_key_west","family_youth",3,"private",360,N,None,"verified","Legacy 'South Dade and Upper Keys Homeschoolers' not found."),
 ("treasure-village-montessori-parents","Treasure Village Montessori Parents","350333557913158","islamorada","family_youth",3,"private",111,J,True,"verified","School parents group; community-only, no promo."),
 ("fl-youth-sports-forum","FLORIDA YOUTH SPORTS FORUM RELOAD","1115138580004138","statewide","family_youth",3,"public",14000,N,None,"verified","Statewide."),
 ("upcoming-fl-wrestling-events","UPCOMING FLORIDA WRESTLING EVENTS","120274904848453","statewide","family_youth",3,"public",None,J,None,"verified","Joined; wrestling network."),
 # ---------- UPPER KEYS: KEY LARGO / TAVERNIER ----------
 ("whats-happening-key-largo-islamorada","What's Happening in Key Largo/Islamorada (The Upper Florida Keys)","WhatsHappeningInKeyLargo","upper_keys","community_hub",1,"private",39900,J,True,"verified","THE Upper Keys hub. Private. Legacy called it 'Key Largo and Islamorada Happenings'."),
 ("i-love-key-largo","I LOVE Key Largo!","1431693918645912","key_largo_tavernier","community_hub",2,"public",1300,J,False,"verified","Legacy DB said 638."),
 ("key-largo-civic-club","Key Largo Civic Club","2464927900253435","key_largo_tavernier","community_cause",3,"public",645,J,True,"verified",""),
 ("key-largo-yard-sale","Key largo yard sale","934728987202638","key_largo_tavernier","marketplace",3,"public",10000,N,None,"verified","Retail/product only."),
 ("upper-fk-employers-jobs","Upper Florida Keys Employers & Job Seekers","3019302308186160","key_largo_tavernier","jobs_board",2,"public",5200,J,True,"verified",""),
 ("key-largo-tavernier-for-rent","Key Largo/Tavernier, FL. - Real Estate- For Rent","1777594715856755","key_largo_tavernier","housing_board",3,"public",2400,N,None,"verified",""),
 ("tavernier-fl","Tavernier Fl.","1630351238393664","key_largo_tavernier","community_hub",3,"public",24,N,None,"verified","Tiny."),
 ("tavernier-key-sandbar","Tavernier Key Sandbar","567378590935046","key_largo_tavernier","tourism_recreation",3,"public",282,N,None,"verified",""),
 # ---------- UPPER KEYS: ISLAMORADA ----------
 ("i-love-islamorada","I LOVE Islamorada!","5922334941156509","islamorada","community_hub",1,"public",23000,J,True,"verified","Biggest public Islamorada group. Legacy DB said 2,000."),
 ("good-morning-islamorada","GOOD MORNING ISLAMORADA","328732054396576","islamorada","community_hub",2,"public",3100,J,False,"verified",""),
 ("islamorada-florida-keys","Islamorada Florida Keys","1696415441661122","islamorada","community_hub",3,"public",398,J,False,"verified","Legacy 'Islamorada, FL Keys'."),
 ("islamorada-florida","Islamorada, Florida","1029209540037668","islamorada","community_hub",3,"public",225,N,None,"verified","Legacy DB said 132,600 — real count is 225."),
 ("islamorada","Islamorada","231972199955310","islamorada","community_hub",3,"public",1400,N,None,"verified",""),
 ("islamorada-travel-tips","Islamorada Travel Tips","802708672733292","islamorada","tourism_recreation",3,"public",1900,N,None,"verified","Visitor-facing."),
 ("islamorada-eats","Islamorada Eats, Drinks & More","578593814395855","islamorada","food_drink",1,"public",6200,N,None,"verified","Best Islamorada restaurant/bar group."),
 ("islamorada-sandbar","Islamorada Sandbar","227833241701015","islamorada","tourism_recreation",1,"private",75000,N,None,"candidate","Private, 75K. Likely the intended 'Experience the Islamorada Sandbar!'."),
 ("islamoradas-sandbar","ISLAMORADA'S SANDBAR","1943217599384743","islamorada","tourism_recreation",3,"public",2500,N,None,"verified",""),
 ("islamorada-sandbar-day-drinkers","Islamorada Sandbar Day Drinkers","453929826754427","islamorada","tourism_recreation",3,"public",833,N,None,"verified",""),
 ("islamorada-deals-clearance","Islamorada Florida Keys Deals & Clearance","4067378650251629","islamorada","marketplace",2,"private",55000,N,None,"verified","Private, 55K, 90+ posts/day. Deals/retail only."),
 ("islamorada-small-business-ads","Islamorada, Florida - Small Business Ads","567264623467617","islamorada","business_board",3,"public",196,N,None,"verified","Small but promo-friendly."),
 ("islamorada-fish-pics","Islamorada Fish Pics","317205428409587","islamorada","fishing_marine",3,"public",582,N,None,"verified",""),
 ("the-nott","The Nott","277344980442","islamorada","community_hub",3,"public",868,J,False,"verified",""),
 # ---------- MIDDLE KEYS: MARATHON / KCB ----------
 ("whats-happening-marathon","What's Happening in Marathon and the Florida Keys","2039906393440770","marathon_middle_keys","community_hub",1,"public",2900,J,False,"verified","Only joined Marathon hub."),
 ("marathon-fl-keys-fishing","Marathon FL Keys Fishing group","1142378252529069","marathon_middle_keys","fishing_marine",2,"private",10000,N,None,"verified","Private."),
 ("marathon-fishing-charters","Marathon FL Fishing, Top spots, Charters and Visitors","2086755288431404","marathon_middle_keys","fishing_marine",3,"public",2100,N,None,"verified",""),
 ("marathon-services","Marathon Services","243218266009965","marathon_middle_keys","business_board",2,"public",1400,N,None,"verified","Service-business board."),
 ("marathon-long-term-rentals","Marathon area Long Term rentals","MarathonRentals","marathon_middle_keys","housing_board",2,"public",16000,N,None,"verified",""),
 ("marathon-vacation-rentals","Marathon Area Vacation Rentals","marathonvacation","marathon_middle_keys","housing_board",3,"public",1600,N,None,"verified",""),
 ("key-colony-beach-florida","Key Colony Beach Florida","191851100255452","marathon_middle_keys","community_hub",2,"public",1800,N,None,"candidate","Legacy 'Key Colony Beach Facebook Group'."),
 # ---------- LOWER KEYS / KEY WEST ----------
 ("key-west-underground","Key West Underground","367803624102331","lower_keys_key_west","community_hub",1,"private",145000,N,None,"verified","Largest Keys group found (private). Strict rules expected."),
 ("key-west-fl-keys","Key West, FL Keys","774906927734780","lower_keys_key_west","community_hub",1,"public",13000,N,None,"verified",""),
 ("i-love-key-west-fl-keys","I LOVE KEY WEST & FL KEYS","1828426688002336","lower_keys_key_west","community_hub",2,"public",15000,N,None,"verified",""),
 ("key-west-anything","KEY WEST, FL - Anything About Key West Here.","keywest1","lower_keys_key_west","community_hub",2,"public",9600,N,None,"verified",""),
 ("key-west-info-events","Key West information and Events.","630139812570199","lower_keys_key_west","events_board",2,"public",8500,N,None,"verified",""),
 ("key-west-events-fun","Key West Events & fun things to do","1426994451571196","lower_keys_key_west","events_board",1,"public",12000,N,None,"verified",""),
 ("things-to-do-key-west","Things to do in Key West","168169300627004","lower_keys_key_west","tourism_recreation",3,"public",1900,N,None,"verified","Legacy 'THINGS TO DO IN KEY WEST'."),
 ("key-west-happy-hours","Key West Happy Hours & Then Some!","306189633673172","lower_keys_key_west","food_drink",2,"public",7600,N,None,"verified",""),
 ("everything-key-west","Everything Key West!","717013633700795","lower_keys_key_west","community_hub",3,"public",6200,N,None,"verified",""),
 ("whats-up-key-west","WHAT'S UP KEY WEST?","whatsupkeywest","lower_keys_key_west","community_hub",3,"public",5300,N,None,"verified",""),
 ("key-west-travel-tips","Key West, Florida Travel Tips","keywesttraveltips","lower_keys_key_west","tourism_recreation",3,"public",5100,N,None,"verified","Visitor-facing."),
 ("kw-lower-keys-businesses","Key West and Lower Keys Businesses","1004912736225389","lower_keys_key_west","business_board",2,"public",2700,N,None,"verified",""),
 ("kw-lower-keys-business-ads","Key West and Lower Keys Business Advertising","1544322812562257","lower_keys_key_west","business_board",2,"public",2500,N,None,"verified",""),
 ("key-west-fl-jobs","KEY WEST FL JOBS","1683105378655795","lower_keys_key_west","jobs_board",2,"private",27000,N,None,"verified","Private."),
 ("key-west-cribs","Key West Cribs 2.0","1048106905260864","lower_keys_key_west","housing_board",2,"public",25000,N,None,"verified",""),
 ("big-pine-key","Big Pine Key","142512893071964","lower_keys_key_west","community_hub",1,"private",26000,N,None,"candidate","Private. Legacy 'Big Pine, FL Keys'."),
 ("big-pine-key-florida","Big Pine Key , Florida","3076891382397940","lower_keys_key_west","community_hub",2,"private",4700,N,None,"verified","Private."),
 # ---------- STATEWIDE WITH KEYS RELEVANCE ----------
 ("offshore-fishing-club","Offshore Fishing Club","241811260099406","statewide","fishing_marine",2,"public",108000,N,None,"candidate","Replaces legacy 'Florida offshore fishing' (not found)."),
 ("fl-surf-saltwater-fishing","Florida's Surf/Saltwater Fishing Group","770865447400880","statewide","fishing_marine",2,"public",67000,N,None,"verified",""),
 ("all-things-lobstering","All Things Lobstering","387375017591261","statewide","fishing_marine",2,"public",15000,N,None,"candidate","Replaces legacy 'Florida Lobster Mini Season and Regular' (not found). Private sister group 1589283464618222 has 34K."),
 ("bully-netting-nation","Bully Netting and Lobstering Nation","345274400648814","statewide","fishing_marine",3,"public",8000,N,None,"verified",""),
]

# Legacy names that could not be found on Facebook on 2026-09-02
PHANTOM = [
 ("Florida Keys Events","No group by this name; use Florida Keys Art & Music, Key West Events & fun things to do, What's Happening in Key Largo/Islamorada"),
 ("Florida Keys Business Directory","Not found; use the two Keys-wide business boards"),
 ("Florida Keys Forever Home","Not found"),
 ("Upper Fl Keys Rentals","Not found; see Florida Keys FOR RENT / Key Largo-Tavernier For Rent"),
 ("South Dade and Upper Keys Homeschoolers","Not found; only Key West Home Schoolers exists"),
 ("Upper Keys Wine Beer & Food Events","Not found; nearest is Beer, Liquor, Events in the Keys (269)"),
 ("Florida Keys History with Brad Bertelli","Not found as a group (Brad Bertelli is a Page); use Florida Keys History"),
 ("Florida Sargassum Reports + Daily News","Not found; use Key West and Florida Keys Sargassum Daily Updates"),
 ("Key Largo, FL Keys","Not found. Legacy count 145,500 was wrong."),
 ("Key Largo Life","Not found"),
 ("Key Largo","Not found as a general community group"),
 ("Key Largo Running Club","Not found"),
 ("Experience the Islamorada Sandbar!","Not found by exact name; see Islamorada Sandbar (private, 75K)"),
 ("Florida Bay Forever","Nonprofit Page, not a group"),
 ("Marathon, FL Keys Past|Present|Future- (uncensored)","Not found. Legacy count 50,100 was wrong."),
 ("Marathon, FL Keys","Not found"),
 ("Marathon, Florida Area Jobs and career opportunites","Not found; use Jobs in Monroe Florida"),
 ("I LOVE Marathon!","Not verified (not searched this pass)"),
 ("Sea Base Trek Talk - Prep, News, Info","Not found (Philmont Trek Talk exists, 33K, not Keys)"),
 ("Florida Lobster Mini Season and Regular","Not found; use All Things Lobstering"),
 ("Florida offshore fishing","Not found by exact name; see Offshore Fishing Club (108K)"),
 ("Key Colony Beach Facebook Group","Not found by exact name; see Key Colony Beach Florida"),
]

REGIONS = {
 "keys_wide": "Keys-Wide (entire island chain)",
 "upper_keys": "Upper Keys (Key Largo through Islamorada)",
 "key_largo_tavernier": "Upper Keys - Key Largo & Tavernier",
 "islamorada": "Upper Keys - Islamorada",
 "marathon_middle_keys": "Middle Keys - Marathon & Key Colony Beach",
 "lower_keys_key_west": "Lower Keys - Big Pine to Key West",
 "statewide": "Statewide with Keys relevance",
}
IDENTITIES = {
 "community_hub": "Broad local discussion and announcements",
 "business_board": "Business advertising, local services, directories",
 "events_board": "Public events, happenings, live music",
 "food_drink": "Restaurants, bars, food and drink",
 "fishing_marine": "Fishing, boating, marina, lobster, seafood, charters",
 "tourism_recreation": "Visitor-facing things to do, sandbar, attractions",
 "jobs_board": "Hiring and job-seeker posts",
 "housing_board": "Rentals, home, and housing posts",
 "marketplace": "Yard sale / deals boards - products only",
 "environment_water": "Sargassum, Florida Bay, conservation, water quality",
 "history_culture": "History, heritage, old Keys stories",
 "family_youth": "Parents, kids, homeschool, youth sports (FitKidz)",
 "community_cause": "Causes, civic clubs, local improvement efforts",
}

groups = []
for slug,name,fbid,region,ident,tier,priv,members,membership,rules,status,notes in G:
    groups.append({
        "slug": slug,
        "name": name,
        "fb_id": fbid,
        "url": f"https://www.facebook.com/groups/{fbid}",
        "region": region,
        "identity": ident,
        "tier": tier,
        "privacy": priv,
        "members": members,
        "members_verified_on": TODAY if members is not None else None,
        "verification_status": status,
        "membership": {"dan_heart": membership},
        "has_group_rules": rules,
        "promo_policy": "unknown",
        "allowed_post_days": [],
        "admin_post_approval": "unknown",
        "automation_mode": "assist",
        "clean_posts": 0,
        "last_posted": None,
        "notes": notes,
    })

master = {
    "version": TODAY,
    "owner": "a.i. STaRR / Dan Heart (Coach)",
    "source": "Facebook group search + group About pages, captured via Chrome on " + TODAY,
    "poster_accounts": [
        {"key": "dan_heart", "label": "Dan Heart (personal profile)", "profile_url": "https://www.facebook.com/dan.heart.615367"}
    ],
    "regions": REGIONS,
    "identities": IDENTITIES,
    "field_guide": {
        "tier": "1 = post first for reach; 2 = town/niche match; 3 = only when content fits exactly",
        "verification_status": "verified = ID confirmed on Facebook; candidate = best real match for a legacy name, confirm before relying on it",
        "membership": "per poster account: joined | not_joined | pending | unknown",
        "promo_policy": "unknown | allowed | designated_days | no_promo | community_only  (fill from each group's rules)",
        "admin_post_approval": "unknown | yes | no",
        "automation_mode": "assist = agent drafts + human approves; autopilot = agent posts unattended (earned after 5 clean posts)",
    },
    "posting_rules": {
        "normal_post_group_count": "3-8",
        "keys_wide_post_group_count": "8-12",
        "stagger_minutes": "10-15",
        "max_posts_per_client_per_group_per_days": 7,
        "vary_first_sentence_per_group": True,
        "check_group_rules_before_first_post": True,
        "never_post_to": ["not_joined", "promo_policy=no_promo", "identity=marketplace unless product offer"],
    },
    "groups": groups,
    "legacy_entries_not_found": [{"legacy_name": n, "note": note} for n, note in PHANTOM],
}

with open("data/groups.json", "w", encoding="utf-8") as f:
    json.dump(master, f, indent=2, ensure_ascii=False)
print(f"wrote data/groups.json with {len(groups)} groups, {len(PHANTOM)} legacy names flagged")
