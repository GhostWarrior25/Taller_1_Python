class total_TIME:
    def __init__(self, dur):
        self.dur = dur

    def is_valid_total_TIME(self):
        return isinstance(self.dur, int) and self.dur > 0

    def getFee(self):
        return 200 if self.dur < 7 else 0

    def getTheBestPromoEver(self):
        return 200 if self.dur > 30 else 0

    def getWeekend(self):
        return 100 if self.dur > 7 else 0
