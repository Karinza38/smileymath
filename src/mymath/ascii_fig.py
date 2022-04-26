import matplotlib.pyplot as plt
from random import randint
from ascii_animals import ASCII_ANIMALS

class AsciiFig:

  def __init__(self, db=ASCII_ANIMALS, max_width=None, max_height=None):
    self.db = db
    self.max_width = max_width
    self.max_height = max_height
    self.score_list = [ 100, 99, 97, 94, 90, 85, 80, 70 ]
    self.meta_list = self.get_meta_list()

  def get_meta_list( self ):
    """builds metadata associated to each figure. This includes the size as well as a score. 
       The score value is used to select the larger pictures according to a given score.  """
    meta_list = [] 
    for fig in self.db:
      index = self.db.index( fig ) 
      fig = fig.splitlines()
      width = max( [ len(line) for line in fig ] )
      height = len( fig )
      if self.max_width != None:
        if width > self.max_width: 
          continue
      if self.max_height!= None:
        if height > self.max_height:
          continue
      meta_list.append({ 'db_index': index, 'size' : width * height } )
    size_list = [ meta[ 'size' ] for meta in meta_list ]
    size_list.sort()
    ## assign score according to the figure size
    q5 = int( 5 * len(size_list) / 100 )
    for meta in meta_list:
      for q5_counter in range( len( self.score_list ) ):
        if meta[ 'size' ] > size_list[ - (q5_counter + 1 ) * q5 ]:
          meta[ 'score' ]  = self.score_list[ q5_counter ]
          break
      try:
        a = meta[ 'score' ]
      except KeyError:
        meta[ 'score' ] = self.score_list[ -1 ] 
    return meta_list

  def plot_size( self ):
   size_list = [ meta[ 'size' ] for meta in self.meta_list ]
   plt.hist( size_list, bins=25, density=False, alpha=0.6, color='b')
   plt.show()


  def pick_fig( self, score):
    """ select randomly a figure that corresponds to the score. Score is between 0 and 100. 
        When score is set to None a random picture is selected.
    """
    if score == None:
      fig_list = self.db
    else:
      ## define the corresponding fig_score 
      for fig_score in self.score_list:
        if fig_score <= score:
          break
      fig_list = []
      for meta in self.meta_list:
        if meta[ 'score' ] == fig_score:
          fig_list.append( self.db[ meta[ 'db_index' ] ] )  
    try:
      fig = fig_list[ randint(0, len(fig_list) ) ]
    except:
      fig = ''
    return fig

if __name__ == "__main__":
    db = AsciiFig()
    for i in range(20):
      score = 100 - i
      print( db.pick_fig( score ) )

