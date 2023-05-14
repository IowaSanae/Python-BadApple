import cv2 as cv
from threading import Thread
from reader import video_reader, audio_player


def main():
    try:
        video = Thread(target=video_reader, args=(cv.VideoCapture("bad_apple.mp4"), 400, 250))
        audio = Thread(target=audio_player, args=("bad_apple.mp3",))
        video.start()
        audio.start()
        video.join()
        audio.join()
    except Exception as e:
        print("Either the video ends or an error occured: " + str(e))
    finally:
        video.release()
        cv.destroyAllWindows()


if __name__ == "__main__":
    main()
