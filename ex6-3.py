import json
import zipfile
import tkinter as tk
from tkinter import Canvas

class FullBodyVisualizer:
    def __init__(self, root, canvas_width, canvas_height):
        self.root = root
        self.root.title("Full Body Animation")
        
        self.canvas = Canvas(root, width=canvas_width, height=canvas_height)
        self.canvas.pack()

    def read_keypoints_from_json(self, json_file):
        with open(json_file, 'r') as f:
            data = json.load(f)
        return data['people']

    def draw_full_body(self, person_data, color):
        
        links = [
            [17, 15], [15, 0], [16, 0], [16, 18], [0, 1], [1, 2], [2, 3], [3, 4],
            [1, 5], [5, 6], [6, 7], [1, 8], [8, 9], [9, 10], [10, 11], [11, 24],
            [11, 22], [22, 23], [8, 12], [12, 13], [13, 14], [14, 21], [14, 19], [19, 20]
        ]

        keypoints = person_data["pose_keypoints_2d"]
        for link in links:
            start_point = (int(keypoints[link[0] * 3])/2, int(keypoints[link[0] * 3 + 1])/2)
            end_point = (int(keypoints[link[1] * 3])/2, int(keypoints[link[1] * 3 + 1])/2)

            
            if start_point[0] > 0 and start_point[1] > 0 and end_point[0] > 0 and end_point[1] > 0:
                self.canvas.create_line(start_point, end_point, fill=color, width=2)

    def load_and_draw(self, zip_file_path, json_file_path, person_indices, colors):
        with zipfile.ZipFile(zip_file_path) as zip_f:
            with zip_f.open(json_file_path) as file:
                data = json.load(file)

        people_data = data["people"]

        for person_index, color in zip(person_indices, colors):
            if person_index < len(people_data):
                self.draw_full_body(people_data[person_index], color)

if __name__ == "__main__":
    root = tk.Tk()
    
    visualizer = FullBodyVisualizer(root, canvas_width=1500, canvas_height=1000)
    for frame in range(100):  
        visualizer.canvas.delete("all")  
        visualizer.load_and_draw('kabeposter.zip', f'kabeposter/kabeposter_000000000{frame:03d}_keypoints.json', person_indices=[0, 1], colors=["black", "black"])
        visualizer.root.update() 
        visualizer.root.after(100)

    root.mainloop()