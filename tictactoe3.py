import random

t=['None','None','None','None','None','None','None','None','None']

def displayboard():
    print('\n',t[0],'|',t[1],'|',t[2],'\n',t[3],'|',t[4],'|',t[5],'\n',t[6],'|',t[7],'|',t[8],'\n')

def update():
    i=[x for x in range(0,9) if t[x]=='None']
    return i

options=['X','O']
displayboard()
turn=0

def result():
    y=(t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6])
    print(turn)
    if turn>=5 and turn<9:
        if 'XXX' in y:
            print(dict1['X'],"won the match")
        elif 'OOO' in y:
            print(dict1['O'],"won the match")
    elif turn==9:
        if 'XXX' in y:
            print(dict1['X'],"won the match")
        elif 'OOO' in y:
            print(dict1['O'],"won the match")
        else:
            print("Draw game")
    else:
        pass

def play():
    global option
    global turn
    global dict1
    move=input("Do you want to make the first move? ")
    if move=='Yes' or 'yes':
        option=input("what do you choose from 'X' or 'O'? ")
        if option=='X':
            dict1={'X':'You','O':'Computer'}
        else:
            dict1={'X':'Computer','O':'You'}
         
        while turn<9:
            if turn%2==0:
                block=int(input("where you want to make the move?Choose a value between 0-8 "))
                t[block]=option
                turn+=1
                update()
                displayboard()
            else :
                z=options.copy()
                z.remove(option)
                block1=random.choice(update())
                t[block1]=z[0]
                turn+=1
                update()
                displayboard()
            result()
    elif move=='No' or 'no':
        option=random.choice(options)
        if option=='X':
            dict1={'X':'Computer','O':'You'}
        else:
            dict1={'X':'You','O':'Computer'}
           
        while turn<9:
            if turn%2==0:
                block=random.choice(update())
                t[block]=option
                turn+=1
                update()
                displayboard()
            else :
                z=options.copy()
                z.remove(option)
                block1=int(input("where you want to make the move?Choose a value between 0-8 "))
                t[block1]=z[0]
                turn+=1
                update()
                displayboard()
            result()

play()