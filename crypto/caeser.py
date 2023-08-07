def enc(plain,key):
    result=""
    for i in range(len(plain)):
        char = plain[i]
        if(char.isupper()):
            result+= chr((ord(char)-65+key)%26+65)
        else:
            result+= chr((ord(char)+key-97)%26+97)
    return result

text=input("enter plain text : ")
key=int(input("enter a key : "))
print("cipher text is : " + enc(text,key))
