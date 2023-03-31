from ultralytics import YOLO
import cv2
import cvzone
import math
import em

def main():
	model = YOLO("yolov8n.pt")
	cap = cv2.VideoCapture(0)
	cap.set(3,1280)
	cap.set(4,720)
	classnames = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light', 'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow', 'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee', 'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard', 'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple', 'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch', 'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone', 'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear', 'hair drier', 'toothbrush']
	flag=1
	while True:
		success,img = cap.read()
		results = model(img,stream=True)
		for r in results:
			boxes = r.boxes
			for box in boxes:
				bbox = box.xyxy[0]
				bbox = list(map(int,bbox))
				bbox[2]=bbox[2]-bbox[0]
				bbox[3]=bbox[3]-bbox[1]
				conf = math.ceil((box.conf[0]*100))/100
				clss = classnames[(int(box.cls[0]))]
				if clss=="person" and conf>0.8:
					cvzone.cornerRect(img, bbox, l=30, t=5, rt=1, colorR=(255, 0, 255), colorC=(0, 255, 0))
					cvzone.putTextRect(img, f"Conf: {conf}", (max(0,bbox[0]),max(35,bbox[1]-20)), scale=3, thickness=3, colorT=(255, 255, 255),colorR=(255, 0, 255), font=cv2.FONT_HERSHEY_PLAIN, offset=10, border=None, colorB=(0, 255, 0))
					flag=0
					cv2.imwrite("caught.jpg",img)

		cv2.imshow("Image",img)
		if flag==0:
			em.notify("caught")
			break
		if (cv2.waitKey(1) & 0xFF==ord("q")):
			break

	cap.release()




main()