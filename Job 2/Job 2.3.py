#POWER GAME 4
class Board:
    def __init__(self,i,j):
        self.j=j
        self.i=i
        self.table = [["O" for _ in range(i)] for _ in range(j)]
    
    def play(self,column,color):

        column = int(column)
        if type(column) != int:
            print("wrong type value") 

        elif color != "red" and color != "yellow":
            print("wrong color")

        else:
            if color=="red" :
                color="R"
            else: color = "J" 

            for ligne in range(self.i,-1,-1):
                if self.table[ligne-1][column] == "O" :
                    print("cette colonne", column)
                    print(self.table[ligne-1][column])
                    print(color)
                    self.table[ligne-1][column] = color
                    return True


    def print_board(self):
        print("*"*(3*self.i-9) + "GAME POWER 4 ARENA" + "*"*(3*self.i-9))
        for ligne in range(self.i):
            print(self.table[ligne])
        print("*"*5*self.i)


    
New=Board(4,4)
New.print_board()
New.play(1,"red")
New.print_board()
New.play(2,"yellow")
New.print_board()
New.play(1,"red")
New.print_board()
