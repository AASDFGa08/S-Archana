# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import csv
def detect_defects(input_json, image_folder, output_csv):
    with open(input_json) as f:
        data = json.load(f)

        

    die_width = data['die_width']
    die_height = data['die_height']
    steer_width = data['steer_width']
    careArea_width = data['careArea_width']
    exclusion_zones = data.get('exclusion_zones', [])
    

    num_frames = data['num_frames']
    num_swaths = data['num_swaths']


    with open(output_csv, 'w', newline='') as f:
        writer = csv.writer(f)

        for frame in range(1, num_frames+1):
            for swath in range(1, num_swaths+1):
                image_filename = f"{image_folder}/wafer_image_{frame:02d}_{swath:02d}.png"
                
                defects = process_image(image_filename, die_width, die_height, steer_width, care_areas, exclusion_zones)
                
                
                for defect in defects:
                    die_index, x_pix, y_pix = defect
                    writer.writerow([die_index, x_pix, y_pix])

def process_image(image_filename, die_width, die_height, steer_width, care_areas, exclusion_zones):
   
    defects = []
    return defects


input_json = 'input.json'
image_folder = 'images'
detect_defects(input_json, image_folder, output_csv)'