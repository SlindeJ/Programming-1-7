from stanfordkarel import *


class ktools:

    def m(self):
        """Shorthand for Move"""
        move()

    def tl(self):
        """Turn Left"""
        turn_left()

    def tr(self):
        """Turn Right"""
        self.tl()
        self.tl()
        self.tl()

    def ta(self):
        """Turn Around"""
        self.tl()
        self.tl()

    def pick(self):
        """Pick Beeper"""
        pick_beeper()

    def put(self):
        """Put Beeper"""
        put_beeper()

    def put2(self):
        """Put 2 beepers in a line"""
        self.put()
        self.m()
        self.put()

    def put5(self):
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.put()

    def fic(self) -> bool:
        """Front is clear"""
        return front_is_clear()

    def fib(self) -> bool:
        """Front is blocked"""
        return not self.fic()

    def ric(self) -> bool:
        """Right is clear"""
        self.tr()
        if self.fic():
            self.tl()
            return True  #  return immeditely exit the funcition
        self.tl()
        return False

    def rib(self) -> bool:
        """Right is blocked"""
        return not self.ric()

    def mazemove(self):
        """Maze Move"""
        if self.fib():
            self.tl()
        else:  #    otherwise...
            self.m()
            if self.ric():
                self.tr()
                self.m()
                if self.ric():
                    self.tr()
                    self.m()

    def mm(self, num):
        """Move Multiple"""
        for number in range(0, num):
            self.m()

    def putm(self, num):
        """Put Multiple"""
        for i in range(num - 1):
            self.put()
            self.m()
        self.put()

    def pickm(self, num):
        """Pick Multiple"""
        for _ in range(num - 1):
            self.pick()
            self.m()
        self.pick()

    def sob(self) -> bool:
        """Standing on beeper"""
        return beepers_present()

    def jump(self):
        """Jump for karel 510"""
        while self.fic():
            self.m()
        self.tl()
        while self.rib():
            self.m()
        self.tr()
        self.m()
        self.tr()
        while self.fic():
            self.m()
        self.tl()

    def find(self):
        """Find for 515"""
        while not facing_north():
            self.tl()
        self.m()
        if not self.sob():
            self.tl()
            self.m()
            self.tl()
            self.m()
        for _ in range(2):
            if not self.sob():
                self.m()
                self.tl()
                self.m()
        pass

    def garden(self, num):
        """Karel will plant beepers until all sides have beepers"""
        for _ in range(0, num):
            while front_is_clear() and right_is_clear() and left_is_blocked():
                self.put()  #karel follows the left wall
                self.m()
            while left_is_clear():
                self.tl()  #was an if
                self.put()
                self.m()
            while left_is_blocked() and front_is_blocked() and right_is_clear(
            ):
                self.tr()  #  was an if
        pass


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.mm(4)
    kt.tl()
    kt.mm(4)
    kt.tr()
    kt.garden(7)
    pass


if __name__ == "__main__":
    run_karel_program()
