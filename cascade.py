import cv2
import glob

HAAR_FILE = "haarcascade_frontalface_alt.xml"
cascade = cv2.CascadeClassifier(HAAR_FILE)

load_img_list = []
face_cut = []
count = 0
# 出力ディレクトリパス
output_path = "./data/cascade/output/"
# 入力ディレクトリパス
img_list = glob.glob("./data/cascade/input/*")

for img in img_list:
    load_img_list.append(cv2.imread(img))

for load_img in load_img_list:
    face_rects = cascade.detectMultiScale(load_img)
    print(face_rects)
    if (len(face_rects) != 0):
        for face_rect in face_rects:
            x = face_rect[0]
            y = face_rect[1]
            w = face_rect[2]
            h = face_rect[3]
            face_cut = load_img[y:y + h, x:x + w]
            face_cut = cv2.resize(face_cut, dsize=(256, 256))
            img_name = output_path + str(count) + ".jpg"
            cv2.imwrite(img_name, face_cut)
            count += 1
    else:
        pass