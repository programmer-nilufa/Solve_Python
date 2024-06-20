import math
def paint_color(height,width,cover):
    area = height*width
    # cans = round(area/cover) # 2.445 = 2
    cans = math.ceil(area/cover) # 2.445 = 3
    print(f"You will need {cans} number of cans")

h = int(input("Enter the height here: \n"))
w = int(input("Enter the width here: \n"))
coverage = 7

paint_color(height=h, width=w, cover=coverage)
