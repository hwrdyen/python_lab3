def rotate_90_degrees(image_array, direction):
    vector = []
    row_number = len(image_array)
    
    if direction == -1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[j][row_number-(i+1)][k]
                else:
                    vector[i][j] = image_array[j][row_number-(i+1)]
    
    elif direction == 1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[row_number-(j+1)][i][k]
                else:
                    vector[i][j] = image_array[row_number-(j+1)][i]
    '''            
    if direction == -1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                for k in range(0,3):
                    vector[i][j].append([])
                    vector[i][j][k] = image_array[j][row_number-(i+1)][k]
    if direction == 1:
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                for k in range(0,3):
                    vector[i][j].append([])
                    vector[i][j][k] = image_array[row_number-(j+1)][i][k]'''

    return vector


if __name__ == "__main__":
    image_array1 = [[1,0,0],[0,0,0],[1,0,0]]
    a = rotate_90_degrees(image_array1, -1)
    print(a)
    z = rotate_90_degrees(image_array1, 1)
    print(z)
    print("\n")
    
    image_array2 = [[[1,0,0],[0,0,0],[0,0,1]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]]]
    q = rotate_90_degrees(image_array2, -1)
    print(q)
    l = rotate_90_degrees(image_array2, 1)
    print(l)
