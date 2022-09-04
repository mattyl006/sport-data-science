def which_sector(loc_x,loc_y,areas_x,areas_y):
    #120=x; 80=y
    X = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P']
    Y = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    sector_x = '';
    sector_y = 1;
    
    for i in range (0,areas_x+1):
        if loc_x <= (120/areas_x)*i:
            sector_x = X[i]

    for i in range (0,areas_y):
        if loc_y <= (120/areas_y)*i:
            sector_y = Y[i]
            
    sector = str(sector_x) + str(sector_y)
    
    return sector