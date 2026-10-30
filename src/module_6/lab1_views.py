import csv
import numpy as np
from PIL import Image


def main():
    with open("views.csv", "r", newline="") as views:
        reader = csv.DictReader(views)
        
        with open("analysis.csv", "w", newline="") as analysis: 
            writer = csv.DictWriter(analysis, fieldnames= ["id", "title", "brightness"])
            writer.writeheader()
        
            for row in reader:
                brightness = calculate_brightness(f"{row['id']}.jpeg")
                writer.writerow(
                    {
                        "id": row["id"],
                        "title": row["title"],
                        "brightness": round(brightness, 2)
                    }
                )
    
    
def calculate_brightness(filename):
    with Image.open(filename) as image:
        brightness = np.mean(np.array(image.convert("L"))) / 255
    return brightness


main()