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
        self.n=10
        self.x=1
        self.y=1
        self.n_wolves=50
        random.seed(42)
        self.steps={
        "a":[-1,0],
        "d":[1,0], 
        "w":[0,-1],
        "s":[0,1]
        }
        self.end_x=8
        self.end_y=8
        



    def display(self):
        for y_i in range(self.n):
            for x_i in range(self.n):
                if [x_i,y_i] in self.wolves:
                    label="*"
                elif [x_i,y_i]==[self.x,self.y]:
                    label="x"
                elif [x_i,y_i]==[self.end_x,self.end_y]:
                    label="E"
                elif [x_i,y_i] in self.points_covered:
                    label="o"
                else:
                    label=" "
                print(label,end=" ")
            print(" ")





    def command_loop(self):
        while True:
            print("Enter a direction: W,A,S,D, z or r ")

            command=get_char().lower()
            print("you entered",command)
            if command=='z':
                break
            elif command=='r':
                self.set_wolves()
                self.display()
                continue
            if command  not in self.steps:
                print("invalid command")
                continue
            dx=self.steps[command][0]
            dy=self.steps[command][1]

            print("dx",dx)
            print("dy",dy)

            # check the step
            if (self.x+dx not in range(0,self.n)) or (self.y+dy not in range(0,self.n)):
                print("no more space",self.x+dx,self.y+dy)
                continue
            # make the step
            self.x +=dx
            self.y +=dy

                
            if [self.x,self.y] in self.wolves:
                print("A wolf ate you!")
                self.display()
                break
            elif [self.x,self.y]==[self.end_x,self.end_y]:
                print("You Won!")
                self.display()
                break
            self.display()
        return

    def set_wolves(self):
        self.wolves=[]
        for i in range(self.n_wolves):
            w_x=random.randint(0,self.n-1)
            w_y=random.randint(0,self.n-1)
            if [w_x,w_y] in [[self.x,self.y],[self.end_x,self.end_y]]:
                continue

            self.wolves.append([w_y,w_x])
        self.points_covered=[[self.x,self.y]]
        if not self.path_found(self.x,self.y):
            print("Bad wolves")
        else:
            print("Good wolves")
        # print("WOLVES",len(self.wolves),self.wolves)
        print("----------------------")

    def path_found(self,x,y):
        self.points_covered.append([x,y])
        for command in self.steps:
            dx=self.steps[command][0]
            dy=self.steps[command][1]
            if [x+dx,y+dy]==[self.end_x,self.end_y] : 
                print("points",self.points_covered)
                self.display()
                self.points_covered.pop()
                return True
            elif (x+dx not in range(0,self.n)) or (y+dy not in range(0,self.n)):
                continue
            elif [x+dx,y+dy] in self.wolves:
                continue
            if [x+dx,y+dy]  in self.points_covered:
                continue
            found=self.path_found(x+dx,y+dy)
            if found:
                self.points_covered.pop()
                return True
        self.points_covered.pop()
        return False 

  


g1=game()
g1.set_wolves()
g1.display()
g1.command_loop()
