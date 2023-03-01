import print_cards
import values
import random
import time 
import os

def cls():
    os.system('cls')

#initiate the cards
class Card:
    def __init__(self,suit,value,card_value):
        self.suit=suit
        self.value=value
        self.card_value=card_value

def blackjack_game(deck):
    global cards_value
    player_cards=[]
    dealers_cards=[]
    player_score=0
    dealers_score=0

    cls()
    #PHASE1
    while len(player_cards)<2:
        player_card=random.choice(deck)
        player_cards.append(player_card)
        deck.remove(player_card)
        player_score += player_card.card_value

        if len(player_cards)==2:
            if player_cards[0].card_value == 11 and player_cards[1].card_value == 11:
                player_cards[0].card_value=1
                player_score-=10

        cls()
        print("PLAYER'S CARDS:")
        print_cards.print_cards(player_cards,False)
        print("PLAYER'S SCORE:{}".format(player_score)) 
    
        input()  

        dealers_card=random.choice(deck)
        dealers_cards.append(dealers_card)
        deck.remove(dealers_card)
        dealers_score+=dealers_card.card_value
    
        print("DEALER'S CARD:")
        if len(dealers_cards)== 1:
            print_cards.print_cards(dealers_cards,0)
            print("DEALER'S SCORE:",dealers_score)
        else:
            print_cards.print_cards(dealers_cards[:-1],1)
            print("DEALER'S SCORE:", dealers_score - dealers_cards[-1].card_value)

        if len(dealers_cards)==2:
            if dealers_cards[0].card_value==11 and dealers_cards[1].card_value==11:
                dealers_cards[0].card_value=1
                dealers_score-=10

        input()

    if player_score==21:
        print("BLACKJACK ! PLAYER WINS")
        quit()

    cls()
    #PHASE 2
    print("DEALER'S CARDS: ")
    print_cards.print_cards(dealers_cards[:-1],1)
    print("DEALER'S SCORE:",dealers_score-dealers_cards[-1].card_value)

    print()

    print("PLAYER'S CARDS: ")
    print_cards.print_cards(player_cards,0)
    print("PLAYER'S SCORE:",player_score)

    #Happens during the process of playing the game
    while player_score<21:
        choice=input("Enters H to hit and S to stand:")
        if len(choice)!= 1 or (choice.upper()!='H' and choice.upper!='S'):
            cls()
            print("Wrong choice, try again")

        if choice.upper()=='H':
            player_card=random.choice(deck)
            player_cards.append(player_card)
            deck.remove(player_card)

            player_score += player_card.card_value

        c=0
        while player_score > 21 and c < len(player_cards):
            if player_cards[c].card_value == 11:
                player_cards[c].card_value == 1
                player_score -= 10
                c+=1
            else:
                c+=1

        cls()

        print("DEALER'S CARD:")
        print_cards.print_cards(dealers_cards[:-1],1)
        print("DEALER'S SCORE:",dealers_score-dealers_cards[-1].card_value)

        print()

        print("PLAYER'S CARD:")
        print_cards.print_cards(player_cards,0)
        print("PLAYER'S SCORE:",player_score)


        if choice.upper() ==  'S':
            break
    
    if player_score == 21:
        print("PLAYER HAS A BLACKJACK !")
        quit()

    if player_score >21:
        print("PLAYER BUSTED!! GAME OVER!")
        quit()

    input()

    #PHASE 3
    while dealers_score<player_score:
        cls()    
        print("DEALER DECIDE TO HIT..........")
        
        time.sleep(2)

        dealers_card=random.choice(deck)
        dealers_cards.append(dealers_card)
        deck.remove(dealers_card)

        dealers_score+=dealers_card.card_value

        c=0
        while dealers_score>21 and c<len(dealers_cards):
            if dealers_cards[c].card_value==11:
                dealers_cards[c].card_value=1
                dealer_score=10
                c+=1
            else:
                c+=1
        
        print("PLAYER'S CARD:")
        print_cards.print_cards(player_cards,0)
        print("PLAYER'S SCORE",player_score)

        print()

        print("DEALER'S CARD:")
        print_cards.print_cards(dealers_cards,0)
        print("DEALER'S SCORE:",dealers_score)

        input()

        if dealers_score > 21:
            print("DEALER BUSTED!! YOU WIN!")
            quit()

        if dealers_score==21:
            print("DEALER HAS A BLACKJACK !! PLAYER LOSES!")
            quit()

        if dealers_score>player_score:
            print("DEALER WINS!!!")
        elif dealers_score<player_score:
            print("PLAYER WINS!!!") 
        else:
            print("IT'S A TIE!!!")   

if __name__ == '__main__':
    #Initiate the deck to play with
    deck = []
    for suits in values.suits:
        for cards in values.cards:
            deck.append(Card(values.suits_values[suits],cards,values.cards_values[cards]))
    
    #Play the game
    blackjack_game(deck)