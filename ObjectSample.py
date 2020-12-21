class Security:
    sec_name = 'Secrity'
    def __init__(self, name):
        self.sec_name = name
    def price(self):
        print("abstract price of a security")
    def printname(self):
        print( self.sec_name + '\n')


class Bond(Security):

    def __init__(self, secname='Bond', par=100):
        super().__init__(secname)
        self.par=par
    
    def price(self):
        print("Bond price is "+ str(self.par))

    
    
def main():

    s1 = Security('Note-A')
    s1.printname()

    b1 = Bond("BoneC", 99)
    b1.printname()


if __name__ == '__main__':
    main()
else:
    #module-spcific init code



