import os
from PIL import Image
dir_img = "C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\mine\\"
dir_save = "C:\\Users\\wkn_4\\Pictures\\Rock-Paper-Scissors\\mine_resize\\"

size = (75,100)
list_img = os.listdir(dir_img)
 
#将图片修改为指定尺寸
for img_name in list_img:
    img_path = dir_img + img_name
    old_image = Image.open(img_path)
    save_path = dir_save+img_name
    old_image.resize(size, Image.ANTIALIAS).save(save_path)
