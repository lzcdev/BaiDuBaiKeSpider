
import urllib.request


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
        except:
            print ('timeout')
        # print response.read()
        return response.read()

