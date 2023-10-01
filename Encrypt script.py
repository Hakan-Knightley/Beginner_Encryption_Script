import random
import string
#imports

encrypt = True
whileloop = True
repeat = True
answered = False
#booleans

text_to_decrypt=[]
#arrays


encrypted_string=0
#integers

key =""
userkey=""
decrypted_text=""
dore=""
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
    
def Ask_For_Text(dore,encrypt,key):
    text=str(input("Enter text that needs to be "+dore+"ed"))
    if encrypt == False:
        key=str(input("Enter the key that will be used to decrypt the text"))
        while len(key) != 32:
            key=str(input("Please enter a valid 32 character key."))
    return text,key
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

def Decrypt_Text_Using_Key(key,text,text_to_decrypt,decrypted_text):
    key_array=[]
    key_nested_array=[]
    tempval=""
    tempval2=[]
    tempval3=0
    count1=0
    count2=1
    count3=0
    for character in range(0,len(text)):
        if text[character] == " ":
            text_to_decrypt.append(tempval)
            tempval=""
        else:
            tempval+=str(text[character])
    #takes each number of the encrypted string and puts it into an array using a for loop
    for number in range(0,len(key)):
        key_array.append(key[number])
    for character in range(0,4):
        for character2 in range(0,7):
            tempval2.append(key_array.pop(0))
        key_nested_array.append(tempval2)
        tempval2=[]
        key_nested_array.append(key_array.pop(0))
    for value in text_to_decrypt:
        try:
            str(key_nested_array[count1])
        except:
            count1=0
            count2=1
        tempval3 = int(value) // int(key_nested_array[count2])
        for key_char in key_nested_array[count1]:
            tempval3 -= int(ord(key_char))
        decrypted_text += str(chr(tempval3))
        count1+=2
        count2+=2
        tempval3=0
    return decrypted_text,key
        #Reverses the encryption algorithm and returns the decrypted value
           
def Loop_Program(repeat):
    answered = False
    while answered == False:
        ask_repeat=str(input("Repeat the program?"))
        ask_repeat=ask_repeat.lower()
            
        if ask_repeat == "no":
            repeat = False
            answered = True
        elif ask_repeat == "yes":
            repeat = True
            answered = True
        else:
            print("Please answer with either yes or no.")
    return repeat
#asks user if they want to re-run     
    
def Print_Text(text,key,encrypt):
    if encrypt == True:
        print("This is the encrypted text:\n" + text + "\n\nThis is the key:\n" + key)
    else:
        print("This is the text after being decrypted:\n" + text + "\n\nThis is the key that was used:\n" + key)
    #Prints decrypted/encrypted text    

while repeat == True:
    
    encrypt,dore = Beginning_Question(whileloop,dore,encrypt)
    text,key = Ask_For_Text(dore,encrypt,key)
    #Calling mandatory functions

    if encrypt == True:
        encrypted_string,key = Encrypt_Text_And_Create_Key(key,text,encrypted_string)
        Print_Text(encrypted_string,key,encrypt)
    elif encrypt == False:
        decrypted_string,key = Decrypt_Text_Using_Key(key,text,text_to_decrypt,decrypted_text)
        Print_Text(decrypted_string,key,encrypt)
    else:
        Error_protection()
    #Calls encryption or decryption function depending on what user selected at start and then prints
    repeat = Loop_Program(repeat)
    #Allows the program to repeat endlessly if asked






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
