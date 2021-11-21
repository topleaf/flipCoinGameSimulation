from random import random

class FlipGame(object):
    def __init__(self, prob_host,prob_guest):
        self.prob_host = prob_host
        self.prob_guest = prob_guest
        self.host_side = 0
        self.guest_side = 0

    def getResult(self):
        """

        :return: hostSide, guestSide
         0 : positive side, 1 : negative side
        """
        return self.host_side,self.guest_side

    def play(self):
        r = random()
        if r < self.prob_host:
            self.host_side = 0
        else:
            self.host_side = 1
        if r < self.prob_guest:
            self.guest_side = 0
        else:
            self.guest_side = 1

