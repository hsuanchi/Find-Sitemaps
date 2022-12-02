from Find_Sitemap.tag import slugs_L1, slugs_L2, subdomains, filetypes
import requests

#TODO: add split function for sturcture data
#TODO: add set



class FindSitemap:
    """
    A class used to find sitemap.xml

    ...

    Attributes
    ----------
    success_url : list
        list of success urls
    total_urls : list
        list of total urls
    domain : str
        the domain that you want to find sitemap.xml
    slugs_L1 : list
        the list of slugs_L1 will be check
    slugs_L2 : list
        the list of slugs_L2 will be check
    subdomains : list
        the list of subdomains will be check
    filetypes : list
        the list of filetypes will be check

    Methods
    -------
    crawl()
        Check all the url in total_urls, if the url content mention about keyword
        (sitemap, lastmod, loc) then add it to success_url
    """

    def __init__(self, domain):
        """
        Parameters
        ----------
        success_url : list
            list of success urls
        total_urls : list
            list of total urls
        domain : str
            the domain that you want to find sitemap.xml
        slugs_L1 : list
            the list of slugs_L1 will be check
        slugs_L2 : list
            the list of slugs_L2 will be check
        subdomains : list
            the list of subdomains will be check
        filetypes : list
            the list of filetypes will be check
        """
        self.success_url = []
        self.total_urls = []
        self.check_urls: int = 0
        self.domain = domain
        self.slugs_L1 = slugs_L1
        self.slugs_L2 = slugs_L2
        self.subdomains = subdomains
        self.filetypes = filetypes

    def _strcture_url(self):
        for subdomain in self.subdomains:
            for slug_L1 in self.slugs_L1:
                for slug_L2 in self.slugs_L2:
                    for filetype in self.filetypes:
                        url = f"https://{subdomain}{self.domain}{slug_L1}{slug_L2}.{filetype}"
                        self.total_urls.append(url)
        return len(self.total_urls)

    def crawl(self):
        total_urls_len = self._strcture_url()
        for url in self.total_urls:
            self.check_urls += 1
            try:
                print(f"{self.check_urls}/{total_urls_len}: {url}")
                r = requests.get(url)
                if r.status_code != 200:
                    continue
                content = r.text
                if content.find("sitemap") == -1:
                    continue
                if content.find("lastmod") == -1:
                    continue
                if content.find("loc") == -1:
                    continue
                print(f"get!!!!!!!!!!!!!!!!!!!!!!!!!")
                self.success_url.append(url)
            except:
                pass
        print("-" * 20)
        print(f"Success urls: {len(self.success_url)}")
        print(f"Success urls: {self.success_url}")


if __name__ == "__main__":
    find_sitemap = FindSitemap("maxlist.xyz")
    # find_sitemap.slugs_L1.append("/node")
    # find_sitemap.slugs_L1.remove("/node")
    find_sitemap.crawl()
