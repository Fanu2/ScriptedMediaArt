# Import required libraries
from vidgear.gears import VideoGear
import numpy as np
import cv2

def main():
    # Open any valid video stream with stabilization enabled (`stabilize = True`)
    stream_stab = VideoGear(source="/home/jasvir/Pictures/fanu/2.mp4", stabilize=True).start()

    # Open the same stream without stabilization for comparison
    stream_org = VideoGear(source="/home/jasvir/Pictures/fanu/2.mp4").start()

    # Loop over
    while True:
        # Read stabilized frames
        frame_stab = stream_stab.read()

        # Check for stabilized frame if NoneType
        if frame_stab is None:
            break

        # Read un-stabilized frame
        frame_org = stream_org.read()

        # Check for un-stabilized frame if NoneType
        if frame_org is None:
            break

        # Concatenate both frames
        output_frame = np.concatenate((frame_org, frame_stab), axis=1)

        # Put text over concatenated frame
        cv2.putText(
            output_frame,
            "Before",
            (10, output_frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )
        cv2.putText(
            output_frame,
            "After",
            (output_frame.shape[1] // 2 + 10, output_frame.shape[0] - 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.6,
            (0, 255, 0),
            2,
        )

        # Show output window
        cv2.imshow("Stabilized Frame", output_frame)

        # Check for 'q' key if pressed
        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    # Close output window
    cv2.destroyAllWindows()

    # Safely close both video streams
    stream_org.stop()
    stream_stab.stop()

if __name__ == "__main__":
    main()
