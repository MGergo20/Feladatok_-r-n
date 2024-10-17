"""Adott egy lista
lista= [12, 21, 56, 32, -5, -23, 35]
Az alábbi metódusok paraméterként kapják a fenti listát
1. Háy pozitív szám van benne?
2. Mennyi a negatív számok összege?
3. Mennyi az öttel osztható számok átlaga?
"""
import random


def poz_szamok_szama(lista=[]):

    i:int=0
    db:int=0
    while(i<len(lista)):
        # print(lista[i])
        if(lista[i]>0):
            db+=1
        i+=1
    return db

def negativ_szamok_osszege(lista):
    i:int=0
    szam:int=0
    while(i<len(lista)):
        if(lista[i]<0):
            szam += lista[i]
            
        i+=1
    return szam

def öttel_osztható(lista):
    i:int=0
    db:int=0
    osszeg:int=0
    while(i<len(lista)):
        if(lista[i]%5==0):
            osszeg+=lista[i]
            db+=1
        i+=1
    return osszeg
    


def ermedobas():
    eredmeny_lista=[]
    i:int=0
    while(i<10):
        erem:int=int(random.random()*2) +1
        if(erem==1):
            eredmeny_lista.append("Fej")
        elif(erem==2):
            eredmeny_lista.append("írás")
        i+=1
    return eredmeny_lista


def fej_dobasok(eredmeny_lista):
    i:int=0
    fej:int=0

    while(i<len(eredmeny_lista)):
        if(eredmeny_lista[i]=="Fej"):
            fej +=1
        i+=1
    return fej

def kockadobas():
    kocka_lista=[]
    i:int=0
    while(i<200):
        kocka:int=int(random.random()*7) +1
        if(kocka==1):
            kocka_lista.append(1)
        elif(kocka==2):
            kocka_lista.append(2)
        elif(kocka==3):
            kocka_lista.append(3)
        elif(kocka==4):
            kocka_lista.append(4)
        elif(kocka==5):
            kocka_lista.append(5)
        elif(kocka==6):
            kocka_lista.append(6)
        i+=1
    return kocka_lista
        
def kockaszamok(kocka_lista):
    i:int=0
    egy:int=0
    ketto:int=0
    harom:int=0
    negy:int=0
    ot:int=0
    hat:int=0
    while (i < len(kocka_lista)):
        if(kocka_lista[i]==1):
            egy+=1
        elif(kocka_lista[i]==2):
            ketto+=1
        



    