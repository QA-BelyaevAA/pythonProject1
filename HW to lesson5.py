class Football_player:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

class Forward(Football_player):
    def __init__(self, name, surname, scores_goals):
        super().__init__(name, surname)
        self.scores_goals = scores_goals

    def smoking(self):
        return 'I am like smoking kalyany'

class Goalkeeper(Football_player):
    def __init__(self, name, surname, catches_balls):
        super().__init__(name, surname)
        self.catches_balls = catches_balls

    def travmatics(self):
        return 'I am often travmatics'

class Half_back(Football_player):
    def __init__(self, name, surname, passing):
        super().__init__(name, surname)
        self.__passing = passing

    def get_passing(self):
        return f'I have {self.__passing}'

    def set_passing(self, newpassing):
        self.__passing = newpassing

    def rudeness(self):
        return 'I am so rudeness'

football_player1 = Football_player('Andrey', 'Tihonov')
print(football_player1.name, football_player1.surname)

forward1 = Forward('Роман', 'Павлюченко', 57)
print(forward1.name, forward1.surname, forward1.scores_goals)
print(forward1.smoking())

goalkeeper1 = Goalkeeper('Igor', 'Akinfeev', 50)
print(goalkeeper1.name, goalkeeper1.surname, goalkeeper1.catches_balls)
print(goalkeeper1.travmatics())

halfback1 = Half_back('Aleksey', 'Smertin', '85%')
print(halfback1.name, halfback1.surname, halfback1.passing)
print(halfback1.rudeness())
print(halfback1.passing)
halfback1.set_passing('90%')
