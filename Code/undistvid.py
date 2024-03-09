import cv2
import numpy as np

class Undistortion():
    def __init__(self):
        self.calibration_image = {"matrix_k": None, "dist_coefficient": None, "dimension": None}

    def intrinsic_data(self, K, D, dimension):
        self.calibration_image["matrix_k"] = np.array(K)
        self.calibration_image["dist_coefficient"] = np.array(D)
        self.calibration_image["dimension"] = np.array(dimension)

    def process_undistortion(self, frame):
        K = self.calibration_image["matrix_k"]
        D = self.calibration_image["dist_coefficient"]
        width, height = frame.shape[:2]
        new_camera_matrix, _ = cv2.getOptimalNewCameraMatrix(K, D, (width, height), 1, (width, height))
        undistorted_frame = cv2.undistort(frame, K, D, None, new_camera_matrix)
        return undistorted_frame

# Create an instance of the Undistortion class
undistortion = Undistortion()

# Example calibration parameters (replace these with your own)
K = [[1000, 0, 500], [0, 1000, 400], [0, 0, 1]]  # Example camera matrix
D = [0.1, 0.2, 0.0, 0.0]  # Example distortion coefficients
dimension = [800, 600]  # Example resolution

# Load intrinsic parameters
undistortion.intrinsic_data(K, D, dimension)

# Create a VideoCapture object (0 represents the default camera, you can change it if you have multiple cameras)
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Break the loop if there's an issue with capturing frames
    if not ret:
        print("Error reading frame")
        break

    # Undistort the frame
    undistorted_frame = undistortion.process_undistortion(frame)

    # Display the original and undistorted frames
    cv2.imshow('Original Frame', frame)
    cv2.imshow('Undistorted Frame', undistorted_frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
