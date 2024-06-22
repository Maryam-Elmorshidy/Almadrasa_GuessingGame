# libraries
import random

# start of game
print("_____________________________________\n\n ✨ Welcome everybody✨ \n Are you ready✨ \n ")

attempt = 0

success = 0
while True :

    x = input("Do you want to play (y/n)?\n ").lower()
    if x == 'n' :
        print(f"number of your attempts : {attempt} ")
        print(f"number of your success : {success} ")
        print("good bye 👋👋")
        exit()
    elif x == "y" :
        choicePC = random.randint(1,10)
        while True :
            try :
                choicePlayer = int(input("please enter number between 1 and 10 : "))
                if choicePlayer > 10 or choicePlayer < 1 :
                    raise ValueError("It's out of range")
                    #print("It's out of range")
                    #continue
            except ValueError as arr :
                print(arr)        
            else :
                if choicePlayer == choicePC :
                    print("nice , guess is right ")
                    attempt +=1
                    success +=1
                    print(f"number of your attempts : {attempt} ")
                    print(f"number of your success : {success} ")
                    print("_____________________ \n")
                    break
                elif choicePlayer < choicePC :
                    print("It's upper")
                    attempt +=1
                    continue
                elif choicePlayer > choicePC :
                    print("It's lower")
                    attempt +=1
                    continue



    else :
        print("please enter correct answer")     
