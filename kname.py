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

    def j(self):
        """Print J using beepers"""
        self.tl()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.m()
        self.tl()
        self.put5()
        self.tl()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.m()
        self.put()
        self.tr()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()

    def a(self):
        """Print A using beepers"""
        self.tl()
        self.put2()
        self.m()
        self.put2()
        self.m()
        self.tr()
        self.m()
        self.put2()
        self.m()
        self.tr()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.put2()
        self.ta()
        self.m()
        self.m()
        self.tr()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()

    def c(self):
        """Print C using beepers"""
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.put()
        self.m()
        self.tr()
        self.m()
        self.put2()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.put2()
        self.m()
        self.put()
        self.m()
        self.m()

    def o(self):
        """Print O using beepers"""
        self.tl()
        self.put5()
        self.ta()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.put2()
        self.m()
        self.tl()
        self.put5()
        self.tl()
        self.m()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()
        self.tl()
        self.m()
        self.m()
        self.m()
        self.m()

    def b(self):
        """Print B using beepers"""
        self.tl()
        self.put5()
        self.tr()
        self.m()
        self.put2()
        self.tr()
        self.m()
        self.tl()
        """edited"""
        self.m()
        self.put()
        self.ta()
        self.m()
        self.tl()
        self.m()
        self.tr()
        self.put2()
        self.tl()
        self.m()
        self.m()
        self.tl()
        self.put2()
        self.m()
        self.tl()
        self.m()
        self.put()
        self.ta()
        self.m()
        self.tl()
        self.m()


def main():
    """ Karel code goes here! """
    kt = ktools()
    kt.tl()
    kt.m()
    kt.tr()
    kt.j()
    kt.a()
    kt.c()
    kt.o()
    kt.b()

    pass


if __name__ == "__main__":
    run_karel_program()
