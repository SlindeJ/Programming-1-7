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
        return True    #  return immeditely exit the funcition
      self.tl()
      return False
      
    def rib(self) -> bool:
      """Right is blocked"""
      return not self.ric()

    def mazemove(self):
      """Maze Move"""
      if self.fob():
        self.tl()
      else:       #    otherwise...
        self.m()
        if self.ric():
          self.tr()
          self.m()
          if self.ric():
            self.tr()
            self.m()
      pass

def main():
    """ Karel code goes here! """
    kt = ktools()
    pass


if __name__ == "__main__":
    run_karel_program()
