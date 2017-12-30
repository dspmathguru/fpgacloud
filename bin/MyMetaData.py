import requests


class MyMetaData:
  meta_url = 'http://169.254.169.254/latest/meta-data/'
  meta = {}

  def __init__(self):
    self.getMetaData(self.meta, self.meta_url)

  def getMetaData(self, meta_dict, meta_url):
    rsp = requests.get(meta_url).text.split('\n')
    for item in rsp:
      if item.endswith('/'):
        name = item[:-1]
        meta_dict[name] = {}
        self.getMetaData(meta_dict[name], meta_url + item)
      else:
        meta_dict[item] = requests.get(meta_url + item).text
