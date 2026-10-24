# age = int(input("Enter age :"))

# if age >= 18:
#     print("คุณมีสิทธิ์เข้าร่วม")
# else:
#     print("คุณไม่มีสิทธิ์เข้าร่วม")


age = int(input("Enter age : "))
has_ticket = True

if age >= 18 and has_ticket:
    print("You can access")
else:
    print("Access Denied") 

