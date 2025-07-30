import json
import os
def createUserList():
    userList=[]

    while True:
        name= input("Enter name (or quit) for termination ")
        if name == 'quit':
            break
        email = input("Enter email ")
        contact = input("Enter contact Number ")
        user ={
            "userName": name,
            "userEmail" :email,
            "userCOntact" : contact
        }
        userList.append(user)

    if os.path.exists('fileJson.json'):
        with open('fileJson.json','r') as file:
            userList.extend(json.load(file))

    with open('fileJson.json','w') as file:
        json.dump(userList,file)

    print("userList added sucessfully ")

createUserList()