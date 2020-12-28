from pygame import *
import random
font.init()

class Image():
    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        
        self.background_x = background_x
        self.background_y = background_y
    def create_image(self):
        window.blit(self.image,(self.background_x,self.background_y))

class Phrase():
    def __init__(self,color1,color2,color3,font_type,text,x_pos,y_pos,font_size):
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.font_type = font_type
        self.text = text
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font_size = font_size
    def draw_text(self):
        self.font = font.SysFont(self.font_type,self.font_size)
        screen_text = self.font.render(self.text, True,(self.color1,self.color2,self.color3))
        window.blit(screen_text, [self.x_pos,self.y_pos])

class Button():
    def __init__(self,xLoc,yLoc,width,length):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.width = width
        self.length = length
    def button_press(self):
        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if e.button == 1 and self.xLoc <= e.pos[0] and self.yLoc <= e.pos[1] and self.xLoc + self.width >= e.pos[0] and self.yLoc + self.length >= e.pos[1]:
                    return True

window_width = 1080
window_height = 720
display.set_caption("Food Game")
window = display.set_mode((window_width,window_height))

world_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/world_map.jpg",10,10,600,400)
food_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/Food_Ya.jpg",620,10,400,400)
background_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/background_image.png",0,0,1080,720)

clicker_button = Button(620,10,400,400)

food_counter = 0
food_counter_text = Phrase(0,0,0,"Arial","Food Amount: " + str(food_counter),10,410,50)

while True:
    background_image.create_image()
    world_image.create_image()
    food_image.create_image()

    if clicker_button.button_press() == True:
        food_counter += 1
        food_counter_text = Phrase(0, 0, 0, "Arial", "Food Amount: " + str(food_counter), 10, 410, 50)

    food_counter_text.draw_text()

    display.update()
