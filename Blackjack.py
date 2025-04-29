import random
import time

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10,11]
house = [10,10,9,9,8,7,2,3]
cheats = [10,10,11,9]
cash = 1

def hand(): 
    you = random.choice(cards) + random.choice(cards)
    return you

def opponent(hand):
    opponent = 10 + random.choice(hand)
    return opponent

def blackjack(rich):
    money = rich
    cash = 1
    x = hand()
    y = opponent(house)
    print("You have: " + str(money) + " Dollars.")
    while True:
        while True:
            while cash == 1:
                bet = int(input("how much money do you want to bet? "))
                if bet > money:
                    print("Bet lower.")
                elif bet == money:
                    print("That's a bad idea.")
                else:
                    if bet >= 10000:
                        y = opponent(cheats)
                    cash = 0
            if x > 21:
                print("sorry, you went over 21!")
                money = money - bet
                print("Opponent had: " + str(y))
                break
            elif x == 21:
                print("You got 21!")
                money = money + bet
                print("Opponent had: " + str(y))
                break
            elif y == 21:
                print("Your opponent got 21.")
                money = money - bet
                break
            print("your hand is: " + str(x))
            ask = input("Hit or Fold? ")
            if ask == "hit":
                x += random.choice(cards)
                print(x)
            elif ask == "fold":
                if y > x:
                    print("Sorry, you lost!")
                    money = money - bet
                    print("Opponent had: " + str(y))
                    break
                elif y < x:
                    print("Wow, you won!")
                    money = money + bet
                    print("Opponent had: " + str(y))
                    break
        time.sleep(3)
        print("You have: " + str(money) + " Dollars.")
        time.sleep(2)
        question = input("Do you want to play again? ")
        if question == "no":
            break
        elif question == "yes":
            x = hand()
            y = opponent(house)
            cash = 1
        else:
            time.sleep(2.5)
            print("I'm gonna guess that's a yes.")
            x = hand()
            y = opponent(house)
            cash = 1
starting_money  = random.randint(3,10) * 1000
blackjack(starting_money)