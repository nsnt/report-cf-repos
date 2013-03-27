#!/usr/bin/env python

import json, requests

repos_api = 'https://api.github.com/users/cloudfoundry/repos'
readme_path = 'README.md'

repos = []
for pn in range(1,4):
  res = requests.get(url=repos_api, params=dict(page=pn))
  # print res.content
  repos.extend(json.loads(res.content))

# print repos[0]
# sys.exit()

for repo in repos:
  raw_url = repo['html_url'].replace('github.com', 'raw.github.com', 1)
  readme_url = '/'.join([raw_url, 'master', readme_path])
  res = requests.get(url=readme_url)
  readme_head = ';;'.join(res.content.splitlines()[0:16])
  output = '\t'.join([repo['name'], repo['description'], readme_head])
  print output
