
import cv2
import numpy as np
import math


#  Read Input Image 
input_image = cv2.imread('file-20181107-74757-1nzaxpf.jpg') 
input_image = np.uint8(input_image)
 

def sobelmain(input_image):
#  Convert the truecolor RGB image to the grayscale image 

    input_image = cv2.cvtColor(input_image, cv2.COLOR_BGR2GRAY) 
    cv2.imwrite('yo.jpg',input_image)
# % Pre-allocate the filtered_image matrix with zeros

    filtered_image = np.zeros(np.shape(input_image))

# % Sobel Operator Mask 

    Mx = ([-1 ,0 ,1],   #
      [-2 ,0 ,2],
      [-1, 0, 1])

    My = ([-1 ,-2 ,-1], 
      [0 ,0, 0],
      [1 ,2 ,1]) 

    Mx=np.asarray(Mx)

    My=np.asarray(My)
# Edge Detection Process 
# When i = 0 and j = 0, then filtered_image pixel 
# position will be filtered_image(2, 2) 
# The mask is of 3x3, so we need to traverse 
# to filtered_image(size(input_image, 1) - 2 
#  size(input_image, 2) - 2) 
# Thus we are not considering the borders. 

    sq = lambda i:i**2 #vectorizedfunction to square each element in the matrix
    sq_f = np.vectorize(sq)
    for i in range(0,np.shape(input_image)[0] - 2):
        for j in range(0,np.shape(input_image)[1] - 2):

# 		% Gradient approximations 
            Gx = np.sum(np.sum(np.multiply(Mx,input_image[i:i+3,j:j+3])))
            Gy = np.sum(np.sum(np.multiply(My,input_image[i:i+3,j:j+3]))) 
				
# 		% Calculate magnitude of vector 
            filtered_image[i][j] = math.sqrt(sq_f(Gx)+sq_f(Gy))
		
        filtered_image = np.uint8(filtered_image)

    input_copy = cv2.imread('file-20181107-74757-1nzaxpf.jpg')


# % Define a threshold value 
    thresh = 100
    output_image= cv2.threshold(filtered_image, thresh, 255, cv2.THRESH_BINARY)[1]

    cv2.imshow('image',input_copy)
    cv2.imshow('Filtered Image',filtered_image)
    cv2.imwrite('filtered_image.jpg',filtered_image)
    cv2.imshow('edge detacted pic',output_image)
    cv2.imwrite('edge_detected_image.jpg',output_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

sobelmain(input_image)
