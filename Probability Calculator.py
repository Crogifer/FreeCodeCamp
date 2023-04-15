import random
import copy

class Hat:

    #takes dictionary of balls and multiplies keys by values to create list
    def __init__(self, **balls):

        self.contents = []

        for k, v in balls.items():
            self.contents += [k]*v

    #draw input number of balls or total amount of balls and for each unit in number picks a random index which is then removed and added to ball draw object
    def draw(self, n):
        num = min(n, len(self.contents))
        ball_draws = []
        for nums in range(num):
            removed = random.randint(0, len(self.contents)-1)
            ball_draws.append(self.contents.pop(removed))
        return ball_draws


    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    Matches = 0
    Successes = 0

    #for each experiment, a deep copy of hat is made and the draw method called. For all colours drawn, if the number of required balls of that colour is met, colour matches is iterated, if all colour numbers are met, match true
    for run in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        ball_draw = new_hat.draw(num_balls_drawn)

        for colour in expected_balls.keys():
            if ball_draw.count(colour) >= expected_balls[colour]:
                Matches += 1
                print("m" + str(Matches))

        #print(len(expected_balls))
        if Matches == len(expected_balls):
            Successes += 1
            Matches = 0
            print("s" + str(Successes))
        else:
            Matches = 0

    print(Successes, num_experiments)
    probability = Successes / num_experiments
    return probability

hat = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability)