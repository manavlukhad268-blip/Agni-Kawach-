import cv2
import numpy as np

def process_image(image_path):
    # Load image using OpenCV
    image = cv2.imread(image_path)
    if image is None:
        print("Error: Could not load image.")
        return
    
    # Placeholder logic for Fire & Hazard Detection (Safe vs Unsafe)
    # In full implementation, YOLOv8 model processes this frame.
    print("Processing image for Agni Kawach safety check...")
    
    # Example logic simulation
    is_hazard = False # Set based on detection results
    
    if is_hazard:
        print("UNSAFE FIRE DETECTED! Triggering siren.")
    else:
        print("Scene is Safe (Controlled Activity / Cooking).")

if __name__ == "__main__":
    print("Agni Kawach Backend Initialized.")


opencv-python==4.8.1.78
numpy==1.26.4
ultralytics==8.1.0
flask==3.0.0
