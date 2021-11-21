# simulate 2 person flip coin,
# the game rule is:
# 1. 2 players play this game, player host and guest
# 2. both players show a coin, if both coins' upside , then the guest win 3 bucks
#    if both coins' downside, the the guest win 1 bucks. otherwise, the guest lose 2 bucks
from simStat import SimStat
from flipGame import FlipGame


class Simulation(object):
    def __init__(self, probA, probB, n, id):
        self.probHost = probA
        self.probGuest = probB
        self.iteration = n
        self.simStat = SimStat(probA, probB, n, id)

    def run(self):
        for i in range(self.iteration):
            aGame = FlipGame(self.probHost, self.probGuest)
            aGame.play()
            self.simStat.update(aGame)

    def print_result(self):
        self.simStat.print_result()

if __name__ == "__main__":
    for i in range(11):
        for j in range(11):
            probA = 0.333 + (0.4-0.333)/10 * i
            probB = j * 0.1
            aSimu = Simulation(probA, probB, 30000, i*11+j)
            aSimu.run()
            aSimu.print_result()
