class myclass:
    def __init__(self):
        self.myFav = {'Paris': 500, 'NYC': 600}

    def get_extraCost(self, dist):
        return self.myFav.get(dist, 0)

    def validThis(self, dist):
        return isinstance(dist, str)
