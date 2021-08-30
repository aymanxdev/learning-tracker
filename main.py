import requests
import os
from datetime import datetime

USERNAME = 'Your username'
TOKEN = os.environ.get('APP_TOKE')
pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint =f'{pixela_endpoint}/{USERNAME}/graphs'

#TODO:1 Register a new user

body_params = {
    'token': TOKEN,
    'username': USERNAME,
    'agreeTermsOfService': 'yes',
    'notMinor': 'yes'
}

# response = requests.post(url=pixela_endpoint, json=body_params)
# print(response)
# print(response.text)

#TODO:2 Add Graph


graph_header = {
'X-USER-TOKEN': TOKEN,
}
graph_params = {

    'id': 'graph1',
    'name': 'Learning Graph',
    'unit': '%',
    'type': 'int',
    'color':'ajisai'
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=graph_header)
# print(response.text)


#TODO:3 Add pixels to the graph

TODAYS_DATE = datetime.today().strftime('%Y%m%d')
one_pixel_endpoint = f'{graph_endpoint}/graph1'
pixel_header = {
    'X-USER-TOKEN': TOKEN,
}

pixel_graphs = {
    'date': TODAYS_DATE,
    'quantity': '9'
}

response = requests.post(url=one_pixel_endpoint, json=pixel_graphs, headers=pixel_header)
response.
print(response.text)

#TODO:4 Update pixels to the graph


#TODO:5 Delete pixels to the graph
