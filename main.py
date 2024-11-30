import cv2
from src.detector.object_detector import ObjectDetector

def main():
    # Initialize detector
    detector = ObjectDetector(conf_threshold=0.3)
    
    # Initialize video capture
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        raise RuntimeError("Failed to open webcam")
    
    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Failed to grab frame")
                break
                
            # Process frame
            annotated_frame, results = detector.process_frame(frame)
            
            # Display results
            cv2.imshow("YOLOv5 Live Detection", annotated_frame)
            
            # Break loop on 'q' press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except Exception as e:
        print(f"Error during detection: {str(e)}")
        
    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 