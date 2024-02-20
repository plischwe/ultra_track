from ultralytics import YOLO

model = YOLO('/yolov8n_openvino_model/')
#model.export(format='openvino')

results = model.track(source=2, tracker='bytetrack.yaml', persist=True, show=True)
