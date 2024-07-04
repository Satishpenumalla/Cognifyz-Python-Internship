def is_palindrome(str):
    start = 0
    end = len(str)-1

    while(start < end):
        if(str[start] == str[end]):
            start += 1
            end -= 1
        else:
            return False
    return True


string = input("Enter a Sting : ")

if(is_palindrome(string)):
    print(string + " is a palindrome")
else:
    print(string + " is not a palindrome")

