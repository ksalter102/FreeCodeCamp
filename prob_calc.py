import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for key, value in kwargs.items():
            for i in range(value):
                self.contents.append(key)

    def draw(self, number_of_balls):
        balls_returned = list()
        for i in range(min(len(self.contents), number_of_balls)):
            removed = self.contents.pop(random.randrange(len(self.contents)))
            balls_returned.append(removed)

        return balls_returned

    def draw_experiment(self, number_of_balls):
        balls_returned = list()
        contents_copy = self.contents.copy()
        for i in range(min(len(self.contents), number_of_balls)):
            removed = self.contents.pop(random.randrange(len(self.contents)))
            balls_returned.append(removed)

        self.contents = contents_copy.copy()
        return balls_returned

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    N = num_experiments

    for _ in range(N):
        result = hat.draw_experiment(num_balls_drawn)

        if all(result.count(key) >= value for (key,value) in expected_balls.items()):
            M = M + 1

    return M / N

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red":2,"green":1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)