#We will have a secret word, the user will keep trying to guess what the word is

secret_word = "giraffe"

#Now we want a variable to store the user's guess

guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False
#We want a continuous guess, not once, therefore we need a loop

while guess != secret_word and not(out_of_guesses):
   if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
   else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of guesses, you dumb loser hehehehe")
else:
    print("You win")