from utils import read_video, save_video

def main():
    # read video
    video_path = "input_video/challenge-1140_1.mp4"
    video_frames = read_video(video_path)
    print(f"Total frames read: {len(video_frames)}")
    # save video
    save_video(video_frames, "output_video/saved_video.mp4")

if __name__ == "__main__":
    main()