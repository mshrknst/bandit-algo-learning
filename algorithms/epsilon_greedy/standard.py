import random

class EpsilonGreedy(object):
    def __init__(self, epsilon, counts, values):
        self.epsilon = epsilon
        self.counts = counts
        self.values = values
        return

    def initialize(self, n_arms):
        self.counts = [0 for count in range(n_arms)]
        self.values = [0.0 for value in range(n_arms)]
        return

    def select_arm(self):
        """
        return int: arm index which you should select in next turn
        """
        if random.random() > self.epsilon:
            return self.__get_max_index(self.values)

        else:
            return random.randrange(len(self.values))

    def update(self, chosen_arm, reward):
        ##
        self.counts[chosen_arm] += 1
        n = self.counts[chosen_arm]

        ##
        now_value = self.values[chosen_arm]
        new_value = ((n - 1) / float(n)) * now_value + (1 / float(n)) * reward  # weighted ave
        self.values[chosen_arm] = new_value
        return

    def __get_max_index(self, x):
        max_x = max(x)
        return x.index(max_x)