#tic-tac-toe using OOP in python
#first define a class that contains different methods that are needed to perform some tasks
from tkinter import *
class tic_tac_toe:
    #consrtuctor to create the board and initialize the player
    def __init__(self):
        self.board=[[0 for i in range(3)] for i in range(3)]
        self.player=1
    
    #to get the spots that are free
    def get_open_spots(self):
        return [[r,c] for r in range(3) for c in range(3) if self.board[r][c]==0]
    
    #to Chechking the move is valid or not
    def is_valid_move(self,r,c):
        if 0<=r<=2 and 0<=c<=2 and self.board[r][c]==0:
            return True
        return False
    
    #making the move on board
    def make_move(self,r,c):
        if self.is_valid_move(r,c):
            self.board[r][c]=self.player
            self.player=(self.player+2)%2+1
            return self.board[r,c],self.player
    
    #Checking that who is the winner
    def check_for_winner(self):
        for c in range(3):
            if self.board[0][c]==self.board[1][c]==self.board[2][c]!=0:
                return self.board[0][c]

        for r in range(3):
            if self.board[r][0]==self.board[r][1]==self.board[r][2]!=0:
                return self.board[r][0]   
        
        if self.board[0][0]==self.board[1][1]==self.board[2][2]!=0:
            return self.board[0][0]
        
        if self.board[2][0]==self.board[1][1]==self.board[0][2]!=0:
            return self.board[2][0]
        
        if self.get_open_spots()==[]:
            return 0
        return -1


# Printing the Tic tac toe board
def print_board():
    chars=['-','X','O']
    for r in range(3):
        for c in range(3):
            print(chars[game.board[r][c]],end=' ')
        print()
    

if __name__=="__main__":
    #creating game as object of class tic_tac_toe
    game=tic_tac_toe()

    #looping so that it will works till the game will finish
    while game.check_for_winner()==-1:
        print_board()
        r,c=map(int,input("Enter spot, player"+str(game.player)+":").split())
        game.make_move(r,c)
    
    print_board()
    x=game.check_for_winner()
    if x==0:
        print("It's a draw...")
    else:
        print('Player ',x,'wins...')
