// this program is designed to search a word from the dictionary
   and display the definition.

start

input randomWord = "Choose a word to search in the dictionary"

Open dictionary in the middle
Read word on that page
    if randomWord comes alphabetically after the word on that page
        continue searching the second half of the dictionary
        if randomWord comes alphabetically before the word on that page
            continue searching the first half of the dictionary
            if randomWord is not found
                print "Word not found"
                if randomWord matches the word on the page
                    print "Here is the definition of ", & randomWord
                    print the definition of the word on the page
    endif

end
