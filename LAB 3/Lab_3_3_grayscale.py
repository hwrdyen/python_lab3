def crop(image_array,direction,n_pixels):
    vector = []
    row_number = len(image_array)
    output_row_number = (row_number)-(n_pixels)
    if direction == "left":
        for i in range(0, row_number):
            vector.append([])
            for j in range(0,(output_row_number)):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[i][(n_pixels)+j][k]
                else:
                    vector[i][j] = image_array[i][n_pixels+j]
    
    elif direction == "right":
        for i in range(0,row_number):
            vector.append([])
            for j in range(0,(output_row_number)):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[i][j][k]
                else:
                    vector[i][j] = image_array[i][j]
            
    elif direction == "up":
        for i in range(0,(output_row_number)):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[(n_pixels)+i][j][k]
                else:
                    vector[i][j] = image_array[(n_pixels)+i][j]

    elif direction == "down":
        for i in range(0,output_row_number):
            vector.append([])
            for j in range(0,row_number):
                vector[i].append([])
                if image_array[i][j] == list:
                    for k in range(0,3):
                        vector[i][j].append([])
                        vector[i][j][k] = image_array[i][j][k]
                else:
                    vector[i][j] = image_array[i][j]

                
    return vector

if __name__ == "__main__":
    image_array1 = [[1,0,0],[0,0,0],[0,0,1]]
    print(crop(image_array1, "left",2))
    print(crop(image_array1, "right",2))
    print(crop(image_array1, "up",2))
    print(crop(image_array1, "down",2))
    print("\n")
    
    image_array2 = [[1,1,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
    print(crop(image_array2, "left",2))
    print(crop(image_array2, "right",2))
    print(crop(image_array2, "up",2))
    print(crop(image_array2, "down",2))
    print("\n")
    
    image_array3 = [[1,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,1]]
    print(crop(image_array3, "left",2))
    print(crop(image_array3, "right",2))
    print(crop(image_array3, "up",2))
    print(crop(image_array3, "down",2))
    print("\n")

    image_array4 = [[[1,0,0],[0,0,0],[0,0,1]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]]]
    print(crop(image_array4, "left",2))
    print(crop(image_array4, "right",2))
    print(crop(image_array4, "up",2))
    print(crop(image_array4, "down",2))
    print("\n")
    
