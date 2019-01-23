# https://www.reddit.com/r/dailyprogrammer/comments/a72sdj/20181217_challenge_370_easy_upc_check_digits/

#* [2018-12-17] Challenge #370 [Easy] UPC check digits

#? To calculate the check digit:
#? 1. Sum the number at odd # positions
#? 2. Multiply the result by 3
#? 3. Sum digits at even # positions
#? 4. Add the result to step 2 result
#? 5. Calculate (step 3 result) modulo 10, assign to var M
#? 6. if M == 0: check_digit = 0; else: check_digit = 10 - M

#TODO: Given an 11-digit number, find the 12th digit that would make a valid UPC. You may treat the input as a string if you prefer, whatever is more convenient. If you treat it as a number, you may need to consider the case of leading 0's to get up to 11 digits. That is, an input of 12345 would correspond to a UPC start of 00000012345.

def upc():
    
