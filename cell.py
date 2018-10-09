class Cell:
  def __init__(self,x,y,piece):
    self.piece = piece
    self.y = y
    self.x = x
  def add_piece(self,piece):
    self.piece = Piece(piece)
  def remove_piece(self):
    self.piece = Piece()  
    
