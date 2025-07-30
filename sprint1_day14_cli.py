import argparse

def main():
    parser=argparse.ArgumentParser(description="MyApp: unit converter and flashcard quiz")
    subparser=parser.add_subparsers(dest="command",required=True)
    converter=subparser.add_parser("converter", help="Run unit converters")
    converter.add_argument("--km-to-miles",type=float,help="Convert kilometers to miles")
    converter.add_argument("--miles-to-km",type=float,help="Convert miles to kilometers")
    converter.add_argument("--c-to-f",type=float,help="Convert Celsius to Farenheit")
    converter.add_argument("--f-to-c",type=float,help="Convert Farenheit to Celsius")
    converter.add_argument("--kg-to-lbs",type=float,help="Convert kilograms to pounds ")
    converter.add_argument("--lbs-to-kg",type=float,help="Convert pounds to kilograms")

    quiz=subparser.add_parser("quiz",help="Run the flash card quiz")

    args=parser.parse_args()

    if args.command == "converter":
        from myapp.converter import (
            km_to_miles, miles_to_km, c_to_f, f_to_c, lbs_to_kg, kg_to_lbs
        )

        if args.km_to_miles is not None:
            print(km_to_miles(args.km_to_miles))
        elif args.miles_to_km is not None:
            print(miles_to_km(args.miles_to_km))
        elif args.c_to_f is not None:
            print(c_to_f(args.c_to_f))
        elif args.f_to_c is not None:
            print(f_to_c(args.f_to_c))
        elif args.lbs_to_kg is not None:
            print(lbs_to_kg(args.lbs_to_kg))
        elif args.kg_to_lbs is not None:
            print(kg_to_lbs(args.kg_to_lbs))
        else:
            converter.print_help()   # show converter usage

    else:  # args.command == "quiz"
        from myapp.quizzer import main as quiz_main
        quiz_main()

if __name__ == "__main__":
    main()




    