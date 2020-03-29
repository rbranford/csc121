import random


# Intro
def print_intro():
    print()
    print("~Welcome to Getaway~")
    print("In your attempt at robbing a bank, it appears you have been setup.")
    print("Law enforcement is hot on your tail and you are on foot running.")
    print("Your only option is to escape with the riches or be captured and spend life in prison.")
    print("You must escape!")
    print()

thirst = 0
leg_tiredness = 0 
police = -20
flask_drinks = 4

fountain = random.randrange(0, 20)

full_speed = random.randrange(10, 20)
moderate_speed = random.randrange(5, 12)


def main():
    
    print_intro()

    done = False
    miles_traveled = 0
    police_closing = random.randrange(10, 20)


    while not done:
    
        print("A. Drink from your hydro flask.")
        print("B. Ahead moderate speed.")
        print("C. Ahead full speed.")
        print("D. Stop for the night.")
        print("E. Status check.")
        print("Q. Quit")
        print()

        user_choice = input("What is your move? ")
        print()

        # Quit
        if user_choice.upper() == "Q":
            done = True
            print("You quit!")

        
        # Status
        elif user_choice.upper() == "E":
            print("Miles traveled: ", miles_traveled)
            print("Drinks in flask: ", flask_drinks)
            print("The police are", (police + 40), "miles behind you")
            print()

        
        # Stop for the night
        elif user_choice.upper() == "D":
            tiredness = 0
            print("Your legs feel great!")
            police_closing = police_closing + police
            print("The police are", police_closing, "miles behind you.")
            print()

        
        # Ahead full speed 
        elif user_choice.upper() == "C":
            if fountain == 1:
                print("Wow you found a fountain")
                canteen = 5
                thirst = 0
                tiredness = 0

            else:
                miles_traveled = miles_traveled + full_speed
                print("You walked", full_speed, "miles.")
                thirst += 1
                tiredness = tiredness + random.randrange(1, 4)
                police_closing = police_closing + police
                print(police)
                print("The police are", police_closing, "miles behind you.")
                print()

        
        # Ahead moderate speed 
        elif user_choice.upper() == "B":
            if fountain == 1:
                print("Wow you found a fountain!")
                canteen = 5
                thirst = 0
                tiredness = 0

            else:
                miles_traveled = miles_traveled + moderate_speed
                print("You walked", moderate_speed, "miles")
                thirst += 1
                tiredness = tiredness + random.randrange(1, 3)
                police_closing = police_closing + police
                print("The police are", police_closing, "miles behind you.")
                print()

        
        # Drink from hydro flask
        elif user_choice.upper() == "A":
            if canteen >= 1:
                canteen -= 1
                thirst = 0
            if canteen == 0:
                print("You have no drinks in the flask!")
                print()

            if miles_traveled >= 200:
                print("You have won!")
                done = True

            if not done and thirst >= 6:
                print("You died of thirst!")
                done = True
                print()

            if not done and thirst >= 4:
                print("You are thirsty.")
                print()

            if not done and tiredness >= 8:
                print("Your legs are broken")
                done = True
                print()

            if not done and tiredness >= 5:
                print("Your legs are getting tired.")
                print()

            if police_closing >= miles_traveled:
                print("The police have caught you!")
                done = True
                print()

            elif police_closing <= 15:
                print("The police are getting close!")
                print()
           
        

if __name__ == '__main__':
    main()