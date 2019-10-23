from __future__ import print_function
import random

def Craps():
    print ("Welcome...")
    guess = str(raw_input("Pass or Don't Pass the line?: "))
    Dice1 = random.randint(1,6)
    Dice2 = random.randint(1,6)
    Dice3 = random.randint(1,6)
    Dice4 = random.randint(1,6)
    RollVal1 = Dice1+Dice2
    RollVal2 = Dice3+Dice4
    lose = (2,3,12)
    natural = (7,11)
    print ("Rolled:", RollVal1)
    if guess == "Pass" or guess == "pass" or guess == "P" or guess == "p":
        pass1 = 1
        play = 1
    else:
        pass1 = 0
        play = 1
    if RollVal1 in lose:
        if pass1 == 1:
            print ("Craps! You lose!", RollVal1)
        else:
            print ("Congrats!", RollVal1)
    else:
        if RollVal1 in natural:
            if pass1 == 1:
                print ("Lucky Shot!! You win!", RollVal1)
            else:
                print ("Should've passed the line...", RollVal1)
        else:
          while (True):
                print("Roll!")
                print(RollVal2)
                if RollVal2 == 7 or RollVal2 == RollVal1:
                    if RollVal2 == 7 and RollVal1 != RollVal2:
                        if pass1==1:
                            print("You Lose! You rolled", RollVal2,"and your first roll was", RollVal1,".")
                            playagain = str(raw_input("Play again? Yes or No?: "))
                            if playagain == "Yes" or playagain == "yes":
                              Craps()
                            else:
                              print("Nope! Too bad!")
                              Craps()
                            break
                        else:
                            print("You're one lucky gambler! You rolled a", RollVal2)
                            playagain = str(raw_input("Play again? Yes or No?: "))
                            if playagain == "Yes" or playagain == "yes":
                              Craps()
                            else:
                              print("Nope! Too bad!")
                              Craps()
                            break
                    else:
                        if pass1==1:
                            print("You Win! You rolled", RollVal2,"and your first roll was", RollVal1,".")
                            playagain = str(raw_input("Play again? Yes or No?: "))
                            if playagain == "Yes" or playagain == "yes":
                              Craps()
                            else:
                              print("Nope! Too bad!")
                              Craps()
                            break
                        else:
                            print("The odds were not in your favor today friend. You rolled a", RollVal2)
                            playagain = str(raw_input("Play again? Yes or No?: "))
                            if playagain == "Yes" or playagain == "yes":
                              Craps()
                            else:
                              print("Nope! Too bad!")
                              Craps()
                            break
                else:     
                    Dice3 = random.randint(1,6)
                    Dice4 = random.randint(1,6)
                    RollVal2 = Dice3 + Dice4
                    continue
        if play == 1 :
          playagain = str(raw_input("Play again? Yes or No?: "))
          if playagain == "Yes" or playagain == "yes":
           Craps()
          else:
            print("Nope! Too bad!")
            Craps()
Craps()