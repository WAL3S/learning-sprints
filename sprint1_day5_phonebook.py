#(A)dd  (L)ookup  (D)elete  (V)iew all  (Q)uit

phonebook = {}


while True:
    user_choice=input('Welcome to your phonebook, what would you like to do?\n(A)dd  (L)ookup  (D)elete  (V)iew all  (Q)uit: ')

    if user_choice.strip().lower()=='a':
        name_input=input('Name: ').strip().lower()
        number_input =input('Phone Number: ').strip()
        phonebook[name_input]=number_input
        print(f'Added {name_input} with number {number_input}')
    elif user_choice.strip().lower()=='l':
        if not phonebook:
            print("the phonebook is empty")
        else:
            name_presence = False
            name_input=input('Enter Name to Find Number: ').strip().lower()
            for name in phonebook:
                if name==name_input:
                    name_presence = True
            if name_presence==True:
                print(phonebook[name_input])
            else:
                print('Name is not in phonebook')
    elif user_choice.strip().lower()=='d':
        deleted_user_input=input('Name of user to delete: ')
        if deleted_user_input in phonebook:
            phonebook.pop(deleted_user_input, None)
            print(f"Sucessfully deleted {deleted_user_input}")
        else:
            print("Name not found")
    elif user_choice.strip().lower()=='v':
        if not phonebook:
            print('the phonebook is empty')
        else:
            for name in phonebook:
                print(f'{name}: {phonebook[name]}')
    elif user_choice.strip().lower() == 'q':
        print('bye!')
        break
    else:
        print('not a valid choice')
        