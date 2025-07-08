def parse_numbers(raw):
    return [int(x.strip()) for x in raw.split(",") if x.strip()]

def main():
    raw = input("Enter numbers, comma-separated: ")
    nums = parse_numbers(raw)

    squares = [n*n for n in nums]
    print("Squares:", squares)

    evens = [n for n in nums if n % 2 == 0]
    print("Evens:", evens)

    digit_chars = {d for n in nums for d in str(abs(n))}
    digits = sorted(int(d) for d in digit_chars)
    print("Unique digits:", digits)

    combos = [(x, y) for x in nums for y in nums]
    print("Combinations:", combos)

if __name__ == "__main__":
    main()
