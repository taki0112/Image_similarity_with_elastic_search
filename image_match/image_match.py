from elasticsearch import Elasticsearch
from image_match.elasticsearch_driver import SignatureES
from PIL import Image
from time import time
import os

def folder_make(folder) :
    if not os.path.isdir(folder) :
        os.mkdir(folder)

es = Elasticsearch()
ses = SignatureES(es)
# Start Elastic search server



extensions = (".png", ".jpg", ".jpeg", ".gif")
original_image_folder = "C:/sample_image" # Folder where images are stored, that is, the original image is found here
save_folder = "C:/test/save_folder" # Folder to save the original image of converted images
folder_make(save_folder)

converted_image = "C:/test/modified_image.jpg" # converted image

'''
# If you do not have a file stored on the elasticsearch server, you can run the following code.

for(path, dir, files) in os.walk(original_image_folder) :
    for filename in files :
        path_file = os.path.join(path,filename)
        ext = os.path.splitext(filename)[1] # File extensions
        if ext in extensions :
            if(os.path.getsize(path_fil e) == 0) :
                pass
            else :
                ses.add_image(path_file) # save image to elastic search server
# After saving, this part may not be executed.
'''

s = time()
original_image = ses.search_image(converted_image)
# Original images of the converted image are saved
# If you want to search rotated photos, you can also change sess.search_image (crop_image, all_orientations = True)
# If no options are added, only resize and cropped images are searched.
# However, if you add an option, the search takes a little longer.


elapsed = time() - s # Found in 0.3 ~ 0.7 seconds
print(converted_image)
print(elapsed)
print(len(original_image))
for i in range(len(original_image)) :
    image_path = original_image[i].get('path') # Path to the original image
    # At this time, the similarity value is extracted when "original_image[i].get('score')"
    image_path = image_path.replace('\\','/')
    img = Image.open(image_path).save(save_folder+"/"+image_path.split("/")[-1])





