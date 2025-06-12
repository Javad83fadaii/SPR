while True:
    print("1) pack password \n 2) on pack password\n 3) exit")
    if int(input("Enter your choice: ")) == 1:
        text_user = input("Enter your text: ")
        for c in text_user:
            x = ord(c) * 5 + 2
            print(chr(x), end="")
        print("\n")
        print("Thank You")
        print("*"*40)
        
    elif int(input("Enter your choice: ")) == 2:
        text_user = input("Enter your text: ")
        for c in text_user:
            x = (ord(c) - 2) // 5
            print(chr(x), end="")
        print("\n")1
        print("Thank You")
        print("*" * 40)
    elif int(input("Enter your choice: ")) == 3:
        print("Thank you!")
    else: print("Invalid choice")
