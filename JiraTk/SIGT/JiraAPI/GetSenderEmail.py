# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
import json
from JiraAuth import *

url = f"{host}/rest/api/3/project/COD/email"

headers = header

response = requests.request(
                           "GET",
                           url,
                           headers=header
                           )

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
