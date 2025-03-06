import random

cards = [1,2,3,4,5,6,7,8,9,10,10,10,10]
house = [10,10,9,9,8,7,2,3]
cash = 1

def hand(): 
    you = random.choice(cards) + random.choice(cards)
    return you

def opponent():
    opponent = 10 + random.choice(house)
    return opponent

def blackjack():
    money = 3000
    cash = 1
    x = hand()
    y = opponent()
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
            elif y > 21:
                print("Your opponent went over 21.")
                money = money + bet
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
        print("You have: " + str(money) + " Dollars.")
        question = input("Do you want to play again? ")
        if question == "no":
            break
        elif question == "yes":
            x = hand()
            y = opponent()
            cash = 1
        else:
            print("I'm gonna guess that's a yes.")
            x = hand()
            y = opponent()
            cash = 1

blackjack()