from email import message
from os import access
from shutil import unregister_unpack_format
import string
import mysql.connector
from time import sleep
from string import *
from mysql.connector import RefreshOption
refresh = RefreshOption.LOG | RefreshOption.THREADS

mydb = mysql.connector.connect(
  host="209.209.40.91",
  port = 19584,
  user="admin",
  password="lS3fVCxE",
  database="moodpy"
)

def register(username , password):
    mycursor = mydb.cursor()
    sql = "INSERT INTO users (username, password, state) VALUES (%s, %s, %s)"
    val = ("{}".format(username), "{}".format(password) , "offine")
    mycursor.execute(sql, val)
    mydb.commit()

    print("Compt Cree avec Succes")

def Login(username , password):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username ='{}'".format(username)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    x = ""
    for x in myresult:
        print("Try to Connect ...")
        sleep(4)
    if("{}".format(password) in x):
        print("Connected")
        return 1 
    else:
        print("Incorect username or Password ...")
        return 0

    

def SendMessage(message , destinataire, myself):
    mycursor = mydb.cursor()
    sql = "INSERT INTO chat (message, snds, sender, destinataire) VALUES (%s,%s ,%s, %s)"
    val = ("{}".format(message), "< {} > : ".format(myself),"{}".format(myself), "{}".format(destinataire))
    mycursor.execute(sql, val)
    mydb.commit()
    print("sending ...")
    sleep(3)
    print("message sent to {}".format(destinataire))

def checking(username, myself):
    mycursor = mydb.cursor()
    sql = "SELECT * FROM users WHERE username ='{}'".format(username)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    x = ""
    for x in myresult:
        print("Try to Connect ...")
        sleep(4)
    if(x != ""):
        choice = input("Do you want to send friend request(y|n)")
        if(choice == "y" or choice == "Y" or choice == "Yes" or choice == "yes"):
            sendfriend(myself,username)
        else:
            return 0
        
    else:
        print("Username doesn't exist")
        return 2

def sendfriend(sender, destinataire):
    mycursor = mydb.cursor()
    sql = "INSERT INTO friend (sender, destinataire, state) VALUES (%s, %s, %s)"
    val = ("{}".format(sender), "{}".format(destinataire) , "pending")
    mycursor.execute(sql, val)
    mydb.commit()
    print("sending Friend Request to {} ...".format(destinataire))
    sleep(3)
    print("Friend Request sent")

def AcceptFriendReq(username, myself):
    mycursor = mydb.cursor()
    sql = "UPDATE friend SET state = 'accept' WHERE destinataire = %s AND sender = %s "
    val = ("{}".format(myself) , "{}".format(username))
    mycursor.execute(sql, val)
    mydb.commit()
    print("friend request accepted")



def FreindRequestVerif(myself):
    mycursor = mydb.cursor()
    sql = "SELECT sender FROM friend WHERE destinataire ='{}' AND state = 'pending'".format(myself)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    tp = 1
    print("Collecting data ")
    sleep(4)
    if(tp == 1):
        print("Friend Request List {pending} ")
        for x in myresult:
            print(x)
        choice = input("Do you want interract (y|n)")
        if(choice == "y" or choice == "Y" or choice == "Yes" or choice == "yes"):
            t = True
            while(t):
                for x in myresult:
                    print(x)   
                name = input("Enter username you wanna accept : ")
                AcceptFriendReq(name , myself)
                choice = input("Do you want accept another one (y|n)")
                if(choice == "y" or choice == "Y" or choice == "Yes" or choice == "yes"):
                    continue
                else:
                    t = False

        
    else:
        print("you don't have any friend request")

def friendlist(myself):
    mycursor = mydb.cursor()
    sql = "SELECT sender FROM friend WHERE destinataire ='{}' AND state = 'accept' ".format(myself)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("Collecting data")
    sleep(4)
    
    print("Friend Request List {pending} ")
    for x in myresult:
        print(x)

def ReceiveMessage(myself):

    friendlist(myself)

    convers = input("Enter chat you wanna see : ")
   
    mycursor = mydb.cursor()
    sql = "SELECT snds,message FROM chat WHERE sender ='{}' AND destinataire = '{}'  OR sender = '{}' AND destinataire = '{}' ORDER BY ID".format(convers, myself, myself, convers)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    print("Collecting data")
    sleep(4)
    print("Message list")
    for x in myresult:
        s = str(x)
        s = s.replace('(','')
        s = s.replace(',','')
        s = s.replace('\'','')
        s = s.replace(')','')
        print(s)
    choice = input("Do you wanna send another message (y|n)")
    if(choice == "y" or choice == "Y" or choice == "Yes" or choice == "yes"):
        txt = input("message you want to send : ")
        SendMessage(txt, convers, myself)
   
def TrueFriend(myself,friend):
    mycursor = mydb.cursor()
    sql = "SELECT state FROM friend WHERE sender ='{}' AND destinataire = '{}'  OR sender = '{}' AND destinataire = '{}'".format(friend, myself, myself, friend)
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        s = str(x)
        s = s.replace('(','')
        s = s.replace(',','')
        s = s.replace('\'','')
        s = s.replace(')','')
        
        if(s == "accept"):
            return 1
        else:
            return 0
    
