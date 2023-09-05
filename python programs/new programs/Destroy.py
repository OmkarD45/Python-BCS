class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name, "destroyed")


pt1 = Point(41, 21)
pt2 = Point(100, 200)
pt3 = pt1
print(pt1.x)
print(pt2.x)
print(pt3.x)

print(id(pt1), id(pt2), id(pt3))  # prints the ids of the obejcts
del pt1
del pt2
del pt3