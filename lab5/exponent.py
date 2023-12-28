def is_palindrome(string):
    if len(string) <= 1:
        return True
    if string[0] == string[-1]:

        return is_palindrome(string[1:-1])
    else:
        return False
input_string = input("Enter a string: ")
input_string = input_string.replace(" ", "").lower()
if is_palindrome(input_string):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
