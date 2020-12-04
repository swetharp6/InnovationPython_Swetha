import random
t=['None','None','None','None','None','None','None','None','None']
def displayboard():
    print('\n',t[0],'|',t[1],'|',t[2],'\n',t[3],'|',t[4],'|',t[5],'\n',t[6],'|',t[7],'|',t[8],'\n')
def update():
    i=[x for x in range(0,9) if t[x]=='None']
    return i
y=(t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6])
def win():
    while True:
        if 'XXX' in y:
            print(dict['X'],"won the match")
        elif 'OOO' in y:
            print(dict['O'],"won the match")
        else:
            break
           
def draw():
    while True:
       if 'XXX' or 'OOO' not in y:
            print("Draw game")
            break
            
options=['X','O']
displayboard()
while True:
    move=input("Do you want to make the first move? ")
    turn=0
    if move=='Yes' or 'yes':
        option=input("what do you choose from 'X' or 'O'? ")
        if option=='X':
            dict={'X':'player1','O':'player2'}
        else:
            dict={'X':'player2','O':'player1'}
    while turn<9:
        if turn%2==0:
            block=int(input("where you want to make the move?Choose a value between 0-8 "))
            t[block]=option
            turn+=1
            update()
            displayboard()
        else :
            block=random.choice(update())
            x=options.copy()
            x.remove(option)
            t[block]=x[0]
            turn+=1
            update()
            displayboard()
        while turn>=5:
            win()
            if turn==9:
                win()
                draw()
                break
    elif move=='No' or 'no':
        option=random.choice(options)
        if option=='X':
            dict={'X':'player1','O':'player2'}
        else:
            dict={'X':'player2','O':'player1'}
        while turn<9:
            if turn%2==0:
                update()
                block=random.choice(update())
                t[block]=option
                turn+=1
                update()
                displayboard()
            else :
                block=int(input("where you want to make the move?Choose a value between 0-8 "))
                x=options.copy()
                x.remove(option)
                t[block]=x[0]
                turn+=1
                update()
                displayboard()
            while turn>=5:
                win()
                if turn==9:
                    win()
                    draw()
                    break
