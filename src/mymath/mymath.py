#!/usr//bin/python3

from picotui.context import Context
from picotui.screen import Screen
from picotui.widgets import *
from picotui.defs import *
from ascii_animals import ASCII_ANIMALS
from ascii_starwars import ASCII_STARWARS
from ascii_harry_potter import ASCII_HARRY_POTTER
from ascii_fig import AsciiFig
#import practice
from practice import PracticeAddition, PracticeSubtraction, PracticeMultiplication, PracticeDivision, PracticeDivisionWithRemainder, PracticeComplementTo10 
from random import randint 

class MyMathTUI:
  
  def __init__( self ):
    param_width = 7 # size of the box containing configuration par maters
    self.practice_list = [
      { 'text' : "Addition",
        'default_range' : [ 0, 10 ],
        'input_box': WTextEntry( param_width, "0-10" ) },  
      { 'text' : "Complement to 10",
        'default_range' : [ 0, 10 ],
        'input_box': WTextEntry( param_width, "0-10" ) },  
      { 'text' : "Subtraction", 
        'default_range' : [ 0, 10 ],
        'input_box': WTextEntry( param_width, "0-10" ) }, 
      { 'text' : "Mult. Table [X] x [0-10]",
        'default_range' : [ 2, 9 ],
        'input_box': WTextEntry( param_width, "2-9" ) }, 
      { 'text' : "Mult. [X] x [X]",
        'default_range' : [ 1, 10 ],
        'input_box': WTextEntry( param_width, "1-10" ) }, 
      { 'text' : "Division", 
        'default_range' : [ 1, 10 ],
        'input_box' : WTextEntry( param_width, "1-10" ) },
      { 'text' : "Division With Remainder", 
        'default_range' : [ 1, 10 ],
        'input_box' : WTextEntry( param_width, "1-10" ) },
]
#    self.practice_list = ["Addition", "Substraction",  "Multiplications", "Division", "Division with Remainder" ]
    self.theme_list = ["animals", "star wars", "Harry Potter", "none"]
    self.launch()

  def get_practice( self, text:str ):
    """ returns the input configuration associated to txt """
    for p in self.practice_list:
      if p[ 'text' ] == text :
        return p
  

  def get_range( self, practice ):
    """ convert the user input into a range

    The user provides a string of the following format:  
    "3-7" or "7" whihc is outputs into a range [3, 7] or [3, 3]). 
    In case of error, default_range is returned
    """
    user_input = practice[ 'input_box' ].get()
    try: 
      if '-' in user_input: # expecting "3-7"
        user_input = user_input.split('-')
        if len( user_input ) != 2:
          int_range = practice[ 'default_range' ]
        else:
          user_input = [ int(i) for i in user_input ] 
          int_range =  [ min( user_input) , max( user_input ) ]
      else:  # expecting "7"
        int_range = [ int( user_input ), int( user_input ) ]
    except:
      int_range = practice[ 'default_range' ]
    ## forbidden values making the test too easy!!
    if practice[ 'text' ] in [ "Multiplications", "Division",\
                               "Division With Remainder" ] and\
      int_range in [ [ 0, 0 ], [ 1, 1 ], [ 0, 1 ], [ 10, 10 ] ]:
      int_range = practice[ 'default_range' ]

    if practice[ 'text' ] in [ "Addition", "Subtraction" ] and\
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

  def get_ascii_fig( self, input_theme_index ):
    theme = self.theme_list[ input_theme_index ]
    if theme == "animals":
      db = ASCII_ANIMALS
    elif theme == "star wars":
      db = ASCII_STARWARS
    elif theme == "Harry Potter":
      db = ASCII_HARRY_POTTER
    elif theme == "none" :
      db = None
    if db == None:
      return None
    else: 
      return AsciiFig( db=db ) 

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
      d.add( 1, line, WFrame( tui_width - 2, len( self.practice_list ) + 3, "Please select Today's practice" ) )
      line += 2
    
      input_practice = WRadioButton( [ p[ 'text' ] for p in self.practice_list ] )
      d.add( 2, line, input_practice)

      ## adding all input_box
      for p in [ p[ 'input_box' ] for p in self.practice_list ]:  
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
      training = self.practice_list[ input_practice.get() ]
      challenge_nbr =  self.check_int_input( input_challenge_nbr.get(), 20 )
      ascii_fig = self.get_ascii_fig( input_theme.get() )
      user_range = self.get_range( training )
      timeout = self.check_int_input( input_timeout.get(), None )

      args = { 'y_range' : user_range, 'x_range' : [ 0, 10 ], \
               'challenge_nbr' : challenge_nbr, 'ascii_fig' : ascii_fig, \
               'timeout' : timeout }
      if training[ 'text' ] == "Addition" :
        args[ 'x_range' ] = user_range
        PracticeAddition( **args )
      elif training[ 'text' ] == "Complement to 10" :
        PracticeComplementTo10( **args )
      elif training[ 'text' ] == "Subtraction" :
        args[ 'x_range' ] = user_range
        PracticeSubtraction( **args )
      elif training[ 'text' ] == "Mult. Table [X] x [0-10]" :
        PracticeMultiplication( **args )
      elif training[ 'text' ] == "Mult. [X] x [X]" :
        args[ 'x_range' ] = user_range
        PracticeMultiplication( **args )
      elif training[ 'text' ] == "Division" :
        PracticeDivision( **args )
      elif training[ 'text' ] == "Division With Remainder" :
        PracticeDivisionWithRemainder( **args )

if __name__ == '__main__' :
  MyMathTUI()

