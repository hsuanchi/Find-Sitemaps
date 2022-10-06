import requests
import re
import pandas as pd

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

sitemap_list = []


url_list = pd.read_csv("../csv/top_website.csv", header=None).values.tolist()

counts = 0
for url in url_list[1:]:

    if url[0][-1] != "/":
        url[0] = url[0] + "/"

    if re.match(r"^(http|https)://", url[0]) == None:
        url[0] = "https://" + url[0]

    query_url = f"{url[0]}robots.txt"

    try:
        r = requests.get(query_url, headers=headers)
        content = r.text
        sitemaps = re.findall(r"Sitemap: (.*)", content)

        print(query_url, len(sitemaps))

        if len(sitemaps) > 0:
            counts += 1
        for sitemap in sitemaps:
            sitemap = sitemap.replace("\r", "").replace(" ", "")
            sitemap_list.append(sitemap)
    except Exception as e:
        print(e)
print(counts / (len(url_list) - 1))
sitemap_list = list(set(sitemap_list))

pd.DataFrame(sitemap_list).to_csv("../csv/sitemap.csv", index=False, header=False)
