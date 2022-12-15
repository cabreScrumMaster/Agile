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

# Return True if the user is connected, False otherwise
def connect(username, password):
    # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    f.close()
    #Write the user as connected in the database
    if (username in users) and users[username]["password"] == password:
        users[username]["connected"] = True
    # Save the updated database to the JSON file
    with open('data/users.json', 'w') as f:
        json.dump(users, f)
    f.close()
    return username in users and users[username]["password"] == password


def deleteUser(username):
        # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    f.close()
    # Check if the user exists in the database
    if username in users:
        # If the user exists, delete them from the database
        del users[username]
        # Save the updated database to the JSON file
        with open('data/users.json', 'w') as f:
            json.dump(users, f)
        f.close()

def disconnect(username):
    # Load the database of users from the JSON file
    with open('data/users.json', 'r') as f:
        users = json.load(f)
    f.close()
    # Write the user as disconnected in the db
    if (username in users):
        users[username]["connected"] = False
    # Save the updated database to the JSON file
    with open('data/users.json', 'w') as f:
        json.dump(users, f)
    f.close()