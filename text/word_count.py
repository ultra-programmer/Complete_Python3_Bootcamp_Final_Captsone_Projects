"""
Count the number of words coming in from an imported text file
"""
from collections import Counter
import re

def get_words(text):
    return Counter(re.findall('[^.!? ]+', text)).items()

def count_words(words):
    word_count = 0

    #For every tuple (word, count) in the list passed in...
    for item in words:
    	#Add the number of occurences of that word to the total number of words
        word_count += item[1]

    return word_count

def main():
	#Open the test file
    with open('word_count.txt', 'r') as TEXT_FILE:
    	#Get the content of the test file
        FILE_CONTENTS = TEXT_FILE.read()

        #Turn the file contents into a list of each word and the number of times it occurs
        word_list = get_words(FILE_CONTENTS)

        #Find the number of words in the word list
        NUM_WORDS = count_words(word_list)
        print(f'There are {NUM_WORDS} words in your file!')

        print('Here are the following occurences of each of the words in your file:')
        for word, count in word_list:
            print(f'\tThe word \'{word}\' occurs {count} time(s).')

if __name__ == '__main__':
    main()
