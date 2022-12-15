import json

def createUser(username, password, role="joueur"):
    # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)

    # Check if the user already exists in the database
    if username in users:
        # If the user already exists, do nothing
        return
    
    f.close()
    
    # If the user does not exist, add them to the database
    # with the specified role
    users[username] = {
        "username": username,
        "password": password,
        "role": role
    }

    # Save the updated database to the JSON file
    with open('data/users.json', 'w') as f:
        json.dump(users, f)

    f.close()

def getUser(username):
    # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    f.close()
    # Check if the user exists in the database
    if username in users:
        # If the user exists, return the user
        return users[username]
    else:
        # If the user does not exist, return None
        return None

def isUser(username):
    # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    f.close()
    # Check if the user exists in the database
    return username in users