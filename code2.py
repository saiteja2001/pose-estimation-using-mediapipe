import mediapipe as mp
import cv2
mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils
cam = cv2.VideoCapture("video_2.mp4")
output=cv2.VideoWriter("output2.mp4",cv2.VideoWriter_fourcc(*'mpv4'),10,(700,500))
while(cam.isOpened()):
    _,frame = cam.read()

    if _ == True:
        imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(imgRGB)
        # print(results.pose_landmarks)
        mpDraw.draw_landmarks(frame, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        frame = cv2.resize(frame,(700,500))
        cv2.imshow("video",frame)
        output.write(frame)
        key=cv2.waitKey(1)&0xFF
        if key==ord('q'):
            break
    else:
        break
cam.release()
output.release()
cv2.destroyAllWindows()