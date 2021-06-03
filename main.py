import os


introMsg = """ 
****************************************************************************************
* Welcome,stranger.                                                                     *                                 
* Here in Hinderlands, you'll get to fight dragons and conquer the deadliest dungeons.  *                               
* In a country where magic rules, anything is possible if you wish so.                  *                          
* It all depends on you, brave hero.                                                    *              
****************************************************************************************
"""

print(introMsg)
print("Would you like to start the adventure ?")
user_answer = input("Yes or No -> ")
if user_answer.upper() == "YES":
    print("OK")
    os.system('cls')#windows
    #os.system('clear')  # mac/linux
else:
    print("Thank you, good bye")
