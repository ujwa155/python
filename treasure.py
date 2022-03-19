print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
''')
print("welcome to the tresure island.")

choice1 = input('you\' re at a crossroad side,where do you want to go? Type "left" or "right".').lower()
if choice1 == "left":
     choice2 = input('you have come to the lake.there is an island in the middle of the lake. type "wait" to wait for the lake or type "swim" to swim in the lake.').lower()
     if choice2 == "wait":
          choice3 = input("you are at the island unharmed. there is a house with 3 door.one red, one yellow and one is blue.which colour do you choose?.").lower()
          if choice3 == "red":
               print("its a room full of fire.game over")
          elif choice3 == "yellow":
               print("you found a treasure! you win")
          elif choice3 == "blue":
               print("you enter s room of beasts.game over")
          else:
               print("you chose a door that doesnot exit.game over")
     else:
          print("you got attacked by an angry trout.game over")
else:
          print("you fell into hole.game over")
          
