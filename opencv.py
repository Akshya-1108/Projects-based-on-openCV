import cv2 as cv

def resolution(width,height):
    cat.set(3,width)
    cat.set(3,height)

def resize(frame , scale = 0.75):
    width = int(frame.shape[0] * scale)
    height = int(frame.shape[1] * scale)
    
    dimension = (height, width)
    
    return cv.resize(frame , dimension , interpolation=cv.INTER_AREA)

# img = cv.imread('opencv/Screenshot 2024-03-14 144521.png')

# cv.imshow('Me',img)

# cv.waitKey(0)


cat = cv.VideoCapture('opencv/854982-hd_1280_720_25fps.mp4')

while True:
    isTrue, frame = cat.read()
    
    frame_resized = resize(frame,scale=.2)
    
    cv.imshow("cat", frame_resized)
    cv.imshow("cat", frame)
    
    if cv.waitKey(20) and 0xFF == ord('d'):
        break
    
cat.release()
cv.destroyAllWindows()
