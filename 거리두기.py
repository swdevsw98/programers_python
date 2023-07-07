def solution(places):    
    return [check(place) for place in places]
    # return check(places[0])

def check(place):
    for idx_row, row in enumerate(place):
        for idx_col, cell in enumerate(row):
            # print(idx_row, idx_col)
            if cell != 'P' :
                continue
            
            #거리 1
            if idx_col <= 3:
                if place[idx_row][idx_col+1] == 'P':
                    return 0
                
            if idx_row <= 3:
                if place[idx_row+1][idx_col] == 'P':
                    return 0
                
            if idx_col <=3 and idx_row <=3:
                if place[idx_row+1][idx_col+1] == 'P':
                    if place[idx_row+1][idx_col] != 'X' or place[idx_row][idx_col+1] != 'X':
                        return 0
            
            if idx_col >= 1 and idx_col <= 4 and idx_row <= 3:
                if place[idx_row+1][idx_col-1] == 'P':
                    if place[idx_row+1][idx_col] != 'X' or place[idx_row][idx_col-1] != 'X':
                        return 0
                    
            #거리2
            if idx_col <= 2:
                if place[idx_row][idx_col+2] == 'P':
                    if place[idx_row][idx_col+1] != 'X':
                        return 0
            if idx_row <=2:
                if place[idx_row+2][idx_col] == 'P':
                    if place[idx_row+1][idx_col] != 'X':
                        return 0
    return 1

    
        
        