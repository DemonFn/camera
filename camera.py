import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number = random.randint(0,100)
    video_captureobject= cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame = video_captureobject.read()
        img_name="img"+ str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    return img_name
    print("picture has been taken")
    video_captureobject.release()
    cv2.destroyAllWindows()
def upload_file(img_name):
    access_token="sl.BGiEtj42Xgelr4sz5GY1WAw6jVR15A6cG8jjxWsxwiqtophU0xAoSZQ59S08wSWeNpC8EE12dycU8UR9qvYHRyt_mnIAkzlNL6_xh8htNKXOGh_S5mv3pxigL8T3spl59vJsm4gfATO9"
    file=img_name
    filefrom=file
    fileto="/Pictures/"+ (img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(filefrom,"rb")as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("File has been uploaded")
def main():
    while (True):
        if ((time.time()-start_time)>=300):
            name=take_snapshot()
            upload_file(name)
main()


