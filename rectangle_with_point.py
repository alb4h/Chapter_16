from unit_tester import test


class Point:

    def __init__(self, x=0, y=0):
        """Create a new Point, at coordinates x, y"""
        self.x = x
        self.y = y

    def distance_from_origin(self):
        """Compute my distance from the origin"""
        return ((self.x ** 2) + (self.y ** 2)) ** .5

    def midpoint(p1, p2):
        """Return the midpoint of points p1 and p2"""
        mx = (p1.x + p2.x) / 2
        my = (p1.y + p2.y) / 2
        return Point(mx, my)

    def halfway(self, target):
        """ REturn the halfway point between myself and the target"""
        mx = (self.x + target.x) / 2
        my = (self.y + target.y) / 2
        return Point(mx, my)

    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)


    def get_line_to(self, pt2):
        m = (self.y - pt2.y) / (self.x - pt2.x)
        b = self.y - m * self.x
        return "({0}, {1})".format(m,b)


class Rectangle:
    '''A class to manufacture rectangle objects'''

    def __init__(self, posn, w, h):
        """ Initialize rectangle at posn, with width w, height h"""
        self.corner = posn
        self.width = w
        self.height = h

    def __str__(self):
        return "({0}, {1}, {2})".format(self.corner, self.width, self.height)

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * self.width + 2 * self.height

    def flip(self):
        """ Swaps the values of height and width"""
        (self.height, self.width) = (self.width, self.height)

    def contains_point(self, pt):
        """ Return True if my sprite rectangle contains point pt"""
        # (my_x, my_y) = (self.corner.x, self.corner.y)
        # my_width = self.width
        # my_height = self.height
        # (x, y) = (pt.x, pt.y)

        # return ( x >= my_x and x< my_x + my_width and y >= my_y and y < my_y + my_height)

        return (
                self.corner.x <= pt.x < self.corner.x + self.width
                and self.corner.y <= pt.y < self.corner.y + self.height)


box = Rectangle(Point(0, 0), 100, 200)
bomb = Rectangle(Point(100, 80), 5, 10)

# print("box:  ", box)
# print("bomb:  ", bomb)
# print(box.area())
# print(bomb.area())

r = Rectangle(Point(0, 0), 10, 5)
test(r.area() == 50)
test(r.perimeter() == 30)

r = Rectangle(Point(100, 50), 10, 5)
test(r.width == 10 and r.height == 5)
r.flip()
test(r.width == 5 and r.height == 10)
print(Point(0, 0))
test(r.contains_point(Point(104, 50)))

p = Point(3,3)
print(p.get_line_to(Point(0,3)))
print(Point(4,11).get_line_to(Point(6,15)))