from pl_square import PL_Square 

class PL_Board( object ):
	def __init__( self, ifile ):
		self.board = []
		self.tick = 0

		#Populate Board
		for row_txt in open( ifile, 'r' ):
			row = []
			for char in row_txt.rstrip():
				if char == '#':
					row.append( PL_Square( True ) )
				elif char == '_':
					row.append( PL_Square( False ) )
				else:
					raise Exception( "Invalid Char!" )
			self.board.append( row )
		if( len( self.board ) != len( self.board[ 0 ] ) ):
			raise Exception( "Shape Error!" )

		for row in self.board:
			if len( row ) != len( self.board[0] ):
				raise Exception( "Shape Error 2!" )

		#Populate neighbors:
		for row_ct, row in enumerate( self.board ):
			for col_ct, square in enumerate( row ):
				for col_posn in [ -1, 0, 1 ]:
					for row_posn in [ -1, 0, 1 ]:
						if col_posn == 0 and row_posn == 0:
							continue

						n_col = col_ct + col_posn
						n_row = row_ct + row_posn

						if( ( ( n_row >= 0 ) and ( n_col >= 0 ) ) and ( ( n_row < len( self.board ) ) and ( n_col < len( row ) ) ) ):
							square.add_neighbor( self.board[ n_row ][ n_col ] )


	def string_render( self ):
		board_string = ""
		for row in self.board:
			for sq in row:
				char = "# " if sq.is_alive() else "_ "
				board_string += char
			board_string += '\n'
		board_string += ( "Tick: %d\n" % self.tick )
		return board_string

	def updt_tick( self ):
		for row in self.board:
			for sq in row:
				sq.prepare_next_state()

		for row in self.board:
			for sq in row:
				sq.update_state()

		self.tick += 1

def demo( ):
	board = PL_Board( "board.txt" )

	while( True ):
		print board.string_render()
		board.updt_tick()
		raw_input( "..." )
	return

if __name__ == '__main__':
	demo()
