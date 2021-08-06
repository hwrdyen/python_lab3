def invert_grayscale(image_array):
    vector = []
    row_number = len(image_array)
    for i in range(0,row_number):
        vector.append([])
        for j in range(0,row_number):
            vector[i].append([])
            invert = 255 - image_array[i][j]
            vector[i][j] = invert

    return vector


if __name__ == "__main__":
    image_array1 = [[1,1,0],[0,0,0],[0,0,1]]
    print(invert_grayscale(image_array1))
