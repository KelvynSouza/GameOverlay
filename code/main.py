import cv2
import Helpers.image_ocr_helper as ocr_helper
from util import image_textarea_contour

image_local = '../Support/ImagesTest/In_Game_Image_edited.jpg'
image = cv2.imread(image_local)

if __name__ == '__main__':
    image_refined = image_textarea_contour.captch_ex(image_local)
    result = ocr_helper.get_characters_to_string(image_refined)
    print(result)
    cv2.imshow('img', image_refined)
    cv2.waitKey(0)

