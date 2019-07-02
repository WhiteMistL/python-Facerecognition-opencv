import face_recognition
import os
#建立可识别的列表
#后期将列表名单和图传到数据库进行保存，要用的时候再从数据库中拿出并给list循环赋值使用
Peoplelist = []
peoplelist=[]
def Reading():
    Peoplelist = os.listdir("Material bank")
    for i in Peoplelist:
        peoplelist.append(os.path.splitext(i)[0])


#根据列表转化为流
known_face_encodings=[]
known_face_names=[]
#直接在change函数中从数据库获取name并加进peoplelist
def change():
    for name in peoplelist:
       known_face_names.append(name)
       image=face_recognition.load_image_file("Material bank\\%s.jpg"%name)
       known_face_encodings.append(face_recognition.face_encodings(image)[0])



