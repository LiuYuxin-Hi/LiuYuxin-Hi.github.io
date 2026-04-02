from PIL import Image
import math

img_path = r"d:\GitHub Desktop\LiuYuxin-Hi.github.io-main\LiuYuxin-Hi.github.io\pictures\SmartPLS.png"
img = Image.open(img_path).convert('RGBA')
width, height = img.size

# Get pixel data
datas = img.getdata()
new_data = []

# Calculate center and radius of the circle
center_x = width // 2
center_y = height // 2
# Radius is approximately half of the smaller dimension
radius = min(width, height) // 2 - 5  # slight padding

for y in range(height):
    for x in range(width):
        idx = y * width + x
        item = datas[idx]

        # Calculate distance from center
        dist = math.sqrt((x - center_x)**2 + (y - center_y)**2)

        # If outside the circle and white, make transparent
        if dist > radius:
            # White or near-white background -> transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)
        else:
            # Inside circle, keep original
            new_data.append(item)

img.putdata(new_data)
img.save(img_path, 'PNG')
print("SmartPLS.png processed - circular transparent background applied")
