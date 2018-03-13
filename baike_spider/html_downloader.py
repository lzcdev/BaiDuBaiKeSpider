
import urllib2

class HtmlDownloader(object):

    def download(self, url):
        if url is None:
            print 'url is None'
            return  None

        try:
            response = urllib2.urlopen(url, timeout=10)
            if response.getcode() != 200:
                print 'false'
                return None
            print 'success'
        except:
            print 'timeout'
        return response.read()

