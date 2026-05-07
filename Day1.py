#  given data = [10,none,20,10,"",30,none,40]
data = [10,None,20,10,"",None,30,40]
#remove duplicates
set = list(set(data))
print(set)
#remove invalid values 
set.remove(None)
set.remove("")
print(set)
#count how many elements removed 
original_length= len(data)
new_length=len(set)
element_removed=original_length-new_length
print(element_removed)
#sorting the list
print(sorted(set))