def cards_distribution(c_deck,shuffle):
	shuffle(c_deck)
	player1_cards = c_deck[0:26]
	player2_cards = c_deck[26:52]
	print("Your cards are :-")
	print(player1_cards)
	input("Press ENTER to Shuffle and Continue the Game....  ")
	shuffle(player1_cards)
	shuffle(player2_cards)
	return [player1_cards,player2_cards]