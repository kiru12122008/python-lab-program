name = input("enter the name :")
n = int (input ("enter the number of subjects:"))
total = 0
for i in range (1,n+1):
    marks = float (input (f"enter the mark for subect {i}:"))
    total += marks

percentage = total/n

if percentage >=90 :
    grade = "A+"
    perfomance = "outstanding "
elif percentage >= 80 :
    grade = "A"
    perfomance = "excellent "
elif percentage >= 70:
    grade = "B"
    perfomance = "very good "
elif percentage >= 60:
    grade = "C"
    perfomance = "good"
elif percentage >=50:
    grade = "D"
    perfomane = " average"
elif percentage >=40 :
    grade = "E"
    perfomance = "need improvement "
else :
    grade = "F"
    perfomance = "fail"

print ("----student academic details----")
print ("NAME:",name)
print ("TOTAL MARKS:",total)
print ("PERCENTAGE :",percentage)
print ("GRADE:",grade)
print ("PERFOMANCE:",perfomance)

