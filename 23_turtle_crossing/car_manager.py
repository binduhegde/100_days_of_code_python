from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        # these are the cars which go from left to right
        self.left_cars = []
        # these are the cars which go from right to left
        self.right_cars = []
        # all the cars added
        self.all_cars = self.left_cars+ self.right_cars
        self.move_distance = STARTING_MOVE_DISTANCE
        # draws road's white lanes
        self.draw_lanes()

    def draw_lanes(self):
        t = Turtle()
        t.pensize(2)
        t.color('white')
        t.hideturtle()
        # double lines
        # these are the 4 lines it will draw. 2 in the middle separating the left-to-right and ight-to-left cars
        # and 2 as the border lines
        line_positions = [(300, 270), (300, 5), (300, -5), (300, -260)]
        for position in line_positions:
            t.penup()
            t.goto(position)
            t.pendown()
            t.backward(600)

        # dashed lanes
        # in the middle of each seaction
        dash_positions = [(300,138), (300, -138)]
        for position in dash_positions:
            t.penup()
            t.goto(position)
            for _ in range(15):
                t.penup()
                t.backward(20)
                t.pendown()
                t.backward(20)

    def create_car(self):
        # possible position for a car which goes from right to left
        positions_right = [36, 72, 108, 174, 220, 250]
        # possible position for a car which goes from left to right
        positions_left = [-36, -72, -108, -174, -220, -250]

        # starting x cordinates for the 2 sections(left-to-right and ight-to-left)
        for x in [300, -300]:
            # probability of creation of a car is 10%
            # otherwise the freq of cars will be too much
            rand_num = random.randint(1, 10)
            if rand_num == 1:
                new_car = Turtle('square')
                new_car.color(random.choice(COLORS))
                new_car.penup()
                # to make it a rectangle instead of a square
                new_car.shapesize(stretch_wid=1, stretch_len=2)
                # if x cordinate is 300 (if car is going from right to left),
                # new car's y cordinate will be chosen from positions_right
                if x == 300:
                    new_car.goto(x, random.choice(positions_right))
                    self.right_cars.append(new_car)
                # if x cordinate is -300 (if car is going from left to right),
                # new car's y cordinate will be chosen from positions_left
                else:
                    new_car.goto(x, random.choice(positions_left))
                    self.left_cars.append(new_car)

    def move_cars(self):
        # move left cars forward and right cars backwards
        for car in self.right_cars:
            car.backward(self.move_distance)
        for car in self.left_cars:
            car.forward(self.move_distance)

    def next_level(self):
        self.move_distance += MOVE_INCREMENT


