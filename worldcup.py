# -*- coding:UTF-8 -*-
'''
Created on 2013-2-26

@author: Jonathan Lu
'''

def cardLuhnChecksumIsValid(card_number):
    """ checks to make sure that the card passes a luhn mod-10 checksum """
    sum = 0
    num_digits = len(card_number)
    oddeven = num_digits & 1
    for count in range(num_digits):
        digit = int(card_number[count])
        if not (( count & 1 ) ^ oddeven):
            digit = digit * 2
        if digit > 9:
            digit = digit - 9
        sum = sum + digit
    return (sum % 10) == 0    

my_card = "4581230118454166"

ret = cardLuhnChecksumIsValid(my_card)
if ret:
    print 'Valid'
else:
    print 'Invalid'