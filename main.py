import cv2
import numpy as np

def main():
    video = cv2.VideoCapture('green.mp4')
    image = cv2.imread('sogang.jpg')

    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = video.get(cv2.CAP_PROP_FPS)  # this may be float such as 29.97
    nframes = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    image = cv2.resize(image, (width,height))

    canvas = np.zeros((height, nframes, 3), dtype='uint8')

    recorder = cv2.VideoWriter('chromakey_res.mp4', 
                                cv2.VideoWriter_fourcc(*'MP4V'), 
                                fps, 
                                (nframes, height))

    #for using video we need to make a loop for each frame cutting
    while video.isOpened():
        ret, frame = video.read() 
        if ret == False:
            break

        #change color to HSV for better masking
        #in HSV its easier to select green values  based on hue
        video_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        green_L = np.array([50,150,0]) #from dark green
        green_H = np.array([110, 255, 255]) #to light green

        #create a mask based on low and high values that we set
        mask = cv2.inRange(video_hsv, green_L, green_H)
        #blur the mask to make edges look better
        mask_blurred = cv2.GaussianBlur(mask, (3,3), 0)
        
        #first version
        #copy cut video frame on top of the image based on mask
        #cv2.copyTo(image, mask, frame)
        #cv2.imshow('frame', frame)
        
        #second version
        #convert video back to display colors properly
        video_bgr = cv2.cvtColor(video_hsv, cv2.COLOR_HSV2BGR)
        #create copies based on mask black or white zones
        masked_video = np.copy(video_bgr)
        masked_video[mask_blurred != 0] = [0, 0, 0]
        masked_image = np.copy(image)
        masked_image[mask_blurred == 0] = [0, 0, 0]
        #compile cut versions together
        final = masked_video + masked_image
        cv2.imshow('final', final)

        recorder.write(final)

        if cv2.waitKey(20) == 27: break
    recorder.release()

if __name__ == "__main__":
    main()
