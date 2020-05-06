"""Generate Markov text from text files."""

import random


def open_and_read_file(input_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    contents = open(input_path).read()
    return contents


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains("hi there mary hi there juanita")

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']
        
        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    words = text_string.split()
    
    for i in range(len(words)-2):
        word_pair = (words[i], words[i+1])
        next_word = words[i+2]
        chains[word_pair] = chains.get(word_pair, [])
        chains[word_pair].append(next_word)

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    # your code goes here
    first_link = (random.choice(list(chains.keys())))

    words.extend(list(first_link))

    words.append(random.choice(chains[first_link]))

    while chains.get((words[-2], words[-1]), False):
        key = (words[-2], words[-1])
        words.append(random.choice((chains[key])))

    return " ".join(words)


input_path = "gettysburg.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
