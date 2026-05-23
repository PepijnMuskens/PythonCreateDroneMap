import cv2

picture_count = 25

vidcap = cv2.VideoCapture('ScanVideo.mp4')
success,image = vidcap.read()
counter = 0
count = 0
length = int(vidcap.get(cv2.CAP_PROP_FRAME_COUNT))
skip_counter = length / picture_count

while success:
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  if counter > skip_counter:
    cv2.imwrite("Images/frame%d.jpg" % count, image)     # save frame as JPEG file      
    counter = 0
    count += 1

  counter += 1