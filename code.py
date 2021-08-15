# encryption

# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 17:21:59 2020

@author: Tianyu Ma
"""


#PART 1.1
#PART 4
def getCipherMode(): 
    
    while True:
        # PART 1.1 cipher mode
      print("cipher mode：")
      print("encrypt or e")
      print("decrypt or d")
      print("auto-decrypt or a")
      Ciphermode = input()
      if Ciphermode in "encrypt e decrypt d auto-decrypt a".split(" ",-1):
        return Ciphermode
      else: 
          #PART 1.2 input again
        print("Note: input again：")



# def exeCipherMode():
#     Ciphermode = getCipherMode()
#     if Ciphermode == "e" or Ciphermode == "encrypt":
#         print(encryption())
#     elif Ciphermode == "d" or Ciphermode == "decrypt":
#         print(decryption())
#     elif Ciphermode == "a" or Ciphermode == "auto-decrypt":
#         #????
#         print("???")



# print("message：")
#PART 1.1
def getMessage():
    return input()
   #PART 1.1 text to be encrypted/decrypted
   


# print("rotation value：")
#PART 1.1
def getRotation():
    rot = int(input())
    return rot
    #PART 1.1 rotation value


# print("so ur rot is ", getRotation())


#PART 1.3 encrypt mode
def encryption(): 
    
    #PART 1.3 encryption
    message_change = message.lower()
    str_list = list(message_change) #convert str in list
    str_list_encry = str_list

    
    i = 0
    while i < len(str_list):
        modulo = rot % 26
        if ord(str_list[i]) in range(97,123):
            if ord(str_list[i]) + modulo >= 123:
                str_list_encry[i] = chr(ord(str_list[i]) + modulo - 26)
            else:
                str_list_encry[i] = chr(ord(str_list[i]) + modulo)
        elif ord(str_list[i]) in range(65,91):
            if ord(str_list[i]) + modulo >= 91:
                str_list_encry[i] = chr(ord(str_list[i]) + modulo - 26)
            else:
                str_list_encry[i] = chr(ord(str_list[i]) + modulo)
        else:
            str_list_encry[i] = chr(ord(str_list[i]))
        i = i+1
      
    return "".join(str_list_encry).upper()


#PART 1.4 decrypt mode
def decryption():
    
    #PART 1.4 decryption
  # message = getMessage()  
    message_change = message.lower()
    str_list = list(message_change)
    str_list_decry = str_list
    # rot = getRotation()
    
    i = 0
    while i < len(str_list):
        modulo = rot % 26
        if ord(str_list[i]) in range(97,123):
            if ord(str_list[i]) - modulo <= 97:
                str_list_decry[i] = chr(26 - modulo + ord(str_list[i]))
            else:
                str_list_decry[i] = chr(ord(str_list[i]) - modulo)
        elif ord(str_list[i]) in range(65,91):
            if ord(str_list[i]) - modulo <= 65:
                str_list_decry[i] = chr(26 - modulo + ord(str_list[i]))
            else:
                str_list_decry[i] = chr(ord(str_list[i]) - modulo)
        else:
            str_list_decry[i] = chr(ord(str_list[i]))
            
        i = i+1

      
    return "".join(str_list_decry).upper()
    

#--------------------------------------------------------------------------


#PART 2 
#convert encrypted/decrypted message in str and save in file respectively
def getTranslated():
    mode = ""
    if mode == "encrypt" or mode == "e":
        
        f = open("plain_text.txt", "w")
        f_list = f.readlines()
        f_str = "".join(f_list)
        #make encrypted message into plain message
        return decryption(f_str)

    else:
        f = f.open("decrypted message", "r")
        f_list = f.readlines()
        f_str = "".join(f_list)
        return f_str





#PART 2 
#convert str into str without punctuation
def getText(): 
    #open final message.txt
    f = getTranslated() 
    #read from final message.txt
    txt = f
    #make txt into list
    txt_list = []  
    
    #disregard punctuations and numbers
    for char in "!#$%&()*+,-./:;<=>?@[\\]^_‘{|}~1234567890": 
        txt = txt.replace(char, " ")
        for word in txt.split(" "): 
            txt_list.append(word)
        #make list into str
        txt_str = "".join(txt_list) 
    return txt_str


#PART 2 
#total number of words
def TotalNum():
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    t=set(items)
    return ("\n"+"the total number of words: {}\n".format(len(t))) 


#PART 2 
#tem common words
def TenCommon():
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    for i in range(len(items)):
        word, count = items[i]
          
    for i in range(10):
        word, count = items[i]
        return ("the top ten most commonly used words in the text: "+
                "\n"+
                "{0:<10}{1:>5}".format(word, count))


#PART 2 
#maximum word length
def MaxLength():
    lines = getText()
    #make a list including all information without \n
    for i in range(0,len(lines)):
        lines[i] = lines[i].strip('\n') 
    
    
    maximum = max(lines, key=len)#PART 2 number of maximum
    return("\n"+"maximum word length: " + str(len(maximum)) +"\n")


#PART 2 
#minimum word length
def MinLength():
    lines = getText()
    #make a list including all information without \n
    for i in range(0,len(lines)):
        lines[i] = lines[i].strip('\n') 
    
    minimum = min(lines, key=len)#PART 2 number of minimum
    return("minimum word length: " + str(len(minimum)) +"\n")


#PART 2 
#number of unique words
def UniNum():
    lines = getText()
    from collections import Counter 
    c = Counter(lines)
    return("the number of unique words: {}\n".format(len(c))) 

#------------
#assigned words and counts for PART 2
words = getText().split( )
counts = {}
#count for number in words
for word in words:
    counts[word] = counts.get(word,0) + 1 
#--------------------------


#----------------
#execution of PART 2
#PART 2.2 print out above statistic
print(TotalNum())
print(TenCommon())
print(MaxLength)
print(MinLength())
print(UniNum())

#PART 2.3 save metrics as metrics.txt
f3 = open("metrics.txt", "a")
f3 = f3.write(TotalNum())
f3 = f3.write(MaxLength())
f3 = f3.write(MinLength())
f3 = f3.write(UniNum())
f3.close()
#---------------------

#----------------------------------------------------------------------

#PART 3
# def EntryMode():
#     print("select entry mode to encrypt or decrypt: ")
#     print("manual entry or m")
#     print("read from file or r")
#     mode = input()
    
    
#     if mode == "m" or mode == "manual entry":
#         print("type your message: ")
#         getMessage()
#         return encryption()
            
        
#     if mode == "r" or mode == "read from file":
#        print("provide filename and filepath: ")
#        while True:
#            filename = input("filename: ")
#            filepath = input("filepath: ")
           
#            import os
#            if os.path.exists(filepath + "/" +filename) == True:
#                try:
#                    file = open(filename, "r+")
#                    f = file.readlines()
#                except FileNotFoundError:
#                    #if file does not exist
#                    print("error")
#                    #input filename and filepath again
#                    continue  
#                else:
#                    #if file exists
#                    message = " ".join(f)
#                    print("rotation:")
#                    getRotation()
#                    print(encryption(message))




#----------------------
#------------------------
#choose Cipher mode
Ciphermode = getCipherMode()

#get the rot
print("rotation value：")
rot = getRotation()
print(rot)

#choose Entry mode
print("select entry mode to encrypt or decrypt: ")
print("manual entry or m")
print("read from file or r")
Entrymode = input()


def exeCipherMode():
    # Ciphermode = getCipherMode()
    if Ciphermode == "e" or Ciphermode == "encrypt":
        return ("Encrypted message: " + encryption())
    elif Ciphermode == "d" or Ciphermode == "decrypt":
        return ("Decrypted message: " + decryption())
    elif Ciphermode == "a" or Ciphermode == "auto-decrypt":
        #????
        print("???")

def TotalNum():
    newlist = []
    print("Total number of words: ", len(newlist))

def MaxMinLength():
    newlist = []
    print("Max word length: ", len(max(newlist)))
    print("Min word length: ", len(min(newlist)))

def getDict():
    newlist = []
    dict = {}
    for key in newlist:
        dict[key] = dict.get(key,0) + 1
    key_list = list(dict.keys())
    value_list = list(dict.values())
    


if Entrymode == "m" or Entrymode == "manual entry":
    print("type your message: ")
    message = input()
    print(exeCipherMode())
    
    if Ciphermode == "e" or Ciphermode == "encrypt":
        #input is the plain_text for encrypt mode
        plain_text = message
        #make str into list 
        plain_list = list(plain_text)
        #make sure that the str in list without any numbers or punctuations
        #newlist is only including the words
        newlist = [pllist.replace("!#$%&()*+,-./:;<=>?@[\\]^_‘{|}~1234567890","") for pllist in plain_list]
        #total number of the words
        print("Total number of words: ", len(newlist))
        #Max and min word length
        print("Max word length: ", len(max(newlist)))
        print("Min word length: ", len(min(newlist)))
        #make the dict of keys and values which refers to the wordname and times
        dict = {}
        for key in newlist:
            dict[key] = dict.get(key,0) + 1
        word_list = list(dict.keys())
        times_list = list(dict.values())
        #the unique value which means the time is 1
        unique = times_list.counter(1)
        print("The number of unique words are: ", unique)                        

        
















if Entrymode == "r" or Entrymode == "read from file":
    print("provide filename and filepath: ")
    while True:
        filename = input("filename: ")
        filepath = input("filepath: ")
        
        import os
        if os.path.exists(filepath + "/" +filename) == True:
            try:
                file = open(filename, "r+")
                f = file.readlines()
            except FileNotFoundError:
                #if file does not exist
                print("\nerror")
                #input filename and filepath again
                continue  
            else:
                #if file exists
                message = " ".join(f)
                print("rotation:")
                getRotation()
                print(encryption(message))









#PART 3 choose entry mode


# entrymode = EntryMode()
# message = getMessage()
# rot = getRotation()

#PART 1.1 encrypt mode
# if mode == "encrypt" or mode == "e":
#     print(encryption())
#     f1 = open("encrypted message.txt", "a")
#     f1.write(encryption())
    
# #PART 1.1 dncrypt mode
# elif mode == "decrypt" or mode == "d":
#     print(decryption())
#     f2 = open("decrypted message.txt", "a")
#     f2.write(decryption())

# #PART 4.3 
# #auto-decrypt mode
# elif mode == "auto-decrypt" or mode == "a":
#     import re
#     match = []
#     for rot in range(1,27):
#         text = decryption()
#         text = str(text)
        
#         #PART 4.3 first line in wordslist
#         t = text.split("\n",1)[0]
#         t = t.lower()
        
#         #PART 4.2 read in words.txt
#         with open("words.txt", "r") as f:
#             wordlist = f.read()
#             wordlist = wordlist.split("\n")
#         for i in wordlist:
#             i = str(i)
#             newitem = re.findall(" "+i+" ",t)
#             if len(newitem)>= 1:
#                 match.append(newitem)
        

#         for item in match:
#             if len(item) >= 1:
#                 print(t, "\nis this what you want?")
#                 answer = str(input("yes or no: "))
                
#                 if answer == "no":
#                     match = []
#                     newitem = []
#                     continue
                
#                 elif answer == "yes":
#                     text = decryption()
#                     print("the message you want is: ", text)
#                     #PART 3.3 collect metrics on plain message
#                     with open("metrics.txt", "w") as f:
#                         print(TotalNum())
#                         print(TenCommon())
#                         print(MaxLength)
#                         print(MinLength())
#                         break
    
# #PART 1.1 input again   
# else:
#   print ("Note: input again: ")
#--------------








