from tag import slugs_L1, slugs_L2, subdomains, filetypes

# from Find_Sitemap.tag import slugs_L1, slugs_L2, subdomains, filetypes
import requests


class FindSitemap:
    """
    FindSitemap is a simple SEO tool to help you find the sitemap.

    ...

    Attributes
    ----------
    checking_list : list
        list of all possible combinations of slugs, subdomains, filetypes
    sitemap_list : list
        list of sitemap urls that return 200
    domain : str
        the domain that you want to find sitemap.xml
    slugs_L1 : set
        the set of slugs_L1 will be check
    slugs_L2 : set
        the set of slugs_L2 will be check
    subdomains : set
        the set of subdomains will be check
    filetypes : set
        the set of filetypes will be check

    Methods
    -------
    crawl()
        Check all the url in checking_list, if the url content mention about keyword
        (sitemap, lastmod, loc) then add it to sitemap_list
    """

    def __init__(self, domain):
        """
        Parameters
        ----------
        checking_list : list
            list of all possible combinations of slugs, subdomains, filetypes
        sitemap_list : list
            list of sitemap urls that return 200
        domain : str
            the domain that you want to find sitemap.xml
        slugs_L1 : set
            the set of slugs_L1 will be check
        slugs_L2 : set
            the set of slugs_L2 will be check
        subdomains : set
            the set of subdomains will be check
        filetypes : set
            the set of filetypes will be check
        """
        self.checking_list = []
        self.sitemap_list = []
        self.domain = domain
        self.slugs_L1 = slugs_L1
        self.slugs_L2 = slugs_L2
        self.subdomains = subdomains
        self.filetypes = filetypes
        self.already_check_urls: int = 0

    def _strcture_url(self):
        for subdomain in self.subdomains:
            for slug_L1 in self.slugs_L1:
                for slug_L2 in self.slugs_L2:
                    for filetype in self.filetypes:
                        url = f"https://{subdomain}{self.domain}{slug_L1}{slug_L2}.{filetype}"
                        self.checking_list.append(url)
        return len(self.checking_list)

    def crawl(self):
        checking_list_len = self._strcture_url()
        for url in self.checking_list:
            self.already_check_urls += 1
            try:
                print(f"check {self.already_check_urls}/{checking_list_len}: {url}")
                r = requests.get(url)
                if r.status_code != 200:
                    continue
                content = r.text
                if content.find("sitemap") == -1:
                    continue
                if content.find("loc") == -1:
                    continue
                self.sitemap_list.append(url)
            except:
                pass
        print("-" * 20)
        print(f"Find sitemap urls len: {len(self.sitemap_list)}")
        print(f"Find sitemap urls list: {self.sitemap_list}")


if __name__ == "__main__":
    find_sitemap = FindSitemap("google.com")
    print(find_sitemap.subdomains)
    print(find_sitemap.slugs_L1)
    print(find_sitemap.slugs_L2)
    print(find_sitemap.filetypes)
    find_sitemap.crawl()
