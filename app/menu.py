# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

from app.user import *

user = None

def login(): 
    global user
    pseudo = input("Pseudo : ")
    password = input("Mot de passe : ")
    connected = connect(pseudo, password)
    menu = NoneMenu()
    if connected :
        user = getUser(pseudo)
        menu = switcher.get(user["role"].lower(), NoneMenu())
    menu.show()

def inscription():
    global user
    pseudo = input("Pseudo : ")
    password = input("Mot de passe : ")
    createUser(pseudo, password)
    connected = connect(pseudo, password)
    menu = NoneMenu()
    if connected :
        user = getUser(pseudo)
        menu = switcher.get(user["role"].lower(), NoneMenu())
    menu.show()

def disconnection():
    global user
    disconnect(user["username"])
    user = None
    menu = NoneMenu()
    menu.show()

def deleteAcc():
    global user
    print("Vérification de l'identité de ", user["username"], " :\n")
    pseudo = input("Pseudo :")
    if pseudo == user["username"]:
        deleteUser(pseudo)
    user = None
    menu = NoneMenu()
    menu.show()

def NoneMenu():
    menu = ConsoleMenu("Not connected", "please connect")

    connection = FunctionItem("Connection", login)
    inscription_choice = FunctionItem("Inscription", inscription)

    
    menu.append_item(connection)
    menu.append_item(inscription_choice)
    return menu

def PlayerMenu():
    # find_tournoi= FunctionItem("Find tournament", input, ["Enter the name"])
    delete_account = FunctionItem("Delete account", deleteAcc)
    deconnexion_choice = FunctionItem("Deconnexion", disconnection)
    menu = ConsoleMenu("Player", "choose one of these : ")
    menu.append_item(delete_account)
    menu.append_item(deconnexion_choice)
    return menu

def OrgaMenu():
    create_tournoi = FunctionItem("Create tournament", input, ["Enter the name"])
    deconnexion_choice = FunctionItem("Deconnexion", disconnection)
    menu = ConsoleMenu("orga", "choose one of these : ")
    menu.append_item(create_tournoi)
    menu.append_item(deconnexion_choice)
    return menu

switcher = {
    "joueur": PlayerMenu(),
    "organisateur": OrgaMenu(),
    # "admin": AdminMenu
}

menu = NoneMenu()
menu.show()