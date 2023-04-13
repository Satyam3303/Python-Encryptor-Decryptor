import string

def enc(all,key,pazz):
    f = open('hello.txt','r')
    pl_text = f.read()
    f.close()
    cip_text=""
    for letter in pl_text:
        index = all.index(letter)
        cip_text += key[index]
    f = open('hello.txt','w')
    f.write(cip_text)
    f.write(pazz)
    f.close()
    print(cip_text)
    Main()

def dec(all,key,pazz):
    f = open('hello.txt','r')
    cip_text = f.read()
    f.close()
    if pazz in cip_text:
        cip_text = cip_text.replace(pazz,'')
        pl_text=""
        for letter in cip_text:
            index = key.index(letter)
            pl_text += all[index]
        f = open('hello.txt','w')
        f.write(pl_text)
        f.close()
        print(pl_text)
        Main()
    
    else:
        print("Wrong Password")
        Main()



def Main():
    allchar = " " + string.punctuation + string.digits + string.ascii_letters
    keychar = string.punctuation + string.ascii_letters  + string.digits + " "

    allchar = list(allchar)
    keychar = list(keychar)
    x = input("Enter the operation\n 1 Encryption\n 2 Decryption")
    a = input("Enter the key")
    if(x=='1'):
        enc(allchar,keychar,a) 

    elif(x=='2'):
        dec(allchar,keychar,a)
    
if __name__=='__main__':
    Main()
