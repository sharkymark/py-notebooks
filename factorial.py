import argparse

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def main():
    parser = argparse.ArgumentParser(description="Calculate the factorial of a given number.")
    parser.add_argument("number", type=int, help="The number to calculate the factorial for")
    args = parser.parse_args()
    
    result = factorial(args.number)
    print(f"The factorial of {args.number} is {result}")

if __name__ == "__main__":
    main()
