import numpy as np
import argparse
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to the image")
args = vars(ap.parse_args())

# load the image
image = cv2.imread(args["image"])
image = cv2.resize(image, (720, 480))

# define the list of boundaries for yellow, green, red, and blue colors in HSV
boundaries = [
    ([20, 100, 100], [30, 255, 255]),  # yellow in HSV
    ([40, 40, 40], [80, 255, 255]),    # green in HSV
    ([0, 70, 50], [10, 255, 255]),     # red in HSV (lower range)
    ([170, 70, 50], [180, 255, 255]),  # red in HSV (upper range)
    ([100, 150, 0], [140, 255, 255])   # blue in HSV
]

# convert the image from BGR to HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# loop over the boundaries
for (lower, upper) in boundaries:
    # create NumPy arrays from the boundaries
    lower = np.array(lower, dtype="uint8")
    upper = np.array(upper, dtype="uint8")
    
    # find the colors within the specified boundaries and apply the mask
    mask = cv2.inRange(hsv_image, lower, upper)
    output = cv2.bitwise_and(image, image, mask=mask)
    
    # show the images
    cv2.imshow("images", np.hstack([image, output]))
    cv2.waitKey(0)

cv2.destroyAllWindows()
