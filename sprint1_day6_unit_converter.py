def km_to_miles(km):
    return km * 0.621371

def miles_to_km(mi):
    return mi / 0.621371

def c_to_f(c):
    return c * 9/5 + 32

def f_to_c(f):
    return (f - 32) * 5/9

def lbs_to_kg(lbs):
    return lbs * 0.453592

def kg_to_lbs(kg):
    return kg / 0.453592

def check_for_proper_input(prompt):
    while True:
        user_input = input(prompt).strip()
        try:
            return float(user_input)
        except ValueError:
            print('Please only enter numbers')
    

def main():
    while True:
        print("\nUnit Converter")
        print("  1) km → miles")
        print("  2) miles → km")
        print("  3) °C → °F")
        print("  4) °F → °C")
        print("  5) lbs → kg")
        print("  6) kg → lbs")
        print("  Q) Quit")
        choice = input('Choose the following options or (Q)uit:  ').strip().lower()

        if choice == '1':
            user_input = check_for_proper_input("Enter the number of kilometers you want to convert: ")
            print(f'{user_input} km is {km_to_miles(user_input)} miles')

        elif choice == '2':
            user_input = check_for_proper_input("How many miles do you want to convert to kilometers: ")
            print(f'{user_input} miles is {miles_to_km(user_input)} km')

        elif choice == '3':
            user_input = check_for_proper_input("How many degrees Celsius do you want to convert to Fahrenheit: ")
            print(f'{user_input}°C is {c_to_f(user_input)}°F')

        elif choice == '4':
            user_input = check_for_proper_input("How many degrees Fahrenheit do you want to convert to Celsius: ")
            print(f'{user_input}°F is {f_to_c(user_input)}°C')

        elif choice == '5':
            user_input = check_for_proper_input("How many pounds would you like to convert to kilograms: ")
            print(f'{user_input} lb is {lbs_to_kg(user_input)} kg')

        elif choice == '6':
            user_input = check_for_proper_input("How many kilograms would you like to convert to pounds: ")
            print(f'{user_input} kg is {kg_to_lbs(user_input)} lbs')

        elif choice == 'q':
            print('Goodbye!')
            break

        else:
            print('Not a valid choice — please choose 1–6 or Q.')

if __name__ == "__main__":
    main()
