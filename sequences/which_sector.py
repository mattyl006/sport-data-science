def which_sector(loc_x,loc_y,areas_x,areas_y):
    #120=x; 80=y
    X = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    Y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    
    sector_x = '';
    sector_y = 1;
    
    for i in range (0,areas_x+1):
        if loc_x <= (120/areas_x)*i and loc_x > (120/areas_x)*(i-1):
            sector_x = X[i-1]

    for i in range (0,areas_y+1):
        if loc_y <= (80/areas_y)*i and loc_y > (80/areas_y)*(i-1):
            sector_y = Y[i-1]
            
    sector = str(sector_x) + str(sector_y)
    
    return sector
