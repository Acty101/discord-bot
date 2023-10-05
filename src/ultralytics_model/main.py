from ultralytics import YOLO


def main():
    model = YOLO("yolov8n.pt")
    results = model("./data/src/2_people.jpg")
    for result in results:
        boxes = result.boxes  # Boxes object for bbox outputs
        masks = result.masks  # Masks object for segmentation masks outputs
        keypoints = result.keypoints  # Keypoints object for pose outputs
        probs = result.probs
    print(boxes)


if __name__ == "__main__":
    main()
