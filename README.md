# A-real-congressional-districing-plan
Let's just crowd source this. I'm starting with code written by ChatGPT and we can work from there.

**Python Pre-reqs**  
pip install geopandas shapely networkx matplotlib

**Next Steps**  
Add shapefile paths, test on a small region (e.g. a single state), tune the weights.

**Variables**  
|Parameter|Description|Typical Range|
|-----------------|-----------|-------------|
|dist_weight|Compactness factor (e.g., centroid distance)|1.0 – 10.0|
|split_penalty|Penalty for crossing county/city lines|5.0 – 50.0|
|pop_slack_percent|Allowed deviation from ideal population|0.5% – 1.0%|

**Example**  
score = dist_weight * dist + split_penalty * (county_split or city_split)

# Policy Brief #  
A Simple, Fair, and Nonpartisan Redistricting Algorithm for the U.S.

**What’s the Problem?**    
Every 10 years, political maps are redrawn—and too often manipulated. Gerrymandering lets politicians choose their voters instead of the other way around.

**What’s the Solution?**  
Use an open, data-driven algorithm to draw districts based only on geography and population. Our proposed method does not use party data and applies uniformly across the country.

**Core Principles**  
Equal Population – Every district must have nearly the same number of people.
Contiguous – A district must be one whole shape, not split into pieces.
Compact – No sprawling or snaking districts.
Community Integrity – Try to keep towns, counties, and neighborhoods whole.

**How the Algorithm Works**  
Input: Census data and community boundaries.
Seed: Place initial “centers” across the map.
Grow: Expand districts by adding nearby blocks, prioritizing compact shapes and intact communities.
Check: Ensure all population targets are met, without political data.

**Why It’s Fair**  
It ignores partisanship completely.
It’s transparent—anyone can run it and verify the results.
It produces many possible fair maps, not just one.

**What You Can Do**  
Ask your state to adopt algorithmic redistricting laws.
Support independent redistricting commissions.
Use open-source tools to test your own state’s fairness.
For demos and code, visit: https://github.com/jrwellshpc/A-real-congressional-redistricting-plan
