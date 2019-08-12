import cv2

def main():
    
    windowName = "Live Webcam Video Feed Capture"
    cv2.namedWindow(windowName)
    
    cap = cv2.VideoCapture(0)
    
    filename = 'C:\\Users\\win10\\Desktop\\opencv\\Output.avi'
    codec = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    framerate = 30
    resolution = (640, 480)
    
    VideoFileOutput = cv2.VideoWriter(filename, codec, framerate, resolution)
    
    if cap.isOpened():
        ret, frame = cap.read()
    else:
        ret = False

    while ret:
    
        ret, frame = cap.read()
        
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        VideoFileOutput.write(frame)
        
        cv2.imshow(windowName, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()    
    VideoFileOutput.release()
    cap.release()

if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------------------------------------------------------------------
# import cv2
# import numpy as np
 
# # Create a VideoCapture object
# cap = cv2.VideoCapture(0)
 
# # Check if camera opened successfully
# if (cap.isOpened() == False): 
#   print("Unable to read camera feed")
 
# # Default resolutions of the frame are obtained.The default resolutions are system dependent.
# # We convert the resolutions from float to integer.
# frame_width = int(cap.get(3))
# frame_height = int(cap.get(4))
 
# # Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
# out = cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
# while(True):
#   ret, frame = cap.read()
 
#   if ret == True: 
     
#     # Write the frame into the file 'output.avi'
#     out.write(frame)
 
#     # Display the resulting frame    
#     cv2.imshow('frame',frame)
 
#     # Press Q on keyboard to stop recording
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#       break
 
#   # Break the loop
#   else:
#     break 
 
# # When everything done, release the video capture and video write objects
# cap.release()
# out.release()
 
# # Closes all the frames
# cv2.destroyAllWindows() 
