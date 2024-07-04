total_marks = 750
obtained_marks = float(input("Enter obtained marks: "))

percentage = (obtained_marks / total_marks) *100
print("Your percentage is ", percentage)

if percentage >= 90:
    print("Your Grade is A+")
elif percentage >= 80:
    print("Your Grade is A")  
elif percentage >= 70:
    print("Your Grade is B")
elif percentage >= 60:
    print("Your Grade is C")
elif percentage >= 50:
    print("Your Grade is D")
elif percentage >= 40:
    print("Your Grade is E")
else:
    print("Your Grade is F")