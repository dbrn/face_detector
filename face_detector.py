# python 3.5+
import cv2
import glob
import argparse


def main():
    face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", nargs=1, type=str, help="Where the faces "
                                                             "are")
    parser.add_argument("scalefactor", nargs=1, type=float)
    parser.add_argument("minneighbors", type=int, nargs=1)
    args = parser.parse_args()
    files = glob.glob(f"{args.directory[0]}/*.jpg")
    for file in files:
        img = cv2.imread(file, 1)
        img_work = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(img_work,
                                              scaleFactor=args.scalefactor[0],
                                              minNeighbors=args.minneighbors[0])
        for face in faces:
            cv2.rectangle(img, (face[0], face[1]), (face[0] + face[2], face[1]
                                                    + face[3]), (0, 255, 0), 3)
            extension = file.rindex(".")
            cv2.imwrite(f"{file[0:extension]}face{file[extension:]}", img)


if __name__ == "__main__":
    main()
