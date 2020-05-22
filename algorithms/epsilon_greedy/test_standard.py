import random

SEED = 19930219

random.seed(SEED)
means = [.1, .1, .1, .1, .9]
n_arms = len(means)
random.shuffle(means)
arms = map(lambda (mu): BernoulliArm(mu), means)