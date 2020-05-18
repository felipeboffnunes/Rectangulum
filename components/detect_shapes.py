import cv2
import numpy as np


def detect_shapes(pil_image, visual=False):
    opencvImage = cv2.cvtColor(np.array(pil_image), cv2.COLOR_BGR2GRAY)

    thresh_inv = cv2.threshold(opencvImage, 0, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)[1]

    # Blur the image
    blur = cv2.GaussianBlur(thresh_inv,(1,1),0)

    thresh = cv2.threshold(blur, 0, 10, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]

    # find contours
    contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    mask = np.ones(opencvImage.shape[:2], dtype="uint8") * 255

    coordinates = []
    for c in contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)
        if w*h>1000:
            cv2.rectangle(mask, (x, y), (x+w, y+h), (0, 0, 255), -1)
            coordinates.append([x,y,w,h])

    res_final = cv2.bitwise_and(opencvImage, opencvImage, mask=cv2.bitwise_not(mask))
    mask_r = ResizeWithAspectRatio(mask, height=1000)
    final_r = ResizeWithAspectRatio(res_final, height=1000) 
    if visual:
        print(coordinates)
        cv2.imshow("boxes", mask_r)
        cv2.imshow("final image", final_r)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return coordinates

def ResizeWithAspectRatio(image, width=None, height=None, inter=cv2.INTER_AREA):
    dim = None
    (h, w) = image.shape[:2]

    if width is None and height is None:
        return image
    if width is None:
        r = height / float(h)
        dim = (int(w * r), height)
    else:
        r = width / float(w)
        dim = (width, int(h * r))

    return cv2.resize(image, dim, interpolation=inter)