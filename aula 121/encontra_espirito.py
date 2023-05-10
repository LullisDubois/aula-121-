import cv2

video = cv2.VideoCapture(0)
ret, frame = video.read()
proximo_frame = frame

while True:
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    proximo_frame_gray = cv2.cvtColor(proximo_frame, cv2.COLOR_BGR2GRAY)

    frame_dif = cv2.absdiff(frame_gray, proximo_frame_gray)
    cv2.imshow("se vir espirito nao me culpe", frame_dif)

    if cv2.waitKey(2) == 32:
        break
    
    proximo_frame = frame.copy()
    ret, frame = video.read()

video.release()
cv2.destroyAllWindows()