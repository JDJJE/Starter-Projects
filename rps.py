import random

def play():
	user = input("'R' for rock, 'P' for paper and 'S' for scissors. What's your choice? ")
	computer = random.choice(['R', 'P', 'S'])

	if user == computer:
		return "It's a tie"

	# if R > S. S > P, P > R
	if is_win(user, computer):
		return "You won"

	return "You Lost"

def is_win(player, opponent):
	# return true if player wins
	# R > S, S > P, P > R
	if(player == 'R' and opponent == 'S') or (player == 'S' and opponent == 'P') or (player == 'P' and opponent == 'R'):
		return True

print(play())
