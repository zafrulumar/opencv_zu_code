import cv2

cap = cv2.VideoCapture(1)

tracker = cv2.TrackerMOSSE_create()
success , frame = cap.read()
bbox = cv2.selectROI("Tracking", frame, False)
tracker.init(frame, bbox)

def drawBox(img, bbox):
    x,y,w,h = int(bbox[0]), int(bbox[1]), int(bbox[2]), int(bbox[3])
    cv2.rectangle(frame, (x, y), ((x+w, y+h)), (255,0,255),3,1)
    cv2.putText(frame , 'Tracking', (6, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255,0,0), 2)

while True:

    timer = cv2.getTickCount()

    success , frame = cap.read()
    success, bbox = tracker.update(frame)

    if success:
        drawBox(frame, bbox)
    else:
        cv2.putText(frame , 'Loss', (6, 45), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)

    fps = cv2.getTickFrequency() / ( cv2.getTickCount() - timer )

    cv2.putText(frame , 'FPS -> '+str(int(fps)), (6, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255), 2)
    cv2.imshow('Image Tracking', frame)

    if cv2.waitKey(1) & 0xff == ord('q'):
        break