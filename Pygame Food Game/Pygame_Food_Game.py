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
    def button_press(self,e):
        if e.button == 1 and self.xLoc <= e.pos[0] and self.yLoc <= e.pos[1] and self.xLoc + self.width >= e.pos[0] and self.yLoc + self.length >= e.pos[1]:
            return True
    def hovering(self):
        if self.xLoc <= mouse.get_pos()[0] and self.yLoc <= mouse.get_pos()[1] and self.xLoc + self.width >= mouse.get_pos()[0] and self.yLoc + self.length >= mouse.get_pos()[1]:
            return("hovering")

# Imformation Pop Up

def information_page(page_num):
    global list_power_ups_names
    global num_power_ups

    end = False
    while end == False:

        for e in event.get():
            if e.type == MOUSEBUTTONDOWN:
                if X_Button_button.button_press(e) == True:

                    end = True

        if page_num == 0:
            in_game_des = Phrase(0, 0, 0, "Arial", "Decreases the amount of food needed to feed people by 10%", 50, 200, 30)
            in_game_picture = Image("food-waste.jpg",50,250,980,420)
        if page_num == 1:
            in_game_des = Phrase(0, 0, 0, "Arial", "Increases the income multiplier by 0.5", 50, 200, 30)
            in_game_picture = Image("C:/Users/joshu/Downloads/Pygame Food Game/Irragation.jpg", 50, 250, 980, 420)
        if page_num == 2:
            in_game_des = Phrase(0, 0, 0, "Arial", "Increases food income from clicks by 1", 50, 200, 30)
            in_game_picture = Image("soil.jpg", 50, 250, 980, 420)
        if page_num == 3:
            in_game_des = Phrase(0, 0, 0, "Arial", "Passive income giving food every second", 50, 200, 30)
            in_game_picture = Image("Trackter.jpg", 50, 250, 980, 420)

        in_game_effect = Phrase(0,0,0,"Arial",list_power_ups_names[page_num] + "'s Power Up Bonus",50,50,50)

        if num_power_ups[page_num] <= 4:
            power_up_cost = Phrase(0,0,0,"Arial","Power Up Cost: " + str(num_power_ups[page_num] * 100 + 100),50,150,30)
        else:
            power_up_cost = Phrase(0, 0, 0, "Arial", "Power Up Cost: Maximum Amount Acquired", 50, 150, 30)

        background_image.create_image()
        X_Button.create_image()

        in_game_effect.draw_text()

        power_up_cost.draw_text()
        in_game_des.draw_text()
        in_game_picture.create_image()

        display.update()

    print("out")
    return


# ----------------------------------------------------------------------------------------------------------


# Game Inital Step Up

window_width = 1080
window_height = 720
display.set_caption("Broccoli distro")
window = display.set_mode((window_width,window_height))

world_image = Image("world_map.jpg",20,20,600,400)
food_image = Image("broccoli.png",620,10,400,400)
background_image = Image("background_image.png",0,0,1080,720)

# X Button

X_Button = Image("X_Button.png",980,50,50,50)
X_Button_button = Button(980,50,50,50)

list_power_ups_names = [
    "Reduced Food Waste",
    "Improved Irrigation",
    "Efficient Fertilizer",
    "Industrialization"
]

# Power Up Text

power_ups = Phrase(0,0,0,"Arial","Power Ups",100,450,30)
food_waste = Phrase(0,0,0,"Arial","Reduced Food Waste",100,500,30)
irrigation_system = Phrase(0,0,0,"Arial","Improved Irrigation",100,550,30)
fertilizer = Phrase(0,0,0,"Arial","Efficient Fertilizer",100,600,30)
industrialization = Phrase(0,0,0,"Arial","Industrialization",100,650,30)

num_power_ups = [0,0,0,0]

# Power Up Button Picture

plus_button_image_list = []
for i in range(4):
    plus_button_image_list.append(Image("plus_image.png",50,505 + (i * 50),30,30))

# Power Up Button

button_image_list = []
for i in range(4):
    button_image_list.append(Button(50,505 + (i * 50),30,30))

rand_time = 0

# Green Power Up Box

green_box = [[],[],[],[]]
black_box = [[],[],[],[]]
for i in range(4):
    for j in range(5):
        green_box[i].append(Image("C:/Users/joshu/Downloads/Pygame Food Game/Green_Square.jpg",350 + (j * 40),505 + (i * 50),30,30))
        black_box[i].append(Image("C:/Users/joshu/Downloads/Pygame Food Game/box_outline.png",350 + (j * 40),505 + (i * 50),30,30))
# Imformation Icon

info_icon_list = []
for i in range(4):
    info_icon_list.append(Image("Information_icon.png",550,502.5 + (i * 50),30,30))

info_icon_button_list = []
for i in range(4):
    info_icon_button_list.append(Button(550,502.5 + (i * 50),30,30))

# Food Stuff

clicker_button = Button(620,10,400,400)

food_counter = 0
total_food_counter = 0
food_counter_text = Phrase(0,0,0,"Arial","Food Counter:",650,450,50)

# + 1

plus_one_text = Phrase(0,0,0,"Arial","+" + str(1 + (1 * num_power_ups[2])),950,100,100)
plus_one_time = -1

# Hearts

heart_list = []
for i in range(3):
    heart_list.append(Image("C:/Users/joshu/Downloads/Pygame Food Game/Heart.png",780 + (i * 70),570,50,50))

gray_heart_list = []
for i in range(3):
    gray_heart_list.append(Image("C:/Users/joshu/Downloads/Pygame Food Game/Heart_Outline.png", 790 + (i * 70), 580, 35, 35))

number_lives = 3

lives = Phrase(0,0,0,"Arial","Lives:",650,570,50)

#Score

score_text = Phrase(0,0,0,"Arial","Score: " + str(int(time.get_ticks() / 1000)),650,660,50)
dead_list = []

# Light Blue Squares

light_blue_square1 = Image("C:/Users/joshu/Downloads/Pygame Food Game/lightblue.png",25,435,570,265)
light_blue_square2 = Image("C:/Users/joshu/Downloads/Pygame Food Game/lightblue.png",635,435,420,265)

# Game Over Stuff

final_score1 = ""

gameover_text = Phrase(255, 0, 0, "Arial","GAMEOVER", 300, 200, 100)
final_score = Phrase(0, 0, 0, "Arial","Score: " + final_score1, 350, 400, 100)
light_blue_square3 = Image("C:/Users/joshu/Downloads/Pygame Food Game/lightblue.png",300,200,480,110)
light_blue_square4 = Image("C:/Users/joshu/Downloads/Pygame Food Game/lightblue.png",350,400,280 + (40 * len(str(final_score1))),110)

#Brocoli 2

broccoli_image = Image("C:/Users/joshu/Downloads/Pygame Food Game/broccoli_2.jpg",0,0,1080,720)

# List Icon Storage


time1 = 10
random_num_list = []
random_picture_list = []
random_buttom_list = []
cost_list = []
urgency_list = []

# ----------------------------------------------------------------------------------------------------------

# Starting Screen

kill_switch = False
main_game = True
while main_game == True:

    for e in event.get():

        # Quiting Pygame

        if e.type == QUIT:
            main_game = "kill switch"
            kill_switch = "kill switch"

        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                main_game = False

    broccoli_image.create_image()

    display.update()


# ----------------------------------------------------------------------------------------------------------

# Main Game Loop
if kill_switch == False:
    main_game = True
else:
    main_game = "kill switch"


while main_game == True:

    # Everything that need to be updated every game loop


    background_image.create_image()
    world_image.create_image()
    food_image.create_image()
    light_blue_square1.create_image()
    light_blue_square2.create_image()

    score_text.draw_text()
    final_score1 = str(int(time.get_ticks() / 1000))
    score_text = Phrase(0, 0, 0, "Arial", "Score: " + str(int(time.get_ticks() / 1000)), 650, 640, 50)

    food_counter_text = Phrase(0, 0, 0, "Arial", "Food Amount: " + str(int(food_counter)), 650, 430, 50)
    food_counter_text.draw_text()
    plus_one_text = Phrase(0, 0, 0, "Arial", "+" + str(1 + (1 * num_power_ups[2])), 950, 100, 100)
    income_multiplier = 1 + (0.5 * num_power_ups[1])
    income_text = Phrase(0, 0, 0, "Arial", "Income Multiplier: " + str(income_multiplier), 650, 500, 50)
    lives.draw_text()

    # Making a new icon every ten seconds

    if time.get_ticks() / 1000 >= time1:
        time1 += 10
        random_num = [random.randint(20, 580), random.randint(20, 380)]
        random_num_list.append(random_num)
        random_buttom_list.append(Button(random_num[0], random_num[1], 40, 40))
        random_picture_list.append(Image("C:/Users/joshu/Downloads/Pygame Food Game/flat_location_logo.png", random_num[0], random_num[1], 40, 40))
        cost_list.append(int((total_food_counter + 1) / random.randint(5, 10) + random.randint(1, 5)) / (1 + (0.1 * num_power_ups[0])))
        urgency_list.append([time.get_ticks() / 1000,"None"])

    for i in range(len(cost_list)):
        cost_list[i] = int(cost_list[i])

    # Printing the icons

    for i in range(len(random_picture_list)):
        random_picture_list[i].create_image()

    # Game Urgency List Update

    for i in range(len(urgency_list)):
        if urgency_list[i][0] + 50 <= time.get_ticks() / 1000 and urgency_list[i][1] == "High":
            number_lives -= 1
            urgency_list[i][1] = "Dead"
        elif urgency_list[i][0] + 50 <= time.get_ticks() / 1000:
            urgency_list[i][1] = "Dead"
        elif urgency_list[i][0] + 30 <= time.get_ticks() / 1000:
            urgency_list[i][1] = "High"
        elif urgency_list[i][0] + 20 <= time.get_ticks() / 1000:
            urgency_list[i][1] = "Medium"
        elif urgency_list[i][0] <= time.get_ticks() / 1000:
            urgency_list[i][1] = "Low"
        else:
            urgency_list[i][1] = "None"


    # Hovering over the icons

    for i in range(len(random_buttom_list)):
        if random_buttom_list[i].hovering() == "hovering":
            black_box1 = Image("C:/Users/joshu/Downloads/Pygame Food Game/blackbox.jpeg", random_num_list[i][0] + 50, random_num_list[i][1], 110 + len(str(cost_list[i])) * 6, 40)
            cost_text = Phrase(255, 255, 255, "Arial", "Food Amount: " + str(cost_list[i]), random_num_list[i][0] + 55, random_num_list[i][1] + 2.5, 15)
            need_text = Phrase(255, 255, 255, "Arial", "Urgency: " + str(urgency_list[i][1]), random_num_list[i][0] + 55, random_num_list[i][1] + 20, 15)

            black_box1.create_image()
            cost_text.draw_text()
            need_text.draw_text()

    for e in event.get():

        # Quiting Pygame

        if e.type == QUIT:
            print("quit")
            main_game = False

        if e.type == MOUSEBUTTONDOWN:

            # Clicking on the icon

            del_index = -1
            for i in range(len(random_buttom_list)):
                if random_buttom_list[i].button_press(e) == True and food_counter - cost_list[i] >= 0 and urgency_list[i][1] != "Dead":
                    del_index = i

            # Deleting the icon

            if del_index != -1:
                food_counter -= cost_list[del_index]
                del cost_list[del_index]
                del random_num_list[del_index]
                del random_picture_list[del_index]
                del random_buttom_list[del_index]
                del urgency_list[del_index]

            # Main Clicker

            if clicker_button.button_press(e) == True:
                food_counter += (1 + (1 * num_power_ups[2])) * income_multiplier
                total_food_counter += (1 + (1 * num_power_ups[2])) * income_multiplier
                plus_one_time = time.get_ticks()

            for i in range(len(button_image_list)):
                if button_image_list[i].button_press(e) == True and num_power_ups[i] <= 4 and food_counter >= (num_power_ups[i] + 1) * 100:
                    food_counter -= (num_power_ups[i] + 1) * 100
                    num_power_ups[i] += 1

            if info_icon_button_list[0].button_press(e) == True:
                information_page(0)
            if info_icon_button_list[1].button_press(e) == True:
                information_page(1)
            if info_icon_button_list[2].button_press(e) == True:
                information_page(2)
            if info_icon_button_list[3].button_press(e) == True:
                information_page(3)

    if plus_one_time + 100 >= time.get_ticks():
        plus_one_text.draw_text()

    # Power Ups

    power_ups.draw_text()
    food_waste.draw_text()
    irrigation_system.draw_text()
    fertilizer.draw_text()
    industrialization.draw_text()
    income_text.draw_text()

    # Plus Power Up Image

    for i in range(len(plus_button_image_list)):
        plus_button_image_list[i].create_image()

    # Power Up Green Squares

    for i in range(4):
        for j in range(5):
            black_box[i][j].create_image()

    for i in range(4):
        for j in range(num_power_ups[i]):
            green_box[i][j].create_image()

    # Power Up Imformation Icons

    for i in range(len(info_icon_list)):
        info_icon_list[i].create_image()

    if rand_time + 1000 <= time.get_ticks():
        rand_time = time.get_ticks()
        food_counter += (1 * num_power_ups[3]) * income_multiplier
        total_food_counter += (1 * num_power_ups[3]) * income_multiplier

    for i in range(len(gray_heart_list)):
        gray_heart_list[i].create_image()

    for i in range(number_lives):
        heart_list[i].create_image()

    # Checking Lives Count

    if number_lives <= 0:
        main_game = "dead"

    display.update()
# ----------------------------------------------------------------------------------------------------------

# Ending Screen

if main_game == "dead":
    main_game = True
    while main_game == True:

        for e in event.get():

            # Quiting Pygame

            if e.type == QUIT:
                print("quit")
                main_game = False

        broccoli_image.create_image()
        light_blue_square3.create_image()
        light_blue_square4.create_image()
        gameover_text.draw_text()
        final_score.draw_text()

        display.update()