# Part 5
# Author: Antoine Bonnet

from text_to_braille import *

ENG_CAPITAL = '..\n..\n.o'
ENG_NUMBER_END = '..\n.o\n.o'
####################################################
# Here are two helper functions to help you get started

def two_letter_contractions(text):
    '''(str) -> str
    Process English text so that the two-letter contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.
    Provided to students. You should not edit it.

    >>> two_letter_contractions('chat')
    'âat'
    >>> two_letter_contractions('shed')
    'îë'
    >>> two_letter_contractions('shied')
    'îië'
    >>> two_letter_contractions('showed the neighbourhood where')
    'îœë ôe neiêbürhood ûïe'
    >>> two_letter_contractions('SHED')
    'ÎË'
    >>> two_letter_contractions('ShOwEd tHE NEIGHBOURHOOD Where') 
    'ÎŒË tHE NEIÊBÜRHOOD Ûïe'
    '''
    combos = ['ch', 'gh', 'sh', 'th', 'wh', 'ed', 'er', 'ou', 'ow']
    for i, c in enumerate(combos):
        text = text.replace(c, LETTERS[-1][i])
    for i, c in enumerate(combos):
        text = text.replace(c.upper(), LETTERS[-1][i].upper())
    for i, c in enumerate(combos):
        text = text.replace(c.capitalize(), LETTERS[-1][i].upper())

    return text


def whole_word_contractions(text):
    '''(str) -> str
    Process English text so that the full-word contractions are changed
    to the appropriate French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    If the full-word contraction appears within a word, 
    contract it. (e.g. 'and' in 'sand')

    Provided to students. You should not edit this function.

    >>> whole_word_contractions('with')
    'ù'
    >>> whole_word_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meow'
    >>> whole_word_contractions('With')
    'Ù'
    >>> whole_word_contractions('WITH')
    'Ù'
    >>> whole_word_contractions('wiTH')
    'wiTH'
    >>> whole_word_contractions('FOR thE Cat WITh THE purr And The meow')
    'É thE Cat WITh À purr Ç À meow'
    >>> whole_word_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> whole_word_contractions('wither')
    'ùer'
    '''
    # putting 'with' first so wither becomes with-er not wi-the-r
    words = ['with', 'and', 'for', 'the']
    fr_equivs = ['ù', 'ç', 'é', 'à', ]
    # lower case
    for i, w in enumerate(words):
        text = text.replace(w, fr_equivs[i])
    for i, w in enumerate(words):
        text = text.replace(w.upper(), fr_equivs[i].upper())
    for i, w in enumerate(words):
        text = text.replace(w.capitalize(), fr_equivs[i].upper())
    return text



####################################################
# These two incomplete helper functions are to help you get started

def convert_contractions(text):
    '''(str) -> str
    Convert English text so that both whole-word contractions
    and two-letter contractions are changed to the appropriate
    French accented letter, so that when this is run
    through the French Braille translator we get English Braille.

    Refer to the docstrings for whole_word_contractions and 
    two_letter_contractions for more info.

    >>> convert_contractions('with')
    'ù'
    >>> convert_contractions('for the cat with the purr and the meow')
    'é à cat ù à purr ç à meœ'
    >>> convert_contractions('chat')
    'âat'
    >>> convert_contractions('wither')
    'ùï'
    >>> convert_contractions('aforewith parenthetical sand')
    'aéeù parenàtical sç'
    >>> convert_contractions('Showed The Neighbourhood Where')
    'Îœë À Neiêbürhood Ûïe'
    '''

    return two_letter_contractions(whole_word_contractions(text))
#Converts the whole word contractions then the two-letter contractions in text


def convert_quotes(text):
    '''(str) -> str
    Convert the straight quotation mark into open/close quotations.
    >>> convert_quotes('"Hello"')
    '“Hello”'
    >>> convert_quotes('"Hi" and "Hello"')
    '“Hi” and “Hello”'
    >>> convert_quotes('"')
    '“'
    >>> convert_quotes('"""')
    '“”“'
    >>> convert_quotes('" "o" "i" "')
    '“ ”o“ ”i“ ”'
    '''
    
    if text.count('"') == 0:
            return text

    quote_count = 0
    translated_word = ""
    
    for i in range(0, len(text)):
        
        if text[i] != '"': #if given character is not a quotation mark
            translated_word += text[i] #adds letter unchanged
            
        elif text[i] == '"' and (quote_count+2)%2 == 0: #if even number of quot. mark
            translated_word += '“' #adds open quot. mark
            quote_count += 1

        elif text[i] == '"' and (quote_count+1)%2 == 0: #if odd number of quot.mark
            translated_word += '”' #adds closed quot. mark
            quote_count += 1
            
    return translated_word #reconstructed word is returned


####################################################

#Helper functions:

def transfer_quotes_parentheses(text):
    '''(str) -> (str)
    Before translating to French Braille, exchange corresponding terms such that
    the French Braille conversion yields an English braille conversion
    knowing that '(' and ')'in E.B. are equivalent to '“' and '”' in F.B.
    >>> transfer_quotes_parentheses('(and)')
    '“and”'
    >>> transfer_quotes_parentheses('My (first) name is "Antoine"')
    'My “first” name is (Antoine)'
    >>> transfer_quotes_parentheses('("J. K. Rowling")')
    '“(J. K. Rowling)”'
    >>> transfer_quotes_parentheses('() "" ("")')
    '“” () “()”'
    >>> transfer_quotes_parentheses('(hi)')
    '“hi”'
    '''
    
    text = convert_quotes(text) #Converts quotes in text
    new_text = '' #initializes a new text
    for i in range(0, len(text)):
        if text[i] == '“' or text[i] == '?':
            new_text += '('

        elif text[i] == '”':
            new_text += ')'

        elif text[i] == '(':
            new_text +=  '“'
            
        elif text[i] == ')':
            new_text += '”'
        else:
            new_text += text[i]
            
    return new_text

#replaces '“' or '?' with '(', '”' with ')', '(' with '“' and ')' with '”' in text

def english_braille_numbers(text):
    '''(str) -> (str)
    Before translating to French Braille, keep the first digit of a number unchanged, then
    replace numbers 0-9 to their a-j letter equivalent in the first decade.
    '..\n.o\n.o' is placed at the end of the number

    >>> english_braille_numbers('2')
    '2⠰'
    >>> english_braille_numbers('202')
    '2jb⠰'
    >>> english_braille_numbers('I ate 34 crepes') 
    'I ate 3d⠰ crepes'
    >>> english_braille_numbers('COMP202') 
    'COMP2jb⠰'
    >>> english_braille_numbers('12978514 !') 
    '1bighead⠰ !'
    '''
    eng_text = '' #initialize new text
    FIRST_DECADE = 'abcdefghij' #all letters in first decade
    END_NUMBER = ostring_to_unicode('..\n.o\n.o') #English braille for end of number
    
    for i in range(len(text)):
        if len(text) == 1:# if text is one digit, adds end number. if it's one letter, adds nothing
            if text in DIGITS:
                eng_text += text + END_NUMBER
            else:
                eng_text += text
        else: #if text is longer than one character
            if i < len(text) - 1: #for all character until last one excluded
                if text[i] not in DIGITS: #character letter, adds nothings
                    eng_text += text[i]  
                else: #if character is a digit
                    if i == 0 : #first character, adds nothing
                        eng_text += text[i]
                    elif text[i-1] not in DIGITS: #previous character not digit
                        eng_text += text[i] #adds nothing
                    else: #if i != 0 and previous character is digit
                        if text[i+1] not in DIGITS: #if next character not digit
                            eng_text += FIRST_DECADE[DIGITS.find(text[i])] + END_NUMBER #adds corresponding letter in first decade + end_number
                        else: #if next character is digit
                            eng_text += FIRST_DECADE[DIGITS.find(text[i])] #adds corresponding letter in first decade 
            elif i == len(text) - 1: 
                if text[i] not in DIGITS: #if last character is not a digit, adds nothing
                    eng_text += text[i] 
                else: #if last character digit, adds corresponding letter in first decade + end_number
                    eng_text += FIRST_DECADE[DIGITS.find(text[i])] + END_NUMBER
    return eng_text
    
####################################################

def english_text_to_braille(text):
    '''(str) -> str
    Convert text to English Braille. Text could contain new lines.

    This is a big problem, so think through how you will break it up
    into smaller parts and helper functions.
    Hints:
        - you'll want to call text_to_braille
        - you can alter the text that goes into text_to_braille
        - you can alter the text that comes out of text_to_braille
        - you shouldn't have to manually enter the Braille for 'and', 'ch', etc

    You are expected to write helper functions for this, and provide
    docstrings for them with comprehensive tests.

    >>> english_text_to_braille('202') # numbers
    '⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('2') # single digit
    '⠼⠃⠰'
    >>> english_text_to_braille('COMP') # all caps
    '⠠⠠⠉⠕⠍⠏'
    >>> english_text_to_braille('COMP 202') # combining number + all caps
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰'
    >>> english_text_to_braille('and')
    '⠯'
    >>> english_text_to_braille('and And AND aNd')
    '⠯ ⠠⠯ ⠠⠯ ⠁⠠⠝⠙'
    >>> english_text_to_braille('chat that the with')
    '⠡⠁⠞ ⠹⠁⠞ ⠷ ⠾'
    >>> english_text_to_braille('hi?')
    '⠓⠊⠦'
    >>> english_text_to_braille('(hi)')
    '⠶⠓⠊⠶'
    >>> english_text_to_braille('"hi"')
    '⠦⠓⠊⠴'
    >>> english_text_to_braille('COMP 202 AND COMP 250') ###
    '⠠⠠⠉⠕⠍⠏ ⠼⠃⠚⠃⠰ ⠠⠯ ⠠⠠⠉⠕⠍⠏ ⠼⠃⠑⠚⠰'
    >>> english_text_to_braille('For shapes with colour?')
    '⠠⠿ ⠩⠁⠏⠑⠎ ⠾ ⠉⠕⠇⠳⠗⠦'
    >>> english_text_to_braille('(Parenthetical)\\n\\n"Quotation"')
    '⠶⠠⠏⠁⠗⠑⠝⠷⠞⠊⠉⠁⠇⠶\\n\\n⠦⠠⠟⠥⠕⠞⠁⠞⠊⠕⠝⠴'
    '''
    
    #Replace numbers 1-10 to letters a-j before French translation to obtain English translation
    text = english_braille_numbers(text)
    # Here's a line we're giving you to get started: change text so the
    # contractions become the French accented letter that they correspond to
    text = convert_contractions(text)
    #Exchange quotations and parentheses before translation to French Braille
    #so that they are translated to English Braille
    text = transfer_quotes_parentheses(text)
    text = text.replace('“', '"')
    text = text.replace('”', '"') #converts smart quotes to straight quotes
    # Run the text through the French Braille translator          
    text = text_to_braille(text)
    # Replace the French question mark with the English question mark
    text = text.replace(ostring_to_unicode('..\no.\n.o'), ostring_to_unicode('..\no.\noo'))
    # Replace the French capital with the English capital
    text = text.replace(ostring_to_unicode(CAPITAL), ostring_to_unicode('..\n..\n.o'))
    text = text.replace('..\n..\n..', ' ') #replaces empty o-string with a space
    return text

def english_file_to_braille(fname):
    '''(str) -> NoneType
    Given English text in a file with name fname in folder tests/,
    convert it into English Braille in Unicode.
    Save the result to fname + "_eng_braille".
    Provided to students. You shouldn't edit this function.

    >>> english_file_to_braille('test4.txt')
    >>> file_diff('tests/test4_eng_braille.txt', 'tests/expected4.txt')
    True
    >>> english_file_to_braille('test5.txt')
    >>> file_diff('tests/test5_eng_braille.txt', 'tests/expected5.txt')
    True
    >>> english_file_to_braille('test6.txt')
    >>> file_diff('tests/test6_eng_braille.txt', 'tests/expected6.txt')
    True
    '''  
    file_to_braille(fname, english_text_to_braille, "eng_braille")


if __name__ == '__main__':
    doctest.testmod()  
    
