import requests
import json
from JiraAuth import *

ids = {"Por hacer": "2",  # Guardo los ids de los bloques del tablero que traje con getStatuses
       "En curso": "4",
       "Listo": "3",
       }


def get_issue():
    url = host + "/rest/api/latest/search"
    headers = header
    query = {
        'jql': 'project = COD AND status = Parking'
    }
    response = requests.request(
        "GET",
        url,
        headers=headers,
        params=query
    )
    data = json.loads(response.text)
    # print("Tipo: ", type(data))
    # print(data["issues"][0])

    for i in data['issues']:
        issue_key = i['key']
        if issue_key:
            return issue_key
        else:
            return False


def move_issue(id_columna, id_issue):
    url = f"{host}/rest/api/latest/issue/{id_issue}/transitions"
    headers = header
    payload = json.dumps({
      "transition": {
        "id": id_columna
      }
    })

    response = requests.request("POST",
                                url,
                                headers=headers,
                                data=payload
                                )

    print(response.text)


issue = get_issue()
print(issue)
move_issue('31', issue)
