a=int(input("enter a number between 1 and 15"))
match a:
    case 1 :
        print("you won a car")
    case 2 :
        print("you won a dollar")
    case 3 :
        print("you won a house")
    case 4 :
        print("you won a bike")
    case 5 :
        print("you won a cycle")
    case _ :
        print("try again")