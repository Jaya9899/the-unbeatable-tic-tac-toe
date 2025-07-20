from random import randint
import tkinter as tk
import copy
from tkinter import messagebox


class TicTacToe:
    def __init__(self,root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.board=[["","",""],["","",""],["","",""]]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.currplayer="X"
        self.moves=0
        self.boxes()
        
        self.root.after(100,lambda:messagebox.showinfo(
            "Welcome to Tic Tac Toe!",
            "Player X: YOU\nPlayer O: Computer\nClick on a box to mark!"
        ))
    
    def boxes(self):
        for i in range(3):
            for j in range(3):
                btn=tk.Button(self.root,text="",font=("Helvetica", 24),width=5,height=2,
                                command=lambda r=i,c=j:self.player_move(r,c))
                btn.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j]=btn
        
    def wincondition(self,board=None):
        if board is None:
            board = self.board

        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != "":
                return board[i][0]
            if board[0][i] == board[1][i] == board[2][i] != "":
                return board[0][i]

        if board[0][0] == board[1][1] == board[2][2] != "":
            return board[0][0]
        if board[0][2] == board[1][1] == board[2][0] != "":
            return board[0][2]

        return None
    
    def player_move(self,row,col):
        if self.board[row][col] != "":
            return 
        
        self.board[row][col] = "X"
        self.buttons[row][col].config(text="X", state="disabled")
        self.moves+=1
        
        winner=self.wincondition()
        if winner or self.moves==9:
            self.show_result(winner)
            return
        
        self.root.after(500, self.comp_move)
    
    def comp_move(self):
        best_score=float('-inf')
        best_move=None
        
        for i in range(3):
            for j in range(3):
                if self.board[i][j]=="":
                    temp_board = copy.deepcopy(self.board)
                    temp_board[i][j] = "O"
                    score = self.minimax(temp_board, False)

                    if score>best_score:
                        best_score=score
                        best_move= (i,j)
        if best_move:
            i,j=best_move
            self.board[i][j]="O"
            self.buttons[i][j].config(text="O", state="disabled")
            self.moves+=1
            
        winner=self.wincondition()
        if winner or self.moves==9:
            self.show_result(winner)
    
    
    def minimax(self, board, isMax):
        winner=self.wincondition(board)
        if winner=="O":
            return 1
        elif winner=="X":
            return -1
        elif self.is_draw(board): 
            return 0
        
        if isMax:
            best_score=float('-inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j]=="":
                        board[i][j]="O"
                        score=self.minimax(board, False)
                        board[i][j]=""
                        best_score=max(score, best_score)
            return best_score
        else:
            best_score=float('inf')
            for i in range(3):
                for j in range(3):
                    if board[i][j]=="":
                        board[i][j]="X"
                        score=self.minimax(board, True)
                        board[i][j]=""
                        best_score=min(score, best_score)
            return best_score
    
    
    def is_draw(self, board=None):
        if board is None:
            board = self.board
        return all(cell != "" for row in board for cell in row)

    def show_result(self, winner):
        if winner == "X":
            messagebox.showinfo("Game Over", "You Win :)")
        elif winner == "O":
            messagebox.showinfo("Game Over", "Computer Wins :()")
        else:
            messagebox.showinfo("Game Over", "It's a draw :|")

        self.reset_board()  
            
    def reset_board(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.moves = 0
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="normal")
                
                
if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()         
    
                
