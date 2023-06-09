#Rock - R, Paper - P, Scissor - S
def game(player1,player2):
	if player1 == "R":
		if player2 == "S":
			print("Player1 wins")
		elif player2 == "P":
			print("Player2 wins")
		else:
			print("Draw")

	elif player1 == "P":
		if player2 == "S":
			print("Player2 wins")
		elif player2 == "R":
			print("Player1 wins")
		else:
			print("Draw")

	elif player1 == "S":
		if player2 == "R":
			print("Player2 wins")
		elif player2 == "P":
			print("Player1 wins")
		else:
			print("Draw")

player1 = input("What will you choose?")
player2 = input("What will you choose?")
game(player1,player2)

ask = input("Do you want to play again? ")
# Y for yes, N for no
def play_again():
	if ask == "Y":
		p1 = input("What will you choose?")
		p2 = input("What will you choose?")
		game(p1,p2)
		ask1 = input("Do you want to play again? ")
		if ask1=="Y":
			return play_again()
		elif ask1 == "N":
			print("Goodbye")
	elif ask == "N":
		print("Goodbye")
play_again()