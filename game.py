import random
import msvcrt

def get_char():
    """Get a single character from the user."""
    return msvcrt.getch()
    
class game:
    def __init__(self):
        print("enter init")
        self.array=[]
        self.n=5
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append(" ")
            self.array.append(row)
        self.x=0
        self.y=0
        self.array[self.y][self.x]="x"
        self.n_wolves=10
    def display(self):
        for i in range(len(self.array)):
            print(self.array[i])
        return 
    def reset_x(self):
        self.array[self.y][self.x]=" "
    def command_loop(self):
        while True:
            print("Enter a direction: W,A,S,D, or z ")
            # command=input("Enter a direction: W,A,S,D, or stop ").lower()
            command=get_char().lower()
            print(command)
            if command==b'z':
                break
            if command==b'w':
                if self.y==0:
                    print("no more space")
                    continue
                else:
                    self.reset_x()
                    self.y -=1
            elif command==b's':
                if self.y==self.n:
                    print("no more space")
                    continue
                else:
                    self.reset_x()
                    self.y +=1
            elif command==b'a':
                if self.x==0:
                    print("no more space")
                    continue
                else:
                    self.reset_x()
                    self.x -=1
            elif command==b'd':
                if self.x==self.n:
                    print("no more space")
                    continue
                else:
                    self.reset_x()
                    self.x +=1
            else:
                print("invalid command")
                continue 
            if self.array[self.y][self.x]=="W":
                print("A wolf ate you!")
                break
            self.array[self.y][self.x]="X"
            self.display()
        return
        
    def set_wolves(self):
        random.seed(42)
        for i in range(self.n_wolves):
            w_x=random.randint(0,self.n-1)
            w_y=random.randint(0,self.n-1)
            if w_x==self.x and w_y==self.y:
                continue
            self.array[w_y][w_x]="W"
g1=game()
g1.set_wolves()
g1.display()
g1.command_loop()
