import random as r

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
				print("\n \n Nice!! You got one! You have {} attempts left. \n".format(num_of_tries))
				guessed_letters.append(guess_char)
				list_idx = return_secret_dict[guess_char]
				for i in list_idx:
					generating_board[i] = guess_char

		for element in generating_board:
			if element != "__":
				finished_game_check += 1
			if finished_game_check == len(generating_board):
				num_of_tries = 0
				

		print("The guessed letters: {}. \n \n ".format(guessed_letters))
		print(generating_board, '\n \n')
	print('Game over! The word was {}.'.format(secret_word))
	play_again = input("Do you want to play again? Y/N ")
	if play_again.lower() != 'n':
		letter_game()
	else:
		print('bye!')
		num_of_tries = 0

letter_game()