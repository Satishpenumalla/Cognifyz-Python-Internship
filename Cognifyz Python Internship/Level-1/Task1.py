def string_reverse(string):
    return string[::-1]


string = input("Enter a String : ")
print("The Original String is:", string)

print("The reversed String is : " + string_reverse(string))
