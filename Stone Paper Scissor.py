import random

def gamewin(comp,you):
    if comp==you:
        return 'Tie'
    elif comp=='s':
        if you=='c':
            return False
        elif you=='p':
            return True
    elif comp=='p':
        if you=='s':
            return False
        elif you=='c':
            return True
    elif comp=='c':
        if you=='p':
            return False
        elif you=='s':
            return True
    else:
        return None

def main():
    try:
        you = input("Your Turn : Stone(s),Paper(p),Scissor(c) : \n").lower()
        print("Computer's Turn : Stone(s),Paper(p),Scissor(c) : ")
        no = random.randint(1,3)
        if no==1:
            comp='s'
        elif no==2:
            comp='p'
        elif no==3:
            comp='c'

        print("Computer Choose : ",comp)
        print("You Choose : ",you)

        x=gamewin(comp,you)

        if x=='Tie':
            print("Game is Tie...")
        elif x: 
            print("You Win !, Congratulations.")
        elif x==None:
            print("Please Enter Valid Input !!")
            main()
        else:
            print("You Lose. Better Luck Next Time..")
    except:
        print("Please Enter Valid Input !!")
        main()

main()