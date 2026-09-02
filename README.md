# 🌴 Florida Keys Facebook Groups Database

a.i. STaRR's go-to database of real, verified Florida Keys Facebook groups, used to route and post client, a.i. STaRR, and FitKidz USA content quickly and safely.

**Single source of truth:** `data/groups.json`. This README, `ROUTING.md`, and `exports/groups.csv` are generated - run `python3 manage_groups.py generate` after any edit.

## 📊 At a glance

- **Last verified on Facebook:** 2026-09-02
- **Groups in database:** 89 (80 verified, 9 candidates to confirm)
- **Combined reach:** 1,023,454 members
- **Joined by Dan Heart:** 18 groups / 143,344 members
- **Legacy names that turned out not to exist:** 22 (see bottom)

### Reach by region

| Region | Groups | Members | Joined |
| :--- | :---: | :---: | :---: |
| **Keys-Wide (entire island chain)** | 32 | 202,940 | 7 |
| **Upper Keys (Key Largo through Islamorada)** | 2 | 40,390 | 1 |
| **Upper Keys - Key Largo & Tavernier** | 7 | 19,851 | 3 |
| **Upper Keys - Islamorada** | 15 | 171,313 | 5 |
| **Middle Keys - Marathon & Key Colony Beach** | 7 | 35,800 | 1 |
| **Lower Keys - Big Pine to Key West** | 19 | 320,160 | 0 |
| **Statewide with Keys relevance** | 7 | 233,000 | 1 |

### Reach by identity

| Identity | Groups | Members | What it's for |
| :--- | :---: | :---: | :--- |
| `community_hub` | 29 | 370,837 | Broad local discussion and announcements |
| `business_board` | 6 | 23,996 | Business advertising, local services, directories |
| `events_board` | 4 | 26,400 | Public events, happenings, live music |
| `food_drink` | 4 | 15,025 | Restaurants, bars, food and drink |
| `fishing_marine` | 9 | 221,382 | Fishing, boating, marina, lobster, seafood, charters |
| `tourism_recreation` | 7 | 87,515 | Visitor-facing things to do, sandbar, attractions |
| `jobs_board` | 4 | 68,200 | Hiring and job-seeker posts |
| `housing_board` | 6 | 59,600 | Rentals, home, and housing posts |
| `marketplace` | 3 | 95,000 | Yard sale / deals boards - products only |
| `environment_water` | 2 | 6,600 | Sargassum, Florida Bay, conservation, water quality |
| `history_culture` | 1 | 8,400 | History, heritage, old Keys stories |
| `family_youth` | 10 | 21,325 | Parents, kids, homeschool, youth sports (FitKidz) |
| `community_cause` | 4 | 19,174 | Causes, civic clubs, local improvement efforts |

---

## 📂 Groups by region

Tier 1 = post first for reach. Tier 2 = town or niche match. Tier 3 = only when the content fits exactly. ✅ = Dan Heart is a member. 🔒 = private group. ⚠️ = candidate match, confirm before relying on it.

### Keys-Wide (entire island chain)

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| What's Up Florida Keys? LOCALS ONLY | 38,700 | `community_hub` | 1 | ✅ | [Open ↗](https://www.facebook.com/groups/KeysGossip) |
| Jobs in Monroe Florida - Hiring in Key West, Marathon & Key Largo | 15,000 | `jobs_board` | 1 | — | [Open ↗](https://www.facebook.com/groups/jobs.monroe) |
| Florida Keys Local Business information and advertising | 9,600 | `business_board` | 1 | ✅ | [Open ↗](https://www.facebook.com/groups/211495939188593) |
| Keep It Local Florida Keys | 7,600 | `business_board` | 1 | ✅ | [Open ↗](https://www.facebook.com/groups/1514283075319977) |
| Florida Keys Moms | 798 | `family_youth` | 1 | 🔒 | [Open ↗](https://www.facebook.com/groups/2758892740893461) |
| Keys Yard Sale (FL KEYS ) | 30,000 | `marketplace` | 2 | — | [Open ↗](https://www.facebook.com/groups/406989962701110) |
| KeyLife | 11,000 | `community_hub` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/1736804119872023) |
| Florida Keys FOR RENT | 11,000 | `housing_board` | 2 | ⚠️ | [Open ↗](https://www.facebook.com/groups/FloridaKeysForRent) |
| Florida Keys Fishing Forum | 8,700 | `fishing_marine` | 2 | — | [Open ↗](https://www.facebook.com/groups/1120911431585040) |
| Florida Keys History | 8,400 | `history_culture` | 2 | ⚠️ | [Open ↗](https://www.facebook.com/groups/1362248743967131) |
| Florida Keys - Locals Only | 4,900 | `community_hub` | 2 | ✅ | [Open ↗](https://www.facebook.com/groups/1478183676350897) |
| Keys Life (a place to share) | 4,000 | `community_hub` | 2 | ✅ | [Open ↗](https://www.facebook.com/groups/1112742373974472) |
| Florida Keys Art & Music | 4,000 | `events_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/1001370882105457) |
| The Real Florida Keys | 3,200 | `community_hub` | 2 | — | [Open ↗](https://www.facebook.com/groups/therealfloridakeys) |
| Little Conchs aka Florida Keys Kids Playgroup | 476 | `family_youth` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/255153098270822) |
| Lost and Found Pets Florida Keys | 17,000 | `community_cause` | 3 | — | [Open ↗](https://www.facebook.com/groups/LostandFoundPetsFloridaKeys) |
| FLORIDA KEYS | 4,000 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/579572661430932) |
| Florida Keys Vacation Rentals | 3,600 | `housing_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/FloridaKeysVacationRentals) |
| The Florida Keys Environmental Coalition | 3,500 | `environment_water` | 3 | — | [Open ↗](https://www.facebook.com/groups/FKEC.org) |
| Key West and Florida Keys - Sargassum Seaweed Daily Updates | 3,100 | `environment_water` | 3 | ⚠️ | [Open ↗](https://www.facebook.com/groups/316100958070809) |
| Fl Keys ROLL CALL | 2,800 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/2051579451744842) |
| Florida Keys Fishing | 2,000 | `fishing_marine` | 3 | — | [Open ↗](https://www.facebook.com/groups/2972971759613211) |
| KeysKids 4Life | 2,000 | `family_youth` | 3 | — | [Open ↗](https://www.facebook.com/groups/1552938855026561) |
| Florida Keys LIVE Music Report | 1,900 | `events_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/959038414890708) |
| What's up Florida Keys? LOCALS and Respectful Visitors ONLY! | 1,300 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/1138209453245216) |
| Florida Keys News | 1,200 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/1446771849773677) |
| Keys To Peace | 1,100 | `community_cause` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/146688231023) |
| Florida Keys Restaurants & Dining Guide: Key West to Key Largo | 956 | `food_drink` | 3 | — | [Open ↗](https://www.facebook.com/groups/keysbeat) |
| Pirates Saving Paradise Group | 429 | `community_cause` | 3 | — | [Open ↗](https://www.facebook.com/groups/1084161769664023) |
| Florida Keys and Key West Family Fun | 390 | `family_youth` | 3 | — | [Open ↗](https://www.facebook.com/groups/1012857710387060) |
| Beer, Liquor, Events in the Keys | 269 | `food_drink` | 3 | ⚠️ | [Open ↗](https://www.facebook.com/groups/keysbeerevents) |
| Amigos of Florida Keys | 22 | `community_hub` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/1217461423478219) |

### Upper Keys (Key Largo through Islamorada)

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| What's Happening in Key Largo/Islamorada (The Upper Florida Keys) | 39,900 | `community_hub` | 1 | ✅🔒 | [Open ↗](https://www.facebook.com/groups/WhatsHappeningInKeyLargo) |
| Upper Keys Flag Football League | 490 | `family_youth` | 2 | — | [Open ↗](https://www.facebook.com/groups/851347746623201) |

### Upper Keys - Key Largo & Tavernier

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Upper Florida Keys Employers & Job Seekers | 5,200 | `jobs_board` | 2 | ✅ | [Open ↗](https://www.facebook.com/groups/3019302308186160) |
| I LOVE Key Largo! | 1,300 | `community_hub` | 2 | ✅ | [Open ↗](https://www.facebook.com/groups/1431693918645912) |
| Key largo yard sale | 10,000 | `marketplace` | 3 | — | [Open ↗](https://www.facebook.com/groups/934728987202638) |
| Key Largo/Tavernier, FL. - Real Estate- For Rent | 2,400 | `housing_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/1777594715856755) |
| Key Largo Civic Club | 645 | `community_cause` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/2464927900253435) |
| Tavernier Key Sandbar | 282 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/567378590935046) |
| Tavernier Fl. | 24 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/1630351238393664) |

### Upper Keys - Islamorada

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Islamorada Sandbar | 75,000 | `tourism_recreation` | 1 | 🔒⚠️ | [Open ↗](https://www.facebook.com/groups/227833241701015) |
| I LOVE Islamorada! | 23,000 | `community_hub` | 1 | ✅ | [Open ↗](https://www.facebook.com/groups/5922334941156509) |
| Islamorada Eats, Drinks & More | 6,200 | `food_drink` | 1 | — | [Open ↗](https://www.facebook.com/groups/578593814395855) |
| Islamorada Florida Keys Deals & Clearance | 55,000 | `marketplace` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/4067378650251629) |
| GOOD MORNING ISLAMORADA | 3,100 | `community_hub` | 2 | ✅ | [Open ↗](https://www.facebook.com/groups/328732054396576) |
| ISLAMORADA'S SANDBAR | 2,500 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/1943217599384743) |
| Islamorada Travel Tips | 1,900 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/802708672733292) |
| Islamorada | 1,400 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/231972199955310) |
| The Nott | 868 | `community_hub` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/277344980442) |
| Islamorada Sandbar Day Drinkers | 833 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/453929826754427) |
| Islamorada Fish Pics | 582 | `fishing_marine` | 3 | — | [Open ↗](https://www.facebook.com/groups/317205428409587) |
| Islamorada Florida Keys | 398 | `community_hub` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/1696415441661122) |
| Islamorada, Florida | 225 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/1029209540037668) |
| Islamorada, Florida - Small Business Ads | 196 | `business_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/567264623467617) |
| Treasure Village Montessori Parents | 111 | `family_youth` | 3 | ✅🔒 | [Open ↗](https://www.facebook.com/groups/350333557913158) |

### Middle Keys - Marathon & Key Colony Beach

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| What's Happening in Marathon and the Florida Keys | 2,900 | `community_hub` | 1 | ✅ | [Open ↗](https://www.facebook.com/groups/2039906393440770) |
| Marathon area Long Term rentals | 16,000 | `housing_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/MarathonRentals) |
| Marathon FL Keys Fishing group | 10,000 | `fishing_marine` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/1142378252529069) |
| Key Colony Beach Florida | 1,800 | `community_hub` | 2 | ⚠️ | [Open ↗](https://www.facebook.com/groups/191851100255452) |
| Marathon Services | 1,400 | `business_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/243218266009965) |
| Marathon FL Fishing, Top spots, Charters and Visitors | 2,100 | `fishing_marine` | 3 | — | [Open ↗](https://www.facebook.com/groups/2086755288431404) |
| Marathon Area Vacation Rentals | 1,600 | `housing_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/marathonvacation) |

### Lower Keys - Big Pine to Key West

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Key West Underground | 145,000 | `community_hub` | 1 | 🔒 | [Open ↗](https://www.facebook.com/groups/367803624102331) |
| Big Pine Key | 26,000 | `community_hub` | 1 | 🔒⚠️ | [Open ↗](https://www.facebook.com/groups/142512893071964) |
| Key West, FL Keys | 13,000 | `community_hub` | 1 | — | [Open ↗](https://www.facebook.com/groups/774906927734780) |
| Key West Events & fun things to do | 12,000 | `events_board` | 1 | — | [Open ↗](https://www.facebook.com/groups/1426994451571196) |
| KEY WEST FL JOBS | 27,000 | `jobs_board` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/1683105378655795) |
| Key West Cribs 2.0 | 25,000 | `housing_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/1048106905260864) |
| I LOVE KEY WEST & FL KEYS | 15,000 | `community_hub` | 2 | — | [Open ↗](https://www.facebook.com/groups/1828426688002336) |
| KEY WEST, FL - Anything About Key West Here. | 9,600 | `community_hub` | 2 | — | [Open ↗](https://www.facebook.com/groups/keywest1) |
| Key West information and Events. | 8,500 | `events_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/630139812570199) |
| Key West Happy Hours & Then Some! | 7,600 | `food_drink` | 2 | — | [Open ↗](https://www.facebook.com/groups/306189633673172) |
| Big Pine Key , Florida | 4,700 | `community_hub` | 2 | 🔒 | [Open ↗](https://www.facebook.com/groups/3076891382397940) |
| Key West for Kids | 2,700 | `family_youth` | 2 | — | [Open ↗](https://www.facebook.com/groups/577019075821418) |
| Key West and Lower Keys Businesses | 2,700 | `business_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/1004912736225389) |
| Key West and Lower Keys Business Advertising | 2,500 | `business_board` | 2 | — | [Open ↗](https://www.facebook.com/groups/1544322812562257) |
| Everything Key West! | 6,200 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/717013633700795) |
| WHAT'S UP KEY WEST? | 5,300 | `community_hub` | 3 | — | [Open ↗](https://www.facebook.com/groups/whatsupkeywest) |
| Key West, Florida Travel Tips | 5,100 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/keywesttraveltips) |
| Things to do in Key West | 1,900 | `tourism_recreation` | 3 | — | [Open ↗](https://www.facebook.com/groups/168169300627004) |
| Key West Home Schoolers | 360 | `family_youth` | 3 | 🔒 | [Open ↗](https://www.facebook.com/groups/150642021701659) |

### Statewide with Keys relevance

| Group | Members | Identity | Tier | Status | Link |
| :--- | :---: | :--- | :---: | :---: | :---: |
| Offshore Fishing Club | 108,000 | `fishing_marine` | 2 | ⚠️ | [Open ↗](https://www.facebook.com/groups/241811260099406) |
| Florida's Surf/Saltwater Fishing Group | 67,000 | `fishing_marine` | 2 | — | [Open ↗](https://www.facebook.com/groups/770865447400880) |
| All Things Lobstering | 15,000 | `fishing_marine` | 2 | ⚠️ | [Open ↗](https://www.facebook.com/groups/387375017591261) |
| Captains and Mates for hire in Florida | 21,000 | `jobs_board` | 3 | — | [Open ↗](https://www.facebook.com/groups/713556279640347) |
| FLORIDA YOUTH SPORTS FORUM RELOAD | 14,000 | `family_youth` | 3 | — | [Open ↗](https://www.facebook.com/groups/1115138580004138) |
| Bully Netting and Lobstering Nation | 8,000 | `fishing_marine` | 3 | — | [Open ↗](https://www.facebook.com/groups/345274400648814) |
| UPCOMING FLORIDA WRESTLING EVENTS | unknown | `family_youth` | 3 | ✅ | [Open ↗](https://www.facebook.com/groups/120274904848453) |

---

## 🧼 Posting rules

- Normal post: 3-8 groups. Strong Keys-wide announcement: 8-12.
- Stagger 10-15 minutes apart; change the first sentence per group bucket; no identical link-only posts.
- Same client in the same group no more than once every 7 days.
- Never post to a group we haven't joined, a group whose rules forbid promos, or a marketplace/yard-sale board unless it's a product offer.
- Read each group's rules before the first post there and record `promo_policy`, `allowed_post_days`, and `admin_post_approval` in the master.
- Automation: every group starts in `assist` mode (agent drafts, human approves). After 5 clean posts with no admin pushback it can be switched to `autopilot`.

## ⚙️ How to use

```bash
python3 manage_groups.py route --type business --region islamorada     # posting plan for a post
python3 manage_groups.py list --joined                                 # what we can post to today
python3 manage_groups.py join-list                                     # highest-reach groups to join next
python3 manage_groups.py set whats-up-florida-keys promo_policy=designated_days allowed_post_days=Tue
python3 manage_groups.py generate                                      # rebuild README / ROUTING / CSV
```

Post types for `route`: `business`, `event`, `food_drink`, `fishing`, `tourism`, `jobs`, `housing`, `product_deal`, `environment`, `history`, `family_youth`, `community`.

---

## 🗑️ Legacy names not found on Facebook

The July 2026 list contained these names. On 2026-09-02 none could be found as a Facebook group by that name, and several carried member counts that were far off. They are kept here so nobody re-adds them without verifying first.

| Legacy name | Note |
| :--- | :--- |
| Florida Keys Events | No group by this name; use Florida Keys Art & Music, Key West Events & fun things to do, What's Happening in Key Largo/Islamorada |
| Florida Keys Business Directory | Not found; use the two Keys-wide business boards |
| Florida Keys Forever Home | Not found |
| Upper Fl Keys Rentals | Not found; see Florida Keys FOR RENT / Key Largo-Tavernier For Rent |
| South Dade and Upper Keys Homeschoolers | Not found; only Key West Home Schoolers exists |
| Upper Keys Wine Beer & Food Events | Not found; nearest is Beer, Liquor, Events in the Keys (269) |
| Florida Keys History with Brad Bertelli | Not found as a group (Brad Bertelli is a Page); use Florida Keys History |
| Florida Sargassum Reports + Daily News | Not found; use Key West and Florida Keys Sargassum Daily Updates |
| Key Largo, FL Keys | Not found. Legacy count 145,500 was wrong. |
| Key Largo Life | Not found |
| Key Largo | Not found as a general community group |
| Key Largo Running Club | Not found |
| Experience the Islamorada Sandbar! | Not found by exact name; see Islamorada Sandbar (private, 75K) |
| Florida Bay Forever | Nonprofit Page, not a group |
| Marathon, FL Keys Past\|Present\|Future- (uncensored) | Not found. Legacy count 50,100 was wrong. |
| Marathon, FL Keys | Not found |
| Marathon, Florida Area Jobs and career opportunites | Not found; use Jobs in Monroe Florida |
| I LOVE Marathon! | Not verified (not searched this pass) |
| Sea Base Trek Talk - Prep, News, Info | Not found (Philmont Trek Talk exists, 33K, not Keys) |
| Florida Lobster Mini Season and Regular | Not found; use All Things Lobstering |
| Florida offshore fishing | Not found by exact name; see Offshore Fishing Club (108K) |
| Key Colony Beach Facebook Group | Not found by exact name; see Key Colony Beach Florida |
