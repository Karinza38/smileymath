#!/usr/bin/python3

from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
#from ascii_animals import ASCII_ANIMALS
#from ascii_starwars import ASCII_STARWARS
#from ascii_harry_potter import ASCII_HARRY_POTTER
#from ascii_fig import AsciiFig
from random import randint 
import mymath.challenge

class MyMathTUI:
  
  def __init__( self ):
    param_width = 7 # size of the box containing configuration par maters
    self.challenge_set_list = [
      { 'text' : "Addition",
        'default_range' : [ 0, 10 ],
        'input_box': WTextEntry( param_width, "0-10" ) },  
      { 'text' : "Complement to 10",
        'default_range' : [ 0, 10 ],
        'input_box': "" },  
      { 'text' : "Subtraction", 
        'default_range' : [ 0, 10 ],
        'input_box': WTextEntry( param_width, "0-10" ) }, 
      { 'text' : "Mult. Table [X] x [0-10]",
        'default_range' : [ 2, 9 ],
        'input_box': WTextEntry( param_width, "2-9" ) }, 
      { 'text' : "Mult. [X] x [X]",
        'default_range' : [ 1, 10 ],
        'input_box': WTextEntry( param_width, "1-10" ) }, 
      { 'text' : "Division [X]**2 / [X]", 
        'default_range' : [ 1, 10 ],
        'input_box' : WTextEntry( param_width, "1-10" ) },
      { 'text' : "Euclidean Division [X]**2 / [X]", 
        'default_range' : [ 1, 10 ],
        'input_box' : WTextEntry( param_width, "1-10" ) },
      { 'text' : "Adding Time", 
        'default_range' : None,
        'input_box' : ""},
      { 'text' : "Subtracting Time", 
        'default_range' : None,
        'input_box' : "" },
      
]
#    self.practice_list = ["Addition", "Substraction",  "Multiplications", "Division", "Division with Remainder" ]
    self.theme_list = ["animals", "star wars", "Harry Potter", "none"]
    self.launch()

  def get_challenge_set( self, text:str ):
    """ returns the input configuration associated to txt """
    for p in self.challenge_set_list:
      if p[ 'text' ] == text :
        return p
  

  def get_range( self, challenge_set ):
    """ convert the user input into a range

    The user provides a string of the following format:  
    "3-7" or "7" whihc is outputs into a range [3, 7] or [3, 3]). 
    In case of error, default_range is returned
    """
    user_input = challenge_set[ 'input_box' ].get()
    try: 
      if '-' in user_input: # expecting "3-7"
        user_input = user_input.split('-')
        if len( user_input ) != 2:
          int_range = challenge_set[ 'default_range' ]
        else:
          user_input = [ int(i) for i in user_input ] 
          int_range =  [ min( user_input) , max( user_input ) ]
      else:  # expecting "7"
        int_range = [ int( user_input ), int( user_input ) ]
    except:
      int_range = challenge_set[ 'default_range' ]
    ## forbidden values making the test too easy!!
    if challenge_set[ 'text' ] in [ "Multiplications", "Division [X]**2 / [X]",\
                               "Euclidean Division [X]**2 / [X]" ] and\
      int_range in [ [ 0, 0 ], [ 1, 1 ], [ 0, 1 ], [ 10, 10 ] ]:
      int_range = challenge_set[ 'default_range' ]

    if challenge_set[ 'text' ] in [ "Addition", "Subtraction" ] and\
       int_range [ 1 ] - int_range[ 0 ] < 5:
          int_range = [ int_range[ 0 ], int_range[ 0 ] + 5 ]
    return int_range

  def check_int_input(self, user_input:str, default_int:int ):
    """ checks the user_input is an int and return it
    
    In case of error default_int is returned
    """
    try:
      int_output = int( user_input )
    except:
      int_output = default_int
    return int_output 

#  def get_ascii_fig( self, input_theme_index ):
#    return self.theme_list[ input_theme_index ]
#
#    theme = self.theme_list[ input_theme_index ]
#    if theme == "animals":
#      db = ASCII_ANIMALS
#    elif theme == "star wars":
#      db = ASCII_STARWARS
#    elif theme == "Harry Potter":
#      db = ASCII_HARRY_POTTER
#    elif theme == "none" :
#      db = None
#    if db == None:
#      return None
#    else: 
#      return AsciiFig( db=db ) 

  def launch( self): 
    """ launch the interface """
    with Context():
    
      Screen.attr_color(C_WHITE, C_BLACK)
      Screen.cls()
      Screen.attr_reset()
      tui_width = 50
      d = Dialog(5, 5, tui_width, 16)
    
      line = 1
      d.add( 1, line, "Welcome to MyMath!" )
      line += 2
      d.add( 1, line, WFrame( tui_width - 2, len( self.challenge_set_list ) + 3, "Please select Today's practice" ) )
      line += 2
    
      input_challenge_set = WRadioButton( [ p[ 'text' ] for p in self.challenge_set_list ] )
      d.add( 2, line, input_challenge_set)

      ## adding all input_box
      for p in [ p[ 'input_box' ] for p in self.challenge_set_list ]:  
        d.add( 40, line, p )
        line += 1
      line += 2

      d.add( 1, line, WFrame( tui_width - 2, 8, "Advanced Parameters") ) 
      line += 2
    
      input_theme = WListBox(15, 4, self.theme_list )
      d.add( 2, line, "Awards Theme:")
      line += 1
      d.add( 2, line, input_theme )
    
      input_challenge_nbr = WTextEntry(4, "20")
      line -= 1
      d.add( 20, line, "Number of Challenges:") 
      d.add( 42, line, input_challenge_nbr )

      input_timeout = WTextEntry(4, "10")
      line += 1
      d.add( 20, line, "Timeout (s):") 
      d.add( 42, line, input_timeout )
    
      line += 6
      b = WButton(8, "OK")
      d.add(10, line, b)
      b.finish_dialog = ACTION_OK
      b = WButton(8, "Cancel")
      d.add(30, line, b)
      b.finish_dialog = ACTION_CANCEL
    
      res = d.loop()
    
    if res == ACTION_OK:
      training = self.challenge_set_list[ input_challenge_set.get() ]
      challenge_nbr =  self.check_int_input( input_challenge_nbr.get(), 20 )
#      ascii_fig = self.get_ascii_fig( input_theme.get() )
      ascii_fig = self.theme_list[ input_theme.get() ]
      if training[ 'text' ] in [ "Adding Time", "Subtracting Time" ]: 
        user_range = None
      else:
        user_range = self.get_range( training )
      timeout = self.check_int_input( input_timeout.get(), None )

      args = { 'y' : user_range, 'x' : [ 0, 10 ], \
               'challenge_nbr' : challenge_nbr, 'ascii_fig' : ascii_fig, \
               'timeout' : timeout }
      if training[ 'text' ] == "Addition" :
        args[ 'x' ] = user_range
        mymath.challenge.AdditionSet( **args )
      elif training[ 'text' ] == "Complement to 10" :
        del args[ 'x' ]
        del args[ 'y' ]
        mymath.challenge.ComplementTo10Set( **args )
      elif training[ 'text' ] == "Subtraction" :
        args[ 'x' ] = user_range
        mymath.challenge.SubtractionSet( **args )
      elif training[ 'text' ] == "Mult. Table [X] x [0-10]" :
        mymath.challenge.MultiplicationSet( **args )
      elif training[ 'text' ] == "Mult. [X] x [X]" :
        args[ 'x' ] = user_range
        mymath.challenge.MultiplicationSet( **args )
      elif training[ 'text' ] == "Division [X]**2 / [X]" :
        args[ 'x' ] = user_range
        mymath.challenge.DivisionSet( **args )
      elif training[ 'text' ] == "Euclidean Division [X]**2 / [X]" :
        args[ 'x' ] = user_range
        args[ 'y' ] = [ user_range[ 0 ]**2, user_range[ 1 ]**2 ]   
        mymath.challenge.DivisionWithRemainderSet( **args )
      elif training[ 'text' ] == "Adding Time":
        del args[ 'x' ]
        del args[ 'y' ]
        mymath.challenge.HourMinuteAdditionSet( **args )
      elif training[ 'text' ] == "Subtracting Time": 
        del args[ 'x' ]
        del args[ 'y' ]
        mymath.challenge.HourMinuteSubstractionSet( **args )

if __name__ == '__main__' :
  MyMathTUI()

