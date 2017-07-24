# encoding: utf-8
'''
Created on 2017-7-20

@author: NingXi
'''
import urllib2
import re

# 功能：下载网页
def download(url, user_agent='xning', num_retries=2):
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url, headers=headers)
    print 'Downloading --> ',url
    try:
        html = urllib2.urlopen(request).read()
        print '\tDownload Success!'
    except urllib2.URLError as e:
        print '\tDownload error: ', e.reason
        html = None
        if num_retries > 0:
            if hasattr(e, 'code') and 500 <= e.code <600:
                # recursively retry 5xx HTTP errors
                return download(url, user_agent, num_retries-1)
    return html

# 根据sitemap遍历网站
def crawl_setemap(url):
    # download the sitemap file
    sitemap = download(url)
    # extract the sitemap links
    links = re.findall('href="(.*?)"', sitemap)
    print links
    for link in links:
        download('http://example.webscraping.com'+link)

if __name__ =='__main__':
    ans = crawl_setemap('http://example.webscraping.com/sitemap.xml')
    print '\nProgram Exit!'
    #print ans

#增加一些改动
#再次增加改动