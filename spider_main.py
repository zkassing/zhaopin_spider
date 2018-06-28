import UrlManger, JsonDownloader, JsonParser, JsonOutputer

class SpiderMain(object):
  def __init__(self): 
    self.urls = UrlManger.UrlManger()
    self.downloader = JsonDownloader.JsonDownloader()
    self.parser = JsonParser.JsonParser()
    self.outputer = JsonOutputer.JsonOutputer()
  def craw(self):
    start = 0
    while True: 
      try:
        new_url = self.urls.get_new_url(start)
        jsonContent = self.downloader.get_json(new_url)
        json = self.parser.parse_json(jsonContent)
        if(len(json) == 0):
          break
        self.outputer.save_json(json)
        start += 100
      except Exception as e:
        print(e)
        break

if __name__ == "__main__":
  spider = SpiderMain()
  spider.craw()
