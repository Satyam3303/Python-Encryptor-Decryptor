import string

def enc(all,key):
    pl_text= input("Enter the message")
    cip_text=""
    for letter in pl_text:
        index = all.index(letter)
        cip_text += key[index]
    print(cip_text)

def dec(all,key):
    cip_text= input("Enter the ciphered message")
    pl_text=""
    for letter in cip_text:
        index = key.index(letter)
        pl_text += all[index]
    print(pl_text)



def Main():
    allchar = " " + string.punctuation + string.digits + string.ascii_letters
    keychar = string.punctuation + string.ascii_letters  + string.digits + " "

    allchar = list(allchar)
    keychar = list(keychar)
    
    x = input("Enter the operation\n 1 Encryption\n 2 Decryption")

    if(x=='1'):
        enc(allchar,keychar) 

    elif(x=='2'):
        dec(allchar,keychar)
    
if __name__=='__main__':
    Main()
