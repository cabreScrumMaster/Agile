# fichier de test des US liées à l'utilisateur

import pytest
from app.user import createUser, getUser, isUser


def test_admin():
    createUser("admin","admin123","admin")
    assert "admin" == getUser("admin").getUsername()
    assert "admin123" == getUser("admin").getPassword()
    assert "admin" == getUser("admin").getRole()

def test_joueur():
    createUser("user","user123","joueur")
    assert "user" == getUser("user").getUsername()
    assert "user123" == getUser("user").getPassword()
    assert "joueur" == getUser("user").getRole()

def test_organisateur():
    createUser("org","org123","organisateur")
    assert "org" == getUser("org").getUsername()
    assert "org123" == getUser("org").getPassword()
    assert "organisateur" == getUser("org").getRole()

def test_isUser():
    createUser("admin2","admin123")
    assert isUser("toto") == false
    assert isUser("admin2") == true
