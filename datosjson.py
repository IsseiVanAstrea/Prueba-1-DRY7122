import json

with open('/home/devasc/Documents/myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)
    
access_token = ourjson ["access_token"]
refresh_token = ourjson ["refresh_token"]

print(f"Token: {access_token}")
print(f"Tiempo de caducidad: {refresh_token} segundos")