#!/usr/bin/python3
from time import time
from random import randint
from statistics import mean
from math import ceil
from ascii_fig import AsciiFig

class Challenge:
  def __init__( self, question, answer):
    self.question = question
    self.answer = answer
    self.user_resp = None
    self.user_time = None
    self.user_score = None 

  def ask( self ):
    time_start = time()    
    self.user_resp = input("%s"%self.question)
    self.user_time = time() - time_start
    try:
      self.user_score = int(self.user_resp ) == self.answer
    except ValueError:
      self.user_score = False


class Practice:

  def __init__( self, y_range=[ 3, 4 ], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None):
    """ generates challenge_nbr questions for table y """
    self.y_start = y_range[ 0 ]
    self.y_stop = y_range[ 1 ]
    self.x_start = x_range[ 0 ] 
    self.x_stop = x_range[ 1 ] 
    self.challenge_nbr = challenge_nbr
#    for param in  [self.y_start, self.y_stop, self.x_start, self.x_stop ]:
#      if isinstanceof( param, int) == False:
#        raise ValueError 
    self.welcome( self.y_start, self.y_stop, self.challenge_nbr )
    ## building challenges
    self.challenge_list = [ self.get_challenge() for i in range( challenge_nbr ) ]
    self.ascii_fig = ascii_fig
    
    for challenge in self.challenge_list:
      challenge.ask()

    self.evaluate()
    self.score = None
    self.time = None

  def welcome( self, y_start, y_stop, challenge_nbr ):
    print("Hi! \nLet's practice table %s-%s with %s challenges"%( y_start, y_stop, challenge_nbr))

  def get_xy( self, commutative=True ):
    """ return x and y. commutative indicates these can be shuffle """
    y = randint( self.y_start, self.y_stop )
    x = randint( self.x_start, self.x_stop )
    if commutative == True:
      if randint(0, 1) == 0:
        x_tmp = x
        x = y 
        y = x_tmp
    return x, y

  def get_challenge(self):
    """ generates a question of type x * y """
    return Challenge( "%s x %s = "%(x, y), x*y ) 
      

  def evaluate(self):
    score = 0
    for challenge in self.challenge_list:
      if challenge.user_score == True:
        score += 1
    self.score = score / self.challenge_nbr * 100 

    if self.score == 100 :
      print( "SUPER !!!!! SUPER !!! SUPER !!!!" )
      print( "100% - 100% - 100% - 100% - 100%" )
    elif self.score > 50: 
      print("Congratulation!")

    if self.score != 100:
      print("Let's check some of the questions...")
      for challenge in self.challenge_list:
        while challenge.user_score == False:
          challenge.ask()
      print("Super! Your score was %s%% and is now 100%%!"%ceil(self.score))

    self.time = mean( [ challenge.user_time for chalenge in self.challenge_list ] )
    print("Your mean response time is: %.2f"%self.time )
    if self.ascii_fig != None:
      ## the random is use to prevent only the large pictures to be shown
      r = randint(0, 5) 
      if r >= 3:
        score = None
      print(self.ascii_fig.pick_fig( score ) )
      
class PractiseAddition( Practice ):

  def __init__( self, y_range=[ 0, 10], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None ):
    super().__init__( y_range=y_range, x_range=x_range, challenge_nbr = challenge_nbr, ascii_fig=ascii_fig )

  def get_challenge(self):
    """ generates a question of type x * y """
    x, y = self.get_xy()
    return Challenge( "%s + %s = "%(x, y), x + y ) 

class PractiseSubtraction( Practice ):

  def __init__( self, y_range=[ 0, 10], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None ):
    super().__init__( y_range=y_range, x_range=x_range, challenge_nbr = challenge_nbr, ascii_fig=ascii_fig )

  def get_challenge(self):
    """ generates a question of type x * y """
    x, y = self.get_xy(commutative=False)
    m = min( [ x, y ] )
    M = max( [ x, y ] )
    return Challenge( "%s - %s = "%(M, m), M - m ) 

class PractiseMultiplication( Practice ):

  def __init__( self, y_range=[ 3, 4 ], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None ):
    super().__init__( y_range=y_range, x_range=x_range, challenge_nbr = challenge_nbr, ascii_fig=ascii_fig )

  def get_challenge(self):
    """ generates a question of type x + y """
    x, y = self.get_xy()
    return Challenge( "%s x %s = "%(x, y), x*y ) 

class PractiseDivision( Practice ):

  def __init__( self, y_range=[ 3, 4 ], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None ):
    super().__init__( y_range=y_range, x_range=x_range, challenge_nbr = challenge_nbr, ascii_fig=ascii_fig )

  def get_challenge(self):
    """ generates a question of type x + y """
    x, y = self.get_xy()
    m = x * y
    return Challenge( "%s / %s = "%(m, x), y ) 

class PractiseDivisionWithRemainder( Practice ):

  def __init__( self, y_range=[ 3, 4 ], x_range=[ 1, 10 ], challenge_nbr = 20, ascii_fig=None ):
    super().__init__( y_range=y_range, x_range=x_range, challenge_nbr = challenge_nbr, ascii_fig=ascii_fig )

  def get_challenge(self):
    """ generates a question of type x + y """
    x, y = self.get_xy()
    m = min( [ x, y ] )
    M = max( [ x, y ] )
    d = int( M / m )
    r = M - d * m
    return Challenge( "%s / %s = "%(M, m), ( d, r )  ) 

if __name__ == "__main__":
    PractiseMultiplication()

