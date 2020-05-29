# Part 3
# Author: Antoine Bonnet

import doctest

INCOMPLETE = -1


def ostring_to_raisedpos(s):
    ''' (str) -> str
    Convert a braille letter represented by '##\n##\n##' o-string format
    to raised position format. Provided to students. Do not edit this function.

    Braille cell dot position numbers:
    1 .. 4
    2 .. 5
    3 .. 6
    7 .. 8 (optional)

    >>> ostring_to_raisedpos('..\\n..\\n..')
    ''
    >>> ostring_to_raisedpos('oo\\noo\\noo')
    '142536'
    >>> ostring_to_raisedpos('o.\\noo\\n..')
    '125'
    >>> ostring_to_raisedpos('o.\\noo\\n..\\n.o')
    '1258'
    '''
    res = ''
    inds = [1, 4, 2, 5, 3, 6, 7, 8]
    s = s.replace('\n', '')
    for i, c in enumerate(s):
        if c == 'o':
            res += str(inds[i])
    return res 


def raisedpos_to_binary(s):
    ''' (str) -> str
    Convert a string representing a braille character in raised-position
    representation  into the binary representation.
    TODO: For students to complete.

    >>> raisedpos_to_binary('')
    '00000000'
    >>> raisedpos_to_binary('142536')
    '11111100'
    >>> raisedpos_to_binary('14253678')
    '11111111'
    >>> raisedpos_to_binary('123')
    '11100000'
    >>> raisedpos_to_binary('125')
    '11001000'
    '''
    binary_number = "" #initiates the binary_number variable as the empty string
    for i in range(1,9):
        if str(i) in s:
            binary_number += "1"
        else:
            binary_number += "0"
    return binary_number 
# going from numbers 1 to 9, the function looks for the given number in the string s
# if present, it adds a 1 to the binary number. If absent, it adds a 0 to the binary number

def binary_to_hex(s):
    '''(str) -> str
    Convert a Braille character represented by an 8-bit binary string
    to a string representing a hexadecimal number.

    TODO: For students to complete.

    The first braille letter has the hex value 2800. Every letter
    therafter comes after it.

    To get the hex number for a braille letter based on binary representation:
    1. reàverse the string
    2. convert it from binary to hex
    3. add 2800 (in base 16)

    >>> binary_to_hex('00000000')
    '2800'
    >>> binary_to_hex('11111100')
    '283f'
    >>> binary_to_hex('11111111')
    '28ff'
    >>> binary_to_hex('11001000')
    '2813'
    '''
    return hex((int(s[::-1], 2)) + int("2800", 16))[2:]

# reverses the string s, converts it to decimal number adds the decimal conversion of the hexadecimal number 2800
# It then excludes the 0x term at the beginning of the result
    
def hex_to_unicode(n):
    '''(str) -> str
    Convert a braille character represented by a hexadecimal number
    into the appropriate unicode character.
    Provided to students. Do not edit this function.

    >>> hex_to_unicode('2800')
    '⠀'
    >>> hex_to_unicode('2813')
    '⠓'
    >>> hex_to_unicode('2888')
    '⢈'
    '''
    # source: https://stackoverflow.com/questions/49958062/how-to-print-unicode-like-uvariable-in-python-2-7
    return chr(int(str(n),16))


def is_ostring(s):
    '''(str) -> bool
    Is s formatted like an o-string? It can be 6-dot or 8-dot.
    TODO: For students to complete.

    >>> is_ostring('o.\\noo\\n..')
    True
    >>> is_ostring('o.\\noo\\n..\\noo')
    True
    >>> is_ostring('o.\\n00\\n..\\noo')
    False
    >>> is_ostring('o.\\noo')
    False
    >>> is_ostring('o.o\\no\\n..')
    False
    >>> is_ostring('o.\\noo\\n..\\noo\\noo')
    False
    >>> is_ostring('\\n')
    False
    >>> is_ostring('A')
    False
    '''   
    exclude_slash = "" #initiates the version of s without \n 's as the empty string
    
    for index1 in range(0, len(s)):
        if s[index1] not in ("o",".","\n"): # Checks whether all characters in s are either o, . or \n
            return False
        if s[2::3] not in "\n\n\n": #Checks whether the line breaks are at indexes 2, 5 and 8
            return False
        if s[index1] != "\n": #excludes the line breaks from the s string
            exclude_slash += s[index1]

    if len(exclude_slash) not in (6,8) : #returns false if the remaining string (without \n) does not have length 6 or 8
        return False

    for index2 in range(0,8):
       if raisedpos_to_binary(ostring_to_raisedpos(s))[index2] not in ("0","1"):
            return False #Checks whether s converted to a binary number is only made up of 0's and 1's
    return True
   
def ostring_to_unicode(s):
    '''
    (str) -> str
    If s is a Braille cell in o-string format, convert it to unicode.
    Else return s.

    Remember from page 4 of the pdf:
    o-string -> raisedpos -> binary -> hex -> Unicode

    TODO: For students to complete.

    >>> ostring_to_unicode('o.\\noo\\n..')
    '⠓'
    >>> ostring_to_unicode('o.\\no.\\no.\\noo')
    '⣇'
    >>> ostring_to_unicode('oo\\noo\\noo\\noo')
    '⣿'
    >>> ostring_to_unicode('oo\\noo\\noo')
    '⠿'
    >>> ostring_to_unicode('..\\n..\\n..')
    '⠀'
    >>> ostring_to_unicode('a')
    'a'
    >>> ostring_to_unicode('\\n')
    '\\n'
    '''
    if is_ostring(s):
        return hex_to_unicode(binary_to_hex(raisedpos_to_binary(ostring_to_raisedpos(s))))
    else:
        return s

#If s is an ostring, then it converts s as such: ostring -> raisedpos -> binary -> hex -> unicode
# If s is not an ostring, it returns s unchanged

if __name__ == '__main__':
    doctest.testmod()
