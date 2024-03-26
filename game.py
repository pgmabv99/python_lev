import random
# import msvcrt
from getch import getch
import time

def get_char():
    """Get a single character from the user."""
    return getch()

class game:
    def __init__(self):
        print("enter init")
        self.array=[]
        self.n=4

        self.n_wolves=5

        self.i_game=0
        self.max_game=5
        self.begin_x=1
        self.begin_y=1
        self.end_x=self.n-1
        self.end_y=self.n-1
        self.x=self.begin_x
        self.y=self.begin_y
        self.n_iter=0
        random.seed(42)
        self.steps={  
        
        "d":[1,0],
        "a":[-1,0], 
        "s":[0,1],
      
        
        "w":[0,-1],
        
        }
        
        



    def display(self,tail=True):
        print("=============")
        for y_i in range(self.n):
            for x_i in range(self.n):
                if [x_i,y_i] in self.wolves:
                    label="*"
                elif [x_i,y_i]==[self.x,self.y]:
                    label="x"
                elif [x_i,y_i]==[self.end_x,self.end_y]:
                    label="E"
                # elif  not tail and [x_i,y_i] in self.points_covered:
                #     label="o"
                # elif tail and [x_i,y_i]==self.points_covered[-1]:
                #     label="o"
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

            # print("dx",dx)
            # print("dy",dy)

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
                print("You have moved on!")
                if self.i_game==self.max_game:
                    print("You won!")
                    break
                time.sleep(2)
                self.new_game()
            else:
                # regular step
                self.display()
        return

    def set_wolves(self, wall=False):
        self.wolves=[]

        if wall:
            # build a wall!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            for i in range(self.n):
                w_x=i
                w_y=self.n-2
                self.wolves.append([w_y,w_x])
        else:
            # random 
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
        self.n_iter +=1
        if self.n_iter%100000==0:
            print(self.n_iter)

        nsec=0.01
        # self.f1.write(str(self.points_covered))
        self.points_covered.append([x,y])
        # self.display()
        # time.sleep(nsec)

        # if x==self.begin_x-1 and y==self.begin_y and len(self.points_covered)==3:
        #     print("first level branch")
        #     time.sleep(3)
        for command in self.steps:
            found=False
            dx=self.steps[command][0]
            dy=self.steps[command][1]
            if [x+dx,y+dy]==[self.end_x,self.end_y] : 
                print("points",self.points_covered)
                self.display()
                time.sleep(2)
                found=True
                break
            elif (x+dx not in range(0,self.n)) or (y+dy not in range(0,self.n)):
                continue
            elif [x+dx,y+dy] in self.wolves:
                continue
            if [x+dx,y+dy]  in self.points_covered:
                continue
            found=self.path_found(x+dx,y+dy)
            if found:
                break
        self.points_covered.pop()
        # self.display()
        # time.sleep(nsec)
        return found 
    
    def new_game(self):
        self.n +=1
        self.n_wolves +=8
        self.x=self.begin_x
        self.y=self.begin_y
        self.end_x=self.n-1
        self.end_y=self.n-1
        self.i_game +=1
        self.set_wolves()
        self.display()
  


g1=game()
g1.set_wolves()
g1.display()
g1.command_loop()
