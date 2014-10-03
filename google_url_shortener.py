import sublime
import sublime_plugin
import urllib.request
import urllib.parse
import urllib.error
import json


class GoogleurlshortenerCommand(sublime_plugin.TextCommand):

    def run(self, edit):
        sels = self.view.sel()
        apiKey = "AIzaSyBYUUuhT957G8ru5TJ9FcjMldoK7rpFDVY"
        requestUrl = "https://www.googleapis.com/urlshortener/v1/url?key=" + apiKey
        headers = {
            "User-Agent": "Sublime URL Shortener",
            "Content-Type": "application/json",
            'Connection':'close'
        }


        for sel in sels:
            url = self.view.substr(sel)
            data = json.dumps({"longUrl": url})
            binary_data = data.encode("utf-8")
            result = ''
            err = ''
            try:
                request = urllib.request.Request(requestUrl, binary_data, headers)
                response = urllib.request.urlopen(request, timeout=5)
                result = json.loads(response.read().decode())
                result = result["id"]

            except (urllib.error.HTTPError) as e:
                err = "%s: HTTP error %s contacting API. %s." % (__name__, str(e.code), str(e.reason))
            except (urllib.error.URLError) as e:
                err = "%s: URL error %s contacting API" % (__name__, str(e.reason))

            if (err):
                sublime.error_message(err)

            print('url: ' + url)

            if (result):
                self.view.replace(edit, sel, result)
 

class GooglApiCall():
    def __init__(self, sel, url, timeout):
        self.sel = sel
        self.url = url
        self.timeout = timeout
        self.result = None

    def run(self):
        try:
            apiKey = "******************************"
            # 自分で取得して下さい
            requestUrl = "https://www.googleapis.com/urlshortener/v1/url?key=" + apiKey
            data = json.dumps({"longUrl": self.url})
            binary_data = data.encode("utf-8")
            request = urllib.request.Request(requestUrl, binary_data, headers)
            response = urllib.request.urlopen(request, timeout=self.timeout)
            self.result = json.loads(response.read().decode())
            self.result = self.result["id"]
            return

        except (urllib.error.HTTPError) as e:
            err = "%s: HTTP error %s contacting API. %s." % (__name__, str(e.code), str(e.reason))
        except (urllib.error.URLError) as e:
            err = "%s: URL error %s contacting API" % (__name__, str(e.reason))

        sublime.error_message(err)
        self.result = False
