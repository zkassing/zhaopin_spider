from urllib import request, parse
class UrlManger:
  def __init__(self):
    self.url = 'https://fe-api.zhaopin.com/c/i/sou'

  def get_new_url(self, start):
    start += 100
    values = {
      'start': start,
      'pageSize':100,
      'cityId':719,
      'workExperience':-1,
      'education':-1,
      'companyType':-1,
      'employmentType':-1,
      'jobWelfareTag':-1,
      'kw':'php',
      'kt':3
    }

    data = parse.urlencode(values)
  
    full_url = self.url + '?' + data
    return full_url