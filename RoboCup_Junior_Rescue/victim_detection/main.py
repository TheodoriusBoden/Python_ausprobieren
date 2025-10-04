from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml") # built a new model from scratch

# Use the model
results = model.train(data="/home/ag/Dokumente/GitHub/Python_ausprobieren/RoboCup_Junior_Rescue/victim_detection/config.yaml", epochs = 1) # train the model
