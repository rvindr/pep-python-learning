import json, requests
# ids = input('enter user id')

# url = f'http://127.0.0.1:8000/udata/?id={int(ids) if ids else ""}'

url = 'http://127.0.0.1:8000/udata/'

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    # json_data = json.dumps(data)
    r = requests.get(url=url, params=data)
    data = r.json()
    return data

# get_data(2)

# res = requests.get(url=url)
# print(res.json())s



def post_data(name, phone_num, city):
    data =  {
        "name": name,
        "phone_num": phone_num,
        "city": city
    }
    json_data = json.dumps(data)
    res = requests.post(url=url,data=json_data)
    return res.json()


# post_data()

def update(id, name, phone_num, city):
    data =  {
        "id":int(id),
        "name": name,
        "phone_num": phone_num,
        "city": city
    }
    json_data = json.dumps(data)
    res = requests.put(url=url,data=json_data)
    return res.json()

# update()



def delete_data(id):
    data =  {
        "id":id
    }
    json_data = json.dumps(data)
    res = requests.delete(url=url,data=json_data)
    return res.json()
# delete_data()

def get_input():
    name=input("Enter your name: ")
    city=input("Enter your city: ")
    try:
        phone_num=int(input("Enter your phone number: "))
    except Exception as e:
        get_input()
        print("only digits are allowed!")

    return (name, phone_num, city)

# while True:
#     # print('')
#     print()
#     a = int(input("Enter: 1 for create new user\n2 get all user\n3 update the user\n4 delete user\n5 get specific user by id\n6 exit\nEnter your choice : "))

#     match a:
#         case 1:
#             name, phone_num, city = get_input()
#             res = post_data(name, phone_num, city)
#             print(res)
#         case 2:
#             res = get_data()
#             print(res)
#         case 3:
#             id = input('enter user id: ')
#             name, phone_num, city = get_input()
#             res = update(id, name, phone_num, city)
#             print(res)
#         case 4:
#             id = input('enter user id')
#             res = delete_data(id)
#             print(res)
#         case 5:
#             id = int(input('enter user id'))
#             res = get_data(id)
#             print(res)
#         case 6:
#             break



def post_data():
    data =  {
        "name": "name",
        "phone_num": 9876543210,
        "city": "city"
    }
    json_data = json.dumps(data)
    res = requests.post(url='http://127.0.0.1:8000/user-data/',data=json_data, headers={'Content-Type':'application/json'})
    print(res.json())

post_data()

def get_data():
    data =  {
        # "city": "city"
    }
    json_data = json.dumps(data)
    res = requests.get(url='http://127.0.0.1:8000/user-data/',data=json_data, headers={'Content-Type':'application/json'})
    print(res.json())

# get_data()

def delete_data():
    data =  {
        "id":11
    }
    json_data = json.dumps(data)
    res = requests.delete(url='http://127.0.0.1:8000/user-data/',data=json_data, headers={'Content-Type':'application/json'})
    print(res.json())

delete_data()