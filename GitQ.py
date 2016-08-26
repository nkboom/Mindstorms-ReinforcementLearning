import random

class QLearn:
    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {}

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = actions

    def getQ(self, state, action):
        return self.q.get((state, action), 0.0)

    def learnAlg(self, state, action, reward, value):
        OldValue = self.q.get((state, action), None)
        if OldValue is None:
            self.q[(state, action)] = reward
        else:
            self.q[(state, action)] = OldValue + self.alpha * (value - OldValue)

    def chooseAction(self, state):
        if random.random() < self.epsilon:
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            maximumQ = max(q)
            count = q.count(maximumQ)
            if count > 1:
                LookNSee = [i for i in range(len(self.actions)) if q[i] == maximumQ]
                i = random.choice(LookNSee)
            else:
                i = q.index(maximumQ)
            action = self.actions[i]
        return action

    def learn(self, state1, action1, reward, state2):
        maxqnew = max([self.getQ(state2, a) for a in self.actions])
        self.learnAlg(state1, action1, reward, reward + self.gamma*maxqnew)
