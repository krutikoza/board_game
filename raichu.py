#
# raichu.py : Play the game of Raichu
#
# PLEASE PUT YOUR NAMES AND USER IDS HERE!
# Name: Krutik Atulkumar Oza
# ID: kaoza
#
# Based on skeleton code by D. Crandall, Oct 2021
#
import sys
import time
import numpy as np

def board_to_string(board, N):
    return "\n".join(board[i:i+N] for i in range(0, len(board), N))



def evaluation(s, minimizingplayer,depth):
    B=0
    b=0
    w=0
    W=0
    w_raichu=0
    b_raichu=0
    #Count each element on our board
    for line in s:
        B = B + line.count('B')
        b = b + line.count('b')
        w = w + line.count('w')
        W = W + line.count('W')
        w_raichu = w_raichu + line.count('@')
        b_raichu = b_raichu + line.count('$')
        
        
    #If goal state found:
    if (w==0 and W ==0 and w_raichu ==0):
        return (-10000)
    if (B ==0 and b ==0 and b_raichu ==0):
        return (10000)

    #Else return 
    return (10*(W-B)+ 10*(w-b) + 50*(w_raichu-b_raichu)+depth) #evaluation
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# Successor function:

def succ(position, maximizingplayer,N):
    position = list(position)
    fringe = []
    

    if maximizingplayer:
        position.insert(0,'X')
        for index in range(len(position)):
            if position[index] == '.':
                continue



            #For white pichu
            if position[index] == 'w':

                #Move pichu \
                p = position.copy()
                
                if index%N != 0 and p[index+N+1] == 'b':
                    if index+N+N+2 > len(position):
                        pass
                    else:
                        if p[index+N+N+2] =='.' and (index+N+N+2)%N != 1:
                            p[index], p[index+N+N+2]  = p[index+N+N+2], p[index]
                            p[index+N+1] = '.'
                            if index+N+N+2 > (N*N-N):
                                p[index+N+N+2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                p = position.copy()
                #(index)%N !=0 If index at the end of row.
                if (index)%N !=0 and (index+N+1 < len(position)) and p[index+N+1] == '.':
                    p[index],p[index+N+1] = p[index+N+1],p[index]
                    if index+N+1 > (N*N-N):
                        p[index+N+1] = '@'
                    p.pop(0)
                    fringe.append(''.join(p))
                    # print(board_to_string(''.join(p),N))

                #Move pichu /
                p = position.copy()
                
                if ((index)%N != 1) and index+N-1 < len(position) and p[index+N-1] == 'b':
                    if index+N+N-2 > len(position):
                        pass
                    else:
                        if index+N+N-2 < len(position) and (index+N+N-2)%N != 0 and p[index+N+N-2] =='.':
                            p[index], p[index+N+N-2]  = p[index+N+N-2], p[index]
                            p[index+N-1] = '.'
                            if index+N+N-2 > (N*N-N):
                                p[index+N+N-2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))



                p = position.copy()
                if ((index)%N != 1) and p[index+N-1] == '.':
                    p[index],p[index+N-1] = p[index+N-1],p[index]
                    if index+N-1 > (N*N-N):
                        p[index+N-1] = '@'
                    p.pop(0)
                    fringe.append(''.join(p))
                    # print(board_to_string(''.join(p),N))
                p = position.copy()

        #position.pop(0)



            #For white pikachu
            if position[index] == 'W':
                p = position.copy()
                #Move pikachu down
                
                if index+N < len(position):
                    #If black player just below:
                    if p[index+N] == 'b' or p[index+N] == 'B':
                        if index+N+N < len(position) and p[index+N+N] == '.':
                            p[index] = '.'
                            p[index+N] = '.'
                            p[index+N+N] = 'W'
                            if index+N+N > (N*N-N):
                                p[index+N+N] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                    p = position.copy()
                    #One step forward:
                    if p[index+N] == '.':
                        p[index], p[index+N] = p[index+N] + p[index]
                        if index+N > (N*N-N):
                            p[index+N] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))


                    p = position.copy()
                #Black player 2 steps forward:
                if index+N+N < len(position):
                    if (p[index+N+N] == 'b' or p[index+N+N] == 'B') and (p[index+N] == '.'):
                        if index+N+N+N < len(position) and p[index+N+N+N] == '.':
                            p[index] = '.'
                            p[index+N+N] = '.'
                            p[index+N+N+N] = 'W' 
                            if index+N+N+N > (N*N-N):
                                p[index+N+N+N] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                    p = position.copy()
                    if p[index+N+N] == '.' and p[index+N] == '.':
                        p[index] = '.'
                        p[index+N+N] = 'W'
                        if index+N+N > (N*N-N):
                            p[index+N+N] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))

                    p = position.copy()

                #Move pikachu to the right->
                if index%N != 0:
                    if p[index+1] == 'b' or p[index+1] == 'B':
                        if (index+1)%N != 0 and p[index+2] =='.':
                            p[index] = '.'
                            p[index+1] = '.'
                            p[index+2] = 'W'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))
                    p = position.copy()

                    if p[index+1] =='.':
                        p[index],p[index+1] = p[index+1],p[index]
                        p.pop(0)
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))
                        p = position.copy()

                        if (index+1)%N != 0:
                            if p[index+2] =='.':
                                p[index], p[index+2] = p[index+2],p[index]
                                p.pop(0)
                                fringe.append(''.join(p))
                                # print(board_to_string(''.join(p),N))
                    p = position.copy()
                    if (index+1)%N != 0 and p[index+1] == '.':
                        if (index+1+1)%N != 0 and (p[index+1+1] == 'B' or p[index+1+1] == 'b'):
                            if p[index+1+1+1] == '.':
                                p[index] = '.'
                                p[index+1+1] = '.'
                                p[index+1+1+1] = 'W'
                                p.pop(0)
                                fringe.append(''.join(p))
                    p = position.copy()
                #Move pikachu to the <- left:

                if index%N != 1:
                    if p[index-1] == 'b' or p[index-1] == 'B':
                        if (index-1)%N != 1 and p[index-1-1] == '.':
                            p[index] = '.'
                            p[index-1] = '.'
                            p[index-2] = 'W'
                            p.pop(0)
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))
                    p = position.copy()


                    if p[index-1] =='.':
                        p[index],p[index-1] = p[index-1],p[index]
                        p.pop(0)
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))
                        p = position.copy()

                        if (index-1)%N != 1:
                            if p[index-2] =='.':
                                p[index], p[index-2] = p[index-2],p[index]
                                p.pop(0)
                                fringe.append(''.join(p))
                                # print(board_to_string(''.join(p),N))

                            p = position.copy()
                            if (index-2)%N !=1:
                                if p[index-1] == '.':
                                    if p[index-2] == 'b' or p[index-2] == 'B':
                                        if p[index-3] =='.':
                                            p[index] = '.'
                                            p[index-2] = '.'
                                            p[index-3] = 'W'
                                            p.pop(0)
                                            fringe.append(''.join(p))



            
            p = position.copy()
            # For Raichu:
            if position[index] == '@':
                count = 0
                i = index
                loop_count = 0
                #Steps going down:
                while True:
                    if loop_count > N:
                        break
                    if i+N >= len(position):
                        break
                    elif i+N < len(position) and p[i+N] == '.':
                        
                        p[i],p[i+N] = p[i+N], p[i]
                        p.pop(0)
                        fringe.append(''.join(p))
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i = i + N
                    elif i+N < len(position) and (p[i+N] == 'w' or p[i+N] == 'W'):
                        break
                    elif i+N < len(position) and (p[i+N] == 'B' or p[i+N] == 'b' or p[i+N] == '$'):
                        
                        if count == 1:
                            break
                        count = count + 1
                        if i+N+N < len(position) and p[i+N+N] == '.':
                            p[i] = '.'
                            p[i+N] = '.'
                            p[i+N+N] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i+N+N
                        else:
                            break
                    
                    loop_count = loop_count +1
                    

                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go up:
                while True:
                    if loop_count > N:
                        break
                    if i-N < 1:
                        break
                    elif i-N >= 1 and p[i-N] == '.':
                        p[i],p[i-N] = p[i-N], p[i]
                        p.pop(0)
                        fringe.append(''.join(p))
                        p.insert(0,'x')
                        i = i - N
                    elif i-N > 0 and (p[i-N] == 'w' or p[i-N] == 'W'):
                        break

                    elif i-N > 0 and (p[i-N] == 'B' or p[i-N] == 'b' or p[i-N] == '$'):
                        if count == 1:
                            break
                        count = count + 1
                        
                        if i-N-N > 0 and p[i-N-N] == '.':
                            p[i] = '.'
                            p[i-N] = '.'
                            p[i-N-N] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            p.insert(0,'x')
                            i = i-N-N
                        else:
                            break
                    
                    loop_count = loop_count +1


                p = position.copy()
                count = 0
                i = index

                loop_count = 0
                #Steps to go right:
                while True:
                    if loop_count > N:
                        break
                    
                    if i%N == 0 and (i+1)%N == 1:
                        break
                    elif (i)%N != 0 and p[i+1] == '.':
                        p[i],p[i+1] = p[i+1], p[i]
                        p.pop(0)
                        fringe.append(''.join(p))
                        p.insert(0,'x')
                        i = i + 1
                    elif (i)%N != 0  and (p[i+1] == 'w' or p[i+1] == 'W'):
                        break

                    elif (i)%N != 0  and ((p[i+1] == 'B' or p[i+1] == 'b' or p[i+1] == '$') and ((i+1+1)%N == 1)):
                        break

                    elif (i)%N != 0 and (p[i+1] == 'B' or p[i+1] == 'b' or p[i+1] == '$') and i+1+1 < len(position) and (p[i+1+1] == '.'):
                        if count == 1:
                            break
                        count = count + 1
                        if (i+1+1)%N != 1:
                            p[i] = '.'
                            p[i+1] = '.'
                            p[i+1+1] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            p.insert(0,'x')
                            i = i+1+1
                        else:
                            break
                    loop_count = loop_count+1

                
                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go Left:
                while True:
                    #print(p)
                    if loop_count > N:
                        break
                    if i%N == 1 and (i-1)%N == 0:
                        break
                    elif (i)%N != 1 and p[i-1] == '.':
                        p[i],p[i-1] = p[i-1], p[i]
                        p.pop(0)
                        fringe.append(''.join(p))
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i = i - 1
                    elif (i)%N != 1  and (p[i-1] == 'w' or p[i-1] == 'W'):
                        break
                    elif (i)%N != 1 and (p[i-1] == 'B' or p[i-1] == 'b' or p[i-1] == '$'):
                        if count == 1:
                            break
                        count = count + 1
                        if (i-1-1) >0 and (i-1-1)%N != 0 and p[i-1-1] == '.':
                            p[i] = '.'
                            p[i-1] = '.'
                            p[i-1-1] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-1-1
                        else:
                            break
                    loop_count = loop_count +1

                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal \ down:
                while True:
                    if loop_count > N:
                        break
                    if (i+N+1)%N > len(position):
                        break
                    elif (i)%N != 0 and (i+N+1) < len(position) and p[i+N+1] == '.':
                        p[i] = '.'
                        p[i+N+1] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i+N+1
                    elif (i+1)%N != 0 and (i+N+N+2) < len(position) and (p[i+N+1] == 'B' or p[i+N+1] == 'b' or p[i+N+1] == '$'):
                        count = count+1
                        if count == 1:
                            break                        
                        if p[i+N+N+2] == '.':
                            p[i] = '.'
                            p[i+N+1] = '.'
                            p[i+N+N+2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i+N+N+2
                        else:
                            break

                    loop_count = loop_count +1



                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal / up:
                while True:
                    if loop_count > N:
                        break
                    if (i)%N == 0:
                        break
                    elif (i)%N != 0 and (i-N+1) > 0 and p[i-N+1] == '.':
                        p[i] = '.'
                        p[i-N+1] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i-N+1
                    elif (i+1)%N != 0 and (i-N-N+2) > 0 and (p[i-N+1] == 'B' or p[i-N+1] == 'b' or p[i-N+1] == '$'):
                        count = count+1
                        if count == 1:
                            break                        
                        if p[i-N-N+2] == '.':
                            p[i] = '.'
                            p[i-N+1] = '.'
                            p[i-N-N+2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-N-N+2
                        else:
                            break

                    loop_count = loop_count +1




                p = position.copy()
                count = 0
                i = index
                loop_count = 0
           #Steps to go diagonal \ up:
                while True:
                    if loop_count > N:
                        break
                    if (i-N-1)%N < 1:
                        break
                    elif (i)%N != 1 and (i-N-1) > 0 and p[i-N-1] == '.':
                        p[i] = '.'
                        p[i-N-1] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i-N-1
                    elif (i-1)%N != 1 and (i-N-N-2) > 0 and (p[i-N-1] == 'B' or p[i-N-1] == 'b' or p[i-N-1] == '$'):
                        count = count+1
                        if count == 1:
                            break                        
                        if p[i-N-N-2] == '.':
                            p[i] = '.'
                            p[i-N-1] = '.'
                            p[i-N-N-2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-N-N-2
                        else:
                            break 

                    loop_count = loop_count +1         




                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal / down:
                while True:
                    if loop_count > N:
                        break
                    if (i+N-1)%N < 1:
                        break
                    elif (i)%N != 1 and (i+N-1) > 1 and i+N+1 < len(position) and p[i+N-1] == '.':
                        p[i] = '.'
                        p[i+N-1] = '@'
                        p.pop(0)
                        fringe.append(''.join(p))
                        p.insert(0,'x')
                        i=i+N-1
                    elif (i-1)%N != 1 and (i+N+N-2) > 1 and i+N+N-2< len(position) and (p[i+N-1] == 'B' or p[i+N-1] == 'b' or p[i+N-1] == '$'):
                        count = count+1
                        if count == 1:
                            break                        
                        if p[i+N+N-2] == '.':
                            p[i] = '.'
                            p[i+N-1] = '.'
                            p[i+N+N-2] = '@'
                            p.pop(0)
                            fringe.append(''.join(p))
                            p.insert(0,'x')
                            i = i+N+N-2
                        else:
                            break 
                    loop_count = loop_count +1 


    #For Max player code ENDS
    #
    #
    #
    # 
    # 
    #For Min player STARTS:

    else:
        
        position.reverse()
        position.insert(0,'X')
        for index in range(len(position)):
            if position[index] == '.':
                continue



            #For white pichu
            if position[index] == 'b':

                #Move pichu \
                p = position.copy()
                
                if index%N != 0 and p[index+N+1] == 'w':
                    
                    if index+N+N+2 > len(position):
                        pass
                    else:
                        if p[index+N+N+2] =='.' and (index+N+N+2)%N != 1:
                            p[index], p[index+N+N+2]  = p[index+N+N+2], p[index]
                            p[index+N+1] = '.'
                            if index+N+N+2 > (N*N-N):
                                p[index+N+N+2] = '$'

                            p.pop(0)
                            p.reverse()
                            
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                p = position.copy()
                #(index)%N !=0 If index at the end of row.
                if (index)%N !=0 and (index+N+1 < len(position)) and p[index+N+1] == '.':
                    p[index],p[index+N+1] = p[index+N+1],p[index]
                    if index+N+1 > (N*N-N):
                        p[index+N+1] = '$'

                    p.pop(0)
                    p.reverse() 
                    fringe.append(''.join(p))
                    # print(board_to_string(''.join(p),N))

                #Move pichu /
                p = position.copy()
                
                if ((index)%N != 1) and index+N-1 < len(position) and p[index+N-1] == 'w':
                    if index+N+N-2 > len(position):
                        pass
                    else:
                        if index+N+N-2 < len(position) and (index+N+N-2)%N != 0 and p[index+N+N-2] =='.':
                            p[index], p[index+N+N-2]  = p[index+N+N-2], p[index]
                            p[index+N-1] = '.'
                            if index+N+N-2 > (N*N-N):
                                p[index+N+N-2] = '$'

                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))



                p = position.copy()
                if ((index)%N != 1) and p[index+N-1] == '.':
                    p[index],p[index+N-1] = p[index+N-1],p[index]
                    if index+N-1 > (N*N-N):
                        p[index+N-1] = '$'

                    
                    p.pop(0)
                    p.reverse()
                    fringe.append(''.join(p))
                    # print(board_to_string(''.join(p),N))
                p = position.copy()

        #position.pop(0)



            #For white pikachu
            if position[index] == 'B':
                p = position.copy()
                #Move pikachu down
                
                if index+N < len(position):
                    #If black player just below:
                    if p[index+N] == 'w' or p[index+N] == 'W':
                        if index+N+N < len(position) and p[index+N+N] == '.':
                            p[index] = '.'
                            p[index+N] = '.'
                            p[index+N+N] = 'B'
                            if index+N+N > (N*N-N):
                                p[index+N+N] = '$'

                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                    p = position.copy()
                    #One step forward:
                    if p[index+N] == '.':
                        p[index], p[index+N] = p[index+N] + p[index]
                        if index+N > (N*N-N):
                            p[index+N] = '$'

                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))


                    p = position.copy()
                #Black player 2 steps forward:
                if index+N+N < len(position):
                    if (p[index+N+N] == 'w' or p[index+N+N] == 'W') and (p[index+N] == '.'):
                        if index+N+N+N < len(position) and p[index+N+N+N] == '.':
                            p[index] = '.'
                            p[index+N+N] = '.'
                            p[index+N+N+N] = 'B' 
                            if index+N+N+N > (N*N-N):
                                p[index+N+N+N] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))

                    p = position.copy()
                    if p[index+N+N] == '.' and p[index+N] == '.':
                        p[index] = '.'
                        p[index+N+N] = 'B'
                        if index+N+N > (N*N-N):
                            p[index+N+N] = '$'
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))

                    p = position.copy()

                #Move pikachu to the right->
                if index%N != 0:
                    if p[index+1] == 'w' or p[index+1] == 'W':
                        if (index+1)%N != 0 and p[index+2] =='.':
                            p[index] = '.'
                            p[index+1] = '.'
                            p[index+2] = 'B'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))
                    p = position.copy()

                    if p[index+1] =='.':
                        p[index],p[index+1] = p[index+1],p[index]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))
                        p = position.copy()
                        
                        # print("Index =", index)
                        if (index+1)%N != 0:
                            
                            if p[index+2] =='.':
                                p[index], p[index+2] = p[index+2],p[index]
                                p.pop(0)
                                p.reverse()
                                fringe.append(''.join(p))
                                p = position.copy()
                                # print(board_to_string(''.join(p),N))
                                if (index+1)%N != 0 and p[index+1] == '.':

                                    if (index+1+1)%N != 0 and (p[index+1+1] == 'W' or p[index+1+1] == 'w'):
                                        if p[index+1+1+1] == '.':
                                            p[index] = '.'
                                            p[index+1+1] = '.'
                                            p[index+1+1+1] = 'B'
                                            p.pop(0)
                                            p.reverse()
                                            fringe.append(''.join(p))
                    p = position.copy()

                #Move pikachu to the <- left:

                if index%N != 1:
                    if p[index-1] == 'w' or p[index-1] == 'W':
                        if (index-1)%N != 1 and p[index-1-1] == '.':
                            p[index] = '.'
                            p[index-1] = '.'
                            p[index-2] = 'B'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            # print(board_to_string(''.join(p),N))
                    p = position.copy()

                    if p[index-1] =='.':
                        p[index],p[index-1] = p[index-1],p[index]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        # print(board_to_string(''.join(p),N))
                        p = position.copy()

                        if (index-1)%N != 1:
                            if p[index-2] =='.':
                                p[index], p[index-2] = p[index-2],p[index]
                                p.pop(0)
                                p.reverse()
                                fringe.append(''.join(p))
                                # print(board_to_string(''.join(p),N))
                                p = position.copy()
                            if (index-2)%N !=1:
                                if p[index-1] == '.':
                                    if p[index-2] == 'w' or p[index-2] == 'W':
                                        if p[index-3] =='.':
                                            p[index] = '.'
                                            p[index-2] = '.'
                                            p[index-3] = 'B'
                                            p.pop(0)
                                            p.reverse()
                                            fringe.append(''.join(p))

            
            p = position.copy()
            # For Raichu:
            if position[index] == '$':
                count = 0
                i = index
                loop_count = 0
                #Steps going down:
                while True:
                    if loop_count > N:
                        break
                    if i+N >= len(position):
                        break
                    elif i+N < len(position) and p[i+N] == '.':
                        
                        p[i],p[i+N] = p[i+N], p[i]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i = i + N
                    elif i+N < len(position) and (p[i+N] == 'b' or p[i+N] == 'B'):
                        break
                    elif i+N < len(position) and (p[i+N] == 'W' or p[i+N] == 'w' or p[i+N] == '@'):
                        
                        if count == 1:
                            break
                        count = count + 1
                        if i+N+N < len(position) and p[i+N+N] == '.':
                            p[i] = '.'
                            p[i+N] = '.'
                            p[i+N+N] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i+N+N
                        else:
                            break
                    
                    loop_count = loop_count +1
                    

                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go up:
                while True:
                    if loop_count > N:
                        break
                    if i-N < 1:
                        break
                    elif i-N >= 1 and p[i-N] == '.':
                        p[i],p[i-N] = p[i-N], p[i]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        p.insert(0,'x')
                        i = i - N
                    elif i-N > 0 and (p[i-N] == 'b' or p[i-N] == 'B'):
                        break

                    elif i-N > 0 and (p[i-N] == 'W' or p[i-N] == 'w' or p[i-N] == '@'):
                        if count == 1:
                            break
                        count = count + 1
                        
                        if i-N-N > 0 and p[i-N-N] == '.':
                            p[i] = '.'
                            p[i-N] = '.'
                            p[i-N-N] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            p.insert(0,'x')
                            i = i-N-N
                        else:
                            break
                    
                    loop_count = loop_count +1
                    


                p = position.copy()
                count = 0
                i = index

                loop_count = 0
                #Steps to go right:
                while True:
                    if loop_count > N:
                        break
                    
                    if i%N == 0 and (i+1)%N == 1:
                        break
                    elif (i)%N != 0 and p[i+1] == '.':
                        p[i],p[i+1] = p[i+1], p[i]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        p.insert(0,'x')
                        i = i + 1
                    elif (i)%N != 0  and (p[i+1] == 'b' or p[i+1] == 'B'):
                        break

                    elif (i)%N != 0  and ((p[i+1] == 'W' or p[i+1] == 'w' or p[i+1] == '@') and ((i+1+1)%N == 1)):
                        break

                    elif (i)%N != 0 and (p[i+1] == 'W' or p[i+1] == 'w' or p[i+1] == '@') and i+1+1 < len(position) and (p[i+1+1] == '.'):
                        if count == 1:
                            break
                        count = count + 1
                        if (i+1+1)%N != 1:
                            p[i] = '.'
                            p[i+1] = '.'
                            p[i+1+1] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            p.insert(0,'x')
                            i = i+1+1
                        else:
                            break
                    loop_count = loop_count+1

                
                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go Left:
                while True:
                    #print(p)
                    if loop_count > N:
                        break
                    if i%N == 1 and (i-1)%N == 0:
                        break
                    elif (i)%N != 1 and p[i-1] == '.':
                        p[i],p[i-1] = p[i-1], p[i]
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i = i - 1
                    elif (i)%N != 1  and (p[i-1] == 'b' or p[i-1] == 'B'):
                        break
                    elif (i)%N != 1 and (p[i-1] == 'W' or p[i-1] == 'w' or p[i-1] == '@'):
                        if count == 1:
                            break
                        count = count + 1
                        if (i-1-1) >0 and (i-1-1)%N != 0 and p[i-1-1] == '.':
                            p[i] = '.'
                            p[i-1] = '.'
                            p[i-1-1] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-1-1
                        else:
                            break
                    loop_count = loop_count +1

                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal \ down:
                while True:
                    if loop_count > N:
                        break
                    if (i+N+1)%N > len(position):
                        break
                    elif (i)%N != 0 and (i+N+1) < len(position) and p[i+N+1] == '.':
                        p[i] = '.'
                        p[i+N+1] = '$'
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i+N+1
                    elif (i+1)%N != 0 and (i+N+N+2) < len(position) and (p[i+N+1] == 'W' or p[i+N+1] == 'w' or p[i+N+1] == '@'):

                        if count == 1:
                            break                        
                        count = count+1
                        if p[i+N+N+2] == '.':
                            p[i] = '.'
                            p[i+N+1] = '.'
                            p[i+N+N+2] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i+N+N+2
                        else:
                            break

                    loop_count = loop_count +1



                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal / up:
                while True:
                    if loop_count > N:
                        break
                    if (i)%N == 0:
                        break
                    elif (i)%N != 0 and (i-N+1) > 0 and p[i-N+1] == '.':
                        p[i] = '.'
                        p[i-N+1] = '$'
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i-N+1
                    elif (i+1)%N != 0 and (i-N-N+2) > 0 and (p[i-N+1] == 'W' or p[i-N+1] == 'w' or p[i-N+1] == '@'):
                        if count == 1:
                            break                        
                        count = count+1
                        if p[i-N-N+2] == '.':
                            p[i] = '.'
                            p[i-N+1] = '.'
                            p[i-N-N+2] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-N-N+2
                        else:
                            break

                    loop_count = loop_count +1




                p = position.copy()
                count = 0
                i = index
                loop_count = 0
        #Steps to go diagonal \ up:
                while True:
                    if loop_count > N:
                        break
                    if (i-N-1)%N < 1:
                        break
                    elif (i)%N != 1 and (i-N-1) > 0 and p[i-N-1] == '.':
                        p[i] = '.'
                        p[i-N-1] = '$'
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        #print(board_to_string(''.join(p),N))
                        p.insert(0,'x')
                        i=i-N-1
                    elif (i-1)%N != 1 and (i-N-N-2) > 0 and (p[i-N-1] == 'W' or p[i-N-1] == 'w' or p[i-N-1] == '@'):
                        if count == 1:
                            break      
                        count = count+1                  
                        if p[i-N-N-2] == '.':
                            p[i] = '.'
                            p[i-N-1] = '.'
                            p[i-N-N-2] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            #print(board_to_string(''.join(p),N))
                            p.insert(0,'x')
                            i = i-N-N-2
                        else:
                            break 

                    loop_count = loop_count +1         




                p = position.copy()
                count = 0
                i = index
                loop_count = 0
                #Steps to go diagonal / down:
                while True:
                    if loop_count > N:
                        break
                    if (i+N-1)%N < 1:
                        break
                    elif (i)%N != 1 and (i+N-1) > 1 and i+N+1 < len(position) and p[i+N-1] == '.':
                        p[i] = '.'
                        p[i+N-1] = '$'
                        p.pop(0)
                        p.reverse()
                        fringe.append(''.join(p))
                        p.reverse()
                        p.insert(0,'x')
                        i=i+N-1
                    elif (i-1)%N != 1 and (i+N+N-2) > 1 and i+N+N-2< len(position) and (p[i+N-1] == 'W' or p[i+N-1] == 'w' or p[i+N-1] == '@'):
                        if count == 1:
                            break                        
                        count = count+1
                        if p[i+N+N-2] == '.':
                            p[i] = '.'
                            p[i+N-1] = '.'
                            p[i+N+N-2] = '$'
                            p.pop(0)
                            p.reverse()
                            fringe.append(''.join(p))
                            p.reverse()
                            p.insert(0,'x')
                            i = i+N+N-2
                        else:
                            break 
                    loop_count = loop_count +1 
    return fringe















#MINIMAX:
def minmax(position, total_depth,depth, alpha, beta, maximizingplayer, next_move_board,N,our_player):
    
    #if at the last given depth, return evaluation.
    if depth == 0:
        
        return ([evaluation(position,maximizingplayer,depth),position])
    if (position.count('w') ==0 and position.count('W') ==0 and position.count('@') ==0):
        return ([-100,position])
    if (position.count('B') ==0 and position.count('b') ==0 and position.count('$') ==0):
        return ([100,position])
    
    child = succ(position, maximizingplayer, N)
    #For max player
    if maximizingplayer:
        maxEval = -9999999999999
        #If no child then return its cost
        if child == []:
            return ([evaluation(position,maximizingplayer,depth),position])
        for i in child:
            
            eval = minmax(i, total_depth,depth - 1, alpha, beta, False, next_move_board,N,our_player)
            
            if maxEval < eval[0]:
                maxEval = eval[0]
                # update the next move if our player is white
                if depth == total_depth:
                    
                    if our_player == True:
                        next_move_board = i
            
            alpha = max(alpha,eval[0])
            if beta<=alpha:
                break
        return ([maxEval,next_move_board])
    #for min player
    else:
        minEval = 9999999999999
        #If no child then return its cost
        if child == []:
            return ([evaluation(position,maximizingplayer,depth),position])
        for i in child:
            
            eval = minmax(i, total_depth,depth - 1, alpha, beta, True, next_move_board,N,our_player)
            
            
            if minEval > eval[0]:
                minEval = eval[0]
                # update the next move if our player is black
                if our_player == False:
                        next_move_board = i
                
                
            beta = min(beta,eval[0])
            if beta<=alpha:
                break
        return ([minEval,next_move_board])




def find_best_move(board, N, player, timelimit):


   
   

    if player =='w' or player =='W':
        p = True
    else:
        p = False

    #run minimax for 1 to 20 depth
    for i in range(1,20,1):
        k = minmax(board, i,i, -99999999999, 999999999999, p, board,N, our_player = p)
        #if win in very next step:
        if i == 1 and k[0] == 10000:
            yield k[1]
            break
        yield k[1]


if __name__ == "__main__":
    if len(sys.argv) != 5:
        raise Exception("Usage: Raichu.py N player board timelimit")
        
    (_, N, player, board, timelimit) = sys.argv
    N=int(N)
    timelimit=int(timelimit)
    if player not in "wb":
        raise Exception("Invalid player.")

    if len(board) != N*N or 0 in [c in "wb.WB@$" for c in board]:
       raise Exception("Bad board string.")

    print("Searching for best move for " + player + " from board state: \n" + board_to_string(board, N))
    print("Here's what I decided:")
    for new_board in find_best_move(board, N, player, timelimit):
        print(new_board)