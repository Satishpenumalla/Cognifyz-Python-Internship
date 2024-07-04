password = input("Enter the password : ")

def  password_strength(password):
    count = 0
    if len(password) > 8:
        count += 1
    if any(ele.isupper() for ele in password):
        count += 1
    if any(ele.islower() for ele in password):
        count += 1
    if any(ele.isdigit() for ele in password):
        count += 1
    if any(not ele.isalnum() for ele in password):
        count += 1

    return count


strength = password_strength(password)
print("Your password strength is : ",(strength)/5*100,"%")


