#line detection
import cv2 as cv
import numpy as np
img=cv.imread("E://openCV_images/road.png")
cv.imshow("original_image",img)

edges=cv.Canny(img,50,150)
lines=cv.HoughLines(edges,#input image
                    1,#distance resolution in pixels
                    np.pi/180,#angle resoltion in radians
                    170)
for line in lines:
    rho,theta=line[0]
    a=np.cos(theta)
    b=np.sin(theta)
    x0=a*rho
    y0=b*rho
    x1=int(x0+1000*(-b))
    y1=int(y0+1000*(a))
    x2=int(x0-1000*(-b))
    y2=int(y0-1000*(a))
    #draw a line
    line=cv.line(img,(x1,y1),(x2,y2),(255,0,0),2)

cv.imshow("lines",line)
cv.waitKey(0)
cv.destroyAllWindows()