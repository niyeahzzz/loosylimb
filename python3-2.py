import sys

def main():
    # Get a list of all functions in the os module
    os_functions = dir(sys)

    print("Functions available in the 'os' module:")
    for func in os_functions:
        print(func)

if __name__ == "__main__":
    main()
