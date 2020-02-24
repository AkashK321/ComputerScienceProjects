from tkinter import *
from PIL import Image, ImageTk
from random import *

class myApplication(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_textBoxes()
        self.create_buttons()
        self.canvas = Canvas(window, width=500, height=500)
        self.canvas.pack()
        # self.tk.Canvas()
        # self.create_buttons.next_logo.pack_forget()
        self.i = 0
        self.imgArray = ["nike", "adidas", "louis vuitton", "gucci", "under armour", "microsoft", "apple"]
        self.imgDirectory = ""
        shuffle(self.imgArray)
        
        
    def create_buttons(self):
        
        self.start = Button(self)
        self.start["text"] = "Start"
        self.start["command"] = self.displayNextImage
        self.start.pack(side="top")
        
        self.retrieve_input = Button(self)
        self.retrieve_input["text"] = "Submit answer"
        self.retrieve_input["command"] = self.retrieveInput
        self.retrieve_input.pack(side="bottom")
        
        self.next_logo = Button(self)
        self.next_logo["text"] = "Next"
        self.next_logo["fg"] = "green"
        self.next_logo["command"] = self.displayNextImage
        self.next_logo.pack()
        
        self.quit = Button(self, text="QUIT", fg="red", command=window.destroy)
        
        self.quit.pack(side="bottom")
    
    def create_textBoxes(self):
        self.response_box = Text(self)
        self.response_box["relief"] = RIDGE
        self.response_box["height"] = 5
        self.response_box["width"] = 60
        self.response_box["borderwidth"] = 3
        self.response_box.pack(side="bottom")
        
    def displayNextImage(self):
        # self.imgArray = ["adidas", "nike"]
        # shuffle(self.imgArray)
        
        if self.i == 0:
            self.start.pack_forget()
            
        print(self.i)
        
        if self.i >= (len(self.imgArray)):
            print("All logos have been identified")
            self.imgDirectory = "/Users/akkuma22/PythonProjects/gameOver.png"
            self.displayImage(self.imgDirectory)
        else:
            self.imgDirectory = "/Users/akkuma22/PythonProjects/" + self.imgArray[self.i] + ".jpg"
            self.displayImage(self.imgDirectory)
        
        # print("image")
        
    def displayImage(self, imgDirectory):
        self.img = Image.open(imgDirectory)
        self.img = self.img.resize((350,350), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.img)
        self.canvas.create_image(85, 150, anchor=NW, image=self.img)
        
    def retrieveInput(self):
        self.inputValue = self.response_box.get("1.0", "end-1c")
        # print(self.inputValue)
        self.checkAnswer(self.inputValue)
    
    def checkAnswer(self, inputValue):
        if inputValue.lower() == self.imgArray[self.i]:
            print("Correct")
            self.imgDirectory = "/Users/akkuma22/PythonProjects/correct.jpg"
            self.img = Image.open(self.imgDirectory)
            self.img = self.img.resize((350,350), Image.ANTIALIAS)
            self.img = ImageTk.PhotoImage(self.img)
            self.canvas.create_image(85, 150, anchor=NW, image=self.img)
            self.i += 1
            # self.create_buttons.next_logo.pack()
            
        
        
        # print(self.i)
        
        
        
window = Tk()

window.geometry("1000x1000")
app = myApplication(master=window)
app.master.title("Application")

app.mainloop()