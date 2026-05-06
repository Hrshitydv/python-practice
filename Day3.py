phonebook={"Amit":9876543210}\
#Add contact
phonebook.update(
    {"Riya":9123456780}
)
print(phonebook)
#Search contact
print(phonebook.get("Riya"))
#Delete contact
phonebook.pop("Amit")
print(phonebook)
#Prevent duplicate enteries
name=input("Enter name for the entry: ")
number=int(input("enter contact number :"))
checkbook=list(phonebook)
checkbook2=list(phonebook.values())
if name in checkbook or number in checkbook2:
    print("error,Name or Number already present in the phonebook")
else:
    phonebook.update(
        {name : number}
    )
print(phonebook)
#partial contact search
partial_name=input("Enter partial name :")
found=0
for keys in phonebook.keys():
    if (partial_name.lower() in keys.lower()):
        found=1
        break
if found :
    print(keys)
else:
    print("No contact found!")
        
    
    
    