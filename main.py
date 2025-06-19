import sys
import subprocess
import sys
from datetime import datetime
import traceback
try:
    from flask import Flask, render_template, request, jsonify
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "flask"])
import sqlite3
import pandas as pd
import time
from cryptography.fernet import Fernet
import uuid
import random
from difflib import SequenceMatcher
import requests
import urllib3
import urllib.parse
import threading
import secrets

def epgk(password):
    key = Fernet.generate_key()
    mkey=key.decode()


    cipher = Fernet(key)


    text = f"{password}".encode()

    enc= cipher.encrypt(text)

    dec = cipher.decrypt(enc)
    dec2=dec.decode()
    return text,mkey

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


PROJECT_URL = "https://dxomxagqcawaabxtlvoq.supabase.co"
API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImR4b214YWdxY2F3YWFieHRsdm9xIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDk2MDM3NDgsImV4cCI6MjA2NTE3OTc0OH0.9DFqa0kAxe4ziB1ddR80pVPG-W5i_jp7_Bk_b_1hKP4"


TABLE_NAME = "users"

headers = {
    "apikey": API_KEY,
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}



def epgk(password):
    key = Fernet.generate_key()
    mkey=key.decode()


    cipher = Fernet(key)


    text = f"{password}".encode()

    enc= cipher.encrypt(text)

    dec = cipher.decrypt(enc)
    dec2=dec.decode()
    return enc,mkey


def create(username,password):
    headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json",
    "Prefer": "return=representation"
    }
    r = requests.get(f'{PROJECT_URL}/rest/v1/keys', headers=headers, verify=False)
    dat=r.json()
    
    r = requests.get(f'{PROJECT_URL}/rest/v1/users', headers=headers, verify=False)
    datas=r.json()
    for row in datas:
        user=row["user"]
        if f'{username}'==f'{user}':
            print('flagged')
            return 666
    
    password,keys = epgk(password)
    x=0
    for f in dat:
        x+=1

    cookie=secrets.token_hex(64)
    uniq = f'T{username[0]}{username[-1]}|{uuid.uuid4()}'
    data = {
        "uid": f"{uniq}",
        "user": f"{username}",
        "password": f"{password}",
        "kid":f"{x+1}",
        "spc":f'{cookie}'
    }
    
    response = requests.post(
        f"{PROJECT_URL}/rest/v1/users",
        headers=headers,
        json=data,
        verify=False
    )
    data = {
        "id": f"{x+1}",
        "key": f"{keys}"

    }
    
    response = requests.post(
        f"{PROJECT_URL}/rest/v1/keys",
        headers=headers,
        json=data,
        verify=False
    )
    return uniq,cookie

def dpwk(password,key):
    if isinstance(password, str) and password.startswith("b'") and password.endswith("'"):
        password = password[2:-1]  
        password = password.encode()
    key=f'{key}'.encode()
    cipher = Fernet(key)
    dec = cipher.decrypt(password)
    return dec.decode()

def login(username,password):
    headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json",
    "Prefer": "return=representation"
    }
    r = requests.get(f'{PROJECT_URL}/rest/v1/keys', headers=headers, verify=False)
    dat=r.json()
    
    r = requests.get(f'{PROJECT_URL}/rest/v1/users', headers=headers, verify=False)
    datas=r.json()
    flag=0
    for row in datas:
        user=row["user"]
        if f'{username}'==f'{user}':
            keyy=row["kid"]
            pw=row['password']
            uid=row['uid']
            cookie=row['spc']
            flag=1
            break
    if flag==0:
        return 444
    flag=0
    for g in dat:
        if keyy==g["id"]:
            keyy=g["key"]
            
            flag=1
        
    if flag==0:
        return 444
    pasw=dpwk(pw,keyy)
    if pasw==password:
        
        print('success')
        
        
        return uid,cookie
    else:
        print('password incorrect')
        return 0
    
    

def cres(s):
    fn = [
    "Liam", "Olivia", "Noah", "Emma", "Ava", "Elijah", "Isabella",
    "Lucas", "Mia", "Ethan", "Sophia", "James", "Amelia", "Benjamin", "Harper"
]
    ln = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia",
    "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez"
]    

    headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json",
    "Prefer": "return=representation"
    }
    
    for e in range(s):

        r=random.choice(fn)
        t=random.choice(ln)
        uid=f'{r}{t}|{uuid.uuid4()}'
        student = f'{r} {t}'
        data = {
        "student": f"{student}",
        "year": f"{random.randint(7,12)}",
        "sid":f"{uid}",
        "onb":"No",
        "btime":""
    }
    
        response = requests.post(
        f"{PROJECT_URL}/rest/v1/students",
        headers=headers,
        json=data,
        verify=False
    )
        print(response)
            
    
#cres(10)    
            
print(login('alex','1234'))
#print(create("alex","1234"))


def update_students():
    global students
    students=''
    while True:
        r = requests.get(f'{PROJECT_URL}/rest/v1/students', headers=headers, verify=False)
        students=r.json()
        
    
        
def pob(sid,typ,tid):
    flag=0
    opp={"No":"Yes",
         "Yes":"No"}
    inb=''
    g=0
    
    for u in students:
        if u['sid']==sid:
            inb=u['bid']
            opb=opp[u["onb"]]
            if opb=='No':
                flag=1
                typ=''
            else:
                flag=0
            g=1
    if g==0:
        return 'user not found'
                
            
            
    
            
    headers = {
    "apikey": API_KEY,
    "Content-Type": "application/json",
    "Prefer": "return=representation"
    }
    url = f"{PROJECT_URL}/rest/v1/students?sid=eq.{sid}"

    now = datetime.now()
    fort = now.strftime("%d/%m/%Y %I:%M %p")
    day = now.day
    month = now.month
    year = now.year
    tst=f'{day}{month}{year}'
    
    bid=f'B{tst}|{uuid.uuid4()}'
    updata = {
                 "onb": ("Yes" if flag==0 else "No"),
                 "type":typ,
                 "btime":(f'{fort}' if flag==0 else ""),
                 "bid":(f'{bid}' if flag==0 else '')
                 }
    response = requests.patch(url, json=updata, headers=headers,verify=False)
    if flag==1:
        bid=inb
        encbid = urllib.parse.quote(bid)
        now = datetime.now()
        fort = now.strftime("%d/%m/%Y %I:%M %p")
        url = f"{PROJECT_URL}/rest/v1/breaklog?bid=eq.{bid}"
        updata={"timein":f'{fort}',
                "completed":"Yes"
            }
        response = requests.patch(f"{url}",headers=headers,json=updata,verify=False)
        
        
    else:
        data={"sid":sid,
              "tid":tid,
              "bid":bid,
              "type":typ,
              "timeout":fort,
              "timein":'',
              "completed": "No"

            }
        response = requests.post(
        f"{PROJECT_URL}/rest/v1/breaklog",
        headers=headers,
        json=data,
        verify=False
    )
    if (response.status_code == x for x in range(200,300)):
        return "success"
    else:
        return "error"
    
        
        
    
        
def similarity(a, b):
    return SequenceMatcher(None, a, b).ratio()

t = threading.Thread(target=update_students, daemon=True)
t.start()
def sr(u):
    slist=[]
    c=u[0].capitalize()  
    for t in students:
        if t['student'][0] == c:
            sim=similarity(t['student'], u)
            if sim >=0.5:
                slist.append(t)
    print(slist)                
            
            
time.sleep(1)
#print(pob('OliviaDavis|2e88446a-ee35-49a6-b3e4-6e5e16ad9778','toilet',"Tax|66060dfe-8f05-4968-8d0b-e3946f8f8294"))
#print('changing')
#time.sleep(5)
#print(pob('OliviaDavis|2e88446a-ee35-49a6-b3e4-6e5e16ad9778','toilet',"Tax|66060dfe-8f05-4968-8d0b-e3946f8f8294"))




    

