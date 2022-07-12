from email import message
import getpass
from django.forms import PasswordInput
from action import *
from pyfiglet import Figlet
import os



def interface(user):
    t = True
    while(t):
        print("{}".format(genfigelt("raytano")))
        cmd = input("{Hacker_Mood} : ")
        cmds(cmd, user)


def cmds(cmd , myself):
    if(cmd == "message"):
        destinataire = input("Enter destinataire name : ")
        verif = TrueFriend(myself, destinataire)
        if(verif == 1):
            message = input("message <> : ")
            sleep(2)
            SendMessage(message,destinataire,myself)
        else:
            print("Vous n'etes pas ami avec {}".format(destinataire))
    elif(cmd == "friend req"):
        print("{}".format(genfigelt("Make friend is Good")))
        username = input("Destinataire username : ")
        checking(username, myself)
    elif(cmd == "req friend"):
        os.system("cls")
        print("{}".format(genfigelt("Hacking")))
        sleep(3)
        FreindRequestVerif(myself)
    elif(cmd == "friend"):
        os.system("cls")
        print("{}".format(genfigelt("Team Hack")))
        sleep(3)
        friendlist(myself)
    elif(cmd == "convers"):
        ReceiveMessage(myself)


def command(cmd):
    if(cmd == "login"):
        os.system("cls")
        print("{}".format(genfigelt("raytano")))
        username = input("Username : ")
        password = getpass.getpass()
        myself = username
        session = Login(username, password)

        if(session == 1):
            interface(username)

    elif(cmd == "create"):
        
        print("{}".format(genfigelt("Mood Universe")))
        username = input("Username : ")
        password = getpass.getpass()

        register(username, password)

        


def genfigelt(msg):
    f = Figlet()
    return f.renderText(msg)

session = 0


print("{}".format(genfigelt("raytano")))
cmd = input("{Hacker_Mood} : ")

command(cmd)



