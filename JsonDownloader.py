from urllib import request
class JsonDownloader():
  def get_json(self, url):
    response = request.urlopen(url).read()
    response = response.decode('utf-8')
    return response