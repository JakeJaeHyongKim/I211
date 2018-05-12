def get_guess():
    guess = input("Guess a four letter word:").lower()
    return guess if (len(guess)==4) and (guess.isalpha()) else get_guess()

while True:
    secret_word = "hike"
    score = 0

    guess = get_guess()

    for i in range(4):
        if secret_word(i) == guess(i):
            score +=1
    if score == 4:
        break

    else:
        print(score)
