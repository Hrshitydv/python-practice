logs=["ERROR DISK FULL","INFO STARTED","ERROR FILE MISSING","WARNING MEMORY LOW"]
count_error=0
count_warning=0
count_info=0\
#TO COUNT ERROR 
for i in logs:
    if "ERROR" in i:
        count_error += 1
print(count_error)
#TO COUNT WARNING
for i in logs:
    if "WARNING" in i:
        count_warning +=1
print(count_warning)
#TO COUNT INFO
for i in logs:
    if "INFO" in i:
        count_info+=1
print(count_info)
#BONUS
#finding most frequent log type
if (count_error>count_info and count_error>count_warning):
    print("'ERROR' Log type is most frequent")
elif(count_info>count_error and count_info>count_warning):
    print("'INFO' log type is most frequent")
elif(count_warning>count_info and count_warning>count_error):
    print("'WARNING' log type is most frequent")
else:
    print("Two or more log type are having same frequencies")
#ignore case sensitivity
count_error=0
count_info=0
count_warning=0
for i in logs :
    if "info" in i.lower():
        count_info+=1
    if "warning" in i.lower():
        count_warning+=1
    if "error" in i.lower():
        count_error+=1
print(count_info)
print(count_warning)
print(count_error)

        




