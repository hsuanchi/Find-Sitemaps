[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![License:MIT](https://camo.githubusercontent.com/65a1e1765866b3722ff006952b8c7c5f27ad714b26e7fdc60db79ddbc9923303/68747470733a2f2f626c61636b2e72656164746865646f63732e696f2f656e2f737461626c652f5f7374617469632f6c6963656e73652e737667)](https://github.com/hsuanchi/Find-Sitemaps)
[![PyPi:Find-Sitemap](https://badge.fury.io/py/Find-Sitemap.svg)](https://pypi.org/project/Find-Sitemap/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


# **Find-Sitemap**

**Find Sitemap** is a tool that helps you easily locate sitemaps on any website. It provides a quick and easy way to find the sitemap of a website, even if it is hidden deep within the website's directory structure. It can also detect multiple sitemaps, allowing you to view and analyze all the pages that are included in the site's sitemap.

```
>>> from Find_Sitemap import FindSitemap
>>> main = FindSitemap('google.com')
>>> main.crawl()
...
...
check 13801/13804: https://google.com/sitemap.xml
check 13802/13804: https://google.com/feed.xml
check 13803/13804: https://google.com/sitemap_index.xml
check 13804/13804: https://google.com/sitemapindex.xml
--------------------
Find sitemap urls len: 1
Find sitemap urls list: ['https://www.google.com/sitemap.xml']
```

## Getting Started
Installing Requests on PyPI:
```
$ pip install Find-Sitemap
```

## Prerequisites
* [Python](https://www.python.org/downloads/)
* [requests](https://pypi.org/project/requests/)

## Usage
1. Show the subdomains, slugs_L1, slugs_L2, filetypes parameters.
    ```
    >>> from Find_Sitemap import FindSitemap
    >>> main = FindSitemap('google.com')
    >>> main.subdomains
    {'www.'}

    >>> main.slugs_L1
    {'/default', '/sitemap', '/feeds', '/api', '/contents' ...}

    >>> main.slugs_L2
    {'/sitemap', '/stock', '/sitemap1', '/sitemap0', ...}

    >>> main.filetypes
    {'txt', 'xml', 'xml.gz', 'jsp', 'html', ...}
    ```

2. Add the subdomains, slugs_L1, slugs_L2, filetypes parameters.
    ```
    >>> from Find_Sitemap import FindSitemap
    >>> main = FindSitemap('google.com')
    >>> main.subdomains.add("shop.")
    >>> main.slugs_L1.add("/node")
    >>> main.slugs_L2.add("/site")
    >>> main.filetypes.add("xml")
    ```

3. Remove the subdomains, slugs_L1, slugs_L2, filetypes parameters.
    ```
    >>> from Find_Sitemap import FindSitemap
    >>> main = FindSitemap('google.com')
    >>> main.subdomains.remove("shop.")
    >>> main.slugs_L1.remove("/node")
    >>> main.slugs_L2.remove("/site")
    >>> main.filetypes.remove("xml")
    ```

4. Run the crawler.
    ```
    >>> from Find_Sitemap import FindSitemap
    >>> main = FindSitemap('google.com')
    >>> main.crawl()
    ...
    ...
    check 13801/13804: https://google.com/sitemap.xml
    check 13802/13804: https://google.com/feed.xml
    check 13803/13804: https://google.com/sitemap_index.xml
    check 13804/13804: https://google.com/sitemapindex.xml
    --------------------
    Find sitemap urls len: 1
    Find sitemap urls list: ['https://www.google.com/sitemap.xml']
    ```
## Contributing
* See [Contributing](contributing.md)

## Authors
* Email: <a0025071@gmail.com>
* Website: [Max 行銷誌](https://www.maxlist.xyz/)
