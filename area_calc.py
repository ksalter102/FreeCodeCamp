import math


test_h = int(input("Height of the wall:"))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    area = height * width
    num_of_cans = math.ceil(area / cover)
    print(f"You'll need {num_of_cans} cans of paint.")

paint_calc(height=test_h, width=test_w, cover=coverage) #key