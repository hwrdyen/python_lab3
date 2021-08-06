def flip_image(image_array, axis):
    vector = []
    row_number = len(image_array)
    if axis == 0:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[i][row_number-(j+1)][k]
                else:    
                    vector[i][j] = image_array[i][row_number-(j+1)]
                    
    elif axis == 1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[row_number-(i+1)][j][k]
                else:
                    vector[i][j] = image_array[row_number-(i+1)][j]
                
    elif axis == -1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[row_number-(j+1)][row_number-(i+1)][k]
                else:
                    vector[i][j] = image_array[row_number-(j+1)][row_number-(i+1)]
    '''
    if axis == 0:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                for k in range(0,3):
                    vector[i][j].append([])
                    vector[i][j][k] = image_array[i][row_number-(j+1)][k]
    elif axis == 1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                for k in range(0,3):
                    vector[i][j].append([])
                    vector[i][j][k] = image_array[row_number-(i+1)][j][k]
    elif axis == -1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                for k in range(0,3):
                    vector[i][j].append([])
                    vector[i][j][k] = image_array[row_number-(j+1)][row_number-(i+1)][k]'''
                    
                    
                    
    return vector


if __name__ == "__main__":
    image_array1 = [[1,1,0],[0,0,0],[0,0,1]]
    w = flip_image(image_array1, 0)
    print(w)
    e = flip_image(image_array1, 1)
    print(e)
    r = flip_image(image_array1, -1)
    print(r)
    print("\n")
    
    image_array2 = [[[1,0,0],[0,0,1],[0,0,1]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]]]
    q = flip_image(image_array2,0)
    print(q)
    t = flip_image(image_array2, 1)
    print(t)
    y = flip_image(image_array2, -1)
    print(y)
    
