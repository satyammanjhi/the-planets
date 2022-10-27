import cv2

img = cv2.imread('solar-system.jpg')

cv2.putText(img,
            "sun",
            (90,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255),)

cv2.putText(img,
            "mercury",
            (110,190),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "venus",
            (190,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "earth",
            (290,170),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "mars",
            (380,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "jupiter",
            (550,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "saturn",
            (750,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "uranus",
            (965,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))

cv2.putText(img,
            "neptune",
            (1110,150)
            ,cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255))
    
cv2.imshow("output",img)
cv2.waitKey(0)