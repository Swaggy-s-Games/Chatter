def main():
    import json
    import sys
    import time

    print()
    print()
    print(" - Welcome to the 'Keyword Center'")
    print()
    print()
    userInput = input("Wich keyword would you like to change? 1-4 : ")
    print()
    print()
    if userInput == "1":
        kw1File = open("Keywords\Keyword1.txt", "r")
        kw1Print = kw1File.readlines()
        print("Current keyword : " + str(kw1Print))
        kw1File.close()
        print()
        print()
        kw1Input = input("New keyword! : ")
        if kw1Input == "":
            print()
            print()
            print("Incorrect")
            time.sleep(1)
            main()
        kw1Writer = open("Keywords\Keyword1.txt", "w")
        kw1Writer.write(kw1Input)
        kw1Writer.close()
        print()
        print()
        print("Succes")
        print()
        print()
        Restart1 = input("Restart? y/n : ")
        if Restart1.lower() == "y":
            main()
        else:
            sys.exit()
    
    if userInput == "2":
        kw2File = open("Keywords\Keyword2.txt", "r")
        kw2Print = kw2File.readlines()
        print("Current keyword : " + str(kw2Print))
        kw2File.close()
        print()
        print()
        kw2Input = input("New keyword! : ")
        if kw2Input == "":
            print()
            print()
            print("Incorrect")
            time.sleep(1)
            main()
        kw2Writer = open("Keywords\Keyword2.txt", "w")
        kw2Writer.write(kw2Input)
        kw2Writer.close()
        print()
        print()
        print("Succes")
        print()
        print()
        Restart2 = input("Restart? y/n : ")
        if Restart2.lower() == "y":
            main()
        else:
            sys.exit()
    
    if userInput == "3":
        kw3File = open("Keywords\Keyword3.txt", "r")
        kw3Print = kw3File.readlines()
        print("Current keyword : " + str(kw3Print))
        kw3File.close()
        print()
        print()
        kw3Input = input("New keyword! : ")
        if kw3Input == "":
            print()
            print()
            print("Incorrect")
            time.sleep(1)
            main()
        kw3Writer = open("Keywords\Keyword3.txt", "w")
        kw3Writer.write(kw3Input)
        kw3Writer.close()
        print()
        print()
        print("Succes")
        print()
        print()
        Restart3 = input("Restart? y/n : ")
        if Restart3.lower() == "y":
            main()
        else:
            sys.exit()
    
    if userInput == "4":
        kw4File = open("Keywords\Keyword4.txt", "r")
        kw4Print = kw4File.readlines()
        print("Current keyword : " + str(kw4Print))
        kw4File.close()
        print()
        print()
        kw4Input = input("New keyword! : ")
        if kw4Input == "":
            print()
            print()
            print("Incorrect")
            time.sleep(1)
            main()
        kw4Writer = open("Keywords\Keyword4.txt", "w")
        kw4Writer.write(kw4Input)
        kw4Writer.close()
        print()
        print()
        print("Succes")
        print()
        print()
        Restart4 = input("Restart? y/n : ")
        if Restart4.lower() == "y":
            main()
        else:
            sys.exit()

main()