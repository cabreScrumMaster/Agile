
while True:
    if (user == None):
        print("1 - Connexion")
        print("2 - Inscription")
    if (user != None):
        print("1 - Déconnexion")
        print("2 - Supprimer compte")
    if (user["type"]=="organisateur") :
        print("3 - Créer un tournois")
        print("4 - Voir mes tournois")
        print("5 - Supprimer un tournois")
    print("9 - Quitter")

    choice = input("Choix : ")

    if (choice == "1"):
        if (user == None):
            # Connexion
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            user = user.getUser(username)
            if (user == None):
                print("Utilisateur inconnu")
            elif (user["password"] != password):
                print("Mot de passe incorrect")
                user = None
            else:
                print("Connexion réussie")
        else:
            # Déconnexion
            user = None

    elif (choice == "2"):
        if (user == None):
            # Inscription
            username = input("Nom d'utilisateur : ")
            password = input("Mot de passe : ")
            user = user.getUser(username)
            if (user != None):
                print("Utilisateur déjà existant")
            else:
                user.createUser(username, password)
                print("Inscription réussie")
        else:
            # Supprimer compte
            user.deleteUser(user["username"])
            print("Compte supprimé")
            user = None

    elif (choice == "3" & user["type"]=="organisateur"):
        # Créer un tournois
        print("Créer un tournois")

    elif (choice == "4" & user["type"]=="organisateur"):
        # Voir mes tournois
        print("Voir mes tournois")

    elif (choice == "5" & user["type"]=="organisateur"):
        # Supprimer un tournois
        print("Supprimer un tournois")

    elif (choice == "9"):
        # Quitter
        break
