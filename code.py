import face_recognition
import numpy as np
from PIL import Image, ImageDraw
from IPython.display import display

class Model():
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []
        # TODO: Storage Alternatives

    def train_image(self, image_path, name):
        new_person = face_recognition.load_image_file(image_path)
        new_person_encoding = face_recognition.face_encodings(new_person)[0]

        self.known_face_encodings.append(new_person_encoding)
        self.known_face_names.append(name)
        print("Training Complete for image of {}".format(name))
        
        # TODO: Storage Alternatives

    def draw_rectangle(self, draw, left, top, right, bottom, name):
        # Draw a box around the face using the Pillow module
        draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

        # Draw a label with a name below the face
        text_width, text_height = draw.textsize(name)
        draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
        draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))
        
    def predict_image(self, image_path, print_image = True):
        unknown_image = face_recognition.load_image_file(image_path)

        face_locations = face_recognition.face_locations(unknown_image)
        face_encodings = face_recognition.face_encodings(unknown_image, face_locations)
        
        if print_image:
            pil_image  = Image.fromarray(unknown_image)
            draw = ImageDraw.Draw(pil_image)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
            name = "Unknown"

            # Or instead, use the known face with the smallest distance to the new face
            face_distances = face_recognition.face_distance(self.known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]
            if print_image:
                self.draw_rectangle(draw, left, top, right, bottom, name)

        if print_image:
            del draw
            pil_image.save("result.jpg")

facial_rec = Model()
facial_rec.train_image(image_path = "mam.jpg", id= 1)
facial_rec.predict_image(image_path = "ham.jpg", print_image = True)