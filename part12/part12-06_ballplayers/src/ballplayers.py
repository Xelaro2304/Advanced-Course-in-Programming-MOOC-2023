class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')


# Write your solution here
def most_goals (ballplayers: list):
    return max(ballplayers, key= lambda player: player.goals).name

def most_points (ballplayers: list):
    mvp = max(ballplayers, key= lambda player: (player.goals + player.passes))
    return mvp.name, mvp.number

def least_minutes (ballplayers: list):
    return min(ballplayers, key= lambda player: player.minutes)