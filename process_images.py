from PIL import Image
import os

pictures_dir = r"d:\GitHub Desktop\LiuYuxin-Hi.github.io-main\LiuYuxin-Hi.github.io\pictures"

software_images = ['ArcMap.png', 'CiteSpace.png', 'NVivo.jpg', 'Origin.png', 'SPSS.png', 'SmartPLS.png', 'Zotero.png', 'stata.jpg']

for img_name in software_images:
    img_path = os.path.join(pictures_dir, img_name)
    if os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.convert('RGBA')

        # Get pixel data
        datas = img.getdata()
        new_data = []
        for item in datas:
            # White or near-white background -> transparent
            if item[0] > 240 and item[1] > 240 and item[2] > 240:
                new_data.append((255, 255, 255, 0))  # Transparent
            else:
                new_data.append(item)

        img.putdata(new_data)

        # Save as PNG
        base_name = os.path.splitext(img_name)[0]
        new_path = os.path.join(pictures_dir, base_name + '.png')
        img.save(new_path, 'PNG')
        print(f"Processed: {img_name} -> {base_name}.png")

print("Done!")
