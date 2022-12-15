# Import the necessary packages
from consolemenu import *
from consolemenu.items import *


user = None
def NoneMenu():
    menu = ConsoleMenu("Not connected", "please connect")

    usernameInput_item = FunctionItem("Connection", login)
    selection_menu = SelectionMenu(["Google", "Facebook", "Apple", "Normal"])
    Inscription_menu = ConsoleMenu("Main menu", "with")
    submenu_item = SubmenuItem("Inscription", selection_menu, Inscription_menu)
    
    menu.append_item(usernameInput_item)
    menu.append_item(submenu_item)
    return (menu) 

def PlayerMenu():
    find_tournoi= FunctionItem("Find tournament", input, ["Enter the name"])
    menu = ConsoleMenu("Player", "choose one of these : ")
    menu.append_item(find_tournoi)
    return menu

def OrgaMenu():
    create_tournoi = FunctionItem("Create tournament", input, ["Enter the name"])
    menu = ConsoleMenu("orga", "choose one of these : ")
    menu.append_item(create_tournoi)
    return menu

def login(): 
    pseudo = input("Pseudo : ")
    password = input("Mot de passe : ")
    #appelle fn connect
    
    if pseudo == "Orga" and password == "b" :
        user = "Orga"
        menu =  OrgaMenu()
    else :
        user = "player"
        menu =  PlayerMenu()
    menu.show()






if (user != None):
    if (user == "Orga"):
        menu = OrgaMenu()

    else : # pas orga 
        menu = PlayerMenu()


    
else :
    menu = NoneMenu()
menu.show()