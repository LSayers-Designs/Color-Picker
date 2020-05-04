"""Ex on pg 287-288"""

from breezypythongui import EasyFrame
import tkinter.colorchooser

class colorPicker(EasyFrame):
	"""Displays the results of the color choice"""
	def __init__(self):
		"""sets up the window and widgets"""
		EasyFrame.__init__(self, title = "Color Chooser Demo", background = "lightgray",width = 450, height = 170 )
		
		#Labels and output fields
		self.addLabel(text = 'R', row = 0, column = 0, sticky = "NSEW", background = "red", foreground = "white", font="bold")
		self.addLabel(text = 'G', row = 1, column = 0, sticky = "NSEW", background = "green", foreground = "white", font="bold")
		self.addLabel(text = 'B', row = 2, column = 0, sticky = "NSEW", background = "blue", foreground = "white", font="bold")
		self.addLabel(text = "Hex Color", row = 3, column = 0 , sticky = "NSEW", background = "yellow", foreground = "black", font="bold")

		self.r = self.addIntegerField(value = 0, row = 0, column = 1)
		self.g = self.addIntegerField(value = 0, row = 1, column = 1)
		self.b = self.addIntegerField(value = 0, row = 2, column = 1)
		self.hex = self.addTextField(text = "#000000", row = 3, column = 1, width = 10)

		#Canvas with an initial black background
		self.canvas = self.addCanvas(row = 0, column = 3, rowspan = 4, width = 5, background = "#000000")

		#Command button
		self.addButton(text = "Choose color", row = 4, column = 0, columnspan =3, command = self.chooseColor)

	#Event handling method
	def chooseColor(self):
		"""pops up a color chooser and outputs the results."""
		colorTuple = tkinter.colorchooser.askcolor()
		if not colorTuple[0]: return
		((r, g, b), hexString) = colorTuple
		self.r.setNumber(int(r))
		self.g.setNumber(int(g))
		self.b.setNumber(int(b))
		self.hex.setText(hexString)
		self.canvas["background"] = hexString

#Definition of main funcion
def main ():
	colorPicker().mainloop()
#Global call to main()
main()