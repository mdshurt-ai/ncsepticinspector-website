#!/usr/bin/env python3
"""Writes pages-src/septic-inspection-<slug>.main.html + .meta.json for every town.
Each town carries its own paragraphs (TOWNS below); the frame (hero, sidebar, FAQ block, CTA) is shared.
Run:  python3 .claude/tools/make-town-pages.py   then   node .claude/build.js
"""
import json, os, html

SITE = "https://ncsepticinspector.com"
OUT = os.path.join(os.path.dirname(__file__), "..", "pages-src")

TOWNS = [
 dict(name="Morganton", slug="morganton-nc", county="Burke", zip="28655",
  title="Septic Inspection in Morganton, NC | NC Septic Inspector",
  description="Septic inspections in Morganton and Burke County by NC On-Site Wastewater Inspector #6007I. Lake James and Lake Rhodhiss lots, older homes, Burke County records.",
  og="excavator-brick-home", hero="excavator-brick-home", kicker="Burke County &middot; Lake James to Lake Rhodhiss",
  h1="Septic Inspections in Morganton, NC",
  lead="Morganton is home base. From the National Register streets in town to lake lots on Lake James and wooded rural properties with their own tank and well, I inspect septic systems here every week, and the county's permit office is ten minutes away.",
  body="""
<h2>Septic around Morganton</h2>
<p>Inside the city, most homes are on municipal sewer. Step outside the limits toward Lake James, Lake Rhodhiss, Salem, Drexel or the South Mountains and septic becomes the norm. The last count that asked how homes handled wastewater was the 1990 Census, and at that time more than half of the homes in the Catawba basin part of Burke County were on septic. The share has shifted since, but a large part of the county still relies on a tank and a drain field.</p>
<p>Age is the other factor. Census estimates put Morganton's median home at 1976, with more than half the city's houses built before 1980, and the rural housing stock skews older still. Systems from that era were often permitted on a card, installed with a homemade or early precast tank, and never opened again. I've dug up tanks around Morganton that were built by hand out of block and poured concrete, with lids cracked clean through.</p>
<figure><img src="/images/thumbs/homemade-tank-excavation.jpg" alt="Mini excavator uncovering a large old homemade septic tank beside a shed" width="800" height="600" loading="lazy"><figcaption>Uncovering an old homemade tank beside a shed.</figcaption></figure>

<h2>Lake lots and the river</h2>
<p>Lake James and Lake Rhodhiss lots deserve a careful look at the drain field. Setbacks from the water, steep grades down to the shoreline, and seasonal second-home use all affect how a system performs, and a field that looks fine in a dry August can tell a different story in March. Helene put Lake James at its highest level on record in September 2024 and pushed the Catawba River over Green Street in town; on any property that took water, NCDHHS's advice is to have the septic system inspected, and I look for settling over the tank and field, components that shifted, and effluent on the surface.</p>

<h2>Burke County septic records</h2>
<p>Burke County Environmental Health, at 200 Avery Avenue in Morganton (828-764-9000), issues septic permits, repair permits and existing-system verifications, and it keeps the permit and layout records. The county posts a "Septic Requests for Realtors" form on its septic page, which is the fastest way for an agent to get a copy of the permit before an inspection. The permit shows how many bedrooms the system was designed for, and the layout drawing helps put the tank where it belongs instead of where someone remembers it. <a href="/septic-records/">More on Burke County records.</a></p>
""",
  faqs=[
   ("Do you inspect septic systems on Lake James?", "Yes. Lake James lots on both the Burke and McDowell sides are a regular part of my work. Tell me when you book if the lot is steep or the tank is near the water; it affects how long the inspection takes and what equipment I bring."),
   ("Where is the Burke County septic permit office?", "Burke County Environmental Health is at 200 Avery Avenue in Morganton, 828-764-9000. Agents can use the county's \"Septic Requests for Realtors\" form to ask for a copy of an existing permit or layout."),
   ("Can you do the home inspection the same day?", "Yes, through my other company, Inspect-All Home Inspections. Home inspection, septic inspection, radon and well water testing can all be scheduled for one visit."),
  ]),

 dict(name="Hickory", slug="hickory-nc", county="Catawba", zip="28601",
  title="Septic Inspection in Hickory, NC | NC Septic Inspector",
  description="Septic inspections around Hickory, NC by NC On-Site Wastewater Inspector #6007I. Lake Hickory properties, three-county addresses, and where the septic permit lives.",
  og="root-intrusion-tank", hero="root-intrusion-tank", kicker="Catawba, Burke &amp; Caldwell counties &middot; Lake Hickory",
  h1="Septic Inspections in Hickory, NC",
  lead="A Hickory address can fall in Catawba, Burke or Caldwell County, and that decides which office holds the septic permit. I inspect septic systems across all three, from Lake Hickory waterfront to the rural edges of Mountain View, St. Stephens and Long View.",
  body="""
<h2>Public water doesn't mean public sewer</h2>
<p>Hickory runs its own water and sewer utilities, and the city's water system also supplies Maiden, Long View and other nearby areas. That's the trap: a house on city water can still be on a septic tank, especially outside the city limits and in neighborhoods that were built before sewer lines reached them. Confirm how a property handles wastewater before you assume, because a standard home inspection won't tell you, and the answer decides whether a septic inspection belongs on the order.</p>
<p>Where septic is in use, the systems around Hickory range from 1990s-era precast tanks in subdivisions to much older installations on the county roads. Census estimates put Hickory's median year built at 1982, newer than Morganton or Lenoir but with plenty of houses from the 1960s and 1970s whose tanks have never been opened.</p>

<h2>Lake Hickory and Lookout Shoals</h2>
<p>Lake Hickory forms the city's northern edge, and lake properties bring two septic questions: how close the drain field sits to the water, and how a steep lot was graded to fit a system at all. Downstream, Helene pushed Lookout Shoals Lake more than nine feet above full pool in September 2024, the highest since 1940, and Catawba County counted about a hundred flooded homes in that area. A system that was under water needs to be looked at for settling, shifted components and effluent surfacing, and I'll say so in the report if I see them.</p>
<figure><img src="/images/thumbs/tank-dig.jpg" alt="Shallow square hole dug in a fenced lawn, with a shovel stuck in red clay piled on a blue tarp" width="800" height="600" loading="lazy"><figcaption>Hand digging to a lid in a fenced Hickory yard.</figcaption></figure>

<h2>Which county has the permit</h2>
<p>Most of Hickory is in Catawba County, so most records are with <a href="https://catawbacountync.gov/county-services/environmental-health/septic-wells/" rel="noopener" target="_blank">Catawba County Environmental Health</a> in Newton, which takes online requests for a copy of an existing permit. Addresses west of town may be in Burke County (Burke Environmental Health, Morganton) and north of the river in Caldwell County (Caldwell Environmental Health, Lenoir). The county tax record for the parcel settles which one. <a href="/septic-records/">Office details for all three.</a></p>
""",
  faqs=[
   ("My Hickory house is on city water. Could it still have a septic tank?", "Yes. City water and city sewer are separate questions, and plenty of homes around Hickory are on public water with a private septic system. Check the tax record, the disclosure statement, or look for a cleanout and a tank lid in the yard, and when in doubt, ask."),
   ("Which county holds the septic permit for a Hickory property?", "It depends on the parcel. Most of Hickory is in Catawba County; parts of the city reach into Burke and Caldwell counties. The county listed on the tax record is the one whose environmental health office has the permit."),
   ("Do you inspect lake houses on Lake Hickory?", "Yes. Lake lots often have tight setbacks and steep grades, so mention it when you book. If the property flooded during Helene, say that too, and I'll give the drain field area extra attention."),
  ]),

 dict(name="Lenoir", slug="lenoir-nc", county="Caldwell", zip="28645",
  title="Septic Inspection in Lenoir, NC | NC Septic Inspector",
  description="Septic inspections in Lenoir and Caldwell County by NC On-Site Wastewater Inspector #6007I. Older rural systems, Wilson Creek flood areas, Caldwell County records.",
  og="homemade-tank-lid-crop", hero="homemade-tank-lid-crop", kicker="Caldwell County &middot; Blue Ridge foothills",
  h1="Septic Inspections in Lenoir, NC",
  lead="Outside Lenoir's city limits, septic is the rule, not the exception. I inspect systems from in-town lots to Collettsville, Patterson, Yadkin Valley and the Wilson Creek side of the county, and I know what an older Caldwell County tank tends to look like when the lid comes off.",
  body="""
<h2>Septic in Caldwell County</h2>
<p>The last county-wide count of how homes handled wastewater, the 1990 Census, put close to two-thirds of the homes in the Catawba basin part of Caldwell County on septic, and nearly nine in ten in the smaller Yadkin basin area to the north. Lenoir's housing is older than most of the towns I serve, with a median year built of 1972 and more than a third of homes dating from before 1960, so a lot of those systems are forty or fifty years old. That's past the 15-to-40-year range EPA gives as a typical septic lifespan.</p>
<p>What that means in practice: tanks with no permit on file, homemade tanks of block or poured concrete, inlet and outlet pipes that have cracked or corroded, and drain fields that were sized for a smaller house than the one standing there now. The inspection is built to find exactly those things.</p>
<figure><img src="/images/thumbs/homemade-tank-interior.jpg" alt="Inside an old homemade septic tank, a large ragged hole is broken through the lower concrete wall" width="800" height="600" loading="lazy"><figcaption>A hole broken through the wall of a homemade tank.</figcaption></figure>

<h2>After Helene along Wilson Creek</h2>
<p>The National Weather Service described Caldwell County's Helene flooding as likely the worst in its recorded history, with Collettsville the hardest-hit community. A septic system that sat under moving water can come out of it with a settled tank, lines knocked out of position or a drain field full of silt. On any property in those areas, I look for the warning signs NCDHHS listed after the storm and I report what I find, including anything that limited the inspection.</p>

<h2>Caldwell County septic records</h2>
<p><a href="https://caldwellcountync.org/227/Septic-Wells" rel="noopener" target="_blank">Caldwell County Environmental Health</a>, 2345 Morganton Blvd. in Lenoir (828-426-8579, envhealth@caldwellcountync.org), keeps the septic permits and takes requests on its Septic System Record Request form. Ask for the permit, the layout and the soil evaluation; the permit's bedroom count is the number the state's inspection rule asks me to compare with the house. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("The house is old and nobody knows if there's a permit. Can you still inspect it?", "Yes. Many Caldwell County systems predate the county's files. The inspection then starts from the ground: I locate the tank, open it, evaluate what's there, and the report states what records were available and what wasn't."),
   ("Do you cover Collettsville, Patterson and the Wilson Creek area?", "Yes. If the property flooded during Helene, tell me when you book so I can plan extra time for the drain field area and for finding a tank that may have shifted or been buried deeper by silt."),
   ("How do I get the Caldwell County septic permit?", "Use the Septic System Record Request form on Caldwell County Environmental Health's septic and wells page, or call 828-426-8579. Ask for the permit, the layout drawing and the soil evaluation."),
  ]),

 dict(name="Marion", slug="marion-nc", county="McDowell", zip="28752",
  title="Septic Inspection in Marion, NC | NC Septic Inspector",
  description="Septic inspections in Marion and McDowell County by Inspector #6007I. Rural wells and septic, Lake James and Lake Tahoma, Foothills Health District records.",
  og="woods-excavation", hero="woods-excavation", kicker="McDowell County &middot; Upper Catawba basin",
  h1="Septic Inspections in Marion, NC",
  lead="Marion sits where the foothills meet the Blue Ridge, and most of the county around it runs on private wells and septic systems. I inspect septic from East Marion's mill village to Nebo, Lake James and the Lake Tahoma side of the county.",
  body="""
<h2>Septic and wells are the norm here</h2>
<p>The City of Marion runs its own water system and the county system is small, so once you're past the city lines, a property almost always has its own well and its own septic system. Marion's housing is among the oldest in the area, with a median year built of 1968 and more than six in ten homes built before 1980, and about one in four homes countywide is a mobile home. Older systems and manufactured-home systems each have their own patterns: the first often has no permit and a tank that's never been opened, the second often has a system sized for the original unit and not the additions that followed.</p>
<figure><img src="/images/thumbs/woods-locating.jpg" alt="Orange mini excavator in a wooded lot with small blue marker flags in the ground nearby" width="800" height="600" loading="lazy"><figcaption>Locating a tank on a wooded McDowell County lot.</figcaption></figure>

<h2>Helene in McDowell County</h2>
<p>The National Weather Service called Helene's flooding in McDowell County historic, likely the most severe in the county's recorded history, with Buck Creek, the Catawba River, Goose Creek, Lake James and Lake Tahoma all out of their banks. The county reported that calls to its disaster hotline afterward were mostly water, well and septic issues. If the property sat in water or had repairs after the storm, the septic system belongs on the inspection list: settling over the tank or field, components that moved or surfaced, and sewage backing up are the signs NCDHHS told owners to watch for, and they're the first things I look for on a flooded lot.</p>

<h2>McDowell County septic records</h2>
<p>McDowell's environmental health program is run by the <a href="https://www.foothillshd.org/environmental/septic-inspections/" rel="noopener" target="_blank">Foothills Health District</a>, whose online Septic Records Portal holds inspection details, permit information and system layouts where they exist. Read the district's search instructions before you start; finding the right property record is the hard part. The McDowell office is at 408 Spaulding Rd. in Marion, 828-652-6811. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("Do you inspect septic systems at Lake James and Lake Tahoma?", "Yes, on the McDowell side as well as the Burke side of Lake James. Lake lots often mean steep grades and tight setbacks from the water; mention it when you book."),
   ("The property flooded in Helene. What will you look for?", "Settling or sinkholes over the tank and drain field, parts that moved or came to the surface, silt in the tank, effluent on the ground, and anything that limited the inspection. If the system needs more than an inspection, the report refers you to the health district or a certified contractor."),
   ("Where are McDowell County septic permits kept?", "At the Foothills Health District, which runs an online Septic Records Portal for McDowell and Rutherford counties. The Marion office is at 408 Spaulding Rd., 828-652-6811."),
  ]),

 dict(name="Boone", slug="boone-nc", county="Watauga", zip="28607",
  title="Septic Inspection in Boone, NC | NC Septic Inspector",
  description="Septic inspections in Boone and Watauga County by NC On-Site Wastewater Inspector #6007I. Mountain lots, pump systems, second homes, AppHealthCare permit search.",
  og="woods-locating", hero="excavator-yard", kicker="Watauga County &middot; The High Country",
  h1="Septic Inspections in Boone, NC",
  lead="Once you leave Boone's town water and sewer behind, mountain homes depend on a well, a septic system, or both. Slope, soil depth and cold are what shape septic systems in the High Country, and they're what I plan for when I inspect one.",
  body="""
<h2>Septic on a mountainside</h2>
<p>When AppHealthCare evaluates a Watauga County site for a septic permit, it weighs the slope of the lot, the depth of the soil and how wet it is, because those decide what kind of system can go there. Many mountain lots end up with a pump system pushing effluent uphill to a drain field, a pressure-distribution or low-pressure-pipe system, or a field cut into a bench on the slope. Those systems have more parts than a conventional tank-and-gravel field: a pump tank, floats, an alarm and a control panel, all of which are part of the state's point-of-sale inspection.</p>
<p>By a USGS estimate for 2015, a little more than a third of county residents got their household water from their own well or spring rather than a public system, and septic use tracks that pattern. Second homes that sit empty for months add a wrinkle: a system that's used two weeks a year can look fine and still have a drain field that fails under full-time occupancy.</p>
<figure><img src="/images/thumbs/excavator-yard.jpg" alt="Mini excavator in a backyard during a septic inspection" width="800" height="600" loading="lazy"><figcaption>Reaching a buried tank with the excavator.</figcaption></figure>

<h2>Helene in Boone</h2>
<p>Helene dropped about 20 inches of rain on Boone over three days in September 2024, with flash flooding deep enough to get into homes and businesses and roads that collapsed in town. On a lot that saw that kind of water or a slide, a septic inspection looks for settling, shifted components, silt in the tank and effluent surfacing, and the report says what, if anything, limited the inspection.</p>

<h2>Watauga County septic records</h2>
<p>Septic permits in Watauga County come from <a href="https://www.apphealthcare.com/environmental-health" rel="noopener" target="_blank">AppHealthCare</a>, the district health department for Watauga, Ashe and Alleghany counties, which offers an online septic system permit search from its Environmental Health page. The Watauga office number is 828-264-4995. For a pump or pressure system, the permit and layout matter even more, because they show how the system was designed to work. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("Do you inspect pump and pressure-distribution systems?", "Yes. The state's inspection rule covers the pump tank, control panel, alarm and pump operation, and I evaluate all of it. If the power is off at a vacant house, the report says the pump system couldn't be fully evaluated, so have the utilities on."),
   ("Will frozen ground or snow stop the inspection?", "It can slow it down. Frozen ground makes digging harder and snow hides the drain field. Tell me the deadline and we'll plan around the weather; I'd rather reschedule a day than report a system I couldn't actually see."),
   ("Do you serve Blowing Rock, Valle Crucis and Deep Gap?", "Yes, the High Country around Boone is part of my service area. Steep access and long gravel drives are normal here; just let me know what to expect."),
  ]),

 dict(name="Black Mountain", slug="black-mountain-nc", county="Buncombe", zip="28711",
  title="Septic Inspection in Black Mountain, NC | NC Septic Inspector",
  description="Septic inspections in Black Mountain, Swannanoa and eastern Buncombe County by Inspector #6007I. Systems older than county records, Helene flood lots.",
  og="pipe-interior", hero="pipe-interior", kicker="Buncombe County &middot; Swannanoa Valley",
  h1="Septic Inspections in Black Mountain, NC",
  lead="Black Mountain's hillside properties on a well and septic, Swannanoa's older homes, and the lots along Flat Creek and the Swannanoa River that Helene rearranged: I inspect septic systems in eastern Buncombe County and I know where the county's records stop.",
  body="""
<h2>Systems older than the paperwork</h2>
<p>Buncombe County didn't issue septic permits before 1977, and the early permits were kept on carbon paper until they were digitized in 2007. About four in ten homes in Black Mountain were built before 1980 and roughly one in ten before 1940, so a meaningful share of the systems here have no county record at all. That isn't a defect by itself, but it means the inspection has to establish everything on site: where the tank is, what it's made of, what condition it's in, and whether the drain field is doing its job.</p>
<p>At about 2,300 feet in the Swannanoa Valley, the lots run from valley floor to steep hillside, and the systems follow. Hillside homes often have pump systems or fields benched into the slope, with more components to evaluate than a flat-lot gravity system.</p>
<figure><img src="/images/thumbs/root-intrusion-closeup.jpg" alt="Open septic tank with wastewater and thick mats of tree roots growing over the concrete inside" width="800" height="600" loading="lazy"><figcaption>Roots take over a tank a little at a time.</figcaption></figure>

<h2>After Helene: Flat Creek, the river and the slopes</h2>
<p>The National Weather Service's Helene summary describes historic flooding in Buncombe County; in Black Mountain, Flat Creek Road washed out, and news reports counted hundreds of landslides across the county. On a lot that flooded or slid, the septic questions are whether the tank settled or shifted, whether lines were cut, whether silt filled the tank, and whether effluent is surfacing. I look for all of it and report what limited the inspection, if anything did.</p>

<h2>Buncombe County septic records</h2>
<p>Buncombe's Environmental Health office (35 Woodfin St., Asheville, permitting office 828-250-5360) puts well and septic records in the county's online development portal, searchable without registering. The county's own search guide says to try the parcel number first, then the address, then the street name with a wildcard, and that the "OP" attachment on a septic record is the final drawing. Well permitting began in 2005, so an older well has no record either. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("The county has no septic permit for the house. Is that a problem?", "Not by itself. Buncombe County didn't issue septic permits before 1977, so older systems simply predate the files. The inspection establishes the system's location and condition on site, and the report states that no record was available."),
   ("Do you cover Swannanoa, Montreat and Ridgecrest?", "Yes. Eastern Buncombe County, from Swannanoa through Black Mountain to Ridgecrest and Montreat, is part of my service area. Steep access is normal; tell me what to expect."),
   ("Can I search Buncombe County septic records myself?", "Yes, on the county's online development portal, without registering. Search by parcel number first; older parcel numbers sometimes find older permits. The county posts a search guide that explains the tricks."),
  ]),

 dict(name="Old Fort", slug="old-fort-nc", county="McDowell", zip="28762",
  title="Septic Inspection in Old Fort, NC | NC Septic Inspector",
  description="Septic inspections in Old Fort, NC by NC On-Site Wastewater Inspector #6007I. Flood-affected lots along Mill Creek and the Catawba, McDowell County records.",
  og="homemade-tank-uncovered", hero="homemade-tank-uncovered", kicker="McDowell County &middot; At the foot of the Blue Ridge",
  h1="Septic Inspections in Old Fort, NC",
  lead="Old Fort was one of the hardest-hit towns in Western North Carolina during Helene, and the ground around it still carries the story. Outside the town's lines, properties run on their own well and septic, and those are the systems I inspect.",
  body="""
<h2>Septic outside the town's lines</h2>
<p>The Town of Old Fort runs its own water and sewer system, and Helene submerged the sewer plant under fourteen feet of water and left the town with recurring line breaks for months. Beyond the town system, though, properties toward Pisgah, up the Old Fort Mountain and along the county roads have their own septic systems, and those are the ones a point-of-sale inspection covers. Census estimates for a town this small carry wide margins, but they put the median home around 1965 and roughly a quarter of homes as mobile homes, two housing types with their own septic patterns: no permit on file for the first, a system sized for the original unit for the second.</p>
<figure><img src="/images/thumbs/excavating-by-deck.jpg" alt="Mini excavator digging a hole beside wooden deck stairs, with shovels and a sledgehammer nearby" width="800" height="600" loading="lazy"><figcaption>Reaching a tank buried beside a deck.</figcaption></figure>

<h2>Flooded lots along Mill Creek and the Catawba</h2>
<p>On September 27, 2024, Mill Creek flooded the town and met the Catawba River, leaving downtown under several feet of water and a foot of mud. For a septic system, that kind of event can settle the tank, shift the lines, fill the tank with silt and drown the drain field. NCDHHS's post-Helene guidance was to have flooded systems inspected and to watch for soil settling over the tank or field, parts that moved or surfaced, and sewage backing up or standing on the ground. Those are the first things I check on a lot that flooded, and if the house was repaired afterward, any paperwork on the septic work is worth having next to the report.</p>

<h2>McDowell County septic records</h2>
<p>Old Fort's septic permits are with the <a href="https://www.foothillshd.org/environmental/septic-inspections/" rel="noopener" target="_blank">Foothills Health District</a>, which runs McDowell County's environmental health program and an online Septic Records Portal with permits and layouts where they exist. The McDowell office is at 408 Spaulding Rd. in Marion, 828-652-6811. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("The property was repaired after the flood. Does that change the inspection?", "It changes what I pay attention to. I look for settling over the tank and field, shifted or surfaced components, silt in the tank, and effluent on the ground, and the report describes what I can see on inspection day. It doesn't confirm that repairs were permitted; the health district's repair permit file does that."),
   ("Do you inspect septic systems for mobile and manufactured homes?", "Yes. Manufactured-home systems are common around Old Fort. The permit's bedroom count and the home as it stands today, including any additions, are the first comparison the state's inspection rule calls for."),
   ("Where do I find Old Fort septic permits?", "Through the Foothills Health District's Septic Records Portal, or by calling the McDowell office in Marion at 828-652-6811."),
  ]),

 dict(name="Newton", slug="newton-nc", county="Catawba", zip="28658",
  title="Septic Inspection in Newton, NC | NC Septic Inspector",
  description="Septic inspections in Newton, NC by NC On-Site Wastewater Inspector #6007I. Catawba County Environmental Health is in Newton; here's how its septic records work.",
  og="tank-lid-open", hero="tank-lid-open", kicker="Catawba County seat",
  h1="Septic Inspections in Newton, NC",
  lead="Newton is the county seat, and Catawba County's Environmental Health office is here, which makes it the natural place to explain how the county's septic records work. The inspection itself is the same everywhere: tank located and opened, components evaluated, drain field checked, report with photos.",
  body="""
<h2>City sewer in town, septic around it</h2>
<p>The City of Newton runs its own water and wastewater utilities, so inside the city most homes are on sewer. Around Newton, toward Claremont, Startown, Catawba and the county roads, septic systems are common, and so are older houses: Newton's median year built is 1977, older than Hickory, Conover or Maiden, with about 28% of homes built before 1960. Confirm how a particular house handles wastewater before you order; the tax record, the seller's disclosure statement and a look for a tank lid or cleanout in the yard usually settle it.</p>
<figure><img src="/images/thumbs/septic-filter.jpg" alt="Excavated septic tank opening with dark liquid and a mud-covered PVC tee topped by a red slotted cap with a handle" width="800" height="600" loading="lazy"><figcaption>An effluent filter at the outlet tee, one of the components the inspection evaluates.</figcaption></figure>

<h2>Getting Catawba County septic records</h2>
<p><a href="https://catawbacountync.gov/county-services/environmental-health/septic-wells/" rel="noopener" target="_blank">Catawba County Environmental Health</a>, part of Catawba County Public Health, permits septic systems and private wells through its On-Site Water Protection program. The county government offices are at 25 Government Drive in Newton (828-465-8200), and copies of existing septic permits can be requested through an online form on the county's Environmental Health forms page; the division's email is EHAdmin@catawbacountync.gov. Newer applications run through the county's ePermit system.</p>
<p>Ask for three things: the permit, because its bedroom count is the first comparison the state's inspection rule calls for; the layout drawing, because it puts the tank where it belongs; and the soil evaluation, which NC State Extension notes is also kept by the local health department. If the house has gained bedrooms since the permit was issued, that's the conversation to have early. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("How do I request a Catawba County septic permit?", "Through the online permit-copy request on the county's Environmental Health forms page, or by emailing EHAdmin@catawbacountync.gov. Include the property address and parcel number."),
   ("The house has more bedrooms than the permit. What happens?", "The report notes the difference, because the state's inspection rule starts with that comparison. What happens next is between the buyer, the seller and the county: a system permitted for three bedrooms is designed for three bedrooms of wastewater, and the county's environmental health office is the authority on what it would take to change that."),
   ("Do you serve Claremont, Startown and Catawba?", "Yes, the area around Newton is a regular part of my work, including properties on the Catawba River and toward Lookout Shoals."),
  ]),

 dict(name="Conover", slug="conover-nc", county="Catawba", zip="28613",
  title="Septic Inspection in Conover, NC | NC Septic Inspector",
  description="Septic inspections in Conover, NC by NC On-Site Wastewater Inspector #6007I. Newer subdivisions, manufactured homes and rural lots; Catawba County records.",
  og="inlet-flow-test", hero="inlet-flow-test", kicker="Catawba County &middot; Between Hickory and Newton",
  h1="Septic Inspections in Conover, NC",
  lead="Conover's housing is newer than most of the towns I serve, with a median year built around 1991, and a newer system isn't an inspected system. I inspect septic from the subdivisions off Rock Barn and Sweetwater to the manufactured homes and rural lots east of town.",
  body="""
<h2>Newer houses, same questions</h2>
<p>The City of Conover provides water and sewer inside its limits, and much of the city's housing went up in the 1990s and 2000s. Outside the lines, septic systems from that era are mostly precast concrete tanks with proper permits and layouts on file, which makes them easier to find and compare with the house. Easier to find isn't the same as fine: a thirty-year-old tank can have a failed outlet baffle, a crushed line from a vehicle driven over the field, or roots in the inlet, and the drain field may have been sized for a three-bedroom house that now has four.</p>
<p>About one in ten Conover homes is a manufactured home. Their systems are permitted for the original unit, and additions, decks and converted rooms are where the bedroom count and the permit tend to part ways.</p>
<figure><img src="/images/thumbs/inlet-flow-test.jpg" alt="Water pours from a pipe opening in a concrete septic tank wall into the liquid below, with roots hanging above" width="800" height="600" loading="lazy"><figcaption>Running water from the house to watch the inlet.</figcaption></figure>

<h2>Catawba County septic records</h2>
<p>Conover's septic permits are kept by <a href="https://catawbacountync.gov/county-services/environmental-health/septic-wells/" rel="noopener" target="_blank">Catawba County Environmental Health</a> in Newton, which takes online requests for a copy of an existing permit and can be reached at EHAdmin@catawbacountync.gov or through the county at 828-465-8200. For a 1990s system the permit and layout are usually on file and worth pulling before the inspection. <a href="/septic-records/">Records guide.</a></p>

<h2>After Helene</h2>
<p>Catawba County's storm damage in September 2024 was mostly wind and power outages in the Conover area, with the serious flooding downstream around Lookout Shoals. If a property had storm damage or repairs, say so when you book and I'll look for the flood-related signs on the drain field and around the tank.</p>
""",
  faqs=[
   ("Does a 1990s septic system still need an inspection?", "Yes. Age is only one factor. Baffles, tees, filters and lines fail on their own schedule, roots don't care what year a tank was poured, and the bedroom count on the permit may not match the house today."),
   ("Do you inspect manufactured-home septic systems in Conover?", "Yes. The first thing I compare is the permit's bedroom count with the home as it stands, additions included, because that's where manufactured-home systems most often fall short."),
   ("Where are Conover's septic permits?", "With Catawba County Environmental Health in Newton. Request a copy of an existing permit online through the county's Environmental Health forms page, or email EHAdmin@catawbacountync.gov."),
  ]),

 dict(name="Maiden", slug="maiden-nc", county="Catawba", zip="28650",
  title="Septic Inspection in Maiden, NC | NC Septic Inspector",
  description="Septic inspections in Maiden, NC on both sides of the county line by Inspector #6007I. Catawba and Lincoln County records, rural septic along the US 321 corridor.",
  og="tank-interior", hero="homemade-tank-brick", kicker="Catawba &amp; Lincoln counties &middot; US 321 corridor",
  h1="Septic Inspections in Maiden, NC",
  lead="Maiden straddles the Catawba-Lincoln county line, and the line decides which office has the septic permit. I inspect septic systems on both sides, from in-town lots to the rural properties along US 321 and toward Lake Norman's upper reaches.",
  body="""
<h2>Two counties, one town</h2>
<p>Inside town limits, Maiden buys water from the City of Hickory and runs its own sewer system. Outside, septic is common, and especially so on the Lincoln County side: an older NCDHHS table put about four in five Lincoln County homes in the Catawba River basin on septic, a noticeably higher share than the same table showed for Catawba County. Maiden's median year built is 1984, with about one in five homes built before 1960 and about 8% mobile or manufactured homes, so the systems range from older tanks with no record to 2000s subdivisions with everything on file.</p>
<figure><img src="/images/thumbs/homemade-tank-brick.jpg" alt="Inside an old homemade septic tank with concrete and brick walls, wastewater, and a heavily corroded pipe protruding from the wall" width="800" height="600" loading="lazy"><figcaption>A corroded pipe inside an old homemade brick tank.</figcaption></figure>

<h2>Which office has the permit</h2>
<p>For a parcel on the Catawba side, the records are with <a href="https://catawbacountync.gov/county-services/environmental-health/septic-wells/" rel="noopener" target="_blank">Catawba County Environmental Health</a> in Newton, which takes online requests for a copy of an existing permit (EHAdmin@catawbacountync.gov, county line 828-465-8200). On the Lincoln side, <a href="https://lincolncountync.gov/451/Environmental-Health" rel="noopener" target="_blank">Lincoln County Environmental Health</a> (Lincoln County Health Department, 353 N. Generals Blvd., Lincolnton) has a "Request Septic or Well Permit" option on its page; include the property address or parcel number. The county on the tax record is the one to call. <a href="/septic-records/">Records guide.</a></p>

<h2>Wells and septic together</h2>
<p>Many Maiden-area properties on septic are on a private well too, and the two systems are neighbors underground. The state's inspection records the type of water supply, and if the well is private, a water test through Inspect-All Home Inspections can be added to the same visit. EPA counts elevated nitrate or coliform in a nearby well among the signs of a septic problem, which is one more reason to look at both.</p>
""",
  faqs=[
   ("How do I know which county my Maiden property is in?", "The county tax record for the parcel. Catawba County's office is in Newton; Lincoln County's is in Lincolnton. The septic permit is with whichever county the parcel sits in."),
   ("Can you inspect the septic and test the well on the same visit?", "Yes. The septic inspection is this site's service; well water testing is added through Inspect-All Home Inspections, and both happen in one trip."),
   ("Do you cover the Lincoln County side, toward Lincolnton and Denver?", "Yes. The Maiden area on both sides of the line is part of my service area, and I'll go further into Lincoln County on request."),
  ]),

 dict(name="Taylorsville", slug="taylorsville-nc", county="Alexander", zip="28681",
  title="Septic Inspection in Taylorsville, NC | NC Septic Inspector",
  description="Septic inspections in Taylorsville and Alexander County by Inspector #6007I. Farms, homesteads and lake homes where septic is the norm; Alexander County records.",
  og="drainfield-marked", hero="tank-paint-marked", kicker="Alexander County &middot; Brushy Mountains foothills",
  h1="Septic Inspections in Taylorsville, NC",
  lead="Septic has always been the norm in Alexander County. From downtown Taylorsville to the farms and homesteads in the Brushy Mountains foothills and the lake homes near Lake Hickory, most properties here depend on a tank and a drain field, and I inspect them.",
  body="""
<h2>Where septic is nine homes in ten</h2>
<p>The most recent county-level count of how homes handled wastewater, from 1990, showed roughly 88% of housing in the Catawba basin part of Alexander County on septic and about 91% in the Yadkin basin part. Sewer service is still limited: the Town of Taylorsville serves the central and eastern county and the City of Hickory serves Bethlehem. Public water reaches more of the county than sewer does, so a house on county water is very likely still on septic.</p>
<p>Taylorsville's median year built is 1976, about 30% of homes in town were built before 1960, and manufactured homes make up nearly a quarter of the county's housing. Older systems with no record, homemade tanks, and manufactured-home systems outgrown by additions are the recurring themes, and the inspection is built for them.</p>
<figure><img src="/images/thumbs/tank-paint-marked.jpg" alt="Orange paint marking the septic tank outline beside a home" width="800" height="600" loading="lazy"><figcaption>Tank marked out before the digging starts.</figcaption></figure>

<h2>Farms, orchards and lake homes</h2>
<p>About two-thirds of the county is farmland, and rural systems bring their own questions: a drain field under a pasture that's had equipment driven across it, a tank that's been buried deeper by grading, or a system that served a farmhouse for decades before the current addition went on. Lake homes near Lake Hickory and the Catawba River bring the usual setback and slope questions. Either way, the inspection starts by finding the tank, and on an older rural lot that can be the longest part of the day.</p>

<h2>Alexander County septic records</h2>
<p>Septic permits in the county go through the <a href="https://alexanderhealth.org/services/environmental-health/" rel="noopener" target="_blank">Alexander County Health Department's Environmental Health division</a>, 151 W Main Ave. in Taylorsville, 828-632-1000. There's no online search; call or visit to ask for the permit and any layout on file. The office also evaluates existing systems for additions and replacements, which is the conversation to have if the permit's bedroom count doesn't match the house. <a href="/septic-records/">Records guide.</a></p>
""",
  faqs=[
   ("Do you inspect septic systems on farms and large rural lots?", "Yes. Expect the locating step to take longer on a large lot with no layout drawing, and tell me if equipment has been driven over the drain field area; that's one of the things the inspection looks at."),
   ("How do I get the Alexander County septic permit?", "Call or visit Alexander County Environmental Health at 151 W Main Ave., Taylorsville, 828-632-1000. There's no online search. Ask for the permit, any layout drawing and the soil evaluation."),
   ("Do you serve Bethlehem, Stony Point and Hiddenite?", "Yes. All of Alexander County is in my service area, including the Bethlehem community on Lake Hickory."),
  ]),
]

FRAME = """<section class="page-hero" style="--hero-img:url('/images/{hero}.jpg')"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a> › <a href="/service-areas/">Service Areas</a> › {name}</nav>
  <div class="kicker">{kicker}</div>
  <h1>{h1}</h1>
  <p class="lead">{lead}</p>
  <div class="btns"><a href="/schedule/" class="btn btn-green">Book Online</a><a href="tel:+18284432371" class="btn btn-line"><svg><use href="#i-phone"/></svg>Call 828-443-2371</a></div>
</div></section>

<section><div class="wrap content-grid">
  <article class="prose">
{body}
    <h2>What the inspection covers</h2>
    <p>Every inspection follows the state's minimum point-of-sale standard (21 NCAC 39 .1006) and the same order: compare the advertised bedroom count with the permit, locate and mark the tank, uncover and open it, evaluate the tank and its components, evaluate the pump tank and control panel if there is one, check the drain field area, and put it in writing with photos. If you want the tank pumped, I'll <a href="/pumping/">arrange a pumping company for the same visit</a>. The full process, with photos of each step, is on the <a href="/septic-inspection/">septic inspection page</a>.</p>

    <h2>{name} septic FAQ</h2>
    <div class="faq">
{faqs}
    </div>
  </article>

  <aside class="side">
    <div class="side-card"><h3>Credentials</h3><ul><li>NC On-Site Wastewater Inspector<b>#6007I</b></li><li>NC Home Inspector<b>#4327</b></li><li>NC Real Estate Broker<b>#213426</b></li></ul></div>
    <div class="side-card"><h3>{name} at a glance</h3><ul><li>County: {county}</li><li>Septic records: <a href="/septic-records/">{county} County guide</a></li><li>Pumping: <a href="/pumping/">arranged for the same visit</a></li><li>Sellers: <a href="/pre-listing-septic-inspection/">pre-listing inspections</a></li></ul></div>
    <div class="side-card dark"><h3>Nearby</h3><div class="link-row">{nearby}</div></div>
    <div class="side-card"><h3>Ready to schedule?</h3><p>Send the address, your deadline and whether the tank location is known.</p><a href="/schedule/" class="btn btn-green">Book Online</a><a href="tel:+18284432371" class="btn btn-line">Call 828-443-2371</a></div>
  </aside>
</div></section>

<div class="cta-band"><div class="wrap"><div><h2>Have a {name}-area property to inspect?</h2><p>Book a septic inspection, with pumping arranged if you want it.</p></div><div class="btns" style="display:flex;gap:.8rem;flex-wrap:wrap"><a href="/schedule/" class="btn">Book Online</a><a href="tel:+18284432371" class="btn btn-line">Call 828-443-2371</a></div></div></div>
"""

NEARBY = {
 "morganton-nc": ["marion-nc", "lenoir-nc", "hickory-nc", "old-fort-nc"],
 "hickory-nc": ["conover-nc", "newton-nc", "lenoir-nc", "maiden-nc", "taylorsville-nc"],
 "lenoir-nc": ["hickory-nc", "morganton-nc", "boone-nc", "taylorsville-nc"],
 "marion-nc": ["old-fort-nc", "morganton-nc", "black-mountain-nc"],
 "boone-nc": ["lenoir-nc", "taylorsville-nc"],
 "black-mountain-nc": ["old-fort-nc", "marion-nc"],
 "old-fort-nc": ["marion-nc", "black-mountain-nc", "morganton-nc"],
 "newton-nc": ["conover-nc", "hickory-nc", "maiden-nc"],
 "conover-nc": ["hickory-nc", "newton-nc", "maiden-nc"],
 "maiden-nc": ["newton-nc", "conover-nc", "hickory-nc"],
 "taylorsville-nc": ["hickory-nc", "lenoir-nc", "boone-nc"],
}
NAMES = {t["slug"]: t["name"] for t in TOWNS}

def faq_html(faqs):
    return "\n".join(f'      <details><summary>{html.escape(q, quote=False)}</summary><div><p>{html.escape(a, quote=False)}</p></div></details>' for q, a in faqs)

for t in TOWNS:
    nearby = "".join(f'<a href="/septic-inspection-{s}/">{NAMES[s]}</a>' for s in NEARBY[t["slug"]])
    main = FRAME.format(hero=t["hero"], name=t["name"], kicker=t["kicker"], h1=t["h1"], lead=t["lead"],
                        body=t["body"].strip("\n"), faqs=faq_html(t["faqs"]), county=t["county"], nearby=nearby)
    path = f"/septic-inspection-{t['slug']}/"
    meta = {
        "path": path, "title": t["title"], "description": t["description"], "og_image": t["og"],
        "schema": {"@context": "https://schema.org", "@graph": [
            {"@type": "Service", "@id": f"{SITE}{path}#service", "name": f"Septic Inspection in {t['name']}, NC",
             "serviceType": "Point-of-sale septic system inspection", "url": f"{SITE}{path}",
             "description": f"Septic inspections in {t['name']}, NC and {t['county']} County by NC On-Site Wastewater Inspector #6007I, following 21 NCAC 39: tank located and opened, components evaluated, drain field checked, written report with photos.",
             "provider": {"@id": f"{SITE}/#business"},
             "areaServed": {"@type": "City", "name": f"{t['name']}, NC", "containedInPlace": {"@type": "AdministrativeArea", "name": f"{t['county']} County, NC"}}},
            {"@type": "BreadcrumbList", "@id": f"{SITE}{path}#breadcrumb", "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Home", "item": f"{SITE}/"},
                {"@type": "ListItem", "position": 2, "name": "Service Areas", "item": f"{SITE}/service-areas/"},
                {"@type": "ListItem", "position": 3, "name": t["name"], "item": f"{SITE}{path}"}]},
            {"@type": "FAQPage", "@id": f"{SITE}{path}#faq", "mainEntity": [
                {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in t["faqs"]]}
        ]}
    }
    base = os.path.join(OUT, f"septic-inspection-{t['slug']}")
    open(base + ".main.html", "w", encoding="utf-8").write(main)
    json.dump(meta, open(base + ".meta.json", "w", encoding="utf-8"), indent=2, ensure_ascii=False)
    print("wrote", t["slug"], len(main), "chars")
