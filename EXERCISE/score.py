# def gradeCheck(n):
#     if (n >= 0 and n <= 100):
#         if (n >= 80):
#             return "Your grade is A"
#         elif (n >= 70):
#             return "Your grade is B"
#         elif (n >= 60):
#             return "Your grade is C"
#         elif (n >= 50):
#             return "Your grade is D"
#         else:
#             return "Your grade is F"
#     else:
#         return "Invalid Score"
# score = int(input("Enter score: "))
# result = gradeCheck(score)
# print(result) 


score = float(input("Enter score: "))


if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 80:
    print("Your grade is A")
elif score >= 70:
    print("Your grade is B")
elif score >= 60:
    print("Your grade is C")
elif score >= 50:
    print("Your grade is D")
else:
    print("Your grade is F")
