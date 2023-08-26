# passwor generator
import random

Aa1 = ["A","B","C","D","E","F","G","H","I","J",
       "K","L","M","N","O","P","Q","R","S","T",
       "U","V","W","X","Y","Z","a","b","c","d",
       "e","f","g","h","i","j","k","l","m","n",
       "o","p","q","r","s","t","u","v","w","x",
       "y","z","1","2","3","4","5","6","7","8",
       "9"]

Ala = ["A","B","C","D","E","F","G","H","I","J",
       "K","L","M","N","O","P","Q","R","S","T",
       "U","V","W","X","Y","Z","a","b","c","d",
       "e","f","g","h","i","j","k","l","m","n",
       "o","p","q","r","s","t","u","v","w","x",
       "y","z"]

a = ["a","b","c","d","e","f","g","h","i",
            "j","k","l","m","n","o","p","q","r",
            "s","t","u","v","w","x","y","z"]

a1 = ["a","b","c","d","e","f","g","h","i",
      "j","k","l","m","n","o","p","q","r",
      "s","t","u","v","w","x","y","z","1",
      "2","3","4","5","6","7","8","9"]

Al = ["A","B","C","D","E","F","G","H","I",
      "J","K","L","M","N","O","P","Q","R",
      "S","T","U","V","W","X","Y","Z"]

Al1 = ["A","B","C","D","E","F","G","H","I",
       "J","K","L","M","N","O","P","Q","R",
       "S","T","U","V","W","X","Y","Z","1",
       "2","3","4","5","6","7","8","9"]

password = []

def generator1(n):
    i=0
    while i < n:
        password.append(random.randint(0,9))
        i += 1
    return password

def generatorA(n):
    i=0
    while i < n:
        password.append(random.choice(Al))
        i += 1
    return password

def generatora(n):
    i=0
    while i < n:
        password.append(random.choice(a))
        i += 1
    return password

def generatorAa(n):
    i=0
    while i < n:
        password.append(random.choice(Ala))
        i += 1
    return password

def generatora1(n):
    i=0
    while i < n:
        password.append(random.choice(a1))
        i += 1
    return password

def generatorA1(n):
    i=0
    while i < n:
        password.append(random.choice(Al1))
        i += 1
    return password

def generatorAa1(n):
    i=0
    while i < n:
        password.append(random.choice(Aa1))
        i += 1
    return password

intro1 = str(input("Do you want letters and numbers in your password? (y/n)"))
if intro1 == "y":

    intro3 = str(input("Do you want uppercases, downcases or both? (u/d/b)"))
    if intro3 == "b":
        n = int(input("How many letters and number do you want? "))
        print("".join(map(str, generatorAa1(n))))
    elif intro3 == "d":
        n = int(input("How many letters and number do you want? "))
        print("".join(map(str, generatora1(n))))
    else:
        n = int(input("How many letters and number do you want? "))
        print("".join(map(str, generatorA1(n))))
else:
    intro2 = str(input("Only letter or numbers? (l/n)"))
    if intro2 == "l":
        intro3 = str(input("Do you want uppercases, downcases or both? (u/d/b)"))
        if intro3 == "b":
            n = int(input("How many letters do you want? "))
            print("".join(map(str, generatorAa(n))))
        elif intro3 == "d":
            n = int(input("How many letters do you want? "))
            print("".join(map(str, generatora(n))))
        else:
            n = int(input("How many letters do you want? "))
            print("".join(map(str, generatorA(n))))
    else:
        n = int(input("How many numbers do you want? "))
        print("".join(map(str, generator1(n))))