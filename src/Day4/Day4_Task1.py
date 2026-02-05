contacts={
    "Alice": 8660887589,
    "Bob": 987654321,
    "Charlie": 9448833593
}
print("contacts:",contacts)
contacts["David"]=9876543210
print("updated contacts:",contacts)
contacts["Alice"]=8277722135
print("Number updated to the existing contact:",contacts)
print(contacts)
print(contacts.get("Bob"))        
print(contacts.get("Allion","Allion's contact not found"))
print()
for name,number in contacts.items():
    print(f"contacts{name}:| phone:{number}")
