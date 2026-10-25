# password = 123

# for i in range(3):
#     guess = input("Enter password:")

#     if guess == password:
#         print("Acess Granted")
#         break
#     print("Access Denied")
# else:
#     print("Account Locked")


password = "hello123"
attempts = 0


while attempts < 3:
    user_password = input("Enter password: ")


    if user_password == password:
        print("Access Granted")
        break
    else:
        attempts += 1
        print("Access Denied")


        if attempts == 3:
            print("Account Locked")

