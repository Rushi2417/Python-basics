import datetime
class Player:
    def __init__(self, fName, lName, bDate):
        self.firstName= fName
        self.lastName=lName
        self.birthDate=bDate
    def calAge(self):
        return datetime.datetime.now().year-self.birthDate

class CricketPlayer(Player):
    pass

class TennisPlayer(Player):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname, year)
        self.aces = []

Roger = CricketPlayer('Roger', 'Khanna', 1985)
print(Roger.firstName)