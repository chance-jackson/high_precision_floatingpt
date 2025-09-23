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