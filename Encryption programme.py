import random
import string
#imports

encrypt = True
whileloop = True
#booleans

placeholder=[]
#arrays


encrypted_string=0
#integers

key =""
userkey=""
text_to_decrypt=""
decrypted_text=""
#strings

def Error_protection():
        print('\n\n\nError, report this problem to me on discord @Spoon#4704')
        quit()
    #Incase there are any bugs I do not see
        
def Beginning_Question(whileloop,dore,encrypt):
    while whileloop == True:
        dore=str(input("Decrypt or encrypt?"))
        dore=dore.lower()
            
        if dore == "decrypt":
            encrypt = False
            whileloop = False
        
        elif dore == "encrypt":
            encrypt = True
            whileloop = False
        else:
            print("Just enter decrypt or encrypt its not that hard lol.")
    return encrypt,dore
    #Asks user if they want to decrypt or encrypt then returns user's choice
    
def Ask_For_Text(dore):
    text=str(input("Enter text that needs to be "+dore+"ed"))
    return text
    #Asks user text that needs to be encrypted/decrypted

def Encrypt_Text_And_Create_Key(key,text,encrypted_string):
    randomint =0
    randomintlist=[]
    encrypted_text = []
    randomintlist_reform2=[]
    randomintlist_reformat=[]
    randomcharlist=[]
    count1 = 0
    count2 = 1
    count3 = 0
    #preparing local variables
    
    for i in range(0,4):
        for i in range(0,7):
            randomint = random.randint(32,125)
            randomintlist.append(randomint)
            key += chr(int(randomint))
        randomint = random.randint(49,57)
        randomintlist.append(chr(randomint))
        key += chr(int(randomint))
    #nested for loop that creates key

    for i in range(0,4):
        for n in range(0,7):
            randomintlist_reformat.append(randomintlist.pop(0))
        randomintlist_reform2.append(randomintlist_reformat)
        randomintlist_reformat=[]
        randomintlist_reform2.append(randomintlist.pop(0))
    
    for character in range(0,len(text)):
        try:
            str(randomintlist_reform2[count1])
        except:
            count1=0
            count2=1
        encrypted_string = ord(text[character])
        for number in (randomintlist_reform2[count1]):
            encrypted_string += int(number)
        encrypted_string *= int(randomintlist_reform2[count2])
        encrypted_text.append(str(encrypted_string))
        count1+=2
        count2+=2
    encrypted_string=""
    for value in encrypted_text:
        str(encrypted_string)
        encrypted_string = str(encrypted_string) + str(value)
        encrypted_string = encrypted_string + " "
    return encrypted_string,key

def Decrypt_Text_Using_key():
###########WORK ON DECRYPTION
    
def Print_Text(text,key,encrypt):
    if encrypt == True:
        print("This is the encrypted text:\n" + text + "\n\nThis is the key:\n" + key)
    else:
        print("This is the text after being decrypted:\n" + text + "\n\nThis is the key that was used:\n" + key)
    #Prints decrypted/encrypted text    

    
encrypt,dore = Beginning_Question(whileloop,dore,encrypt)
text = Ask_for_text(dore)
#Calling mandatory functions

if encrypt == True:
    encrypted_string,key = Encrypt_Text_And_Create_Key(key,text,encrypted_string)
    Print_text(encrypted_string,key,encrypt)
elif encrypt == False:
    decrypted_string,key = Decrypt_Text_Using_Key(key,text,decrypted_string)
    Print_text(decrypted_string,key,encrypt)
else:
    Error_protection()
#Calls encryption or decryption function depending on what user selected at start and then prints



#            ___________
#           |           |
#  ""   ""  |  HELLO !  |
#   0   0   /___________|
#     D    //
#   ______
#   \____/
#
#
# Thankyou for taking a look at my programme!
# Feedback will be greatly appreciated
# Github: Hakan-Knightley
# Discord: Spoon#4704


























