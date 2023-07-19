import requests

url = "https://ivantomasevich.atlassian.net/rest/api/latest/user/search?query=ivan"

payload = ""
headers = {
  'Authorization': 'Basic dG9tYXNldmljLmluZEBnbWFpbC5jb206QVRBVFQzeEZmR0YwSXNfdXdQUlJmRFBaN0NMaXVqNms0MDFnZEY4N3RWSHJJNTJxeFNScktCdFdVQ1hIa00yV1JhNk1CaGFOQ0t2ajdvTWdxQ1JaaERCVVlJdGNwNDZJVmFRLXdSdmoyS3M5YUNhQXBqbG91NHdCbGd4aGJVOWU0dEdPUHlrdE1IUTNaeTVyckdHOHhMQUZzLVNYSHNTbW1oeGF3cGlDRXFBTHhKSmhuYTlsXzN3PTEzNTgxNTJF',
  'Cookie': 'atlassian.xsrf.token=7212a445-c48b-435b-ac6a-916c490ed00c_80be596cff199d0d453999544a8e736f85533644_lin'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)