#check if string is palindrome

user_input=input('Enter text: ')

new_lower_input=user_input.lower()
checked_input=''.join(ch for ch in new_lower_input if ch.isalnum())

if checked_input==checked_input[::-1]:
    print('palindrome')
else:
    print('not a palindrome')