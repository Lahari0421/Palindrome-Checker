def is_palindrome(text):
    cleaned = ''.join(text.lower().split())
    return cleaned == cleaned[::-1]
user_input = input("Enter a word or phrase: ")

if is_palindrome(user_input):
    print("It's a palindrome!")
else:
    print("Not a palindrome.")
