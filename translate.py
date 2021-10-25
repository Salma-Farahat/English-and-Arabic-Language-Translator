#!/usr/bin/python3
'''
This program is from p. 81 Figure 5.9 "Translating text (badly)" of 
our Gutag textbook.
You can use it as a starter program for assignment 2.

The output from the program is:
--------------------------------------
Input: I drink good red wine, and eat bread.
Output: Je bois "good" rouge vin, et mange pain..
--------------------------------------
Input: Je bois du vin rouge.
Output: I drink of wine red..
--------------------------------------
'''
EtoF = {'bread' : 'pain', 'wine' : 'vin', 'with' : 'avec', 'I' : 'Je',
        'eat' : 'mange', 'drink' : 'bois', 'John' : 'Jean', 'friends' : 'amis', 'and' : 'et', 'of' : 'du', 'red' : 'rouge'}

FtoE = {'pain': 'bread', 'vin': 'wine', 'avec': 'with', 'Je': 'I', 'mange': 'eat', 'bois': 'drink', 'Jean': 'John', 'amis': 'friends', 'et': 'and', 'du': 'of', 'rouge': 'red'}

dicts = {'English to French' : EtoF, 'French to English' : FtoE}

def translateWord(word, dictionary) :
    if word in dictionary.keys() :
        return dictionary[word]
    elif word != '' :
        return '"' + word + '"'
    return word

def translate(phrase, dicts, direction) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters
    dictionary = dicts[direction]
    translation = ''
    word = ''
    for character in phrase :
        if character in letters :
            word = word + character
        else : 
            translation = translation + translateWord(word, dictionary) + character
            word = ''
    translation = translation + translateWord(word, dictionary) + character
    return translation

sentence = 'I drink good red wine, and eat bread.'
translated = translate(sentence, dicts, 'English to French')
print('--------------------------------------')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')
sentence = 'Je bois du vin rouge.'
translated = translate(sentence, dicts, 'French to English')
print('Input:', sentence)
print('Output:', translated)
print('--------------------------------------')


