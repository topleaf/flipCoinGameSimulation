from flipGame import FlipGame

class SimStat(object):
    def __init__(self, probA, probB, n, id):
        self.probA = probA
        self.probB = probB
        self.guestWinCount = 0
        self.guestAmount = 0
        self.hostWinCount = 0
        self.hostAmount = 0
        self.hostWinRatio = 0
        self.total = n
        self.id = id
        self.hostPositiveCount = 0
        self.guestPositiveCount = 0
        self.samePositiveCount = 0
        self.sameNegativeCount = 0
        self.diffPNCount = 0
        self.hostPositiveRatio = 0.0

    def print_result(self):
        if self.hostAmount > 0:
            print('id:%3d, probHost=%0.3f(act %0.3f),probGuest=%0.3f, HostWin#:%5d(p#:%5d), GuestWin#:%5d (p#:%5d)'
                  ' samePosiCount=%5d,sameNegaCount=%5d,diffPNCount=%5d'
                  ' HostAmount:%5d, guestAmount:%5d, HostWinRatio = %0.2f%%'
                  %(self.id, self.probA, self.hostPositiveRatio, self.probB,self.hostWinCount,self.hostPositiveCount,
                    self.guestWinCount, self.guestPositiveCount,
                    self.samePositiveCount,self.sameNegativeCount, self.diffPNCount,
                    self.hostAmount, self.guestAmount, self.hostWinRatio)
                  )
        else:
            print('id:%3d, probHost=%0.3f(act %0.3f),probGuest=%0.3f, HostWin#:%5d(p#:%5d), GuestWin#:%5d (p#:%5d)'
                  ' samePosiCount=%5d,sameNegaCount=%5d,diffPNCount=%5d'
                  ' HostAmount:%5d, guestAmount:%5d, HostWinRatio = %0.2f%% ==> HOST LOSES MONEY'
                  %(self.id, self.probA, self.hostPositiveRatio, self.probB,self.hostWinCount,self.hostPositiveCount,
                    self.guestWinCount, self.guestPositiveCount,
                    self.samePositiveCount,self.sameNegativeCount, self.diffPNCount,
                    self.hostAmount, self.guestAmount, self.hostWinRatio)
                  )

    def update(self, game: FlipGame):
        hostSide, guestSide = game.getResult()
        if guestSide == 0:
            self.guestPositiveCount += 1
        if hostSide == 0:
            self.hostPositiveCount += 1
        if hostSide == guestSide:
            if hostSide == 0:
                self.guestAmount += 3
                self.hostAmount -= 3
                self.samePositiveCount += 1
            else:
                self.guestAmount += 1
                self.hostAmount -= 1
                self.sameNegativeCount += 1
            self.guestWinCount += 1
        else:
            self.hostAmount += 2
            self.guestAmount -= 2
            self.hostWinCount += 1
            self.diffPNCount += 1

        self.hostWinRatio = self.hostWinCount/self.total*100
        self.hostPositiveRatio = self.hostPositiveCount/self.total
