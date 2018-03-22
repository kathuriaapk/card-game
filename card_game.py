from random import shuffle
import cardsDistribution
import mainMatch

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
player_name = input("Enter your name & Press Enter : ")
if player_name == "":
	print("\nAs you haven't entered any name, So your name for this game is Bluff Master\n")
	player_name = "Bluff Master"

#CARDS INITIALIZATION
card_type = ['H','S','C','D']
cards_deck = []
for card in card_type:
	 i = 1
	 while i <= 13:
	 	cards_deck.append(card + str(i))
	 	i += 1

#CARDS DISTRIBUTION BETWEEN TWO PLAYERS
player1,player2 = cardsDistribution.cards_distribution(cards_deck, shuffle)
input("Cards are shuffled (press Enter to throw a card) \nYour Turn :- ")

#MAIN PROGRAMME FOR TOURNAMENT
winner = mainMatch.match(player1,player2, shuffle)

#FINALLY
if winner == 'p2':
	print("\nOhh. YOU LOOSE THIS GAME.BETTER LUCK NEXT TIME\n")
elif winner  == 'p1':
	print("\nCONGRATULATIONS YOU WIN THIS GAME OF LUCK (PATTE PE PATTA)\n")
else:
	print("\nTHE GAME IS DRAW.NO ONE MATHES THE CARDS.BETTER LUCK NEXT TIME\n")
print("\nThankyou " + player_name)



