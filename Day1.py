#  given data = [10,none,20,10,"",30,none,40]
data = [10,None,20,10,"",None,30,40]
#remove duplicates
set = set(data)
print(set)
#remove invalid values 
set.remove(None)
set.remove("")
print(set)
#return clean list 
