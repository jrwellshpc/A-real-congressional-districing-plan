import geopandas as gpd
import networkx as nx
from shapely.geometry import Point, Polygon
import random
import matplotlib.pyplot as plt

# Load census blocks (you must have a shapefile with geometry + population + county/city info)
blocks = gpd.read_file("blocks.shp")
blocks["centroid"] = blocks.geometry.centroid
total_population = blocks["population"].sum()
ideal_pop = total_population / NUM_DISTRICTS

# Build adjacency graph
def build_adjacency(blocks):
    G = nx.Graph()
    for idx, row in blocks.iterrows():
        G.add_node(idx, **row)
    for i, a in blocks.iterrows():
        for j, b in blocks.iterrows():
            if i != j and a.geometry.touches(b.geometry):
                G.add_edge(i, j)
    return G

G = build_adjacency(blocks)

# Seed districts with well-spaced starting points
def seed_districts(blocks, n):
    return random.sample(list(blocks.index), n)

districts = {i: {"nodes": set([seed]), "pop": blocks.loc[seed]["population"]}
             for i, seed in enumerate(seed_districts(blocks, NUM_DISTRICTS))}

# Expand districts while balancing compactness and community integrity
def grow_districts(G, districts):
    unassigned = set(G.nodes()) - set.union(*[d["nodes"] for d in districts.values()])
    while unassigned:
        for i, district in districts.items():
            border = {n for node in district["nodes"] for n in G.neighbors(node) if n in unassigned}
            if not border:
                continue
            best = None
            best_score = float("inf")
            for b in border:
                block = G.nodes[b]
                # Score = weighted distance + subdivision split penalty
                dist = block["centroid"].distance(
                    blocks.loc[list(district["nodes"])]["centroid"].unary_union.centroid
                )
                split_penalty = 10 if any(
                    block["county"] != G.nodes[n]["county"] for n in district["nodes"]
                ) else 0
                score = dist + split_penalty
                if score < best_score and district["pop"] + block["population"] <= ideal_pop * 1.01:
                    best_score = score
                    best = b
            if best:
                district["nodes"].add(best)
                district["pop"] += G.nodes[best]["population"]
                unassigned.remove(best)
    return districts

districts = grow_districts(G, districts)

# Visualize
for i, d in districts.items():
    blocks.loc[list(d["nodes"])].plot()
plt.show()
