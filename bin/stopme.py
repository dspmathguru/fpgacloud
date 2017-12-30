#!/usr/bin/env python
# Stop the instance that this command is run in
#    Assumes you have permission through a role to do this

import requests
import json


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
        meta_dict[item] = requests.get(meta_url + item)


if __name__ == "__main__":
  myMetaData = MyMetaData()
  print(json.dumps(myMetaData.meta, sort_keys=True,
                   indent=2, separators=(",", ": ")))
  print('\n')
