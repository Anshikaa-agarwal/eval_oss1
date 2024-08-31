import numpy as np

c = {
    "name": "ghi",
    "phone": 678
}

contact = [c]

name = input("Enter name: ");
phone = input("Enter phone number: ");


c1 = {
    "name": name,
    "phone": phone
}

np.insert(contact,0, c1)

name2 = input("Enter name2: ");
phone2 = input("Enter phone number2: ");

c2 = {
    "name": name2,
    "phone": phone2
}

np.insert(contact,1, c2)

def display(contact):
    print(contact);
    

display(contact)

contact.pop()

print(contact)

