// This program is designed to allow a user to guess a number from 1-100
and the output will result in too high, too low, or correct

start

input numAnswer = "Choose a number between 1-100"
input numGuess = "Guess a number between 1-100"

    if numGuess > numAnswer
        print "This guess is too high"
        if numGuess < numAnswer
            print "This guess is too low"
            if numGuess != numAnswer
                print "This guess is correct!"
    endif

end
