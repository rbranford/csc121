for i in range(10):
    print("Hi")
 
for i in range(5):
    print("Hello")
print("There")
 
for i in range(5):
    print("Hello")
    print("There")
 
for i in range(10):
    print(i)
 
for i in range(1, 11):
    print(i)
 
for i in range(10):
    print(i + 1)
 
for i in range(2, 12, 2):
    print(i)
 
for i in range(5):
    print((i + 1) * 2)
 
for i in range(10, 0, -1):
    print(i)
 
for i in [2, 6, 4, 2, 4, 6, 7, 4]:
    print(i)

for i in range(3):
    print("a")
    for j in range(3):
        print("b")

a = 0
for i in range(10):
    a = a + 1
print(a)

a = 0
for i in range(10):
    a = a + 1
for j in range(10):
    a = a + 1
print(a)

a = 0
for i in range(10):
    a = a + 1
    for j in range(10):
        a = a + 1
print(a)

sum = 0
for i in range(1, 101):
    sum = sum + i




i = 0
while i < 10:
    print(i)
    i = i + 1

for i in range(10):
    print(i)





i = 0
while i < 10:
    print(i)
    i += 1

i = 1
while i <= 2**32:
    print(i)
    i *= 2

quit = "n"
while quit == "n":
    quit = input("Do you want to quit? ")

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
 
    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True
 
value = 0
increment = 0.5
while value < 0.999:
    value += increment
    increment *= 0.5
    print(value)

i = 10
while i >= 0:
    print(i)
    i -= 1

i = 1
while i <= 10:
    print(i)
    i += 1




#import random
  
#def main():
  
#    print("Hi! I'm thinking of a random number between 1 and 100.")

#    secret_number = random.randrange(1, 101)
#    user_attempt_number = 1
#    user_guess = 0

#    while user_guess != secret_number and user_attempt_number < 8:

#        print("--- Attempt", user_attempt_number)
#        user_input_text = input("Guess what number I am thinking of: ")
#        user_guess = int(user_input_text)
 
        
#        if user_guess > secret_number:
#            print("Too high.")
#        elif user_guess < secret_number:
#            print("Too low.")
#        else:
#            print("You got it!")
 
#        user_attempt_number += 1
 
#    if user_guess != secret_number:
#        print("Aw, you ran out of tries. The number was " + str(secret_number) + ".")

#main()




import math
import random
 
 
def print_instructions():
    print("""
        Welcome to Mudball! The idea is to hit the other player with a mudball.
        Enter your angle (in degrees) and the amount of PSI to charge your gun
        with.
        """)
 
def calculate_distance(psi, angle_in_degrees):
    """ Calculate the distance the mudball flies. """
    angle_in_radians = math.radians(angle_in_degrees)
    distance = .5 * psi ** 2 * math.sin(angle_in_radians) * math.cos(angle_in_radians)
    return distance 

def get_user_input(name):
 
    psi = float(input(name + " charge the gun with how many psi? "))
    angle = float(input(name + " move the gun at what angle? "))
    return psi, angle
  
  
def get_player_names():
    """ Get a list of names from the players. """
    print("Enter player names. Enter as many players as you like.")
    done = False
    players = []
    while not done:
        player = input("Enter player (hit enter to quit): ")
        if len(player) > 0:
            players.append(player)
        else:
            done = True
  
    print()
    return players
  
  
def process_player_turn(player_name, distance_apart):

    psi, angle = get_user_input(player_name)
  
    distance_mudball = calculate_distance(psi, angle)
    difference = distance_mudball - distance_apart
 
    if difference > 1:
        print("You went", difference, "yards too far!")
    elif difference < -1:
        print("You were", difference * -1, "yards too short!")
    else:
        print("Hit!", player_name, "wins!")
        return True
  
    print()
    return False
  
  
def main():
  
    print_instructions()
    player_names = get_player_names()
    distance_apart = random.randrange(50, 150)
  
    done = False
    while not done:
        for player_name in player_names:
            done = process_player_turn(player_name, distance_apart)
            if done:
                break

if __name__ == "__main__":
    main()
    
