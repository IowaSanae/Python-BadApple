import cv2 as cv
import reader
import os

def main():
    try:
        video = cv.VideoCapture("bad_apple.mp4")
        reader.video_reader(video, 400, 250)
    except Exception as e:
        print("Either the video ends or an error occured: " + str(e))
    finally:
        video.release()
        cv.destroyAllWindows()

if __name__ == "__main__":
    main()