import myclass
import passanger
import total_TIME


class vacation:
    costBas = 1000

    def __init__(self, dist, num, dur):
        self.myclass = myclass.myclass()
        self.passanger = passanger.passanger(num)
        self.total_TIME = total_TIME.total_TIME(dur)
        self.dist = dist

    def sum(self):
        # sum the cost of the vacation package here
        if not self.myclass.validThis(self.dist):
            return -1
        elif not self.passanger.validNumber():
            return -1
        elif not self.total_TIME.is_valid_total_TIME():
            return -1

        # sum the total cost
        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)
