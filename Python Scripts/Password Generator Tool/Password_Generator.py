import random
import string

def generate_strong_password(lenght):
    password = string.ascii_letters + string.digits + string.punctuation
    generated_password = ''.join(random.sample(password,lenght))
    return generated_password

Lenght = int(input("Enter the length of the Password: "))
print("Generated Password :{}".format(generate_strong_password(Lenght)))