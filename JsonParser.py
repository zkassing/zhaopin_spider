import json
class JsonParser: 
  def parse_json(self, jsonContent):
    data = json.loads(jsonContent)
    results = data['data']['results']
    info = set()
    for result in results: 
      print(result['id'])
      company = {}
      """ company['id'] = result['id']
      company['name'] = result['company']['name']
      company['scale'] = result['company']['size']['name']
      company['type'] = result['company']['type']['name']
      company['exp'] = result['workingExp']['name']
      company['edu'] = result['eduLevel']['name']
      company['salary'] = result['salary']
      company['emplType'] = result['emplType']
      company['welfare'] = result['welfare']
      info.add(company) """

    return info


