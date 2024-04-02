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
print("Length of Generated Password is {} and Generated Password is:{}".format(len(Generator_password),Generator_password))