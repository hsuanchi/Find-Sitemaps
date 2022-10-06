import pandas as pd
import pprint as pp

df = pd.read_csv("../csv/sitemap.csv", header=None)

sitemap_struct = {
    "l1": set(),
    "l2": set(),
    "l3": set(),
    "l4": set(),
    "l5": set(),
    "l6": set(),
    "l7": set(),
    "l8": set(),
    "http": set(),
    "domain": set(),
}

for sitemap in df[1:].values.tolist():
    sitemap = sitemap[0].split("/")
    print(sitemap)
    # sitemap_struct["filetype"].append(sitemap[-1])
    sitemap_struct["http"].add(sitemap[0])
    sitemap_struct["domain"].add(sitemap[2])
    for i in range(1, 9):
        if i < len(sitemap) and sitemap[-i] != sitemap[2] and sitemap[-i] != "":
            if len(sitemap[-i]) > 2 and len(sitemap[-i]) < 15:
                sitemap_struct[f"l{i}"].add(sitemap[-i])

pp.pprint(sitemap_struct)

with open("../csv/data.txt", "w") as f:
    f.write(str(sitemap_struct))
