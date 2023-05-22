

from tkinter import Button, Canvas, Label, PhotoImage, Tk, font, mainloop, messagebox

player='X'
stop_game=False
mov_count=0

def on_enter(e):
    restart_btn.config(bg='blue',fg='red')

def on_leave(e):
    restart_btn.config(bg='green',fg='black')



def display_winner(plyr):
    if plyr=='draw':
        winner=messagebox.showinfo('Status',"It's Tie...")
    else:
        winner=messagebox.showinfo('Status',plyr+' Wins...')
        print(winner)
        
    player_turn.configure(text="CLICK Restart button to Play Again",font=('Arial',15),fg='red',bg='sky blue')

    

def clicked(r,c):
    global player
    global mov_count    
    mov_count+=1     #to count no of moves done by the player

    if player=='X' and board[r][c]==0 and stop_game==False:
        but[r][c].configure(text='X',font=('Arial',20),bg='red')
        board[r][c]='X'
        player='O'
        
    if player=='O' and board[r][c]==0 and stop_game==False:
        but[r][c].configure(text='O',font=('Arial',20),bg='white')
        board[r][c]='O'
        player='X'
    movs.configure(text=f'Moves Count : {mov_count}',font=('Arial',15),fg='red',bg='blue')
    player_turn.configure(text=f"It's Player: {player} Turn",font=('Arial',15),fg='#12ff21',bg='sky blue')
    check_winner()

def check_winner():
    global stop_game
    for i in range(3):
        if board[i][0]==board[i][1]==board[i][2]!=0:
            stop_game=True
            print(board[i][0])
            display_winner(board[i][0])
            break
        elif board[0][0]==board[1][1]==board[2][2]!=0:
            stop_game=True
            print(board[0][0])
            display_winner(board[0][0])
            break
        elif board[0][i]==board[1][i]==board[2][i]!=0:
            stop_game=True
            print(board[0][i])
            display_winner(board[0][i])
            break
        elif board[0][2]==board[i][1]==board[2][0]!=0:
            stop_game=True
            print(board[0][2])
            display_winner(board[0][2])
            break
        elif board[0][0] and board[0][1] and board[0][2] and board[1][0] and board[1][1] and board[1][2] and board[2][0] and board[2][1] and board[2][2]!=0:
            stop_game=True
            print(board[0][0])
            display_winner('draw')
            break

def restart_game():
    global player
    global stop_game
    global mov_count
    player='X'
    stop_game=False
    mov_count=0
    movs.configure(text=f'Moves Count : {mov_count}',font=('Arial',15),fg='red',bg='blue')
    player_turn.configure(text="Start the game",font=('Arial',15),fg='#12ff21',bg='sky blue')

    for i in range(3):
        for j in range(3):
            board[i][j]=0
            but[i][j].configure(text='',bg='white')


def beginPage():
    new_window=Tk()
    new_window.title("let's tic-tac-toe")
    #new_window.resizable(False,False)
    new_window.geometry('400x270+500+200')
    bgimg=PhotoImage(file="spce2.png")
    
    #create canvas
    main_canvas=Canvas(new_window,width=400,height=300)
    main_canvas.pack(fill='both',expand=True)

    #set image in canves
    main_canvas.create_image(0,0,image=bgimg,anchor='nw')

    #adding some elements to canvas
    main_canvas.create_text(90,120,text="Welcome Click to Play button\n\t to start",font=('Arial',15),fill='white',anchor='nw')

    main_but=Button(new_window,text="Play",fg='white',bg='green',font=('Arial',18),command=new_window.destroy)
    
    but_window=main_canvas.create_window(170,170,anchor='nw',window=main_but)

    new_window.mainloop()
   


if __name__=='__main__':
    #========= main Page ============
    beginPage()
    
    root=Tk()
    root.title('Tic Tac Toe')
    root.resizable(False,False)
    
    #============== Initializing the values ===========
    but=[[0 for i in range(3)] for i in range(3)]
    #print(but)
    
    board=[[0 for i in range(3)] for i in range(3)]

    #============= creating buttons =========
    for i in range(3):
        for j in range(3):
            but[i][j]=Button(width=9,height=4,font=('Arial',20),command=lambda r=i,c=j:clicked(r,c))
            but[i][j].grid(row=i+1,column=j)

    #===================== Status Bar ===========
    player_turn=Label(root,text="Start the game",font=('Arial',15),fg='#12ff21',bg='sky blue')
    player_turn.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

    #===================== Restart button ============
    restart_btn=Button(root,text='Restart',font=('Arial',15),fg='black',bg='green',command=restart_game)
    restart_btn.grid(row=4,column=0,columnspan=2,padx=5,pady=5)

    #applying the hover effect using event in tkinter use bind function to bind elements
    restart_btn.bind('<Enter>',on_enter)
    restart_btn.bind('<Leave>',on_leave)

    #===================== No. of moves done count =============
    movs=Label(root,text='Moves Count : 0',font=('Arial',15),fg='red',bg='blue')
    movs.grid(row=4,column=2)

    mainloop()

    


