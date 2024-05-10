import cv2
import mediapipe as mp
import os
from fastapi import UploadFile, HTTPException

# Machine Learning Operations

mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh

def process_image(file_path: str):
    image = cv2.imread(file_path)
    if image is None:
        raise HTTPException(status_code=400, detail=f"Error: Cannot Load Image from: {file_path}")

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Face Detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.5)
    results = face_detection.process(image_rgb)

    if results.detections:
        print("Face Detected.")
        for detection in results.detections:
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, _ = image.shape
            bbox = (
                int(bboxC.xmin * iw),
                int(bboxC.ymin * ih),
                int(bboxC.width * iw),
                int(bboxC.height * ih)
            )

            cropped_face = image[bbox[1]:bbox[1] + bbox[3], bbox[0]:bbox[0] + bbox[2]]

            # Facial Landmarks Detection
            face_mesh = mp_face_mesh.FaceMesh()
            results_mesh = face_mesh.process(image_rgb)

            face_landmarks = []
            if results_mesh.multi_face_landmarks:
                for face_landmark in results_mesh.multi_face_landmarks:
                    for landmark in face_landmark.landmark:
                        x, y = int(landmark.x * iw), int(landmark.y * ih)
                        face_landmarks.append((x, y))

            # Cleanup mediapipe resources
            face_mesh.close()

            print("Processing...")
            return cropped_face, face_landmarks
    else:
        raise HTTPException(status_code=400, detail="No face detected.")
