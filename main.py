from utils import read_video, save_video
from trackers import Tracker

def main():
    # read video
    video_path = "input_video/challenge-1140_1.mp4"
    video_frames = read_video(video_path)
    print(f"Video frames read from {video_path}")
    # print(f"Total frames read: {len(video_frames)}")
    

    # Initialize Tracker
    tracker = Tracker(model_path="models/best.pt") 
    # Get object tracks
    tracks = tracker.get_object_tracks(video_frames, read_from_stub=True, stub_path="stubs/track_stubs.pkl")

    # Draw output - object tracks
    output_video_frames = tracker.draw_annotations(video_frames=video_frames, tracks=tracks)

    # save video
    save_video(output_video_frames, "output_video/saved_video.mp4")

if __name__ == "__main__":
    main()