def get_sectors_vector(seq):
    list = []
    vectors = []
    areas = []
    for s in seq:
        areas = s['area_code']
        # print(areas)
        for i in areas:
            if len(i) > 1:
                list.append(i) 
        # print(list) 
        vectors.append(list)
        list = []

    return vectors

