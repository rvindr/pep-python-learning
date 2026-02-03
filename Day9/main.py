import json

people = '''
    {"people": [
        {
        "name":"bharat",
        "phone":"987654321",
        "email":["bhart@gmail.com","bhart@lpu.in"],
        "status":false
        },
        {
        "name":"anoop",
        "phone":"789465123",
        "email":["anoop@gmail.com","anoop@lpu.in"],
        "status":false
        }
        ]}
'''

# data = json.loads(people) # convert json to dict 
# print(data)

# for p in data["people"]:
#     print(p['name'])

# # json_format_data = json.dumps(data) #convert dict to json
# json_format_data = json.dumps(data, indent=3) #convert dict to json
# print(json_format_data)


with open('states.json','r') as file:
    data = json.load(file)
    print(data)

    for d in data["states"]:
        del d['abbr']
    
    with open('new_file.json','w') as jfile:
        json.dump(data, jfile, indent=3)
