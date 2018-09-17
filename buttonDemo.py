from breezypythongui import (EasyFrame)

class ButtonDemo(EasyFrame):

	def __init__(self):
		"""sets up the window, label, and buttons"""
		EasyFrame.__init__(self)

		picture = input("pick a picture: ")
		caption = input("what do you want it to say: ")

		# A single label in the first row.
		self.label = self.addLabel(text = "Hello world", row = 0, column = 0, columnspan = 2, sticky = "NSEW")

		#two command buttons i nthe second row, with event
		# handler methods supplied.
		self.clearBtn = self.addButton(text = "Clear", row = 1, column = 0, command = self.clear)
		self.restoreBtn = self.addButton(text = "Restore", row = 1, column = 1, state = "disabled", command = self.restore)

		#methods to handle user events
	def clear(self):
			"""resets the label to the empty string and updates the button states."""
			self.label["text"] = ""
			self.clearBtn["state"] = "disabled"
			self.restoreBtn["state"] = "normal"

	def restore(self):
		"""resets the label "Hello world!" and updates the button states."""
		self.label["text"] = "Hello World!"
		self.clearBtn["state"] = "normal"
		self.restoreBtn["state"] = "disabled"
		imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = "NSEW")
		self.image = PhotoImage(file = picture)
		imageLabel["image"] = self.image

def main():
	ButtonDemo().mainloop()

main()






			