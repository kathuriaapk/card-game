def match(p1,p2,shuffle):
	tour = []
	winner = ''
	p1_lastcard = p1.pop()
	print("				Your Turn: %s"%(p1_lastcard))
	tour.append(p1_lastcard)
	while len(p1) != 0 and len(p2) != 0:
		p2_lastcard = p2.pop()
		tour.append(p2_lastcard)
		print("				Computer Turn: %s"%(p2_lastcard))
		if p2_lastcard[-1] == p1_lastcard[-1]:
			print("Ohh p2 wins this round.")
			p2 += tour 
			print("Player 2 has total %d cards.\nYou have %d cards"%(len(p2), len(p1)))
			print(p2)
			shuffle(p2)
			p2_lastcard = "0"
			tour = []
		print(tour)
		input("Your Turn :-")
		p1_lastcard = p1.pop()
		tour.append(p1_lastcard)
		print("				Your Turn: %s"%(p1_lastcard))
		if p1_lastcard[-1] == p2_lastcard[-1]:
			print("Congratulation You Matches.You win this Round")
			p1 += tour
			print("Player 2 has total %d cards.\nYou have %d cards"%(len(p2), len(p1)))
			shuffle(p1)
			p1_lastcard = '0'
			tour = []
	if len(p1) == 0 and len(p2) != 1 :
		winner = 'p2'   
	elif len(p2)  == 0:
		winner = 'p1'
	return winner