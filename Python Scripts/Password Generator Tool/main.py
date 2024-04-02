import string
import random

string_len = int(input("Enter the length of password:"))
Generator_password = ""
num,str1=1, ""
while num<=string_len:
    str1 = random.choice(string.printable).strip()
    if str1=="":
        continue
    Generator_password+=str1
    num+=1
print("length of generated password is {} and is: \"{}\"".format(len(Generator_password),Generator_password))

save = input("Want to store your password: ([Y]es/[N]o):")
if save=='Y' or save=="y":
    website = input("Enter website for which you are using this password:")
    with open ('passwords.text',"ab") as f:
        f.write(f'{website}:{Generator_password}\n'.encode())