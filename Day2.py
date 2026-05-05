#given marks = [78,85,90,67,85,92,78]
marks = [78,85,90,67,85,92,78]
i = 1
sum=0
while (i<=len(marks)):
    sum = marks[i-1] + sum 
    i+=1
average = sum/7.0
print("Average marks :")
print(average)
#maximum and minimum 
max = max(marks)
print("Maximum marks obtained :")
print(max)
min = min(marks)
print("Minimum marks obtained :")
print(min)
#count how many student scored above average 
count = 0
for i in range (1,len(marks)):
    if (marks[i-1]>average):
        count=count+1
print("Number of student scored more than average :")
print(count)
#Bonus 
score=int(input("Enter your score :"))
if ( score <=100 and score >90):
    print("You have scored A grade ")
elif(score <=90 and score >80):
    print("You have scored B grade ")
elif (score <=80 and score > 60 ):
    print("You have scored C grade ")
else :
    print("You are fail!")




    
    

