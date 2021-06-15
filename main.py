import os
import Player
import Enemy

import simpleaudio as sa
import winsound
import random

import pygame
pygame.init()
pygame.mixer.init()


introMsg = """ 
****************************************************************************************
* Welcome,stranger.                                                                     *                                 
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.  *                               
* In a country where magic rules, anything is possible if you wish so.                  *                          
* It all depends on you, brave hero.                                                    *              
****************************************************************************************
"""

sound = "Main_Menu.wav"
#sounda= pygame.mixer.Sound(sound)
#sounda.play()
winsound.PlaySound(sound, winsound.SND_ASYNC)
print(introMsg)
print("Would you like to start the adventure ?")
user_answer = input("Yes or No -> ")
if user_answer.upper() == "YES":
    print("OK")
    os.system('cls')#windows
    #os.system('clear')  # mac/linux
    answer = input("""What type of player are you: 
1 for Warrior 2 for Wizard -> """)
    if answer == '1':
        player_name = input("""You have chosen to be a mighty warrior
What is your name? ->  """)
        player = Player.Warrior(player_name)
        print("Intro to the world")
        input("Press a key to continue...")

        os.system('cls')
        sound = "Exploring.wav"
        winsound.PlaySound(sound, winsound.SND_ASYNC)
        print("""you are in the middle of a crossroads.
You have 3 paths in front of you:
1. Going to a village
2. Going to a forest
3. Going to a desert """)
        path_option = input("What is your destiny?->")

        '''Create a metod path(userPath)
        that uses the retruned value from crossroads method'''

        if(path_option == '1'):
            #in_the_village() from utils
            print("You are in the village...")
            print("From a backside ally a enemy appears")
            random_number = random.randint(0, 2)

            sound = "BattleFinal.wav"
            winsound.PlaySound(sound, winsound.SND_ASYNC)
            if random_number == 0:
                enemy = Enemy.Goblin()
                input("Press a key to continue...")
            elif random_number == 1:
                enemy = Enemy.Orc()
                input("Press a key to continue...")
            elif random_number == 2:
                enemy = Enemy.Rat()
                input("Press a key to continue...")
            else:
                print("Invalid enemy...")


        elif(path_option == '2'):
            #in_the_forest()
            print("You are in the forest...")
        elif path_option == '3':
            # in_the_desert()
            print("You are in the desert...")
        else:
            print("Path not available")









    elif answer == '2':
        player_name = input("""You have chosen to be a mighty wizard        
What is your name? ->  """)
        player = Player.Wizard(player_name)
        print("Intro to the world")
        os.system('cls')

    else:
        print("Chose a valid option")
else:
    print("Thank you, good bye")
