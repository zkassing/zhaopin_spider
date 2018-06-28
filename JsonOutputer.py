import json
class JsonOutputer(object):
  def save_json(self, json):
    file = open('json.json', 'w', encode="utf-8")
    for j in json:
      jstr = j.dumps()
      file.write(jstr)
    file.close()