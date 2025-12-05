import datetime

class CricketPlayer:
    teamSize = 11
    def __init__(self, fName, lName, bDate, country):
        self.firstName= fName
        self.lastName=lName
        self.birthDate=bDate
        self.country= country
        self.scores = []

    def addScore(self, score):
        self.scores.append(score)

    def avgScore(self):
        return sum(self.scores)/len(self.scores)

    def calAge(self):
        return datetime.datetime.now().year-self.birthDate

    def __str__(self):
        return f"{self.firstName} {self.lastName}, the cricket player from {self.country}"

    def __lt__(self, other):
        selfavgScore = self.avgScore()
        otheravgScore = other.avgScore()
        return selfavgScore<otheravgScore

Virat = CricketPlayer('Virat', 'Kohli', 1980, 'India')
Virat.addScore(87)
Virat.addScore(98)
Virat.addScore(55)

David = CricketPlayer('David', 'Warner', 1977, 'Aus')
David.addScore(78)
David.addScore(55)
David.addScore(47)


print(Virat<David)
