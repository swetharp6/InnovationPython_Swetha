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

options=['X','O']
displayboard()

def result():
    if turn>=5 and turn<9:
        if 'XXX' in y:
            print(dict['X'],"won the match")
        elif 'OOO' in y:
            print(dict['O'],"won the match")
    elif turn==9:
        if 'XXX' in y:
            print(dict['X'],"won the match")
        elif 'OOO' in y:
            print(dict['O'],"won the match")
        else:
            print("Draw game")
    else:
        pass

def game():
    global turn
    turn=0
    while turn<9:
        if turn%2==0:
            t[block]=option
            turn+=1
            update()
            displayboard()
        else :
            z=options.copy()
            z.remove(option)
            t[block1]=z[0]
            turn+=1
            update()
            displayboard()
                   
        result()

def play():
    global option
    global block
    global block1
    move=input("Do you want to make the first move? ")
    if move=='Yes' or 'yes':
        option=input("what do you choose from 'X' or 'O'? ")
        if option=='X':
            dict={'X':'You','O':'Computer'}
        else:
            dict={'X':'Computer','O':'You'}
        block=int(input("where you want to make the move?Choose a value between 0-8 "))
        block1=random.choice(update())
        game()
    elif move=='No' or 'no':
        option=random.choice(options)
        if option=='X':
            dict={'X':'Computer','O':'You'}
        else:
            dict={'X':'You','O':'Computer'}
        block=random.choice(update())
        block1=int(input("where you want to make the move?Choose a value between 0-8 "))
        game()

play()