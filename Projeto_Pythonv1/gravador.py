import cv2
import numpy as np
import pyautogui
SCREEM_SIZE = (700, 600)
fourcc = cv2.VideoWriter_fourcc(*"test")
out = cv2.VideoWriter("gravacao.avi", fourcc, 20.0, SCREEM_SIZE)

while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)

    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
out.release()
