class Board:
	def __init__(self):
		self.sud = [[0,2,7,0,3,0,4,6,0],
					[0,0,8,0,0,4,0,0,0],
					[6,9,0,0,2,0,5,0,0],
					[0,0,0,0,0,0,9,5,0],
					[0,5,0,7,0,1,0,2,0],
					[0,1,9,0,0,0,0,0,0],
					[0,0,6,0,1,0,0,9,5],
					[0,0,0,9,0,0,1,0,0],
					[0,7,1,0,6,0,3,4,0]]
		self.prev_sud = []
		self.completed = False
		self.rows = []
		self.colums = []
		self.boxes = []
		self.cells = {}

	def initialise(self):
		'''
		for i in range(1,10):
			row = []
			raw_row = raw_input("Enter the numbers for row " + str(i) + " without spaces")
			for j in raw_row:
				row.append(int(j))
			self.sud.append(row)
		'''
		self.rows = []
		self.columns = []
		self.boxes = []

		self.ini = []
		for j in range(9):
			self.rows.append([1,2,3,4,5,6,7,8,9])
			self.columns.append([1,2,3,4,5,6,7,8,9])
			self.boxes.append([1,2,3,4,5,6,7,8,9])

	def calculate(self):
		self.prev_sud = []
		for i in self.sud:
			self.prev_sud.append(i[:])

		self.removeVals()
		self.enumerateCells()
		self.placeVals()

		if self.prev_sud==self.sud:
			print "No move applicable"
			self.completed = True


		'''
		print "Numbers allowed in rows:"
		for i in range(9):
			print self.rows[i]
		print "Numbers allowed in columns:"
		for j in range(9):
			print self.columns[j]
		print "Numbers allowed in boxes:"
		for k in range(9):
			print self.boxes[k]
		'''

	def showBoard(self):
		print "Sudoku:"
		for row in range(9):
			st = ""
			for num in range(9):
				st+=str(self.sud[row][num]) + " "
				if((num+1)%3==0 and num!=8):
					st+="| "
			print st
			if((row+1)%3==0 and row!=8):
				print "- - - + - - - + - - -"

	def enumerateCells(self):
		for y in range(9):
			for x in range(9):
				if self.sud[y][x]==0:
					self.looking_for = self.boxes[self.getBoxIndex((y,x))]
					for i in self.looking_for:
						if i in self.columns[x] and i in self.rows[y]:
							if self.cells.has_key((x,y)) and i not in self.cells[(x,y)]:
								self.cells[(x,y)].append(i)
							else:
								self.cells[(x,y)] = [i]
		print self.cells

	def placeVals(self):
		self.completed = True
		for y_coord,y in enumerate(self.sud):
			for x_coord,x in enumerate(y):
				if x==0:
					self.completed = False
					if self.cells.has_key((x_coord,y_coord)):
						if len(self.cells[(x_coord,y_coord)])>1:
							for i in self.cells[(x_coord,y_coord)]:
								enter = True
								for j in range(9):
									if self.cells.has_key((j,y_coord)):
										if i in self.cells[(j,y_coord)] and j!=x_coord:
											enter = False
									if self.cells.has_key((x_coord,j)):
										if i in self.cells[(x_coord,j)] and j!=y_coord:
											enter = False
									orig = ((x_coord/3)*3,(y_coord/3)*3)
									for e in range(3):
										for f in range(3):
											if not (orig[0]+f,orig[1]+e)==(x_coord,y_coord):
												if self.cells.has_key((orig[0]+f,orig[1]+e)):
													if i in self.cells[(orig[0]+f,orig[1]+e)] and j!=y_coord:
														enter = False

								if enter:
									self.sud[y_coord][x_coord] = int(i)
									print "{} at {}".format(int(i),(x_coord,y_coord))
									self.cells.pop((x_coord,y_coord))

						elif len(self.cells[(x_coord,y_coord)])==1:
							self.sud[y_coord][x_coord] = int(self.cells[(x_coord,y_coord)][0])
							print "{} at {}".format(self.cells[(x_coord,y_coord)][0],(y_coord,x_coord))
							self.cells.pop((x_coord,y_coord))


	def removeVals(self):
		for y in range(9):
			for x in range(9):
				val = self.sud[y][x]
				boxInd = self.getBoxIndex((y,x))
				if val in self.rows[y]:
					self.rows[y].remove(val)
				if val in self.columns[x]:
					self.columns[x].remove(val)
				if val in self.boxes[boxInd]:
					self.boxes[boxInd].remove(val)

	def getBoxIndex(self, coords):
		x = coords[1]
		y = coords[0]

		if x<3:
			if y<3:
				return 0
			elif y<6 and y>2:
				return 3
			elif y>5:
				return 6
		elif x<6 and x>2:
			if y<3:
				return 1
			elif y<6 and y>2:
				return 4
			elif y>5:
				return 7
		elif x>5:
			if y<3:
				return 2
			elif y<6 and y>2:
				return 5
			elif y>5:
				return 8


def main():
	b = Board()
	b.initialise()

	while(not b.completed):
		b.showBoard()
		b.calculate()
		b.showBoard()

if __name__ == "__main__":
	main()