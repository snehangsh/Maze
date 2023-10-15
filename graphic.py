from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__canvas = Canvas(self.__root, bg="white", width = width, height = height)
        self.__canvas.pack(fill=BOTH, expand = 1)
        self.__running = False
        #We call the protocol method on the root widget so as to connect the close method we created to the "delete window action so that the program stops when we close the graphical window"
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw_line(self, line, fill_color="black"):
         line.draw(self.__canvas, fill_color)

    # This method when called draws all the graphics in the window. Each time this is called the window redraws itself    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()

    #The data member created to track the running state is set to true here and we call redraw() until it is set to true 
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
        print("window closed...")

    #This sets the running state to False
    def close(self):
        self.__running = False

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    

class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def draw(self, canvas, fill_color="black"):
        canvas.create_line(
            self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_color, width=2
        )
        canvas.pack(fill=BOTH, expand = 1)

