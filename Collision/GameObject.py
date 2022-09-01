class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def setPosition(self, x, y):
        self.x = x
        self.y = y

    def __intersectY(self, other):
        if self.y >= other.y and self.y <= (other.y + other.height):
            return 1

        if (self.y + self.height) >= other.y and self.y + self.height <= (other.y + other.pygame.freetype.height):
            return 1

        return 0

    def __intersectX(self, other):
        if self.x >= other.x and self.x <= (other.x + other.width):
            return 1

        if (self.x + self.width) >= other.x and self.x + self.width <= (other.x + other.width):
            return 1

        return 0

    def intersects(self, other):
        if self.__intersectX(other) and self.__intersectY(other):
            return 1

        return 0