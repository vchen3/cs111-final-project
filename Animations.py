
from Tkinter import *
      
image2 = 'tea.gif'
class Rhys(Tk):
    def __init__ (self,image):
        Tk.__init__(self,image)
        self.title('Answer!')
        pic = PhotoImage(file=image)
        imageLabel = Label(self, image=pic,borderwidth=0)
        imageLabel.pic = pic
        imageLabel.grid(row=0,column=0)

def runRhys(picture): 
    app = Rhys(picture)
    app.mainloop()

#runRhys(image2)
