#! python3

"""
 Have the user enter a username 
 If the username is not "admin" then tell them it is an "invalid user", 
 but if it is, then ask them for a password 
 If they get the password correct (password is 12345password) 
 then display the message "Access granted"
 remember to use .strip() when retrieving strings or you will
 include hidden characters (the carriage return) that will
 not match
 1 marks

 Example:
 Enter username: admin
 Enter password: 12345password
 Access granted

 Enter username: notadmin
 invalid user

 Enter username: admin
 Enter password: password
 Access denied
"""
x = str(input("Enter a username")).strip()
if x != "admin":
    print("Invalid User")
    exit()
y =str(input("enter a password")).strip()
if y == "12345password":
    print("Access Granted")
elif y != "12455password":
    print("Access denied")