import cv2 as cv
"""
Name : luckydipper
team : Visual Recognition
created : 2020.7.8 
purpose : Find ultimate region.
"""

"""
capture = cv.VideoCapture("Video")  # read the video file 

while True:
    check = capture.get(cv.CAP_PROP_POS_FRAMES) == capture.get(cv.CAP_PROP_FRAME_COUNT) # current frame == all frame
    if check : 
        capture.open("Image/Star.mp4")
        
    ret, frame = capture.read()
    cv.imshow("left1",frame[ 150:180 ,60:85 ])
    cv.imshow("left2",frame[ 250:280 ,60:85 ])
    cv.imshow("left3",frame[ 357:385 ,60:85 ])
    cv.imshow("left4",frame[ 460:485 ,60:85 ])
    cv.imshow("left5",frame[ 560:590 ,60:85 ])


    cv.imshow("right1",frame[ 150:180,1835:1860 ])
    cv.imshow("right2",frame[ 250:280,1835:1860 ])
    cv.imshow("right3",frame[ 357:385,1835:1860 ])
    cv.imshow("right4",frame[ 460:485,1835:1860 ])
    cv.imshow("right5",frame[ 560:590,1835:1860 ])
    
    key = cv.waitKey(33)    # analyze 33ms frame
    if key==27:             # Esc key to stop
     break
    
"""

def main() -> None:
    video = cv.imread("test.jpeg")
    cv.imshow("left1", video[150:180, 60:85])
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()

