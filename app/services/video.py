import cv2
import time

def start_video_stream():
    print("Initializing camera... Press 'q' in the video window to quit.")
    # 0 is the default ID for your computer's built-in webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    frame_count = 0
    start_time = time.time()

    while True:
        # Read the current frame from the camera
        success, frame = cap.read()
        if not success:
            print("Error: Failed to capture frame.")
            break
        
        frame_count += 1
        elapsed_time = round(time.time() - start_time, 1)
        
        # Add metadata text directly onto the video frame
        cv2.putText(frame, f"Frame: {frame_count} | Time: {elapsed_time}s", (15, 35), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        
        # Open a window to display the live feed
        cv2.imshow("Retail Stream Verification", frame)

        # Listen for the 'q' key to stop the stream
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Clean up and close the camera gracefully
    cap.release()
    cv2.destroyAllWindows()
    print("Video stream safely closed.")

# This allows us to run this file directly from the terminal
if __name__ == "__main__":
    start_video_stream()