import requests
import socket
socket.gethostbyname("")

success_list = []

subdomains:list[str] = ["shopping.","24."]
# subdomains:list[str] = ["sitemap.","sitemaps.","www.",""]
domain:str = "pchome.com.tw"
# domain:str = "momoshop.com.tw"
# domain:str = "pinkoi.com"
# domain:str = "shopee.tw"
slugs_L1:list[str] = ["/sitemaps","/sitemap","/contents",""]
slugs_L2:list[str] = ["sitemap","/sitemaps","/sitemap","/sitemap_index","/sitemap-index","/sitemapindex","/index","/sitemap0","/sitemap1","/tag-sitemap","/category-sitemap","/post-sitemap","/page-sitemap","/product-sitemap"]
filetypes:list = ["xml","xml.gz","txt","php","jsp"]
i:int = 0

for subdomain in subdomains:
    for slug_L1 in slugs_L1:
        for slug_L2 in slugs_L2:
            for filetype in filetypes: 
                i+=1
                url = "https://"+subdomain+domain+slug_L1+slug_L2+"."+filetype
                print(url)
                try:
                    r = requests.get(url)
                    if r.status_code !=200:
                        continue
                    content = r.text
                    print(content[:10])
                    if content.find("sitemap") == -1:
                        continue
                    if content.find("lastmod") == -1:
                        continue
                    if content.find("loc") == -1:
                        continue

                    print("get!!!!!!!!!!!!!!!!!!!!!!!!!",url)

                    success_list.append(url)
                except Exception as e:
                    print("error")
                    # pass

print("\n\n")
print("-"*20)
print("checked:",i)
print(success_list)
