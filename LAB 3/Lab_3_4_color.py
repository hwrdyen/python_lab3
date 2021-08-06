def invert_rgb(image_array):
    vector = []
    row_number = len(image_array)
    for i in range(0,row_number):
        vector.append([])
        for j in range(0,row_number):
            vector[i].append([])
            for k in range(0,3):
                vector[i][j].append([])
                invert = 255 - image_array[i][j][k]
                vector[i][j][k] = invert
    return vector

if __name__ == "__main__":
    image_array1 = [[[1,0,0],[0,0,0],[0,0,1]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]]]
    print(invert_rgb(image_array1))
