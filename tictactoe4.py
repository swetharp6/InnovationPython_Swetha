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

def play():
    global option
    global turn
    global dict1
    move=input("Do you want to make the first move? ")
    if move=='Yes' or move=='yes':
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
            elif turn>=5 and turn<9:
                if 'XXX' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['X'],"won the match")
                    break
                elif 'OOO' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['O'],"won the match")
                    break
                else:
                    z=options.copy()
                    z.remove(option)
                    block1=random.choice(update())
                    t[block1]=z[0]
                    turn+=1
                    update()
                    displayboard()
                    
            elif turn==9:
                if 'XXX' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['X'],"won the match")
                    break
                elif 'OOO' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['O'],"won the match")
                    break
                else:
                    print("Draw game")
                    break
            else :
                z=options.copy()
                z.remove(option)
                block1=random.choice(update())
                t[block1]=z[0]
                turn+=1
                update()
                displayboard()
            
    elif move=='No' or move=='no':
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
            elif turn>=5 and turn<9:
                if 'XXX' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['X'],"won the match")
                    break
                elif 'OOO' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['O'],"won the match")
                    break
                else:
                    z=options.copy()
                    z.remove(option)
                    block1=int(input("where you want to make the move?Choose a value between 0-8 "))
                    t[block1]=z[0]
                    turn+=1
                    update()
                    displayboard()
            elif turn==9:
                if 'XXX' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['X'],"won the match")
                    break
                elif 'OOO' in (t[0]+t[1]+t[2],t[3]+t[4]+t[5],t[6]+t[7]+t[8],
        t[0]+t[3]+t[6],t[1]+t[4]+t[7],t[2]+t[5]+t[8],
        t[0]+t[4]+t[8],t[2]+t[4]+t[6]):
                    print(dict1['O'],"won the match")
                    break
                else:
                    print("Draw game")
                    break
            else :
                z=options.copy()
                z.remove(option)
                block1=int(input("where you want to make the move?Choose a value between 0-8 "))
                t[block1]=z[0]
                turn+=1
                update()
                displayboard()
            
play()