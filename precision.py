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
        return(numer, dec)
    
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
        a_num, a_dec = self.splitting()
        b_num, b_dec = other.splitting()

        #  same length
        max_len = max(len(str(a_dec)), len(str(b_dec)))
        a_dec = str(a_dec).ljust(max_len, "0")
        b_dec = str(b_dec).ljust(max_len, "0")

        # sub decimals
        dec_sum = int(a_dec) - int(b_dec)
        carry, dec_result = divmod(dec_sum, 10**max_len)

        # sub integers - carry
        int_sum = int(a_num) - int(b_num) - np.abs(carry)

        # join back
        return self.join((int_sum, str(dec_result).zfill(max_len)))
    
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

        if a_num > b_num or a_dec > b_dec:
            return True
        else:
            return False

    def __lt__(self, other):
        a_num, a_dec = self.splitting() #split numbers
        b_num, b_dec = other.splitting()

        if a_num < b_num or a_dec < b_dec:
            return True
        else:
            return False

