import myclass
import passanger
import total_TIME


class plane:
    def __init__(self, dist, num, dur):
        self.myclass = myclass()
        self.passanger = passanger(num)
        self.total_TIME = total_TIME(dur)
        self.dist = dist
        self.seats = 200

    def sum(self):
        if not self.myclass.validThis(self.dist):
            return -1
        if not self.passanger.validNumber():
            return -1
        if not not self.total_TIME.is_valid_total_TIME():
            return -1

        numberTotal = self.costBas
        numberTotal += self.myclass.get_extraCost(self.dist)
        numberTotal += self.total_TIME.getFee()
        numberTotal -= self.total_TIME.getTheBestPromoEver()

        discount = self.passanger.forHereDiscount()
        numberTotal = numberTotal - (numberTotal * discount)

        return max(int(numberTotal), 0)
