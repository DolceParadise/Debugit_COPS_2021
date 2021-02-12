import os
import random
from framework import telegram_chatbot
import bot

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4

def deal(deck):
    hand = []
    for i in range(2):
	    random.shuffle(deck)
	    card = deck.pop()
	    if card == 11:card = "J"
	    if card == 12:card = "Q"
	    if card == 13:card = "K"
	    if card == 14:card = "A"
	    hand.append(card)
    return hand

def play_again():
    # again = input("Do you want to play again? (Y/N) : ").lower()
    framework.send_message("Do you want to play again? (Y/N) : ", from_)
    updates = framework.get_updates(offset=update_id).lower() 
    updates = updates["result"]
    if again == "y":
	    dealer_hand = []
	    player_hand = []
	    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]*4
	    game()
    else:
	    # print("Bye!")
        framework.send_message("Bye", from_)
        exit()      

def total(hand):
    tot = 0
    for card in hand:
	    if card == "J" or card == "Q" or card == "K":
	        tot+= 10
	    elif card == "A":
	        if tot >= 11: tot+= 1
	        else: tot+= 11
	    else: tot += card
    return tot

def hit(hand):
	card = deck.pop()
	if card == 11:card = "J"
	if card == 12:card = "Q"
	if card == 13:card = "K"
	if card == 14:card = "A"
	hand.append(card)
	return hand

def clear():
	if os.name == 'nt':
		os.system('CLS')
	if os.name == 'posix':
		os.system('clear')

def print_results(dealer_hand, player_hand):
	# print ("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)))
	# print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    framework.send_message("The dealer has a " + str(dealer_hand) + " for a total of " + str(total(dealer_hand)), from_)

def blackjack(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        framework.send_message("Congratulations! You got a Blackjack!\n", from_)
        play_again()
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        # print ("Sorry, you lose. The dealer got a blackjack.\n")
        framework.send_message("Sorry, you lose. The dealer got a blackjack.\n", from_)
        play_again()

def score(dealer_hand, player_hand):
    if total(player_hand) == 21:
        print_results(dealer_hand, player_hand)
        # print ("Congratulations! You got a Blackjack!\n")
        framework.send_message("Congratulations! You got a Blackjack!\n", from_)
    elif total(dealer_hand) == 21:
        print_results(dealer_hand, player_hand)		
        # print ("Sorry, you lose. The dealer got a blackjack.\n")
        framework.send_message("Sorry, you lose. The dealer got a blackjack.\n", from_)
    elif total(player_hand) > 21:
        print_results(dealer_hand, player_hand)
        # print ("Sorry. You busted. You lose.\n")
        framework.send_message("Sorry. You busted. You lose.\n", from_)
    elif total(dealer_hand) > 21:
        print_results(dealer_hand, player_hand)			   
        # print ("Dealer busts. You win!\n")
        framework.send_message("Dealer busts. You win!\n", from_)
    elif total(player_hand) < total(dealer_hand):
        print_results(dealer_hand, player_hand)
        #print ("Sorry. Your score isn't higher than the dealer. You lose.\n")
        framework.send_message("Sorry. Your score isn't higher than the dealer. You lose.\n", from_)
    elif total(player_hand) > total(dealer_hand):
        print_results(dealer_hand, player_hand)			   
        # print ("Congratulations. Your score is higher than the dealer. You win\n")		
        framework.send_message("Congratulations. Your score is higher than the dealer. You win\n", from_)

# def game():
# 	choice = 0
# 	clear()
# 	print ("WELCOME TO BLACKJACK!\n")
# 	dealer_hand = deal(deck)
# 	player_hand = deal(deck)
# 	while choice != "q":
# 		print ("The dealer is showing a " + str(dealer_hand[0]))
# 		print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
# 		blackjack(dealer_hand, player_hand)
# 		choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
# 		clear()
# 		if choice == "h":
# 			hit(player_hand)
# 			while total(dealer_hand) < 17:
# 				hit(dealer_hand)
# 			score(dealer_hand, player_hand)
# 			play_again()
# 		elif choice == "s":
# 			while total(dealer_hand) < 17:
# 				hit(dealer_hand)
# 			score(dealer_hand, player_hand)
# 			play_again()
# 		elif choice == "q":
# 			print ("Bye!")
# 			exit()
	
# if __name__ == "__main__":
#     game()

def game():
    choice = 0
    clear()
    # print ("WELCOME TO BLACKJACK!\n")
    framework.send_message("WELCOME TO BLACKJACK!\n", from_)
    dealer_hand = deal(deck)
    player_hand = deal(deck)
    # print ("The dealer is showing a " + str(dealer_hand[0]))
    # print ("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)))
    framework.send_message("The dealer is showing a " + str(dealer_hand[0]), from_)
    framework.send_message("You have a " + str(player_hand) + " for a total of " + str(total(player_hand)), from_)
    blackjack(dealer_hand, player_hand)
    quit=False
    while not quit:
        # choice = input("Do you want to [H]it, [S]tand, or [Q]uit: ").lower()
        framework.send_message("Do you want to [H]it, [S]tand, or [Q]uit: ", from_)
        updates = framework.get_updates(offset=update_id).lower() 
        updates = updates["result"]
        if choice == 'h':
            hit(player_hand)
            # print(player_hand)
            framework.send_message(player_hand, from_)
            if total(player_hand)>21:
                # print('You busted')
                framework.send_message('You busted', from_)
                play_again()
        elif choice=='s':
            while total(dealer_hand)<17:
                hit(dealer_hand)
                # print(dealer_hand)
                framework.send_message(dealer_hand, from_)
                if total(dealer_hand)>21:
                    # print('Dealer busts, you win!')
                    framework.send_message('Dealer busts, you win!', from_)
                    play_again()
            score(dealer_hand,player_hand)
            play_again()
        elif choice == "q":
            # print("Bye!")
            framework.send_message("Bye!", from_)
            quit=True
            exit()


if __name__ == "__main__":
   game()