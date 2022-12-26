#!/usr/bin/python3
from time import time
from random import randint
from statistics import mean
from math import ceil
from ascii_fig import AsciiFig
from inputimeout import inputimeout, TimeoutOccurred

class Challenge:
  def __init__( self, question, answer, index=None, timeout=None ):
    self.answer = answer
    self.user_resp = None
    self.user_time = None
    self.user_score = None 
    if isinstance( index, int ) is True :
      txt = f"{index}: "
    else:
      txt = ""
    self.question = f"{txt}{question}"
    self.timeout = timeout

  def ask( self ):
    time_start = time() 
    if self.timeout is None: 
      self.user_resp = input( self.question )
    else:
      try:
        self.user_resp = inputimeout( prompt=self.question, timeout=self.timeout )
      except TimeoutOccurred:
        self.user_resp = None
    self.user_time = time() - time_start
    try:
      self.user_score = int( self.user_resp ) == self.answer
    except( ValueError, TypeError ):
      self.user_score = False


class Practice:

  def __init__( self, y_range=[ 3, 4 ], x_range=[ 0, 10 ], challenge_nbr = 20, ascii_fig=None, timeout=None):
    """ generates challenge_nbr questions for table y """

    self.y_start = y_range[ 0 ]
    self.y_stop = y_range[ 1 ]
    self.x_start = x_range[ 0 ] 
    self.x_stop = x_range[ 1 ] 
    self.challenge_nbr = challenge_nbr
    self.timeout = timeout
#    for param in  [self.y_start, self.y_stop, self.x_start, self.x_stop ]:
#      if isinstanceof( param, int) == False:
#        raise ValueError 
    self.welcome( self.y_start, self.y_stop, self.challenge_nbr )
    ## building challenges
    self.challenge_list = [ self.get_challenge( index=i+1 ) for i in range( challenge_nbr ) ]
    self.ascii_fig = ascii_fig
    
    for challenge in self.challenge_list:
      challenge.ask()

    self.evaluate()
    self.score = None
    self.time = None

  def name( self ):
    return "Default Practice"

  def welcome( self, y_start, y_stop, challenge_nbr ):
    print( f"Hi! \nLet's practice {self.name()} {y_start}-{y_stop} with {challenge_nbr} challenges" )

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

  def get_challenge(self, index=None):
    """ generates a question of type x * y """
    return Challenge( "%s x %s = "%(x, y), x*y, index=index, timeout=self.timeout ) 
      

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
      
class PracticeAddition( Practice ):

  def name( self ):
    return "adding"

  def get_challenge(self, index=None ):
    """ generates a question of type x + y """
    x, y = self.get_xy()
    return Challenge( "%s + %s = "%(x, y), x + y, index=index, timeout=self.timeout ) 

class PracticeComplementTo10( Practice ):

  def name( self ):
    return "complementing to 10"

  def get_challenge(self, index=None ):
    """ generates a question of type x + y """
    x, y = self.get_xy()
    return Challenge( f"{x} + ? = 10  ", 10 - x, index=index, timeout=self.timeout ) 


class PracticeSubtraction( Practice ):

  def name( self ):
    return "subtracting"

  def get_challenge(self, index=None ):
    """ generates a question of type x - y """
    x, y = self.get_xy(commutative=False)
    m = min( [ x, y ] )
    M = max( [ x, y ] )
    return Challenge( "%s - %s = "%(M, m), M - m, index=index, timeout=self.timeout ) 

class PracticeMultiplication( Practice ):

  def name( self ):
    return "multiplying"

  def get_challenge(self, index=None ):
    """ generates a question of type x x y """
    x, y = self.get_xy()
    return Challenge( "%s x %s = "%(x, y), x*y, index=index, timeout=self.timeout ) 

class PracticeDivision( Practice ):

  def name( self ):
    return "dividing"

  def get_challenge(self, index=None ):
    """ generates a question of type x / y """
    x, y = self.get_xy()
    m = x * y
    return Challenge( "%s / %s = "%(m, x), y, index=index, timeout=self.timeout ) 

class PracticeDivisionWithRemainder( Practice ):

  def name( self ):
    return "dividing"

  def get_challenge(self, index=None ):
    """ generates a question of type x / y """
    x, y = self.get_xy()
    m = min( [ x, y ] )
    M = max( [ x, y ] )
    d = int( M / m )
    r = M - d * m
    return Challenge( "%s / %s = "%(M, m), ( d, r ), index=index, timeout=self.timeout  ) 

