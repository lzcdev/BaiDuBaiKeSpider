
import urllib.request
from urllib import error
import ssl


ssl._create_default_https_context = ssl._create_unverified_context

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            print ('url is None')
            return  None
        try:
            response = urllib.request.urlopen(url, timeout=10)
            if response.getcode() != 200:
                print ('false')
                return None
            print ('success')
        except error.URLError as e:
            print (e.reason)
        # print response.read()
        return response.read()

