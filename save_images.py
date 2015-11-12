import numpy as np
import cv2

cap = cv2.VideoCapture(0)

pic_num = 0

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Display the resulting frame
    cv2.imwrite('imgs/' + str(pic_num) + '.png', frame)
    if cv2.waitKey(500) & 0xFF == ord('q'):
        break

    pic_num += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
