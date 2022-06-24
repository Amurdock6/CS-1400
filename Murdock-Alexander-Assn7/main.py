# Alexander Murdock
# CS-1400-002

class Artomat:
    def __init__(self, text1, text2, text3, text4, bin1=10, bin2=10, bin3=10, bin4=10, money=0, hopper=0):             
        self.text1 = text1
        self.text2 = text2
        self.text3 = text3
        self.text4 = text4
        self.bin1 = bin1
        self.bin2 = bin2
        self.bin3 = bin3
        self.bin4 = bin4
        self.hopper = hopper
        self.money = money
        
    def printStatus(self):
        print("")
        print("1: %d packs of %s" % (self.bin1, self.text1))
        print("2: %d packs of %s" % (self.bin2, self.text2))
        print("3: %d packs of %s" % (self.bin3, self.text3))
        print("4: %d packs of %s" % (self.bin4, self.text4))
        print("There is $ %.2f in the machine." % self.money)
        print("There is $ %.2f in the hopper." % self.hopper)
        print("")
        
    def dropQuarter(self):
        print("ching")
        self.hopper += 0.25
    
    def pullKnob(self, itemSelected):
        if self.hopper >= 0.75:
            if itemSelected == 1:
                print("A pack of %s slide into view." % self.text1)
                self.bin1 -= 1
            elif itemSelected == 2:
                print("A pack of %s slide into view." % self.text2)
                self.bin2 -= 1
            elif itemSelected == 3:
                print("A pack of %s slide into view." % self.text3)
                self.bin3 = - 1
            elif itemSelected == 4:
                print("A pack of %s slide into view." % self.text4)
                self.bin4 = - 1
            else:
                print("Error, Don't know what item you wanted to select?")
            self.money += self.hopper
            self.hopper = 0
            
        else:
            print("(nothing happens)")
    
    def restock(self):
        self.money = 0
        self.bin1 = 10
        self.bin2 = 10
        self.bin3 = 10
        self.bin4 = 10

        print("A grouchy-looking attendent shows up, opens the back, fiddles around a bit, closes it, and leaves.")


# write your class definition above this line
# make no changes below this line

def main():
    photoMachine = Artomat(text1="Adams", text2="Arbus", text3="Dali", text4="Lange")
    portraitMachine = Artomat(money=212, hopper=2, bin1=1, bin2=0, bin3=8, bin4=10, text1="Picasso", text2="Rembrandt", text3="Van Gogh", text4="Monet")

    photoMachine.printStatus()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(1)
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.dropQuarter()
    photoMachine.pullKnob(2)
    photoMachine.printStatus()
    photoMachine.restock()
    photoMachine.printStatus()
    print("----")
    portraitMachine.printStatus()
    portraitMachine.dropQuarter()
    portraitMachine.pullKnob(1)
    portraitMachine.printStatus()


main()
