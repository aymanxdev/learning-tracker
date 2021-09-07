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
YESTERDAYS_DATE = input('Please the date you want to update your pixels: YYYYMMDD \n')
Update_quantity = input('Please enter update value \n')
update_pixel_endpoint = f'{graph_endpoint}/graph1/{YESTERDAYS_DATE}'

pixel_graph_update = {
    'X-USER-TOKEN': TOKEN,
}

pixel_graph_update_json = {
    'quantity': Update_quantity
}

response = requests.put(url=update_pixel_endpoint, json=pixel_graph_update_json, headers=pixel_graph_update)
response.status_code
print(response.text)

#TODO:5 Delete pixels to the graph

DATE_TO_DELETE = input('Please enter the date you would like to delete a pixel graph? \n')
delete_pixel_endpoint = f'{graph_endpoint}/graph1/{DATE_TO_DELETE}'

response = requests.delete(url=delete_pixel_endpoint, headers=pixel_graph_update)
print(response.text)
