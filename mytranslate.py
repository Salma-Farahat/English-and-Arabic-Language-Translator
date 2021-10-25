import arabic_reshaper                         #instalation: pip install --upgrade arabic-reshaper
from bidi.algorithm import get_display         #instalation: pip install python-bidi

# The 2 packages above are imported to allow python to print the Arabic language correctly
# If they are not imported the progam will run if you comment out the lines with a '*' commented next to them
# but the output will look something like this 'boy'='د ل و'
# since python will read the word from left to right and not right to left, which is how arabic is read

# Improvements:
# 1. I chose a language other than French (Arabic) and I expanded the domain to more than just eating and drinking
# 2. I incresed the vocabulary to 50 words
# 3. I fixed the glitch where you see two periods at the end of the translated sentence, even though
#    there is only one period on the input sentence
# 4. I wrote a function reverseDictionary(dictionary) that can generate the AtoE dictionary from the EtoA dictionary
# 5. I added comments
# 6. I added functionality for dealing with articles
# 7. The code can get input from the user
# 8. The code can detect the language that is inputed

EtoA = {'he':'هو', 'boy':'ولد','plays':'يلعب','in':'في','garden':'حديقة',
'football':'كرة القدم','eats':'يأكل','apples':'تفاح','tree':'شجرة','reads':'يقرأ',
'book':'كتاب','basketball':'كرة السلة','orange':'برتقال','steak':'لحمة','and':'و',
'vegetables':'خضار','chicken':'دجاج','fish':'سمك','bread':'خبز','cake':'كعك','breakfast':'فطور',
'dinner':'عشاء','drinks':'يشرب','water':'ماء','milk':'حليب','man':'رجل','magazine':'مجلة',
'walks':'يمشي','watches':'يتفرج على','television':'تلفاز','show':'برنامج','studies':'يدرس',
'biology':'علم الأحياء','chemistry':'الكيمياء','physics':'الفيسياء','mathematics':'الرياضيات',
'attends':'يحضر','lesson':'درس','goes':'يذهب','to':'إلى','morning':'صباح','evening':'مساء',
'school':'مدرسة','university':'جامعة','dances':'يرقص','music':'موسيقى','writes':'يكتب',
'homework':'الواجب','solves':'يحل','poem':'قصيدة',}


def reverseDictionary(dict):                      # this function reverses the dictionary
    return {value : key for (key, value) in dict.items()}

AtoE= reverseDictionary(EtoA)

dicts = {'English to Arabic' : EtoA, 'Arabic to English' : AtoE}

def translateWord(word, dictionary) :
    omitted= 'aA'                    # ther is no equivalent to a in the arabic language
    if word in dictionary.keys() :   # if the word is in the dictionary
        return dictionary[word]      # it returns the value of that word (translated)
    elif word not in dictionary.keys() and word not in omitted: # if the word in not in the dictionary and it is not 'a'
        return '"' + word + '"'      # returns the word in quotations
    elif word != '' :                
        return ''
    return word

def translate(phrase, dicts, direction) :
    UCletters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LCletters = 'abcdefghijklmnopqrstuvwxyz'
    letters = UCletters + LCletters        # A combination of all uppercase and lowercase letters
    dictionary = dicts[direction]         
    translation = ''
    word = ''
    for character in phrase :       # lopps through the phrase given
        if character in letters :   # checks if the charater is a letter
            word = word + character # if it is, it adds it to word
        else :                      # if it is not a letter
            #creates the translation using the function translateWord(word, dictionary) and adds the charater such as ' ' and '.'
            translation = translation + translateWord(word, dictionary) + character 
            word = ''       # resets word to an empty string

    translation1= arabic_reshaper.reshape(translation)  # * comment this out if you dont install the packages
    translation2 = get_display(translation1)            # * comment this out if you dont install the packages

    return translation2                                 # * change translation2 to translation

def translate1(phrase, dicts, direction) :
    letters = 'دجحخهعغفقثصضذشسيبلاتنمكطظزوةىلارؤءئلإإلأأ'  # all of the arabic alphabet
    dictionary = dicts[direction]
    translation = ''
    word = ''
    nouns = ['ولد','حديقة','شجرة','لحمة','دجاج','سمك', 'كعك', 'ماء', 'رجل', 'مجلة','برنامج' , 'درس', 'قصيدة']
    for character in phrase :          # lopps through the phrase given
        if character in letters :      # checks if the charater is a letter
            word = word + character    # if it is, it adds it to word
        else :                         # if it is not a letter
            if word in nouns:  # adds an 'a' if the word is a noun and begins with a consonant
                translation = translation +'a '+ translateWord(word, dictionary) + character
            else:
                translation = translation + translateWord(word, dictionary) + character
            word = '' # resets word to an empty string

    return translation

english_letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
arabic_letters= "دجحخهعغفقثصضذشسيبلاتنمكطظزوةىلارؤءئلإإلأأ"

#sample:
sentence= 'A boy eats apples.'
translated = translate(sentence.lower(), dicts, 'English to Arabic')
print('Input:', sentence)
print('Output:', translated)

sentence='هو يكتب قصيدة.'
translated = translate1(sentence, dicts, 'Arabic to English')
sentence1= arabic_reshaper.reshape(sentence)                    # * comment this out if you dont install the packages
sentence2 = get_display(sentence1)                              # * comment this out if you dont install the packages
print('Input:', sentence2)                                      # * change 'sentence2' to 'sentence'
print('Output:', translated.capitalize())

sentence = input('Enter a sentence in Arabic or English and do not forget to add a period: ')
for letter in sentence[0]:
    if letter in english_letters:
        translated = translate(sentence.lower(), dicts, 'English to Arabic')
        print('Input:', sentence)
        print('Output:', translated)
    elif letter in arabic_letters:
        translated = translate1(sentence, dicts, 'Arabic to English')
        sentence1= arabic_reshaper.reshape(sentence)                    # * comment this out if you dont install the packages
        sentence2 = get_display(sentence1)                              # * comment this out if you dont install the packages
        print('Input:', sentence2)                                      # * change 'sentence2' to 'sentence'
        print('Output:', translated.capitalize())
