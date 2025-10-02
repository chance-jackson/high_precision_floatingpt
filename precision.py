import numpy as np

class Precision():
    def __init__(self, num):
        self.num = num

    def splitting(self):
        num_str = str(self.num)
        parts = num_str.split('.')
        numer = parts[0]
        if len(parts) > 1:
            dec = parts[1]
        else:
            dec = 0
        return(int(numer), int(dec))
    
    def join(self, parts):
        return str(parts[0]) + "." + str(parts[1])
    
    def __add__(self, other):
        a_num, a_dec = self.splitting()
        b_num, b_dec = other.splitting()

        #  same length
        max_len = max(len(str(a_dec)), len(str(b_dec)))
        a_dec = str(a_dec).ljust(max_len, "0")
        b_dec = str(b_dec).ljust(max_len, "0")

        # add decimals
        dec_sum = int(a_dec) + int(b_dec)
        carry, dec_result = divmod(dec_sum, 10**max_len)

        # add integers + carry
        int_sum = int(a_num) + int(b_num) + carry

        # join back
        return self.join((int_sum, str(dec_result).zfill(max_len)))

    def __sub__(self, other):
        # ... (same length setup) ...
        # ... (a_dec, b_dec are zero-padded strings) ...

        a_num, a_dec = self.splitting()  #10.02 ===10 and 2
        b_num, b_dec = other.splitting()  #9.50 === 9 and 50 

        a_dec_int = int(a_dec)  
        b_dec_int = int(b_dec)

        max_len = max(len(str(a_dec)), len(str(b_dec))) #len = 2, len(50) = 2

        # sub decimals
        dec_diff = a_dec_int - b_dec_int #difference = 48 
        
        # carry will be 0 (no borrow) or -1 (borrow)
        carry = dec_diff // (10**max_len) #integer division, 48 divided by 100, gives me 0.
        dec_result = dec_diff % (10**max_len) #dec_result = 48 modulus 100 gives us 48 

        # sub integers + the carry (which is 0 or -1)
        int_sum = int(a_num) - int(b_num) + carry # carry should usually be zero 

        # join back
        return self.join((int_sum, str(dec_result).zfill(max_len)))

    def _mult_(self, other): 
        a_num, a_dec = self.splitting() #10.02 ---10, 2
        b_num, b_dec = other.splitting() #9.50 ---9, 50 

        # total digits after decimal
        total_dec = len(str(a_dec)) + len(str(b_dec)) # finds total digits in dec,=> len(a_dec) + len(b_dec) 1 + 2 = 3 

        # make whole integers
        a_whole = int(str(a_num) + str(a_dec)) #makes 10.02, 1002
        b_whole = int(str(b_num) + str(b_dec))

        # multiply
        prod = a_whole * b_whole
        prod_str = str(prod).zfill(total_dec + 1)

        # split back
        int_part = prod_str[:-total_dec] if total_dec else prod_str #converts back to decimal places 
        dec_part = prod_str[-total_dec:] if total_dec else "0"

        return self.join((int(int_part), dec_part))
    
    
    def __div__(self, other, precision=10):
        a_num, a_dec = self.splitting()
        b_num, b_dec = other.splitting()

        # scale to integers
        a_whole = int(str(a_num) + str(a_dec))
        b_whole = int(str(b_num) + str(b_dec))

        # adjust scaling factors
        scale = 10 ** max(len(str(a_dec)), len(str(b_dec)))
        a_scaled = a_whole * scale
        b_scaled = b_whole

        # do integer division
        quotient = a_scaled // b_scaled
        remainder = a_scaled % b_scaled

        # build decimal part manually
        dec_digits = []
        for _ in range(precision):
            remainder *= 10
            dec_digit, remainder = divmod(remainder, b_scaled)
            dec_digits.append(str(dec_digit))

        return self.join((quotient, "".join(dec_digits)))

    def __eq__(self, other):
        a_num, a_dec = self.splitting() #split numbers
        b_num, b_dec = other.splitting()
        
        #easiest to use in-built fltpt comparison
        if a_num != b_num or a_dec != b_dec:   #if either num or dec don't match
            return False                       #numbers dont match
        else:
            return True                        #else: true
    
    def __gt__(self, other):
        a_num, a_dec = self.splitting() #split numbers
        b_num, b_dec = other.splitting()
        
        if a_num > b_num:              
            return True
        elif a_num == b_num and a_dec > b_dec:
            return True
        else:
            return False

    def __lt__(self, other):
        a_num, a_dec = self.splitting() #split numbers
        b_num, b_dec = other.splitting()

        if a_num < b_num:
            return True
        if a_num == b_num and a_dec < b_dec:
            return True
        else:
            return False

    def __str__(self):
        a_num, a_dec = self.splitting() #split number, get two floating pt reps

        return str(a_num) + '.' + str(a_dec) #return concatenated string
