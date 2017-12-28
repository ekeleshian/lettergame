#make a list of words
# pick a random word
# draw spaces
#take a guess
#draw guessed letters and strikes
#print out win/lose

"""
One idea, make a dictionary where 
keys are the unique characters of the string 
and values are lists of integers where integer represents 
all the indexes of where that key (the letter) appears in string. 
Expect most values of keys to be arrays of length 1. 
When user gives a character input, check if that key 
exists in dictionary, if so, 
then the value of the key (its a list of indexes) is where 
you fill in new string with that key
"""


import random as r

# def draw_board(solution):
# 	for letter in solution:
# 		print('__', end =' ')
def secret_dict(string):
	secret_dict = {}
	for idx, value in enumerate(string):
		if value not in secret_dict:
			secret_dict[value] = [idx]
		else:
			secret_dict[value].append(idx)
	return secret_dict



def letter_game():
	list_of_words = []
	for line in open('words.txt'):
		list_of_words.append(line.strip())



	generating_board = []
	guessed_letters = []


	secret_word = r.choice(list_of_words)

	for char in secret_word:
		generating_board.append("__")

	print(generating_board)

	num_of_tries = int(len(secret_word)*1.5)

	return_secret_dict = secret_dict(secret_word)



	while num_of_tries > 0:
		finished_game_check = 0

		guess_char = input("Take a guess: ")

		if guess_char not in return_secret_dict:
			num_of_tries -= 1
			guessed_letters.append(guess_char)
			print(" {} is not found in the word. You have {} tries left.".format(guess_char, num_of_tries))
		if guess_char in return_secret_dict:
			if guess_char in generating_board:
				print("You have already guessed {}. Try again".format(guess_char))
			else:
				num_of_tries -= 1
				guessed_letters.append(guess_char)
				list_idx = return_secret_dict[guess_char]
				for i in list_idx:
					generating_board[i] = guess_char

		for element in generating_board:
			if element != "__":
				finished_game_check += 1
			if finished_game_check == len(generating_board):
				print('game over!')
				num_of_tries = 0
				break

		print("The guessed letters: {}".format(guessed_letters))
		print(generating_board)

	play_again = input("do you want to play again? Y/N ")
	if play_again.lower() != 'n':
		letter_game()
	else:
		print('bye!')
		num_of_tries = 0

letter_game()






