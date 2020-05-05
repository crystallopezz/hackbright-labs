# put your code here.
def word_count (file):
    '''open file and countshow many times each word occurs in that file'''

    #open the text file
    text = open(file)

    #create an empty dictionary to store the words and their count
    word_count = {}

    #iterate through each line in the text
    for line in text:

        #strip any whitespace of each line
        line = line.strip().lower()

        #turn the line into a list of words
        words = line.split(" ")
        #would words = set(line) work as well?

        #iterate through each word in the list
        for word in words:
            # #make each word case insensitive
            # cased_word = word.casefold()
            
            #iterate through each character in the word to see if the character
            #is punctuation. If if it is punctuation, then strip the word of
            #the character
            for char in word: 
                if not char.isalnum():
                    word = word.strip(char)
            
            #update the count if the word is already counted
            #add the word if it hasn't been counted yet
            word_count[word] = word_count.get(word, 0)+1

    return word_count