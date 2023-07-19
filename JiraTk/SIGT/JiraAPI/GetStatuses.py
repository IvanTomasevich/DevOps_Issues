import requests
import json

url = "https://ivantomasevich.atlassian.net/rest/api/latest/statuses"

payload = ""
headers = {
    'Authorization': 'Basic dG9tYXNldmljLmluZEBnbWFpbC5jb206QVRBVFQzeEZmR0YwSXNfdXdQUlJmRFBaN0NMaXVqNms0MDFnZEY4N3RWSHJJNTJxeFNScktCdFdVQ1hIa00yV1JhNk1CaGFOQ0t2ajdvTWdxQ1JaaERCVVlJdGNwNDZJVmFRLXdSdmoyS3M5YUNhQXBqbG91NHdCbGd4aGJVOWU0dEdPUHlrdE1IUTNaeTVyckdHOHhMQUZzLVNYSHNTbW1oeGF3cGlDRXFBTHhKSmhuYTlsXzN3PTEzNTgxNTJF',
    'Cookie': 'atlassian.xsrf.token=7212a445-c48b-435b-ac6a-916c490ed00c_80be596cff199d0d453999544a8e736f85533644_lin'
}

response = requests.request("GET",
                            url,
                            headers=headers,
                            data=payload)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))


response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    for issue_type in data:
        statuses = issue_type["statuses"]
        for status in statuses:
            status_id = status["statusCategory"]["id"]
            status_name = status["statusCategory"]["name"]
            print(f"ID: {status_id}, Nombre: {status_name}")
else:
    print("Error al realizar la solicitud:", response.status_code)
