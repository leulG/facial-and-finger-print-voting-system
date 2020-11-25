from django.shortcuts import get_object_or_404, render
import face_recognition
import cv2
import os
import numpy as np
from acount.models import Account




def facedetaction(request):
    
    video_capture = cv2.VideoCapture(0)
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MEDIA_ROOT = os.path.join(BASE_DIR, 'polls')
    account = get_object_or_404(Account , user = request.user)
    loc = account.profile_pic.url
    loc = (str(MEDIA_ROOT) + loc)
    # Load a sample picture and learn how to recognize it.
    user_image = face_recognition.load_image_file(loc)
    user_face_encoding = face_recognition.face_encodings(user_image)[0]


    # Create arrays of known face encodings and their names
    known_face_encodings = [
        user_face_encoding,
    
    ]

    # Initialize some variables
    face_locations = []
    face_encodings = []
   
    process_this_frame = True
   


        # Grab a single frame of video
    ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
    if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

       
        for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            

                # # If a match was found in known_face_encodings, just use the first one.
            if True in matches:
                #first_match_index = matches.index(True)
                
                return True
            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                
                    
                return True
            
            return False

        process_this_frame = not process_this_frame

    video_capture.release()
    cv2.destroyAllWindows()



    #not accurate

def facedect(request):
    cam = cv2.VideoCapture(0)
    s, img = cam.read()
    if s:

        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        MEDIA_ROOT = os.path.join(BASE_DIR, 'polls')


        account = get_object_or_404(Account , user = request.user)
        loc = account.profile_pic.url
        loc = (str(MEDIA_ROOT) + loc)
        face_1_image = face_recognition.load_image_file(loc)
        face_1_face_encoding = face_recognition.face_encodings(face_1_image)[0]

        #

        small_frame = cv2.resize(img, (0, 0), fx=0.25, fy=0.25)

        rgb_small_frame = small_frame[:, :, ::-1]

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        check = face_recognition.compare_faces(face_1_face_encoding, face_encodings)

        
        if check[0]:
            return True

        else:
            return False


