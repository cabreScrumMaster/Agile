# fichier de test des US liées à l'utilisateur

import pytest
from app.user import *


def test_admin():
    createUser("admin","admin123","admin")
    assert isUser("admin") == True
    assert "admin" == getUser("admin")["username"]
    assert "admin123" == getUser("admin")["password"]
    assert "admin" == getUser("admin")["role"]

def test_joueur():
    createUser("user","user123","joueur")
    assert isUser("user") == True
    assert "user" == getUser("user")["username"]
    assert "user123" == getUser("user")["password"]
    assert "joueur" == getUser("user")["role"]

def test_organisateur():
    createUser("org","org123","organisateur")
    assert isUser("org") == True
    assert "org" == getUser("org")["username"]
    assert "org123" == getUser("org")["password"]
    assert "organisateur" == getUser("org")["role"]

def test_fakeUser():
    assert isUser("toto") == False
    assert getUser("toto") == None

def test_userDeleted():
    createUser("user","user123","joueur")
    assert isUser("user") == True
    assert getUser("user") != None
    deleteUser("user")
    assert isUser("user") == False
    assert getUser("user") == None
    deleteUser("user123")