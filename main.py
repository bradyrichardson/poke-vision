import cvzone
from cvzone.HandTrackingModule import HandDetector
import cv2
import pyautogui as auto

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=2)
while True:
    # Get image frame
    success, img = cap.read()
    hands = False
    if success:
        hands, img = detector.findHands(img, draw=True, flipType=True)
    if hands:
        # Information for the first hand detected
        hand1 = hands[0]  # Get the first hand detected
        lmList1 = hand1["lmList"]  # List of 21 landmarks for the first hand
        bbox1 = hand1["bbox"]  # Bounding box around the first hand (x,y,w,h coordinates)
        center1 = hand1['center']  # Center coordinates of the first hand
        handType1 = hand1["type"]  # Type of the first hand ("Left" or "Right")

        # Count the number of fingers up for the first hand
        fingers1 = detector.fingersUp(hand1)

        fingers2 = False

        # Check if a second hand is detected
        if len(hands) == 2:
            # Information for the second hand
            hand2 = hands[1]
            lmList2 = hand2["lmList"]
            bbox2 = hand2["bbox"]
            center2 = hand2['center']
            handType2 = hand2["type"]

            # Count the number of fingers up for the second hand
            fingers2 = detector.fingersUp(hand2)

        # use a match statement here if using python 3.10 or greater
        if fingers1.count(1) == 1:
            auto.press('up')
        elif fingers1.count(1) == 2:
            auto.press('down')
        elif fingers1.count(1) == 3:
            auto.press('right')
        elif fingers1.count(1) == 4:
            auto.press('left')
        elif fingers1.count(1) == 5:  # start
            auto.press('return')

        if fingers2:
            if fingers2.count(1) == 1:  # a
                auto.press('a')
            elif fingers2.count(1) == 2:  # b
                auto.press('s')
            # elif fingers2.count(1) == 3:  # L
            #     auto.press('a')
            # elif fingers2.count(1) == 4:  # R
            #     auto.press('d')
            elif fingers2.count(1) == 5:  # select
                auto.press('shift')

    cv2.imshow("Image", img)
    if cv2.waitKey(1) == ord('q'):
        cv2.destroyWindow("Image")
        break