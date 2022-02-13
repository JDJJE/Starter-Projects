import random
import string
from words import words

def get_valid_word(words):
	word = random.choice(words)			# Randomly chooses a word from the list
	while "-" in word or " " in word:
		word = random.choice(words)

	return word

def hangman():
	word = get_valid_word(words)
	word = word.upper()
	word_letters = set(word)	# Letters in the word
	alphabet = set(string.ascii_uppercase)
	used_letters = set()	# Letters user has used
	lives = 7

	while len(word_letters) > 0 and lives > 0:
		# letters used
		# " ".join(["a", "b", "cd"]) --> a b cd""
		print("You have used these letters: ", " ".join(used_letters))

		# current word i.e (W - R D)
		word_list = [letter if letter in used_letters else "-" for letter in word]
		print("Current word: ", " ".join(word_list))

		user_letter = input("Guess a letter: ").upper()
		if user_letter in alphabet - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)

			else:
				lives = lives - 1 # remove a life
				print("Letter is not in the word")

		elif user_letter in used_letters:
			print("You have already used that character. Please try again.")

		else:
			print("Invalid character. Please try again.")

	#when word_letters == 0 get here or lives == 0

	if lives == 0:
		print("Sorry you died, the word was: ", word)
	else:
		print("Congrats! You won! Your word was: ", word)

hangman()