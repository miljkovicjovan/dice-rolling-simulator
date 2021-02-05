import random 
import os
os.system('cls')

def generate():
    number = random.randint(1,6)
    print("Dice Rolling Generator")
    print("made by @miljkovicjovan\n\n")
    if number == 1:
        print("[     ]")
        print("[  *  ]")
        print("[     ]")
    elif number == 2:
        print("[*    ]")
        print("[     ]")
        print("[    *]")
    elif number == 3:
        print("[  *  ]")
        print("[  *  ]")
        print("[  *  ]")
    elif number == 4:
        print("[*   *]")
        print("[     ]")
        print("[*   *]")
    elif number == 5:
        print("[*   *]")
        print("[  *  ]")
        print("[*   *]")
    elif number == 6:
        print("[*   *]")
        print("[*   *]")
        print("[*   *]")
    return

print('To roll the dice enter "y" \nTo exit the app enter "n"')

while True:
    choice = input()
    if choice == "y" or choice == "Y":
        os.system('cls')
        generate()
        print('To roll again enter "y"\nTo exit app enter "n"')
    elif choice == "n" or choice == "N":
        os.system('cls')
        exit()
    else:
        print("Wrong input, try again")




    