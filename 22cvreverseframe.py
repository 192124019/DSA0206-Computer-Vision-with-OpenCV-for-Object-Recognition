import cv2

def reverse_video(input_path, output_path):
    cap = cv2.VideoCapture(input_path)

    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(5)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

    frames = []
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.insert(0, frame) 

    for frame in frames:
        cv2.imshow("Reversed Video", frame)
        cv2.waitKey(int(1000 / fps))
        out.write(frame)

    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    input_video_path = "C:/Users/USER/Downloads/Wildlife Windows 7 Sample Video.mp4"
    output_video_path = "output video.mp4"

    reverse_video(input_video_path, output_video_path)
