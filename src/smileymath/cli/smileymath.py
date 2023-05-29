#!/usr/bin/python3

import argparse
import smileymath.gui
import smileymath.challenge


def gui():
  smileymath.gui.SmileyMathTUI()
    

def ce1( ):
  challenge_nbr = 20
  args = { 'y' : [ 0, 20], 'x' : [ 0, 20 ], 'challenge_nbr' : challenge_nbr, \
         'ascii_fig' : "animals", 'timeout' : 7 }
  smileymath.challenge.AdditionSet( **args )
  smileymath.challenge.ComplementTo10Set(  **args )
  smileymath.challenge.SubtractionSet( **args )

  args = { 'y' : [ 0, 3 ], 'x' : [ 0, 10 ], 'challenge_nbr' : challenge_nbr, \
         'ascii_fig' : "star wars", 'timeout' : 5 }
  smileymath.challenge.MultiplicationSet( **args )

def cm1( ):
  challenge_nbr = 20
  args = { 'y' : [ 2, 9], 'x' : [ 2, 9 ], 'challenge_nbr' : challenge_nbr, \
           'ascii_fig' : "animals", 'timeout' : 5 }
  smileymath.challenge.MultiplicationSet( **args )

  args = { 'y' : [ 1, 10], 'x' : [ 1, 10 ], 'challenge_nbr' : challenge_nbr, \
           'ascii_fig' : "star wars", 'timeout' : 8 }
  smileymath.challenge.DivisionSet( **args )

  args = { 'y' : [ 1, 100], 'x' : [ 1, 10 ], 'challenge_nbr' : challenge_nbr, \
           'ascii_fig' : "animals", 'timeout' : 8 }
  smileymath.challenge.DivisionWithRemainderSet( **args )

  args = { 'challenge_nbr' : 10, 'ascii_fig' : "Harry Potter", 'timeout' : 60 }
  smileymath.challenge.HourMinuteAdditionSet( **args )
  smileymath.challenge.HourMinuteSubstractionSet( **args )

def cli( ):
  """ CLI for myMath """
  description = "myMath"  
  parser = argparse.ArgumentParser( description=description )
  parser.add_argument( '-ce1', '--ce1', default=False,  \
  action='store_const', const=True, \
  help="Tests for CE1" )
  parser.add_argument( '-cm1', '--cm1', default=False,  \
  action='store_const', const=True, \
  help="Tests for CM1" )
  args = parser.parse_args()

  if args.ce1 is True:
    ce1()
  elif args.cm1 is True:
    cm1()
  else:  
    gui()    


if __name__ == "__main__":
  cli()  


