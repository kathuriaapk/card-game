from random import shuffle

#GAME DESCRIPTION
print("##	PATTE PE PATTA	##")
print("Please read the instructons carefully :- \
	\n1.Each player will be distributed 26 cards out of 52 cards. \
	\n2.Each player has its turn one after another.\
	\n3.If the numer on the card matches the card of previous turn by other player, \
	 that round will be Win by the player who mathes the previous card.\n \
	 Example :- \n 		1st turn :- H1(player),D3(player2)\n 		2nd turn :- C1,D1 i.e matches , So the player with the card D1 wins the round \
	 \n4.Winner of that round will get all the cards of that round.And the game repeats. \
	 \n5.Finally, Winner will be the one who has maximum number of cards at the end.\n\n")
input("Press ENTER to continue the game PATTE PE PATTA :")

#CARDS INITIALIZATION
card_type = ['H','S','C','D']
cards_deck = []
for card in card_type:
	 i = 1
	 while i <= 13:
	 	cards_deck.append(card + str(i))
	 	i += 1

#CARDS DISTRIBUTION BETWEEN TWO PLAYERS
shuffle(cards_deck)
player_name = input("Enter your name & Press Enter : ")
if player_name == "":
	print("\nAs you haven't entered any name, So your name for this game is Bluff Master\n")
	player_name = "Bluff Master"
player1 = cards_deck[0:26]
player2 = cards_deck[26:52]
print("Your cards are :-")
print(player1)
input("Press ENTER to Shuffle and Continue the Game....  ")
shuffle(player1)
shuffle(player2)
input("Cards are shuffled (press Enter to throw a card) \nYour Turn :- ")

#MAIN PROGRAMME FOR TOURNAMENT
tour = []
p1_lastcard = player1.pop()
print("				Your Turn: %s"%(p1_lastcard))
tour.append(p1_lastcard)
while len(player1) != 0 and len(player2) != 0:
	p2_lastcard = player2.pop()
	tour.append(p2_lastcard)
	print("				Computer Turn: %s"%(p2_lastcard))
	if p2_lastcard[-1] == p1_lastcard[-1]:
		print("Ohh Player2 wins this round.")
		player2 += tour 
		print("Player 2 has total %d cards.\nYou have %d cards"%(len(player2), len(player1)))
		print(player2)
		shuffle(player2)
		p2_lastcard = "0"
		tour = []
	print(tour)
	input("Your Turn :-")
	p1_lastcard = player1.pop()
	tour.append(p1_lastcard)
	print("				Your Turn: %s"%(p1_lastcard))
	if p1_lastcard[-1] == p2_lastcard[-1]:
		print("Congratulation You Matches.You win this Round")
		player1 += tour
		print("Player 2 has total %d cards.\nYou have %d cards"%(len(player2), len(player1)))
		shuffle(player1)
		p1_lastcard = '0'
		tour = []
	
#FINALLY
if len(player1) == 0 and len(player2) != 1 :
	print("\nOhh. YOU LOOSE THIS GAME.BETTER LUCK NEXT TIME\n")
elif len(player2)  == 0:
	print("\nCONGRATULATIONS YOU WIN THIS GAME OF LUCK (PATTE PE PATTA)\n")
else:
	print("\nTHE GAME IS DRAW.NO ONE MATHES THE CARDS.BETTER LUCK NEXT TIME\n")
print("\nThankyou " + player_name)



