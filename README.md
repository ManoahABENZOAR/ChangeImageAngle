# CorrectImageAngle

Probleme : As you can see the box isn’t planar but we aren’t considering the entire box, only the front face where we can see characters from Dragon Ball Z as Son Goku, Cell, Vegito, …
So our objet is this front face. As we can see we are not seeing this objet from a front view : we are on the left and not horizontaly straight.
The goal of the exercice is to create a second image based on this, which seem to have been taken on a front view. But we can’t take a new picture, we could only use our program to change the view.

To succees we need to modify the perspective. Help by a program provide by OpenCV we can procede easily. 
We only need to find the good coordinates for 4 points.


Here the code :
      import numpy as np
      import cv2

      img = cv2.imread("p (1).jpg")
      height, width, _ = img.shape
      cv2.imshow('input', img)
      cv2.waitKey(0)

      pts1 = np.float32([[134,117],[298,193],[56,497],[230,479]])
      pts2 = np.float32([[100,120],[270,124],[100,500],[270, 504]])
      M = cv2.getPerspectiveTransform(pts1,pts2)
      dst = cv2.warpPerspective(img, M, (340, 740))

      cv2.imshow('output',dst)
      cv2.waitKey(0)
      cv2.destroyAllWindows()

With explanations : 
      The first two lines allow us to use some librairies which contain very useful tools.
      The following three lines allow us to show on the computer screen the input image.
      Waitkey waits for 0 milliseconds for a key press on the keyboard.
      
      Now we look at the main part.
        -Pts1 and pts2 are two frames represented by itsfour vertices.
        -In pts1 we entrer the coordinates of the frame of the object, here the frame of the front face of the box.
        -Then, in pts2 we enter its new coordinates. The coordinates which will allow us to give a the new perspective to the object.
        -After, we made the change in a picture named « M ». This is what does the function cv2.getPerspectiveTransform() : we enter the coordinates of the frame on the input image and as second parameter we put the new coordinates.And the function makes it appends.
        -dst is the final picture. On it we print out the modifications made with « getPerspective ».
      
      To do so we enter as first parameter the source image, then the image M where we did the changes and finally the wished size for this new image.
      Finally, we show the result with « imshow ».
      And after press a button we destroy the two windows where are the input and output image.
