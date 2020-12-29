#Imports

from pygame import *
import random
font.init()
init()

#Image Class

class Image():
    def __init__(self,background_image,background_x,background_y,background_width,background_height):
        self.image = transform.scale(image.load(background_image),(background_width,background_height))
        
        self.background_x = background_x
        self.background_y = background_y
    def create_image(self):
        window.blit(self.image,(self.background_x,self.background_y))

#Text Class

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

#Button Class

class Button():
    def __init__(self,xLoc,yLoc,width,length):
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.width = width
        self.length = length
    def button_press(self):
        global e
        if e.button == 1 and self.xLoc <= e.pos[0] and self.yLoc <= e.pos[1] and self.xLoc + self.width >= e.pos[0] and self.yLoc + self.length >= e.pos[1]:
            return True
    def hovering(self):
        if self.xLoc <= mouse.get_pos()[0] and self.yLoc <= mouse.get_pos()[1] and self.xLoc + self.width >= mouse.get_pos()[0] and self.yLoc + self.length >= mouse.get_pos()[1]:
            return("hovering")


# Game Inital Step Up

window_width = 1080
window_height = 720
display.set_caption("Food Game")
window = display.set_mode((window_width,window_height))

world_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/world_map.jpg",20,20,600,400)
food_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/Food_Ya.jpg",620,10,400,400)
background_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/background_image.png",0,0,1080,720)

clicker_button = Button(620,10,400,400)

food_counter = 0
total_food_counter = 0
food_counter_text = Phrase(0,0,0,"Arial","Food Amount: " + str(food_counter),10,410,50)

time1 = 10
random_num_list = []
random_picture_list = []
random_buttom_list = []
cost_list = []

# Main Game Loop

while True:

    # Everything that need to be updated every game loop

    background_image.create_image()
    world_image.create_image()
    food_image.create_image()
    food_counter_text = Phrase(0, 0, 0, "Arial", "Food Amount: " + str(food_counter), 10, 410, 50)
    food_counter_text.draw_text()

    # Making a new icon every ten seconds

    if time.get_ticks() / 1000 >= time1:
        time1 += 10
        random_num = [random.randint(20, 580), random.randint(20, 380)]
        random_num_list.append(random_num)
        random_buttom_list.append(Button(random_num[0], random_num[1], 40, 40))
        random_picture_list.append(Image("C:/Users/joshu/Downloads/Pygame Food Game/flat_location_logo.png", random_num[0], random_num[1], 40, 40))
        cost_list.append(int((total_food_counter + 1) / random.randint(5, 10) + random.randint(1, 5)))

    # Printing the icons

    for i in range(len(random_picture_list)):
        random_picture_list[i].create_image()

    # Hovering over the icons

    for i in range(len(random_buttom_list)):
        if random_buttom_list[i].hovering() == "hovering":
            black_box = Image("C:/Users/joshu/Downloads/Pygame Food Game/blackbox.jpeg", random_num_list[i][0] + 50, random_num_list[i][1], 90 + len(str(cost_list[i])) * 6, 40)
            cost_text = Phrase(255, 255, 255, "Arial", "Food Amount: " + str(cost_list[i]), random_num_list[i][0] + 55, random_num_list[i][1] + 2.5, 15)
            need_text = Phrase(255, 255, 255, "Arial", "Urgency: " + str(cost_list[i]), random_num_list[i][0] + 55, random_num_list[i][1] + 20, 15)

            black_box.create_image()
            cost_text.draw_text()
            need_text.draw_text()

    for e in event.get():
        if e.type == MOUSEBUTTONDOWN:

            # Clicking on the icon

            del_index = -1
            for i in range(len(random_buttom_list)):
                if random_buttom_list[i].button_press() == True and food_counter - cost_list[i] >= 0:
                    del_index = i
                    print(del_index)

            # Deleting the icon

            if del_index != -1:
                food_counter -= cost_list[del_index]
                del cost_list[del_index]
                del random_num_list[del_index]
                del random_picture_list[del_index]
                del random_buttom_list[del_index]

            # Main Clicker

            if clicker_button.button_press() == True:
                food_counter += 1
                total_food_counter += 1



    display.update()


