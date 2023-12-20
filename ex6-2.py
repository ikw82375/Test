import json
import zipfile
import tkinter as tk
from tkinter import Canvas

class ShoulderLineVisualizer:
    def __init__(self, root, canvas_width, canvas_height):
        self.root=root
        self.root.title("Shoulder Lines")
        
        self.canvas=Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

    def read_keypoints_from_json(self, json_file):
        with open(json_file, 'r') as f:
            data=json.load(f)
        return data['people']

    def draw_shoulder_line(self, person_data, color):
        shoulder=[
            int(person_data["pose_keypoints_2d"][6]), int(person_data["pose_keypoints_2d"][7]),
            int(person_data["pose_keypoints_2d"][3]), int(person_data["pose_keypoints_2d"][4]),
            int(person_data["pose_keypoints_2d"][15]), int(person_data["pose_keypoints_2d"][16])
        ]
        self.canvas.create_line(shoulder[0], shoulder[1], shoulder[2], shoulder[3], fill=color, width=2)
        self.canvas.create_line(shoulder[2], shoulder[3], shoulder[4], shoulder[5], fill=color, width=2)

    def load_and_draw(self, zip_file_path, json_file_path, person_index, color):
        with zipfile.ZipFile(zip_file_path) as zip_f:
            with zip_f.open(json_file_path) as file:
                data=json.load(file)

        people_data=data["people"]
        self.draw_shoulder_line(people_data[person_index], color)

if __name__ == "__main__":
    root = tk.Tk()
    
    visualizer=ShoulderLineVisualizer(root, canvas_width=1500, canvas_height=1000)
    visualizer.load_and_draw('kabeposter.zip', 'kabeposter/kabeposter_000000000000_keypoints.json', person_index=0, color="green")
    visualizer.load_and_draw('kabeposter.zip', 'kabeposter/kabeposter_000000000000_keypoints.json', person_index=1, color="pink")

    root.mainloop()