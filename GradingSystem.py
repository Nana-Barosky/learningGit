print("WELCOME TO KTU STUDENT PORTAL")
print("OPTIONS")
print("*******")
print("1. Register")
print("2. SIGN IN")
print("3. ENTER RESULT")
selectedOption = input("select your option: ")
if selectedOption=="1":
    username = input("ENTER USERNAME: ")
    password = input("ENTER PASSWORD: ")
    confirmPassword = input("CONFIRM PASSWORD: ")

    while password!=confirmPassword:
        print("Password does not match, Retype")
        password=input("Enter passwrod")
        confirmPassword = input("Confirm Password")

        print("Registered Successfully")

    # if password!=confirmPassword:
    #     print("Password does not match re-type")
    # else:
    #     print("SUCCESSFULL")


# if selectedOption == "1":
#     username = input("ENTER USERNAME: ")
#     password = input("ENTER PASSWORD: ")
#     confirmPassword = input("CONFIRM PASSWORD: ")

#     while password != confirmPassword:
#         print("Password does not match. Please retype.")
#         password = input("ENTER PASSWORD: ")
#         confirmPassword = input("CONFIRM PASSWORD: ")

#     print("Password confirmed.")


    
