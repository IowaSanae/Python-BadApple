import cv2 as cv
import os
import time
from pygame import mixer


def video_reader(video: cv.VideoCapture, console_width: int, console_height: int) -> None:
    # Define the character list
    character_list = [" ", ".", ",", "-", "~",
                      ":", ";", "=", "!", "*", "#", "$", "@"]

    # Define the desired output width and height (in characters)
    output_width, output_height = console_width // 6, console_height // 10

    # Set the console height and width
    os.system(f"mode con cols={console_width} lines={console_height}")

    while True:
        ret, frame = video.read()

        # Show the original video (as a reference)
        cv.imshow("Video", frame)

        if not ret:
            break

        # Convert frame to grayscale and resize it
        frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame_gray = cv.resize(frame_gray, (output_width, output_height))

        # Map each pixel to a corresponding character based on its brightness
        frame_chars = []
        for row in range(output_height):
            row_chars = ""
            for col in range(output_width):
                brightness = frame_gray[row, col]
                char_index = int(brightness / 255 * (len(character_list) - 1))
                row_chars += character_list[char_index]
            frame_chars.append(row_chars)

        # Print the frame to the console
        os.system("cls")
        print("\n".join(frame_chars))

        if cv.waitKey(1) == ord('q'):
            break


def audio_player(audio_file: str) -> None:
    mixer.init()
    mixer.music.load(audio_file)
    mixer.music.play()