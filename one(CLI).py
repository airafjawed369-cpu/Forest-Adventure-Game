import random
health=100
score=0
def main():
    print("You are in the forest")
    print("1.Cave \n" \
    "2.River \n" \
    "3.Quit")
    try:
        n=int(input("Enter Choice: "))
        print("")
        if n==1:
            cave()
        elif n==2:
            river()
        elif n==3:
            print("Thanku for playing")
            print(f"Final health: {health}")
            print(f"Final Score: {score}")
            exit
        else:
            print("Invalid Choice. Enter 1,2 or 3")
            main()
    except:
        print("Invalid Choice. Enter 1,2 or 3")
        print("")
        main()
        

def cave():
    dam=30
    global health
    global score
    health-=dam
    if health>0:
        score+=20
        print("*********************************")
        print(f"CAVE: Cave spider attacks!! | Damage: {dam} Health: {health}")
        print(f"You've found a key in the cave | Score: {score}")
        print("*********************************")
        main()
    else:
        dead()
    

def dead():
    global health
    health=0
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    print("GAME OVER")
    print(f"You fought bravely and you have died a legend.")
    print(f"Final Health: {health}")
    print(f"Final Score: {score}")
    print("x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")

def river():
    global score
    score+=50
    print("*********************************")
    print(f"RIVER: You've found a treasure(+50 Score)!! \n| Score: {score} Health: {health}")
    print("*********************************")
    main()

main()