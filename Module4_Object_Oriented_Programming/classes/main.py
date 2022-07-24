# Do not modify these lines
__winc_id__ = '04da020dedb24d42adf41382a231b1ed'
__human_name__ = 'classes'

# Add your code after this line

# 1 Players

class Player():
    def __init__(self, name, speed, endurance, accuracy):
        self.name = name
        self.speed = speed
        self.endurance = endurance
        self.accuracy = accuracy
        float_values = [speed, endurance, accuracy]
        for value in float_values:
            if 0 <= value <= 1 or 1 <= value <= 0:
                pass
            else:
                raise ValueError

    def introduce(self):
        return f"Hello everyone, my name is {self.name}."

    def strength(Self):
        if Self.endurance < Self.speed > Self.accuracy:
            return ('speed', Self.speed)
        elif Self.speed < Self.endurance > Self.accuracy:
            return ('endurance', Self.endurance)
        else:
            return ('accuracy', Self.accuracy)


# 2 Commentators

class Commentator():
    def __init__(self, name):
        self.name = name

    def sum_player(self, player):
        speed = getattr(player, 'speed')
        endurance = getattr(player, 'endurance')
        accuracy = getattr(player, 'accuracy')
        return speed + endurance + accuracy

    def compare_players(self, player_1, player_2, attribute):
        p1_name = getattr(player_1, "name")
        p2_name = getattr(player_2, "name")
        p1_attribute = getattr(player_1, attribute)
        p2_attribute = getattr(player_2, attribute)
        p1_strength = player_1.strength()
        p2_strength = player_2.strength()
        p1_sum = self.sum_player(player_1)
        p2_sum = self.sum_player(player_2)
        if p1_attribute > p2_attribute:
            return p1_name
        elif p2_attribute > p1_attribute:
            return p2_name
        elif p1_strength > p2_strength:
            return p1_name
        elif p2_strength > p1_strength:
            return p2_name
        elif p1_sum > p2_sum:
            return p1_name
        elif p2_sum > p1_sum:
            return p2_name
        else:
            return 'These two players might as well be twins!'


if __name__ == "__main__":
    eva = Player("Eva", 0.4, 0.5, 0.8)
    chris = Player("Chris", 0.6, 0.8, 0.7)
    ray = Commentator('Ray Hudson')
    print(type(chris.strength()))
