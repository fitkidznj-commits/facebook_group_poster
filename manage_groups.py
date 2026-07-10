#!/usr/bin/env python3
import json
import os
import urllib.parse

JSON_PATH = "group_research/florida_keys_facebook_subgroups.json"
README_PATH = "README.md"

def load_data():
    if not os.path.exists(JSON_PATH):
        print(f"Error: JSON file not found at {JSON_PATH}")
        return None
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading JSON: {e}")
        return None

def save_data(data):
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.dirname(JSON_PATH), exist_ok=True)
        with open(JSON_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Database successfully updated.")
        return True
    except Exception as e:
        print(f"Error saving JSON: {e}")
        return False

def generate_readme(data):
    if not data:
        return

    # Calculate statistics
    total_groups = 0
    total_members = 0
    subgroup_stats = []

    for key, subgroup in data.get("subgroups", {}).items():
        groups = subgroup.get("groups", [])
        g_count = len(groups)
        total_groups += g_count
        
        m_count = 0
        for g in groups:
            members = g.get("members")
            if members is not None:
                m_count += members
        total_members += m_count
        subgroup_stats.append({
            "label": subgroup.get("label", key),
            "key": key,
            "count": g_count,
            "members": m_count
        })

    # Start writing Markdown
    md = []
    md.append("# 🌴 Florida Keys Facebook Subgroups Database")
    md.append("")
    md.append("This repository contains a curated collection of Facebook groups relevant to the Florida Keys. It is structured to help coordinate targeted local marketing, announcements, and research campaigns.")
    md.append("")
    md.append("## 📊 Database Statistics")
    md.append("")
    md.append(f"- **Owner:** {data.get('owner', 'N/A')}")
    md.append(f"- **Source:** [{data.get('source', 'N/A')}]({data.get('source', '')})")
    md.append(f"- **Last Captured/Updated:** {data.get('captured', 'N/A')}")
    md.append(f"- **Total Facebook Groups:** {total_groups}")
    md.append(f"- **Total Tracked Members:** {total_members:,} (excluding groups with unknown counts)")
    md.append("")
    md.append("### Reach by Subgroup")
    md.append("")
    md.append("| Region / Category | Groups | Tracked Members |")
    md.append("| :--- | :---: | :---: |")
    for stat in subgroup_stats:
        md.append(f"| **{stat['label']}** | {stat['count']} | {stat['members']:,} |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 📂 Subgroups Directory")
    md.append("")
    md.append("> [!TIP]")
    md.append("> Clicking on any group name below will perform a direct search for that group on Facebook, letting you find it instantly.")
    md.append("")

    # Output details of each subgroup
    for key, subgroup in data.get("subgroups", {}).items():
        md.append(f"### {subgroup.get('label', key)}")
        md.append("")
        md.append("| Group Name | Members | Niche Tag | Tier | Link |")
        md.append("| :--- | :---: | :---: | :---: | :---: |")
        
        groups = subgroup.get("groups", [])
        # Sort groups by tier then members descending
        sorted_groups = sorted(
            groups, 
            key=lambda x: (x.get("tier", 3), -(x.get("members") or 0))
        )
        
        for g in sorted_groups:
            name = g.get("name", "")
            members_val = g.get("members")
            members_str = f"{members_val:,}" if members_val is not None else "*Unknown*"
            tag = g.get("tag", "N/A")
            tier = g.get("tier", 3)
            
            # Create search link
            quoted_name = urllib.parse.quote(name)
            fb_link = f"https://www.facebook.com/groups/search/groups/?q={quoted_name}"
            
            md.append(f"| {name} | {members_str} | `{tag}` | Tier {tier} | [Find on FB ↗]({fb_link}) |")
        md.append("")

    # Posting rules
    md.append("---")
    md.append("")
    md.append("## 🧼 Posting Hygiene & Rules")
    md.append("")
    posting_notes = data.get("posting_notes", {})
    md.append(f"- **Tier 1:** {posting_notes.get('tier_1', '')}")
    md.append(f"- **Tier 2:** {posting_notes.get('tier_2', '')}")
    md.append(f"- **Tier 3:** {posting_notes.get('tier_3', '')}")
    md.append(f"- **Hygiene Guideline:** {posting_notes.get('hygiene', '')}")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## ⚙️ How to Manage Groups")
    md.append("")
    md.append("To add new groups or update existing records, use the included CLI management tool:")
    md.append("```bash")
    md.append("python3 manage_groups.py")
    md.append("```")
    md.append("This interactive script will update the [JSON file](group_research/florida_keys_facebook_subgroups.json) and automatically regenerate this `README.md` with sorted tables and clickable links.")

    try:
        with open(README_PATH, "w", encoding="utf-8") as f:
            f.write("\n".join(md) + "\n")
        print("README.md successfully generated.")
    except Exception as e:
        print(f"Error writing README: {e}")

def main():
    print("==================================================")
    print("🌴 Florida Keys Facebook Subgroups Manager 🌴")
    print("==================================================")
    
    data = load_data()
    if not data:
        return

    while True:
        print("\nMenu:")
        print("1. List subgroups and group counts")
        print("2. Add a new Facebook group")
        print("3. Regenerate README.md")
        print("4. Exit")
        
        choice = input("\nChoose an option (1-4): ").strip()
        
        if choice == "1":
            subgroups = data.get("subgroups", {})
            for key, sg in subgroups.items():
                print(f" - [{key}] {sg.get('label')}: {len(sg.get('groups', []))} groups")
        
        elif choice == "2":
            subgroups = data.get("subgroups", {})
            keys_list = list(subgroups.keys())
            
            print("\nSelect a region/subgroup:")
            for i, key in enumerate(keys_list):
                print(f"{i + 1}. {subgroups[key].get('label')} ({key})")
            
            try:
                sg_idx = int(input(f"Select region (1-{len(keys_list)}): ").strip()) - 1
                if sg_idx < 0 or sg_idx >= len(keys_list):
                    print("Invalid selection.")
                    continue
                selected_key = keys_list[sg_idx]
            except ValueError:
                print("Invalid input.")
                continue
                
            name = input("Enter Facebook Group Name: ").strip()
            if not name:
                print("Group name cannot be empty.")
                continue
                
            members_input = input("Enter Member Count (leave blank for Unknown): ").strip()
            if members_input == "":
                members = None
            else:
                try:
                    members = int(members_input)
                except ValueError:
                    print("Invalid member count. Group not added.")
                    continue
                    
            tag = input("Enter Niche Tag (e.g. community, fishing, business): ").strip() or "community"
            
            try:
                tier_input = input("Enter Tier (1, 2, or 3): ").strip()
                tier = int(tier_input) if tier_input in ("1", "2", "3") else 3
            except ValueError:
                tier = 3
                
            new_group = {
                "name": name,
                "members": members,
                "tag": tag,
                "tier": tier
            }
            
            # Add to subgroups
            data["subgroups"][selected_key]["groups"].append(new_group)
            
            # Save data and generate readme
            if save_data(data):
                generate_readme(data)
                
        elif choice == "3":
            generate_readme(data)
            
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-4.")

if __name__ == "__main__":
    import sys
    # If run with a "--generate-only" flag, just rebuild the README and exit
    if len(sys.argv) > 1 and sys.argv[1] == "--generate-only":
        data = load_data()
        if data:
            generate_readme(data)
    else:
        main()
