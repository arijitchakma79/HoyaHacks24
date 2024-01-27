import numpy as np
import cv2
import torch

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Cannot open camera")
    exit()
    
midas = torch.hub.load('intel-isl/MiDaS','MiDaS_small')
midas.to('cpu')
midas.eval()

transforms = torch.hub.load('intel-isl/MiDaS','transforms')
transform = transforms.small_transform

while True:
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    imgbatch = transform(gray).to('cpu')
    with torch.no_grad():
        prediction = midas(imgbatch)
        prediction = torch.nn.functional.interpolate(
            prediction.unsqueeze(1),
            size=gray.shape[:2],
            mode='bicubic',
            align_corners=False
        ).squeeze()

    output = prediction.cpu().numpy()

    output_norm = cv2.normalize(output, None, 0, 1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)

    cv2.imshow('Walking',output_norm)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()