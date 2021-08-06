def rgb_to_grayscale(rgb_image_array):
    vector = []
    row_number = len(rgb_image_array)
    for i in range(0,row_number):
        vector.append([])
        for j in range(0,row_number):
            vector[i].append([])
            for k in range(0,3):
                if k == 0:
                    q = 0.2989*(rgb_image_array[i][j][k])
                elif k == 1:
                    w = 0.5870*(rgb_image_array[i][j][k])
                elif k == 2:
                    r = 0.1140*(rgb_image_array[i][j][k])
            vector[i][j] = q+w+r
            
    return vector


if __name__ == "__main__":
    image_array1 = [[[1,0,0],[0,0,0],[0,0,1]],[[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[1,0,0]]]
    print(rgb_to_grayscale(image_array1))
