print("this code will always execute.")
def main():
    print("This code belongs to the main function in module1.")
    print("Module #1 Name=", __name__)

if __name__ == "__main__":
    main()
    print("Code is being run directly from Python")

else:
    print("Code is being run indirectly from import.")
