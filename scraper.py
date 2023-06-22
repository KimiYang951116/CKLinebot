import  json, ssl, urllib.request
import function as f
class rurl:

    def __init__(self, url):
        self.context = ssl._create_unverified_context()
        self.url = url
        self.link = {'place' : 1,
                     'food' : 2,
                     'youbike' : 3}
    def rjson(self):
        with urllib.request.urlopen(self.url, context=self.context) as jsondata:
            data = json.loads(jsondata.read().decode('utf-8-sig'))
        return data

    def tool(self, link, method):
        if method not in link:
            return 'ERROR'
        method = link[method]
        if method == 1:

        elif method == 2:

        elif method == 3:
            f.youbike()
        else:
            return 'ERROR'