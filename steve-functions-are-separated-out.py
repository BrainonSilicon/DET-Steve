#import standard libraries and packages
import picamera
import pygame as pg 
import os 

from google.cloud import vision
import time 
from time import sleep 
from adafruit_crickit import crickit 
import signal 
import sys 
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../DET190-JSON/Pinky-DET-2019-e4f4274adb35.json"
client = vision.ImageAnnotatorClient()

image = 'image.jpeg'

# take in an image
def take_photo(camera):
    camera.start_preview()
    sleep(0.5)
    camera.capture('image.jpeg')
    camera.stop_preview()

# figure out where the person/object is in the image
def localize_objects(image):
    """Localize objects in the local image.
    
    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()
    
    objects = client.object_localization(image=image).localized_object_annotations
     
    for object_ in objects: #the _ normally means run it but don't grab it
        #print('\n{} (confidence: {})'.format(object_.name, object_.score))
        area = 0
        if object_.name == 'Person':
            vertices = object_.bounding_poly.normalized_vertices
            #print(vertices) #counterclockwise from bottom left
            length = abs(vertices[0].x - vertices[1].x)
            height = abs(vertices[1].y - vertices[2].y)
            new_area = length*height
            if new_area > area:
                area = new_area
                center_x = vertices[0].x + (length/2)
                center_y = vertices[0].y + (height/2)
                return center_x,center_y

#function for knowing if the person has chosen right or left            
def decision_maker(new,old):
    if (new-old) > 0.3:
        print("picked left")
    elif (new-old) < - 0.3:
        print("picked right")
    else:
        print("none chosen")

#function for the choices (eg. hot or cold)
def offer_choice(choice1, choice2):
    print('{} or {}?'.format(choice1, choice2))

# this is steve detecting a person and what starts the interaction 
def person(image):
    response = client.face_detection(image=image)
    face_content = response.face_annotations
    print (face_content)
    
    if face_content and face_content[0].detection_confidence > 0.25:
        print("I see a person(): {}".format(face_content[0].detection_confidence))
        #move the motors 
        my_servo.angle = 10

    else:
        print("I do not see a person(): No Face Detected at High Confidence!")
        my_servo.angle = 0

# these are defining the functions that will be executed when called
def steve_waiting(image):
    #steve's "waiting period" between options
    my_servo.angle = 15
    time.sleep(1)

def options(image):
    # I don't think this while loop needs to be here -> while bounding_box == bounding_box_size_at_start # these aren't defined yet 
    servo[0].angle = 70
    servo[1].angle = 60

def selection(image): 
    # the arm movements for steve when a selection has been made  
    # if the bb functions returns x == right 
        servo[0].angle = 80
        time.sleep (2)
        servo[1].angle = 0
        time.sleep (3)
        servo[0].angle = 0
    # if the bb function returns x == left 
        servo[1].angle = 80
        time.sleep (2)
        servo[0].angle = 0
        time.sleep (3)
        servo[1].angle = 0
      
def main():
    #this is where things start to happen 
    print ("I'm Steve! I'm here to help.")
    
    camera = picamera.PiCamera()
    offer_choice('Hot','Cold')
    take_photo(camera) # First take a picture
    """Run localization request on a single image"""
    with open('image.jpg', 'rb') as image_file:
        #read the image file
        content = image_file.read()
        #convert the image file to a GCP Vision-friendly type
        image = vision.types.Image(content=content)
        (oldx,oldy) = localize_objects(image)
        time.sleep(5)
        
    take_photo(camera)
    with open('image.jpg', 'rb') as image_file:
        #read the image file
        content = image_file.read()
        #convert the image file to a GCP Vision-friendly type
        image = vision.types.Image(content=content)
        (x,y)=localize_objects(image)
        decision_maker(x,oldx)
        (oldx, oldy) = (x,y)
        time.sleep(5)  

    servos = (crickit.servo_1, crickit.servo_2)
    while person = True # something that means steve is active
        for my_servo in servos:
            print ("moving servo # ", servos.index(my_servo)+1)
            my_servo.angle = 15  
            time.sleep(4)
            
if __name__ == '__main__':
        main() 
        
        
        
#import standard libraries and packages
import picamera
import pygame as pg 
import os 

from google.cloud import vision
import time 
from time import sleep 
from adafruit_crickit import crickit 
import signal 
import sys 
import re

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "../DET190-JSON/Pinky-DET-2019-e4f4274adb35.json"
client = vision.ImageAnnotatorClient()

image = 'image.jpeg'

# take in an image
def take_photo(camera):
    camera.start_preview()
    sleep(0.5)
    camera.capture('image.jpeg')
    camera.stop_preview()

# figure out where the person/object is in the image
def localize_objects(image):
    """Localize objects in the local image.
    
    Args:
    path: The path to the local file.
    """
    client = vision.ImageAnnotatorClient()
    
    objects = client.object_localization(image=image).localized_object_annotations
     
    for object_ in objects: #the _ normally means run it but don't grab it
        #print('\n{} (confidence: {})'.format(object_.name, object_.score))
        area = 0
        if object_.name == 'Person':
            vertices = object_.bounding_poly.normalized_vertices
            #print(vertices) #counterclockwise from bottom left
            length = abs(vertices[0].x - vertices[1].x)
            height = abs(vertices[1].y - vertices[2].y)
            new_area = length*height
            if new_area > area:
                area = new_area
                center_x = vertices[0].x + (length/2)
                center_y = vertices[0].y + (height/2)
                return center_x,center_y

#function for knowing if the person has chosen right or left            
def decision_maker(new,old):
    if (new-old) > 0.3:
        print("picked left")
        return 1
    elif (new-old) < - 0.3:
        print("picked right")
        return -1
    else:
        print("none chosen")
        return 0

#function for the choices (eg. hot or cold)
def offer_choice(choice1, choice2):
    print('{} or {}?'.format(choice1, choice2))

# this is steve detecting a person and what starts the interaction 
def person(image):
    response = client.face_detection(image=image)
    face_content = response.face_annotations
    print (face_content)
    
    if face_content and face_content[0].detection_confidence > 0.25:
        print("I see a person(): {}".format(face_content[0].detection_confidence))
        #move the motors 
        my_servo.angle = 10
        return True
    else:
        print("I do not see a person(): No Face Detected at High Confidence!")
        my_servo.angle = 0
        return False

# these are defining the functions that will be executed when called
def steve_waiting(image):
    #steve's "waiting period" between options
    my_servo.angle = 15
    time.sleep(1)

def options(image):
    # I don't think this while loop needs to be here -> while bounding_box == bounding_box_size_at_start # these aren't defined yet 
    servo[0].angle = 70
    servo[1].angle = 60

def selection_right(): 
    # the arm movements for steve when a selection has been made  
    # if the bb functions returns x == right 
        servo[0].angle = 80
        time.sleep (2)
        servo[1].angle = 0
        time.sleep (3)
        servo[0].angle = 0

def selection_left():
    # if the bb function returns x == left 
        servo[1].angle = 80
        time.sleep (2)
        servo[0].angle = 0
        time.sleep (3)
        servo[1].angle = 0
        
def driver():
    #this is where things start to happen 
    print ("I'm Steve! I'm here to help.")
    camera = picamer.PiCamera()
    #take a photo 
    take_photo(camera)
    person_seen = False
    # loop until it sees face
    while person_seen is False:
        person_seen = person(image)
    # proceed
    # define the location and size of the bounding box  
    x, y = localize_objects(image)
    #when it sees a face then raise my_servos to 10
    #wait for 2 seconds 
    time.sleep(2)
    #then present the options (the options are raising the arms)
    offer_choice('Hot','Cold')
    
    #wait for a response from the user which will be in the form of the bounding box expanding right or left
    new_x, new_y = localize_objects(image)
    # respond based on the right or left expansion of the bounding box with a motor output
    res_x = decision_maker(new_x, x)
    if res_x == 1:
        selection_left()
    elif res_x == -1:
        selection_right()
    else:
        # do nothing
    
    #reset to 10 degrees     
    my_servo.angle = 10
    #new event (ie. diferent LCD output but same response loop)
    
    
    
    
    # after all options presented 
    # end 
    
    
    
    
    
    
    
    
    # camera = picamera.PiCamera()
    # offer_choice('Hot','Cold')
    # take_photo(camera) # First take a picture
    # """Run localization request on a single image"""
    # with open('image.jpg', 'rb') as image_file:
    #     #read the image file
    #     content = image_file.read()
    #     #convert the image file to a GCP Vision-friendly type
    #     image = vision.types.Image(content=content)
    #     (oldx,oldy) = localize_objects(image)
    #     time.sleep(5)
        
    # take_photo(camera)
    # with open('image.jpg', 'rb') as image_file:
    #     #read the image file
    #     content = image_file.read()
    #     #convert the image file to a GCP Vision-friendly type
    #     image = vision.types.Image(content=content)
    #     (x,y)=localize_objects(image)
    #     decision_maker(x,oldx)
    #     (oldx, oldy) = (x,y)
    #     time.sleep(5)  

    # servos = (crickit.servo_1, crickit.servo_2)
    # while person = True # something that means steve is active
    #     for my_servo in servos:
    #         print ("moving servo # ", servos.index(my_servo)+1)
    #         my_servo.angle = 15  
    #         time.sleep(4)
      
def main():
    
            
if __name__ == '__main__':
        main() 
