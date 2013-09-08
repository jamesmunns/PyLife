class PL_Square(object):
	"""Game of Life Square"""
	def __init__(self):
		super(PL_Square, self).__init__()
		self.alive_current = False
		self.alive_next    = False
		self.neighbors = []

	def is_alive( self ):
		return self.alive_current

	def live_neighbor_ct( self ):
		#Count the number of neighbors

		#Error checking
		if( len( self.neighbors ) == 0 ):
			raise Exception( "Neighbors not populated!" )

		#Count the live neighbors
		ct = 0
		for n in self.neighbors:
			if( n.is_alive() ):
				ct += 1

		return ct

	def prepare_next_state( self ):
		"""
		Rules:
			<2 Neighbors: Die
			2,3 Neighbors: Stay Alive 
			>3 Neighbors: Die
			Dead+3 Neighbors: live
		"""
		live_ct = self.live_neighbor_ct()
		if self.is_alive():
			if live_ct < 2:
				self.alive_next = False
			elif live_ct in [ 2, 3 ]:
				self.alive_next = True
			elif live_ct > 3:
				self.alive_next = False
			else:
				raise Exception( "CRITICAL ERROR" )
		else:
			if live_ct == 3:
				self.alive_next = True
			else
				self.alive_next = False
		return

	def update_state( self ):
		self.alive_current = self.alive_next
		self.alive_next = None

	def add_neighbor( self, neighbor ):
		if len( self.neighbors < 8 ):
			self.neighbors.append( neighbor )
		else:
			raise Exception( "Too Many Neighbors" )
