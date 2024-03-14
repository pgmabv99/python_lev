import random
# import msvcrt
from getch import getch

def get_char():
    """Get a single character from the user."""
    return getch()

class game:
    def __init__(self):
        print("enter init")
        self.array=[]
        self.n=5
        self.x=0
        self.y=0
        self.n_wolves=10



    def display(self):
        for y_i in range(self.n):
            for x_i in range(self.n):
                if [x_i,y_i] in self.wolves:
                    label="W"
                elif [x_i,y_i]==[self.x,self.y]:
                    label="x"
                else:
                    label=" "
                print(label,end=" ")
            print(" ")





    def command_loop(self):
        while True:
            print("Enter a direction: W,A,S,D, or z ")

            command=get_char().lower()
            print("you entered",command)
            if command=='z':
                break
            dx=0
            dy=0
            if command=='w':
                if self.y==0:
                    print("no more space")
                    continue
                else:
                    self.y -=1
            elif command=='s':
                if self.y==self.n-1:
                    print("no more space")
                    continue
                else:
                    self.y +=1
            elif command=='a':
                if self.x==0:
                    print("no more space")
                    continue
                else:
                    self.x -=1
            elif command=='d':
                if self.x==self.n-1:
                    print("no more space")
                    continue
                else:
                    self.x +=1
            else:
                print("invalid command")
                continue
            if [self.x,self.y] in self.wolves:
                print("A wolf ate you!")
                break
            self.display()
        return

    def set_wolves(self):
        random.seed(42)
        self.wolves=[]
        for i in range(self.n_wolves):
            w_x=random.randint(0,self.n-1)
            w_y=random.randint(0,self.n-1)
            if w_x==self.x and w_y==self.y:
                continue
            self.wolves.append([w_y,w_x])
        print(self.wolves)

g1=game()
g1.set_wolves()
g1.display()
g1.command_loop()
