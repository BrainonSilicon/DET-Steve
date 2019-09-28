
while person = True #something that means steve is active
    for my_servo in servos:
        print ("moving servo # ", servos.index(my_servo)+1)
        my_servo.angle = 15  
        time.sleep(4)

def ocr_handwriting(image):
    
    response = client.text_detection(image=image)
    text = response.full_text_annotation

    word_text = ""

    for page in text.pages:
        for block in page.blocks:
            for paragraph in block.paragraphs:
                for word in paragraph.words:
                    word_text += " "
                    word_text += ''.join([
                        symbol.text for symbol in word.symbols
                        ])                    

    if word_text:
        print('ocr_handwriting(): {}'.format(word_text))
        arm_moves(word_text,arm_up_string,arm_down_string)
    else:
        print('ocr_handwriting(): No Handwriting Text Detected!')

    def arm_moves(text, arm_up_string, arm_down_string)
        if  re.search(arm_up_string, text, re.IGNORECASE):
            servo[0].angle = 70
            servo[1].angle = 70

            if handwriting = ("Coffee") 
                print ("selected coffee")
                servo[0].angle = 80
                time.sleep(1)
                servo[1].angle = 0
            else: handwriting = ("Tea")
                print ("selected tea")
                servo[1].angle = 80
                time.sleep(1)
            servo[0].angle = 0
    
            my_servo.angle = 0 

        elif re.search(arm_down_string, text, re.IGNORECASE):
            print ("no selection made")
            my_servo.angle = 10

