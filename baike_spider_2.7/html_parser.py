
from bs4 import BeautifulSoup
import urlparse
import re


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /view/123.html
        # /item/Python/407313
        # links = soup.find_all('a', href=re.compile(r"/view/\d+\.htm"))
        links = soup.find_all('a', href=re.compile(r"/item/*"))

        for link in links:
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url, new_url)
            new_urls.add(new_full_url)
        return new_urls


    def _get_new_data(self, page_url, soup):
        res_data = {}

        res_data['url'] = page_url
        # <div class="lemmaTitleBox__OVrj"><h1 class="lemmaTitle_qmNnR J-lemma-title">Python</h1> ...

        title_node = soup.find('dd', class_="lemmaTitleBox__OVrj").find("h1")
        res_data['title'] = title_node.get_text()
        print res_data['title']
        # class = "lemma-summary" label-module="lemmaSummary" >
        # summary_node = soup.find('div', classs_="lemma-summary")
        # res_data['summary'] = summary_node.get_text()

        return res_data


    def parse(self, page_url, html_cont):
        if page_url is None or html_cont is None:
            print 'page_url is None'
            return

        soup = BeautifulSoup(html_cont, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

