#pl_list = [[' ', 's1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
#pl_list = [[' ', 's1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], ['s3', 's3', 's3', 's3', ' ', ' ', ' ', ' ', ' ', ' '], ['s4', 's4', 's4', 's4', 's4', ' ', ' ', ' ', ' ', ' '], ['s6', 's6', 's6', 's6', ' ', ' ', ' ', ' ', ' ', ' '], ['s6', 's6', 's6', 's6', ' ', ' ', ' ', ' ', ' ', ' '], ['s7', 's7', 's7', 's7', 's7', ' ', ' ', ' ', ' ', ' '], ['s7', 's7', 's7', 's7', 's7', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]
def check_win():
    for i in range(0,10,1):
        for j in range(0,10,1):
            if(pl_list[i][j] != ' '):
                won = 0
                return won
            else:
                won = 1   
    return won
    
    
    
def check_hit(pl_list):
    check_hit_list = [] #list which will be sent to client
    #pl_hit = [0,1] #temp list with hit coords
    pl_hit = data[1]
    if(pl_list[pl_hit[0]][pl_hit[1]] != ' '):
        hit = 1                                  
        hit_ship = pl_list[pl_hit[0]][pl_hit[1]]
        pl_list[pl_hit[0]][pl_hit[1]] = ' '
        check_hit_list.append(pl_hit)           #hit coords
        check_hit_list.append(hit)              #variable if ship is hit || 1=ship hit  0=ship not hit
        check_hit_list.append(hit_ship)         #which ship is hit
        #loop to check if ship sunken or not
        for i in range(0,10,1):
            for j in range(0,10,1):
                if(pl_list[i][j] == hit_ship):
                    sunken = 0
                    break
                else:
                    sunken = 1
                    win_check = check_win()
            break
        check_hit_list.append(sunken)           #ship sunken || 0=not sunken    1=sunken
        check_hit_list.append(win_check)        #variable if won || 0=didnt win     1=won 
        server.send(client,check_hit_list)     #check_hit_list = [[coords], hit ship, which ship, ship sunken or not, win variable] ||| gui need to check check_hit_list[1]
        ID = get_ID(data[1])
        queue.append(f"{ID};CF;{check_hit_list}")
    else:
        hit = 0                                 
        check_hit_list.append(pl_hit)           #hit coords
        check_hit_list.append(hit)              #variable if ship is hit || 1=ship hit  0=ship not hit
        server.send(client,check_hit_list)     #check_hit_list = [[coords], didnt hit ship] ||| gui need to check check_hit_list[1]
        ID = get_ID(data[1])
        queue.append(f"{ID};CF;{check_hit_list}")
    print(check_hit_list)

check_hit()