# this library's documentation can be accessed here: https://www.pygame.org/docs/
#date of access: 11/01/2024
import pygame

# Please access the library’s documentation here: https://docs.python.org/3/library/csv.html
#date of access: 11/01/2024
import csv

# please access this library's documentation here: https://docs.python.org/3/library/random.html
#date of access: 11/01/2024
import random

# please access this library's documentation here: https://docs.python.org/3/library/math.html
#date of access: 11/01/2024
import math

#Please access this library's documentation here: https://docs.python.org/3/library/time.html
#Date of access: 07/03/2024
import time

#Please access this library's documentation here:https://docs.python.org/3/library/webbrowser.html
#Date of access: 07/03/2024
import webbrowser

#Please access this library's documentation here:
#Date of access: 07/03/2024
import requests as requests
    
#Please access this library's documentation here:https://pypi.org/project/requests/
#Date of access: 07/03/2024
from unsplash.api import Api
    
#Please access this library's documentation here:https://github.com/yakupadakli/python-unsplash
#Date of access: 07/03/2024
from unsplash.auth import Auth
    
#Please access this library's documentation here:https://pillow.readthedocs.io/en/stable/
#Date of access: 07/03/2024
from PIL import Image
    
#Please access this library's documentation here: https://docs.python.org/3/library/io.html
#Date of access: 07/03/2024
from io import BytesIO

#Please see this library's documentation here:https://matplotlib.org/
#Date of access: 07/03/2024
from matplotlib import image as img
from matplotlib import pyplot as plt

#Please see library's documentation here:https://docs.python.org/3/library/random.html
#Date of access: 07/03/2024
import random

#Please access library documentation here: https://docs.python.org/3/library/os.path.html
#Date of Access: 08/03/2024
import os

#Please access this library's documentation here: https://docs.python.org/3/library/ast.html
#Date of Access: 15/04/2024
import ast


pygame.init()

#setting window dimensions to be 
#info = pygame.display.Info()
#SIZE = screen_width, screen_height = info.current_w, info.current_h
global screen_width, screen_height
screen_width, screen_height=1200,700
global screen
screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)

#colours defined here
green=(0, 155, 0)
blue=(204, 255, 255)
black = (0,0,0)
red =(252,81,48)
white=(255,255,255)
dark_blue= (8,127,140)

# create font options
pygame.font.init()
#'PressStart2P-vaV7.ttf'
small_text = pygame.font.Font('PressStart2P-vaV7.ttf', 10)
medium_text = pygame.font.Font('PressStart2P-vaV7.ttf', 25)
large_text = pygame.font.Font('PressStart2P-vaV7.ttf', 45)
option_text = pygame.font.Font('PressStart2P-vaV7.ttf', 15)
question_text=pygame.font.Font('PressStart2P-vaV7.ttf',20)
# 
# the following 'drawText' function can be found at https://www.pygame.org/wiki/TextWrap - date of access: 04.01.2024
# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawText(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = 4

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word      
        if i < len(text): 
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left+7, y+7))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]


    return text

#declaring all global variables

global year
year=2023
 
global time_jumps
time_jumps=[]
        
global albedo
albedo = 0.30
        
global budget
budget=100
        
global sea_levels
sea_levels=[]
        
global greenhouse_effect
greenhouse_effect=0.5841
        
global temps
temps=[]
        
global temp_changes
temp_changes=[]
        
global test_file_name
test_file_name ='pre-test-questions.csv'

global main_file
main_file='main-game-questions-1.csv'

global T_cel
T_cel=0

global level
level=0

global temp_rise
temp_rise=0
    
global sea_level_rise
sea_level_rise=float(0)

global total_temp_rise
total_temp_rise=0

global budget_tracker
budget_tracker = [100]

global question_number
question_number=0

global current_temp
current_temp=14

global greenhouse_tracker
greenhouse_tracker=[]

global pre_score
pre_score=0

global post_score
post_score=0

class Button(object):
    def __init__(self, x, y, width, height, colour, msg,wrap_text, font_size, alignment):
        self.x = x
        self.y = y
        self.colour = colour # must be tuple
        self.msg = msg # must be string
        self.wrap_text = wrap_text
        self.font_size = font_size #font size
        self.alignment = alignment #this will be either y or n in each instance
        self.width=width
        self.height=height

        
    def draw(self):
        pygame.init()
        screen_height = screen.get_height()
        screen_width = screen.get_width()
        # draw on screen
        text_surf= (self.font_size).render(self.msg, True, (0, 0, 0))
        text_width, text_height = text_surf.get_size()
        if self.wrap_text != True and (self.width<=text_width or self.height<=text_height) or (self.width==0) or (self.height==0):
            #dimensions of button are defined by the text it contains
            #or boolean operator used because otherwise program would crash if only one dimension was 0
            text_surf= (self.font_size).render(self.msg, True, (0, 0, 0))
            text_width, text_height = text_surf.get_size()
            self.width = text_width+10
            self.height = text_height+10
        else:
            text_surf= (self.font_size).render(self.msg, True, (0, 0, 0))

        if self.alignment == 'x' or self.alignment =='X':#button centred on x axis
            self.x = (screen_width-self.width)/2
            rect = pygame.rect.Rect((self.x,self.y),(self.width, self.height))
            pygame.draw.rect(screen, self.colour, rect)
            
        elif self.alignment == 'y' or self.alignment =='Y': #button centred on y axis
            self.y = (surface_height-self.height)/2
            rect = pygame.rect.Rect((self.x,self.y),(self.width, self.height))
            pygame.draw.rect(screen, self.colour, rect)

        elif self.alignment == 'c' or self.alignment =='C': #button to be centred on both x and y axis
            self.x = (screen_width-self.width)/2
            self.y = (screen_height-self.height)/2
            rect = pygame.rect.Rect((self.x,self.y),(self.width, self.height))
            pygame.draw.rect(screen, self.colour, rect)
            
        else:#otherwise draw with normal coordinates
            rect = pygame.rect.Rect((self.x,self.y), (self.width, self.height))
            pygame.draw.rect(screen, self.colour, rect)
        if self.wrap_text==True:
            rect = pygame.rect.Rect((self.x,self.y),(self.width, self.height))
            text = drawText(screen, self.msg, black, rect, self.font_size, aa=False, bkg=None)
            if text: #i.e if there is text left over after printing
                print("Error! The screen was too small for the ", self, "Button")
                
        else:
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
            screen.blit(text_surf, text_rect)
        
    def is_clicked(self):
        text_surf= (self.font_size).render(self.msg, True, (0, 0, 0))
        text_width, text_height = text_surf.get_size()
        if self.width<text_width and self.height<text_height:
            self.width = text_width+10
            self.height = text_height+10
        rect = pygame.rect.Rect((self.x,self.y), (self.width, self.height))
        mouse_pos = pygame.mouse.get_pos()
        return rect.collidepoint(mouse_pos)

    
    
def create_question_list(question_file):
    question_data=[]
    #open file in read mode
    with open(question_file,'r') as file:
        #read file in dictionary format
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            new_question={}
            new_question['question']=row["Question"]
            new_question['options']=row["Option A"], row["Option B"], row["Option C"], row["Option D"]
            new_question['correct answer']=row["Answer"]
            question_data.append(new_question)
    return question_data



def tests(created_question_list):
    question_number=0
    pause=False
    score=0
    feedback=''
    answer=''
    answer_click=False
    screen.fill(blue)
    for question in created_question_list:
        if question_number<10:
            screen.fill(blue)
            answer_click=False
            
            #Pause Button
            pause_button = Button ((screen_width*0.85),(screen_height*0.02),120,100,red, "Menu",True, medium_text,'n')
            pause_button.draw()
            #show year in top left
            score_stat =Button((screen_width*0.01),(screen_height*0.02),310,100,red, "Score: "+str(score),True, medium_text,'n')
            score_stat.draw()
            
            #question
            question_content=str(question_number+1) + ". " + question['question'].strip('""')
            
            #image credits test block
            image_credit, link = image(question_content)
            credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
            credit.draw()
            
            #display the question
            question_button=Button((screen_width*0.01), (screen_height*0.07), (screen_width),(screen_height*0.15), blue, question_content,True, question_text, 'n')
            question_button.draw()
            # for each option, print a letter and then the text
            for option in question['options']:
                letters=['a) ','b) ','c) ','d) ']
                #draw option buttons
                if question['options'].index(option)==0: #if this is the first option in the list, since lists in python are zero-indexed
                    option_a=Button((screen_width*0.035),(screen_height*0.65),660, 60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_a.draw()
                elif question['options'].index(option)==1:
                    option_b=Button((screen_width*0.035),(screen_height*0.74),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_b.draw()
                elif question['options'].index(option)==2:
                    option_c=Button((screen_width*0.035),(screen_height*0.83),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_c.draw()
                elif question['options'].index(option)==3:
                    option_d=Button((screen_width*0.035),(screen_height*0.92),660,60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_d.draw()
            #needed for pause function
            screen_surface = pygame.display.get_surface()
            screen_copy = screen_surface.copy()
            
            #condition controlled loop - so user can only click on a button once to prevent crashing from multiple inputs
            while answer_click==False:
                pygame.display.update()
                #event handler
                for event in pygame.event.get():
                    #quit game
                    if event.type == pygame.KEYDOWN:
                        if event.type == pygame.QUIT:
                            running = False
                            pygame.quit()
                        #pause
                        if event.key == pygame.K_SPACE:
                            if pause == False:
                                pause=True
                                pause_screen(pause, screen_copy)
                                # inverts the current state of the boolean variable pause so pause can be toggled
                                pause=False
                    #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause_button.is_clicked():
                            if pause == False:
                                    pause=True
                                    pause_screen(pause, screen_copy)
                                    # inverts the current state of the boolean variable pause so pause can be toggled
                                    pause=False
                        #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                        # Check for mouse click within the text surface area
                        if credit.is_clicked():
                            #required by the unsplash api to link to photographer's profile
                            webbrowser.open(link)
                        #input processing blocks below
                        if option_a.is_clicked():
                            answer='a'
                            
                            acceptable_answers = ['a', 'b', 'c', 'd']
                            if answer in acceptable_answers:
                                if question['options'][acceptable_answers.index(answer)] == question['correct answer']:
                                    score += 1
                                    feedback="Well done!"
                                else:
                                    feedback="That isn't quite right..."

                                answer_click=True
                                                                                    
                                question_number+=1
                        
                                #feedback block
                                feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                                feedback_display.draw()
                                
                                #blit all to screen
                                pygame.display.update()
                                
                                time.sleep(2)
                        elif option_b.is_clicked():
                            answer='b'
                            acceptable_answers = ['a', 'b', 'c', 'd']
                            if answer in acceptable_answers:
                                if question['options'][acceptable_answers.index(answer)] == question['correct answer']:
                                    score += 1
                                    feedback="Well done!"
                                else:
                                    feedback="That isn't quite right..."
                                answer_click=True
                                                                                    
                                question_number+=1
                        
                                #feedback block
                                feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                                feedback_display.draw()
                                
                                #blit all to screen
                                pygame.display.update()
                                
                                time.sleep(2)
                        elif option_c.is_clicked():
                            answer='c'
                            acceptable_answers = ['a', 'b', 'c', 'd']
                            if answer in acceptable_answers:
                                if question['options'][acceptable_answers.index(answer)] == question['correct answer']:
                                    score += 1
                                    feedback="Well done!"
                                else:
                                    feedback="That isn't quite right..."
                                answer_click=True
                                                                                    
                                question_number+=1
                        
                                #feedback block
                                feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                                feedback_display.draw()
                                
                                #blit all to screen
                                pygame.display.update()
                                
                                time.sleep(2)
                        elif option_d.is_clicked():
                            answer='d'
                            acceptable_answers = ['a', 'b', 'c', 'd']
                            if answer in acceptable_answers:
                                if question['options'][acceptable_answers.index(answer)] == question['correct answer']:
                                    score += 1
                                    feedback="Well done!"
                                else:
                                    feedback="That isn't quite right..."
                                answer_click=True
                                                    
                                question_number+=1
                        
                                #feedback block
                                feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                                feedback_display.draw()
                                
                                #blit all to screen
                                pygame.display.update()
                                
                                time.sleep(2)
            
                        else:
                            pygame.display.update()
    return score



def validation(name):
    #avoid type error
    name=str(name)
    #special_chars array created by Gemini, Google's AI model(s)
    #date of access: 07/03/2024
    special_chars = [ '\\', '/', ':', '*', '?', '"', '<', '>', '|', '.', ',','!' ]
    valid=False
    for char in special_chars:
        if char in name:
            valid= False
            break
        else:
            valid= True
            
    return valid

def input_box(text):
    
    #how to get back to original screen
    surface_list=[]
    screen_surface = pygame.display.get_surface()
    initial_screen_copy = screen_surface.copy()
    screen_copy=screen_surface.copy()
    surface_list.append(screen_copy)
    screen.fill(blue)
    
    #clear screen
    screen.fill(blue)
    pygame.display.update()

    #back button
    back_button = Button(screen_width*0.05,screen_height*0.05, 150, 75, green, "Back", False, medium_text, 'n')
    back_button.draw()
    
    pygame.display.flip()
    
    #instruction
    title=Button(0,screen_height*0.2,0,0,blue, text,False, medium_text,'x')
    title.draw()
    #initialise font and colours for text and box
    font = pygame.font.Font(None, 32)
    box_colour = pygame.Color('gray')
    text_colour = pygame.Color('black')
    input_text = ""
    active = True
    cursor_pos = 0
    box_width = screen_width*0.6
    box_height = 32
    box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2, box_width, box_height)
    mouse_pos = pygame.mouse.get_pos()
    running = True
    
    name_not_valid=True
    while running and name_not_valid:
        text_surface = font.render(input_text, True, text_colour)
        screen.fill(box_colour, box_rect)
        screen.blit(text_surface, (box_rect.x + 5, box_rect.y + 5))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if box_rect.collidepoint(mouse_pos):
                    active = not active
                if back_button.is_clicked():
                    running=False
                    screen.blit(initial_screen_copy, (0,0))
                    pygame.display.flip()
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    cursor_pos -= 1
                   #Test code
                elif event.key == pygame.K_RETURN:
                    if validation(input_text)==True:
                        screen.fill(blue)
                        feedback=Button(0,screen_height*0.2,0,0,blue, "Please Wait",False, medium_text,'x')
                        feedback.draw()
                        pygame.display.update()
                        time.sleep(2)
                        name_not_valid=False
                        active=False
                    else:
                        screen.fill(blue)
                        feedback=Button(0,screen_height*0.2,0,0,blue, "Please don't use any special characters!",False, medium_text,'x')
                        feedback.draw()
                        pygame.display.update()
                        time.sleep(3)
                        input_box(text)
                else:
                    input_text = input_text[:cursor_pos] + event.unicode + input_text[cursor_pos:]
                    cursor_pos += 1

        if active:
            cursor_x = box_rect.x + font.size(input_text[:cursor_pos])[0] + 5
            pygame.draw.line(screen, text_colour, (cursor_x, box_rect.y + 5), (cursor_x, box_rect.y + box_height - 5), 2)

        pygame.display.flip()
    return input_text


def save():
    #cast to avoid type errors when concatenating
    file_name=str(input_box("Type in your name and then press enter: ")).strip("''")
    
    with open(file_name+'.txt', 'w') as file:
        #each variable is declared as global and then written to the file
            global level
            file.write(str(level)+"\n")
            
            global year
            file.write(str(year)+"\n")
            
            global question_number
            file.write(str(question_number)+"\n")
            
            global greenhouse_effect
            file.write(str(greenhouse_effect)+"\n")
            
            global temps
            file.write(str(temps)+"\n")
            
            global temp_changes            
            file.write(str(temp_changes)+"\n")
            
            global sea_level_rise
            file.write(str(sea_level_rise)+"\n")
            
            global total_temp_rise
            file.write(str(total_temp_rise)+"\n")
            
            global albedo
            file.write(str(albedo)+"\n")
            
            global budget
            file.write(str(budget)+"\n")
                       
                       
            global temp_rise
            file.write(str(temp_rise)+"\n")
            
            global current_temp
            file.write(str(current_temp)+"\n")
            
            global pre_score
            file.write(str(pre_score))

            file.close()
            
            success_msg=Button(0,0,200,200,blue, "Saved successfully!", True, small_text,'c')
            success_msg.draw()
            #program sleeps so user can read message
            time.sleep(3)
            
            pygame.quit()
    
    
    


def pre_test(pre_test_list):

    global pre_score
    pre_score=tests(pre_test_list)
    pre_score_button = Button(20,30,screen_width*0.5,screen_height*0.5, white,"Your score was:" + str(pre_score) ,True, medium_text, 'c')
    pre_score_button.draw()
    time.sleep(2)
    return pre_score



def post_test(pre_test_list):

    global post_score
    post_test_list = random.sample(pre_test_list, len(pre_test_list))
    post_score = tests(post_test_list)
    time.sleep(2)
    return post_score




def create_main_list(question_file):
    main_list=[]
    #open file in read mode
    with open(question_file,'r') as file:
        #read file in dictionary format
        csv_reader = csv.DictReader(file, delimiter=',')
        for row in csv_reader:
            new_question={}
            new_question['question']=row["Question"]
            new_question['options']=row["Option A"], row["Option B"], row["Option C"], row["Option D"]
            new_question['climate ranking']= row["Climate_Ranking_A"], row["Climate_Ranking_B"],row["Climate_Ranking_C"],row["Climate_Ranking_D"]
            new_question['expenses ranking'] = row["Expenses_Ranking_A"],row["Expenses_Ranking_B"],row["Expenses_Ranking_C"],row["Expenses_Ranking_D"]
            main_list.append(new_question)
    return main_list

def expenses_decisions(main_list, budget, answer, question_index):
    acceptable_answers = ['a', 'b', 'c', 'd']
    if main_list[question_index-1]['expenses ranking'][acceptable_answers.index(answer)] == '1': #1 - least expensive
        budget-=1
    elif main_list[question_index-1]['expenses ranking'][acceptable_answers.index(answer)] == '2':
        budget-=2
    elif main_list[question_index-1]['expenses ranking'][acceptable_answers.index(answer)] == '3':
        budget-=3
    elif main_list[question_index-1]['expenses ranking'][acceptable_answers.index(answer)] == '4':#most expensive
        budget-=5
        
    global budget_tracker
    budget_tracker.append(budget)
    
    return budget

def climate_decisions(main_list, greenhouse_effect, answer, question_index):
    acceptable_answers = ['a', 'b', 'c', 'd']
    feedback=''
    if main_list[question_index]['climate ranking'][acceptable_answers.index(answer)] == '1':#best for climate
        feedback="Well done for making such a great decision!"
    elif main_list[question_index]['climate ranking'][acceptable_answers.index(answer)] == '2':
        feedback="Not bad, keep going!"
        greenhouse_effect+=0.0005
    elif main_list[question_index]['climate ranking'][acceptable_answers.index(answer)] == '3':
        feedback="Careful! Remember, there are lots of people counting on you.."
        greenhouse_effect+=0.015
    elif main_list[question_index]['climate ranking'][acceptable_answers.index(answer)] == '4':#worst for climate
        feedback="Oh no! People aren't very happy with your decisions..."
        greenhouse_effect+=0.025
        
    global greenhouse_tracker
    greenhouse_tracker.append(greenhouse_effect)
    return greenhouse_effect, feedback

def calculate_temperature(greenhouse_effect, albedo):
    pi = 3.14159
    sigma = 5.6703e-8 # e is '10^'
    mass_of_sun = 1.989e30
    distance = 1.496e11
    # Albedo and greenhouse_effect are the two variables that can be changed
    solar_luminosity = 3.846e26
    

    # Effective temperature
    T_eff = math.sqrt(math.sqrt((1 - albedo) * solar_luminosity / (4 * pi * sigma))) * 1 / math.sqrt(2 * distance)
    
    # Equivalent temperature below, which is temperature when the system is in equilibrium (energy is balanced)
    T_eq = (T_eff**2) * (1+(0.24 * greenhouse_effect))

    # Temperature in Kelvin
    T_kel = math.sqrt(T_eq/0.9)
    
    # Converting to Celsius
    T_cel = T_kel - 273
    return T_cel

def calculate_sea_level(temp_changes):
    if temp_changes: #prevents function from executing when array is empty
        global sea_level_rise
        sea_level_rise=(temp_changes[-1])*2.3
    return sea_level_rise

def calulate_albedo(sea_level_rise):
    global albedo
    albedo-=(0.0005*sea_level_rise)
    return albedo

def update_sea(temp_changes):
    global sea_level_rise
    sea_level_rise = calculate_sea_level(temp_changes)
    global albedo
    albedo = calulate_albedo(sea_level_rise)
    global sea_levels
    sea_levels.append(sea_level_rise)
    return sea_level_rise, sea_levels, albedo



def update_temps(greenhouse_effect, temps, temp_changes, year, albedo, temp_rise):
    global current_temp
    current_temp=calculate_temperature(greenhouse_effect, albedo)
    if temps:
        temp_rise = current_temp - temps[-1]
        temp_changes.append(temp_rise)
        global total_temp_rise
        total_temp_rise+=temp_rise
    temps.append(current_temp) # difference between the current temperature and last year's temperature
    time_jumps.append(year)
    
    return temps, temp_rise, temp_changes, time_jumps, total_temp_rise


global end
end=False

def endings(budget):
    global end
    global temps
    global temp_rise
    message=''
    query=''
    tipping_point=False
    if  budget<= 0:
        end=True
        message=str("Oh no! You ran out of money… Better luck next time! The global average temperature was"+ str(round(temps[-1],1))+ "degrees Celsius, which was a"+ str(round(temp_rise,1))+ "degrees Celsius rise from last year.")
        query='money'

    elif temp_rise >= 1.5:
        end=True
        message=str("Oh no! You failed to stop global warming in time. You were left with "+ str(budget)+ " budget points. The global average temperature was"+ str(round(temps[-1],2))+ "degrees Celsius, which was a "+ str(round(temp_rise,1))+ " degrees Celsius rise from last year.")
        query='global warming'
        
    elif 0.8<=temp_rise<1:
        budget-=5
        tipping_point=True
        message = str("Your city experiences harsh drought due to rising temperatures. You have to hand out bottled water and put limits on household use of it too. This uses up 5 budget points... You now have "+ str(budget)+ " budget points.")
        query='drought'
        
    elif sea_level_rise>0.90:
        budget-=5
        tipping_point=True
        message=str("Your city experiences flooding due to rising sea levels. The repairs to infrastructure take 5 budget points... You now have "+ str(budget)+ " budget points.")
        query='floods'
        
    elif temps[-1]>30:
        end=True
        message=str("Oh no! The average global temperature rose above 30°C. 35 degrees Celsius is the absolute limit of human tolerance. Better luck next time! You were left with"+ str(budget)+ "budget points.The global average temperature was"+ str(round(temps[-1],2))+ "degrees Celsius, which was a "+ str(round(temp_rise,1))+ " degrees Celsius rise from last year.")
        query='forest fire'
        
    else:
        pass
      
    if tipping_point==True:
        #creating the tipping point screen
        screen.fill(blue)
        image_credit, link = image(query)
        credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
        credit.draw()
        message_text=str(message).strip("('')',")

        message_button = Button(screen_width*0.1, screen_height*0.7, screen_width*0.7,500, green, message, True, medium_text, 'n')
        message_button.draw()
        pygame.display.flip()
        time.sleep(5)

    if end==True:
        #creating the ending screen
        screen.fill(blue)
        image_credit, link = image(query)
        credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
        credit.draw()
        message_text=str(message).strip("('')',")

        message_button = Button(screen_width*0.1, screen_height*0.7, screen_width*0.7,500, green, message, True, medium_text, 'n')
        message_button.draw()
        pygame.display.flip()
        time.sleep(5)
        global sea_levels
        global pre_score
        global post_score
        global time_jumps
        end_screen(pre_score, post_score, temps, sea_levels, time_jumps)
        
        
    return budget


def help_screen():
    help_needed=True
    #needed to get back
    surface_list=[]
    screen_surface = pygame.display.get_surface()
    initial_screen_copy = screen_surface.copy()
    screen_copy=screen_surface.copy()
    surface_list.append(screen_copy)
    screen.fill(blue)
    
    #same mechanism as pause function
    help_surface=pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    pygame.draw.rect(help_surface,(0,0,0,0), [0,0, screen_width, screen_height]) # 4th value is opacity
    screen.blit(help_surface,(0,0))
    pygame.display.flip()
        
    #welcome text
    screen_number=0
    title="The Basics:"
    text = "You have 100 budget points and every decision you make will have cost points so use them wisely! Make sure that the temperature and sea level rise stay fairly constant too, or else you'll be putting everyone on the planet in danger!"
        
    welcome_title =Button(20,30,screen_width,screen_height*0.1, blue,title ,True, medium_text, 'x')
    welcome_title.draw()
    #welcome message
    welcome_text= Button(50,150,screen_width-150,screen_height-150, blue, text,True, medium_text, 'n')
    welcome_text.draw()

    #back button
    back_button = Button(40,575, 150, 100, green, "Back", False, medium_text, 'n')
    back_button.draw()
    
    pygame.display.flip()
    
    while help_needed==True:
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked():
                    help_needed=False
                    screen.blit(initial_screen_copy, (0,0))
                    pygame.display.flip()
                    

def tutorial_screen():
    help_needed=True
    #needed to get back to screen before help was clicked
    surface_list=[]
    screen_surface = pygame.display.get_surface()
    initial_screen_copy = screen_surface.copy()
    screen_copy=screen_surface.copy()
    surface_list.append(screen_copy)
    screen.fill(blue)
    
    #same mechanism as pause function
    help_surface=pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    pygame.draw.rect(help_surface,(0,0,0,0), [0,0, screen_width, screen_height]) # 4th value is opacity
    screen.blit(help_surface,(0,0))
    pygame.display.flip()

    #welcome text
    screen_number=0
    titles_list=["Welcome to EarthSaver:Climate Challenge","1. The Basics:","2. Objectives", "3. Levels:"]
    text_list = [("This is the ultimate climate change simulator game where you, the newly elected leader, have the power to shape the future of our planet for the next 30 years. Your mission is to make decisions that will help combat climate change, maintain a healthy budget, and save the Earth from environmental disasters."), ("Before you embark on your journey as Earth's leader, you'll take a multiple-choice test to gauge your initial knowledge about climate change. After the game, you'll take the test again to see how much you've learned. You start the game with 100 budget points. Every decision you make costs a certain number of points, so spend wisely! If you run out of budget points, you lose the game."),(" Your goal is to keep the global temperature from rising too high. You can monitor this in the stats bar, alongside sea level rise and the current global temperature. Pay attention to the trends and make decisions to stabilize or reduce the temperature. "),("There are three levels in the game, each containing 10 situations. In each situation, you'll be presented with four options. Choose wisely to ensure a sustainable and safe future for the planet. Top tip: Be cautious! If you choose options that harm the environment, surprise tipping points may occur. These unexpected events will deduct points from your budget, making it even more challenging to achieve your goals. Click next if you're ready to begin!")]
    #rename vars!
    welcome_title =Button(20,30,screen_width,screen_height*0.1, blue,titles_list[screen_number] ,True, medium_text, 'x')
    welcome_title.draw()
    #welcome message
    welcome_text= Button(50,150,screen_width-150,screen_height-150, blue, text_list[screen_number],True, medium_text, 'n')
    welcome_text.draw()
    #next button
    next_button = Button(1000,575, 150, 100, green, "Next", False, medium_text, 'n')
    next_button.draw()

    
    pygame.display.flip()
    
    while help_needed==True:
        pygame.display.update()
        for event in pygame.event.get(): 
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.is_clicked() and screen_number<3:
                    screen_surface = pygame.display.get_surface()
                    screen_copy = screen_surface.copy()
                    surface_list.append(screen_copy)
                    help_surface.fill(blue)
                    welcome_title =Button(20,30,screen_width,screen_height*0.1, blue,titles_list[screen_number+1] ,True, large_text, 'x')
                    welcome_title.draw()
                    #welcome message
                    welcome_text= Button(50,150,screen_width-150,screen_height-150, blue, text_list[screen_number+1],True, medium_text, 'n')
                    welcome_text.draw()
                
                    pygame.display.flip()
                    if screen_number<3:
                        screen_number+=1
                        next_button.draw()
                elif next_button.is_clicked() and screen_number ==3:
                        help_needed=False
                        screen.fill(blue)
                        
                

pause = False

def pause_screen(pause, surface):
    pause_surface= pygame.Surface((screen_width, screen_height), pygame.SRCALPHA)
    if pause== True:
        #needed for pause function
        screen_surface = pygame.display.get_surface()
        screen_copy = screen_surface.copy()
        pygame.draw.rect(pause_surface,(128,128,128,150), [0,0, screen_width, screen_height]) # 4th value is opacity
        screen.blit(pause_surface,(0,0))
        pygame.display.flip()
        
        #help button
        help_button= Button(300,200,200,100, green, "Help",False, medium_text,'n')
        help_button.draw()
        
        #save button
        save_button = Button(700,200,200,100,green, "Save", False, medium_text, 'n')
        save_button.draw()

        
        #resume button
        resume_button = Button(0,380,200,100,dark_blue, "Resume", False, medium_text, 'x')
        resume_button.draw()
        
        #update the display
        pygame.display.flip()
        
        while pause:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if help_button.is_clicked():
                        help_screen()
                        pause=True
                    elif resume_button.is_clicked():
                        pause=False
                    elif save_button.is_clicked():
                        save()
                    

                    

    if pause == False:
        screen.blit(surface, (0,0))
        pygame.display.flip()
        
def undo(copy):
    
    global greenhouse_effect
    global greenhouse_tracker
    greenhouse_effect=greenhouse_tracker.pop()
    
    global temps
    global current_temp
    current_temp= temps.pop()
    
    global temp_changes
    difference=temp_changes[-1]
    
    global sea_levels
    global sea_level_rise
    sea_level_rise=sea_levels.pop()
    
    global total_temp_rise
    total_temp_rise-=difference
    
    global albedo
    albedo+=(0.0005*sea_level_rise)
    
    global budget
    global budget_tracker
    budget=budget_tracker[-2]
    budget_tracker.pop()
    
    global temp_rise

    temp_rise=temp_changes.pop()

    global year
    year-=1
    
    global question_number
    question_number-=1
    

    screen.fill(blue)
    screen.blit(copy,(0,0))

def image(question):


    client_id = "4Vwaw-8lwS3_QfivsLzQNvWsRhKyjiTNMXsqJ2OS7ao"
    client_secret = ""
    redirect_uri = ""
    code = ""

    auth = Auth(client_id, client_secret, redirect_uri, code=code)
    api = Api(auth)
    import requests
    import pygame

    category = str(question)
    # Fetch image data
    url = f"https://api.unsplash.com/photos/random?query={category}&orientation=landscape&client_id=4Vwaw-8lwS3_QfivsLzQNvWsRhKyjiTNMXsqJ2OS7ao"
    data = requests.get(url).json()
    img_data = requests.get(data["urls"]["regular"]).content
    
    #credits
    user_data = data["user"]
    name= user_data["name"] + " /unsplash"
    
    # Initialize pygame
    pygame.init()

    # Load image from byte data
    image = pygame.image.load(BytesIO(img_data))
    DEFAULT_IMAGE_SIZE = (1000, 375)
 
    # Scale the image to your needed size
    image = pygame.transform.scale(image, DEFAULT_IMAGE_SIZE)

    # Draw the image to the screen
    screen.blit(image, (50, 65))
    
    
    #link to photographer's profile
    links = user_data["links"]
    profile_link=links["html"]
    
    return name, profile_link


def level_one(main_list):
    global greenhouse_effect
    global temps
    global temp_changes
    global sea_level_rise
    global total_temp_rise
    global albedo
    global budget
    global temp_rise
    global level
    level+=1
    global year
    global current_temp
    global end
    global sea_levels
    pause=False
    main_questions=create_main_list(main_list)
    answer=''
    answer_click=False
    screen.fill(blue)
   
    global question_number
    question=main_questions[question_number]

    while question_number<10 and not end:
            question=main_questions[question_number]
            screen.fill(blue)
            if question_number>2:
                undo_button= Button((screen_width*0.5),(screen_height*0.02),120,100,red, "Undo",True, medium_text,'n')
                undo_button.draw()
            answer_click=False
            
            #Pause Button
            pause_button = Button ((screen_width*0.85),(screen_height*0.02),120,100,red, "Menu",True, medium_text,'n')
            pause_button.draw()
            #show year in top left
            year_stat =Button((screen_width*0.01),(screen_height*0.02),310,100,red, "Year: "+str(year),True, medium_text,'n')
            year_stat.draw()
            
            #stats panel drawn
            stats_panel=Button((screen_width*0.70),(screen_height*0.70),300,150,red, "Stats:",True, medium_text,'n')
            stats_panel.draw()
            
            #budget block
            budget_change=0
            if len(budget_tracker)>1:
                #difference between the last 2 elements of the array
                budget_change = budget_tracker[-1] - budget_tracker[-2]
                budget_text=str("Budget: "+ str(budget)+ ("(")+str(budget_change) + "pts)")
            else:
                budget_text=str("Budget: "+ str(budget))

            budget_stat=Button((screen_width*0.70),(screen_height*0.76),300,50,white, budget_text,True, small_text,'n')
            budget_stat.draw()
                                        
            #current temperature block
            if temps:
                current_temp=round(temps[-1],1)
            else:
                current_temp=14.0
            temp_text="Current Temperature: "+str(current_temp)
            temp_stat=Button((screen_width*0.70),(screen_height*0.80),300,50,white, temp_text,True, small_text,'n')
            temp_stat.draw()
                    
            #temperature rise from last year block
            temp_rise_text= "Temperature rise: "+str(round(temp_rise,2))
            temp_rise_stat=Button((screen_width*0.70),(screen_height*0.84),300,50,white, temp_rise_text,True, small_text,'n')
            temp_rise_stat.draw()
                    
            #sea level rise from last year block
            sea_level_rise_text="Sea level rise: "+ str(round(sea_level_rise,2))
            sea_level_rise_stat=Button((screen_width*0.70),(screen_height*0.88),300,50,white, sea_level_rise_text,True, small_text,'n')
            sea_level_rise_stat.draw()
            
            #question
            question_content=str(question_number+1) + ". " + question['question'].strip('""')
            #image credits
            image_credit, link = image(question_content)
            credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
            credit.draw()
            #display the question
            question_button=Button((screen_width*0.01), (screen_height*0.07), (screen_width),(screen_height*0.15), blue, question_content,True, question_text, 'n')
            question_button.draw()
            
            # for each option, print a letter and then the text
            for option in question['options']:
                letters=['a) ','b) ','c) ','d) ']
                #draw option buttons
                if question['options'].index(option)==0: #if this is the first option in the list, since lists in python are zero-indexed
                    option_a=Button((screen_width*0.035),(screen_height*0.65),660, 60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_a.draw()
                elif question['options'].index(option)==1:
                    option_b=Button((screen_width*0.035),(screen_height*0.74),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_b.draw()
                elif question['options'].index(option)==2:
                    option_c=Button((screen_width*0.035),(screen_height*0.83),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_c.draw()
                elif question['options'].index(option)==3:
                    option_d=Button((screen_width*0.035),(screen_height*0.92),660,60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_d.draw()
            #needed for pause function
            screen_surface = pygame.display.get_surface()
            screen_copy = screen_surface.copy()
            
            #condition controlled loop - so user can only click on a button once to prevent crashing from multiple inputs
            while answer_click==False:
                pygame.display.update()
                #event handler
                for event in pygame.event.get():
                    #quit game
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        #pause
                        if event.key == pygame.K_SPACE:
                            if pause == False:
                                pause=True
                                pause_screen(pause, screen_copy)
                                # inverts the current state of the boolean variable pause so pause can be toggled
                                pause=False
                    #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause_button.is_clicked():
                            if pause == False:
                                    pause=True
                                    pause_screen(pause, screen_copy)
                                    # inverts the current state of the boolean variable pause so pause can be toggled
                                    pause=False
                        #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                        # Check for mouse click within the text surface area
                        if credit.is_clicked():

                            webbrowser.open(link)
                        #input processing blocks below
                        if question_number>2:
                            if undo_button.is_clicked():
                                undo(undo_screen_copy)
                        if option_a.is_clicked():
                            answer='a'
                            answer_click=True

                        elif option_b.is_clicked():
                            answer='b'
                            answer_click=True

                        elif option_c.is_clicked():
                            answer='c'
                            answer_click=True

                        elif option_d.is_clicked():
                            answer='d'
                            answer_click=True
                        
                        else:
                            pygame.display.update()
                            
 
                        acceptable_answers= ['a','b','c','d']
                        if answer_click==True and answer in acceptable_answers:
                            screen_surface = pygame.display.get_surface()
                            undo_screen_copy = screen_surface.copy()
                            greenhouse_effect, feedback = climate_decisions(main_questions, greenhouse_effect, answer, question_number)
                            temps, temp_rise, temp_changes, time_jumps, total_temp_rise=update_temps(greenhouse_effect, temps, temp_changes, year, albedo, temp_rise)
                            sea_level_rise, sea_levels, albedo = update_sea(temp_changes)
                            #feedback block
                            feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                            feedback_display.draw()
                            pygame.display.flip()
                            time.sleep(2)
                                
                            budget = expenses_decisions(main_questions, budget, answer, question_number)
                            budget=endings(budget)
                            year+=1
                            answer_click=True
                                                    
                            #counter is incremented every time a question is answered, so if a user decides to save their game, they will start with the question they haven't answered yet
                            question_number+=1
                        
                            #blit all to screen
                            pygame.display.update()


                 
def level_two(main_list):

    global greenhouse_effect
    global temps
    global temp_changes
    global sea_level_rise
    global total_temp_rise
    global albedo
    global budget
    global temp_rise
    global level
    level+=1
    global year
    global current_temp
    global end
    global sea_levels
    pause=False
    main_questions=create_main_list(main_list)
    answer=''
    answer_click=False
    screen.fill(blue)
   
    global question_number
    question=main_questions[question_number]

    while 10<=question_number<20 and not end:
            question=main_questions[question_number]
            screen.fill(blue)
            if question_number>12:
                undo_button= Button((screen_width*0.5),(screen_height*0.02),120,100,red, "Undo",True, medium_text,'n')
                undo_button.draw()
            answer_click=False
            
            #Pause Button
            pause_button = Button ((screen_width*0.85),(screen_height*0.02),120,100,red, "Menu",True, medium_text,'n')
            pause_button.draw()
            #show year in top left
            year_stat =Button((screen_width*0.01),(screen_height*0.02),310,100,red, "Year: "+str(year),True, medium_text,'n')
            year_stat.draw()
            
            #stats panel drawn
            stats_panel=Button((screen_width*0.70),(screen_height*0.70),300,150,red, "Stats:",True, medium_text,'n')
            stats_panel.draw()
            
            #budget block
            budget_change=0
            if len(budget_tracker)>1:
                #difference between the last 2 elements of the array
                budget_change = budget_tracker[-1] - budget_tracker[-2]
                budget_text=str("Budget: "+ str(budget)+ ("(")+str(budget_change) + "pts)")
            else:
                budget_text=str("Budget: "+ str(budget))

            budget_stat=Button((screen_width*0.70),(screen_height*0.76),300,50,white, budget_text,True, small_text,'n')
            budget_stat.draw()
                                        
            #current temperature block
            if temps:
                current_temp=round(temps[-1],1)
            else:
                current_temp=14.0
            temp_text="Current Temperature: "+str(current_temp)
            temp_stat=Button((screen_width*0.70),(screen_height*0.80),300,50,white, temp_text,True, small_text,'n')
            temp_stat.draw()
                    
            #temperature rise from last year block
            temp_rise_text= "Temperature rise: "+str(round(temp_rise,2))
            temp_rise_stat=Button((screen_width*0.70),(screen_height*0.84),300,50,white, temp_rise_text,True, small_text,'n')
            temp_rise_stat.draw()
                    
            #sea level rise from last year block
            sea_level_rise_text="Sea level rise: "+ str(round(sea_level_rise,2))
            sea_level_rise_stat=Button((screen_width*0.70),(screen_height*0.88),300,50,white, sea_level_rise_text,True, small_text,'n')
            sea_level_rise_stat.draw()
            
            #question
            question_content=str(question_number+1) + ". " + question['question'].strip('""')
            #image credits
            image_credit, link = image(question_content)
            credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
            credit.draw()
            #display the question
            question_button=Button((screen_width*0.01), (screen_height*0.07), (screen_width),(screen_height*0.15), blue, question_content,True, question_text, 'n')
            question_button.draw()
            
            # for each option, print a letter and then the text
            for option in question['options']:
                letters=['a) ','b) ','c) ','d) ']
                #draw option buttons
                if question['options'].index(option)==0: #if this is the first option in the list, since lists in python are zero-indexed
                    option_a=Button((screen_width*0.035),(screen_height*0.65),660, 60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_a.draw()
                elif question['options'].index(option)==1:
                    option_b=Button((screen_width*0.035),(screen_height*0.74),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_b.draw()
                elif question['options'].index(option)==2:
                    option_c=Button((screen_width*0.035),(screen_height*0.83),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_c.draw()
                elif question['options'].index(option)==3:
                    option_d=Button((screen_width*0.035),(screen_height*0.92),660,60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_d.draw()
            #needed for pause function
            screen_surface = pygame.display.get_surface()
            screen_copy = screen_surface.copy()
            
            #condition controlled loop - so user can only click on a button once to prevent crashing from multiple inputs
            while answer_click==False:
                pygame.display.update()
                #event handler
                for event in pygame.event.get():
                    #quit game
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        #pause
                        if event.key == pygame.K_SPACE:
                            if pause == False:
                                pause=True
                                pause_screen(pause, screen_copy)
                                # inverts the current state of the boolean variable pause so pause can be toggled
                                pause=False
                    #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause_button.is_clicked():
                            if pause == False:
                                    pause=True
                                    pause_screen(pause, screen_copy)
                                    # inverts the current state of the boolean variable pause so pause can be toggled
                                    pause=False
                        #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                        # Check for mouse click within the text surface area
                        if credit.is_clicked():

                            webbrowser.open(link)
                        #input processing blocks below
                        if question_number>12:
                            if undo_button.is_clicked():
                                undo(undo_screen_copy)
                        if option_a.is_clicked():
                            answer='a'
                            answer_click=True

                        elif option_b.is_clicked():
                            answer='b'
                            answer_click=True

                        elif option_c.is_clicked():
                            answer='c'
                            answer_click=True

                        elif option_d.is_clicked():
                            answer='d'
                            answer_click=True
                        
                        else:
                            pygame.display.update()
                            
 
                        acceptable_answers= ['a','b','c','d']
                        if answer_click==True and answer in acceptable_answers:
                            screen_surface = pygame.display.get_surface()
                            undo_screen_copy = screen_surface.copy()
                            greenhouse_effect, feedback = climate_decisions(main_questions, greenhouse_effect, answer, question_number)
                            temps, temp_rise, temp_changes, time_jumps, total_temp_rise=update_temps(greenhouse_effect, temps, temp_changes, year, albedo, temp_rise)
                            sea_level_rise, sea_levels, albedo = update_sea(temp_changes)
                            #feedback block
                            feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                            feedback_display.draw()
                            pygame.display.flip()
                            time.sleep(2)
                                
                            budget = expenses_decisions(main_questions, budget, answer, question_number)
                            budget=endings(budget)
                            year+=1
                            answer_click=True
                                                    
                            #counter is incremented every time a question is answered, so if a user decides to save their game, they will start with the question they haven't answered yet
                            question_number+=1
                            
                        
                            #blit all to screen
                            pygame.display.update()

def level_three(main_list):
    global greenhouse_effect
    global temps
    global temp_changes
    global sea_level_rise
    global total_temp_rise
    global albedo
    global budget
    global temp_rise
    global level
    level+=1
    global year
    global current_temp
    global end
    global sea_levels
    pause=False
    main_questions=create_main_list(main_list)
    answer=''
    answer_click=False
    screen.fill(blue)
   
    global question_number
    question=main_questions[question_number]

    while 20<=question_number<30 and not end:
            question=main_questions[question_number]
            screen.fill(blue)
            if question_number>22:
                undo_button= Button((screen_width*0.5),(screen_height*0.02),120,100,red, "Undo",True, medium_text,'n')
                undo_button.draw()
            answer_click=False
            
            #Pause Button
            pause_button = Button ((screen_width*0.85),(screen_height*0.02),120,100,red, "Menu",True, medium_text,'n')
            pause_button.draw()
            #show year in top left
            year_stat =Button((screen_width*0.01),(screen_height*0.02),310,100,red, "Year: "+str(year),True, medium_text,'n')
            year_stat.draw()
            
            #stats panel drawn
            stats_panel=Button((screen_width*0.70),(screen_height*0.70),300,150,red, "Stats:",True, medium_text,'n')
            stats_panel.draw()
            
            #budget block
            budget_change=0
            if len(budget_tracker)>1:
                #difference between the last 2 elements of the array
                budget_change = budget_tracker[-1] - budget_tracker[-2]
                budget_text=str("Budget: "+ str(budget)+ ("(")+str(budget_change) + "pts)")
            else:
                budget_text=str("Budget: "+ str(budget))

            budget_stat=Button((screen_width*0.70),(screen_height*0.76),300,50,white, budget_text,True, small_text,'n')
            budget_stat.draw()
                                        
            #current temperature block
            if temps:
                current_temp=round(temps[-1],1)
            else:
                current_temp=14.0
            temp_text="Current Temperature: "+str(current_temp)
            temp_stat=Button((screen_width*0.70),(screen_height*0.80),300,50,white, temp_text,True, small_text,'n')
            temp_stat.draw()
                    
            #temperature rise from last year block
            temp_rise_text= "Temperature rise: "+str(round(temp_rise,2))
            temp_rise_stat=Button((screen_width*0.70),(screen_height*0.84),300,50,white, temp_rise_text,True, small_text,'n')
            temp_rise_stat.draw()
                    
            #sea level rise from last year block
            sea_level_rise_text="Sea level rise: "+ str(round(sea_level_rise,2))
            sea_level_rise_stat=Button((screen_width*0.70),(screen_height*0.88),300,50,white, sea_level_rise_text,True, small_text,'n')
            sea_level_rise_stat.draw()
            
            #question
            question_content=str(question_number+1) + ". " + question['question'].strip('""')
            #image credits
            image_credit, link = image(question_content)
            credit= Button(720,450, 0,0,blue, image_credit,False, small_text, 'n')
            credit.draw()
            #display the question
            question_button=Button((screen_width*0.01), (screen_height*0.07), (screen_width),(screen_height*0.15), blue, question_content,True, question_text, 'n')
            question_button.draw()
            
            # for each option, print a letter and then the text
            for option in question['options']:
                letters=['a) ','b) ','c) ','d) ']
                #draw option buttons
                if question['options'].index(option)==0: #if this is the first option in the list, since lists in python are zero-indexed
                    option_a=Button((screen_width*0.035),(screen_height*0.65),660, 60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_a.draw()
                elif question['options'].index(option)==1:
                    option_b=Button((screen_width*0.035),(screen_height*0.74),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_b.draw()
                elif question['options'].index(option)==2:
                    option_c=Button((screen_width*0.035),(screen_height*0.83),660,60,green, letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_c.draw()
                elif question['options'].index(option)==3:
                    option_d=Button((screen_width*0.035),(screen_height*0.92),660,60,green,letters[question['options'].index(option)]+option.strip('"'),True, option_text,'n')
                    option_d.draw()
            #needed for pause function
            screen_surface = pygame.display.get_surface()
            screen_copy = screen_surface.copy()
            
            #condition controlled loop - so user can only click on a button once to prevent crashing from multiple inputs
            while answer_click==False:
                pygame.display.update()
                #event handler
                for event in pygame.event.get():
                    #quit game
                    if event.type == pygame.QUIT:
                        running = False
                        pygame.quit()
                        #pause
                        if event.key == pygame.K_SPACE:
                            if pause == False:
                                pause=True
                                pause_screen(pause, screen_copy)
                                # inverts the current state of the boolean variable pause so pause can be toggled
                                pause=False
                    #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pause_button.is_clicked():
                            if pause == False:
                                    pause=True
                                    pause_screen(pause, screen_copy)
                                    # inverts the current state of the boolean variable pause so pause can be toggled
                                    pause=False
                        #block only runs when game isn't paused
                    if event.type == pygame.MOUSEBUTTONDOWN and not pause:
                        # Check for mouse click within the text surface area
                        if credit.is_clicked():

                            webbrowser.open(link)
                        #input processing blocks below
                        if question_number>2:
                            if undo_button.is_clicked():
                                undo(undo_screen_copy)
                        if option_a.is_clicked():
                            answer='a'
                            answer_click=True

                        elif option_b.is_clicked():
                            answer='b'
                            answer_click=True

                        elif option_c.is_clicked():
                            answer='c'
                            answer_click=True

                        elif option_d.is_clicked():
                            answer='d'
                            answer_click=True
                        
                        else:
                            pygame.display.update()
                            
 
                        acceptable_answers= ['a','b','c','d']
                        if answer_click==True and answer in acceptable_answers:
                            screen_surface = pygame.display.get_surface()
                            undo_screen_copy = screen_surface.copy()
                            greenhouse_effect, feedback = climate_decisions(main_questions, greenhouse_effect, answer, question_number)
                            temps, temp_rise, temp_changes, time_jumps, total_temp_rise=update_temps(greenhouse_effect, temps, temp_changes, year, albedo, temp_rise)
                            sea_level_rise, sea_levels, albedo = update_sea(temp_changes)
                            #feedback block
                            feedback_display= Button(0,0,500,125,white, feedback,True, medium_text,'c')
                            feedback_display.draw()
                            pygame.display.flip()
                            time.sleep(2)
                                
                            budget = expenses_decisions(main_questions, budget, answer, question_number)
                            budget=endings(budget)
                            year+=1
                            answer_click=True
                                                    
                            #counter is incremented every time a question is answered, so if a user decides to save their game, they will start with the question they haven't answered yet
                            question_number+=1
                            
                        
                            #blit all to screen
                            pygame.display.update()

                

def valid_load_file():
    #get file name from user input
    #cast to avoid type errors when concatenating
    file_name=str(input_box("Type filename and press enter:")).strip("''")
    #double black slash needed to denote one backslash as a char in python
    path = os.getcwd()+'\\'+ file_name +'.txt'
    isFile=os.path.isfile(path)
    while not isFile:
        valid_load_file()

    return file_name



def load():
    file_name=valid_load_file()
    with open(file_name+'.txt','r') as file:
        content = file.readlines()

        global level
        level=int(content[0])


        global year
        year=int(content[1])
        
        global question_number
        question_number = int(content[2])

        global greenhouse_effect
        greenhouse_effect = float(content[3])
        
        global temps
        temps = ast.literal_eval(content[4])
  

        global temp_changes
        temp_changes= ast.literal_eval(content[5])
        
        global sea_level_rise
        sea_level_rise = ast.literal_eval(content[6])
        
        global total_temp_rise
        total_temp_rise=float(content[7])
        
        global albedo
        albedo=float(content[8])
        
        global budget
        budget = int(content[9])
        
        global temp_rise
        temp_rise = float(content[10])
        
        global current_temp
        current_temp = float(content[11])

        
        global pre_score
        pre_score=int(content[12])
        
        screen.fill(blue)
        
        success_msg=Button(0,0,200,200,blue, "Loaded successfully!", True, small_text,'c')
        success_msg.draw()
        pygame.display.update()
        #program sleeps so user can read message
        time.sleep(3)
        
        
    
    

def graphs(temps, sea_levels, time_jumps):

    # Create a figure for both graphs
    fig, (temp_axis,sea_axis) = plt.subplots(1,2,figsize=(12, 6))
    # Plot temperature data
    temp_axis.plot(time_jumps, temps)
    temp_axis.set_title("How temperature changed against time")
    temp_axis.set_xlabel('Time')
    temp_axis.set_ylabel('Temperature')


    # Plot sea level data
    sea_axis.plot(time_jumps, sea_levels)
    sea_axis.set_title("How sea level rise changed against time")
    sea_axis.set_xlabel('Time')
    sea_axis.set_ylabel('Sea Level Rise')

    #save figures as one image
    plt.suptitle('Close this window to return to the game!')
    plt.show()
    

def level_stats(level, temps, sea_levels, time_jumps):
    
    graphs(temps, sea_levels, time_jumps)
    
    global screen
    screen.fill(blue)
    pygame.display.flip()
    # Initialize Pygame and set window size
    pygame.init()
    global screen_width
    screen_width+=290
    global screen_height
    screen_height+=200
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
    screen.fill(blue)
    #draw title to screen
    title=Button(0,(screen_height*0.1),0,0, blue, "End of Level "+str(level),False, medium_text,'x')
    title.draw()
    
    #choose a random line from the hints file to display
    #inclusive for upper and lower limit
    number= random.randint(0,5)
    with open('hints.txt','r') as file:
        content=file.readlines()
        hint_text=(content[number]).strip()
        
    hints=Button(90,(screen_height*0.3),screen_width,screen_height*0.5, blue,hint_text, True, medium_text, 'c')
    hints.draw()
    
    #next button
    next_button = Button(screen_width*0.75, screen_height*0.8, 150, 100, green, "Next", False, medium_text, 'n')
    next_button.draw()
    
    pygame.display.flip()

    hints=True
    #event handling
    while hints == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                    running = False
            elif event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_q:
                    running = False
                    pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if next_button.is_clicked():
                    hints=False
                    screen.fill(blue)
                    
def end_screen(pre_score, post_score, temps, sea_levels, time_jumps):
    #create graphs
    graphs(temps, sea_levels, time_jumps)
    #knowledge change block
    percent_change=0
    text=""
    #resizing screen
    global screen_width
    screen_width+=100
    global screen_height
    screen_height+=100
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.SCALED)
    screen.fill(blue)
    pygame.display.update()

    
    if pre_score<post_score: #knowledge improved
        #rounds to 1dp
        percent_change= round((((post_score-pre_score)/10)*100),1)

        text="Your knowledge has improved by "+str(percent_change)+"%! Well done."
    elif pre_score>=post_score: #knowledge worsened
        #rounds to 1dp
        text="Your knowledge hasn't quite improved yet. Play again!"

    text_cleaned=text.strip('"()"')
    title=Button(0,screen_height*0.02,0,0,blue, "The End!", True, large_text, 'x')
    title.draw()
    knowledge_button=Button(0, screen_height*0.1,0,0,blue, text_cleaned, True, medium_text, 'n')
    knowledge_button.draw()
    #stats summary
    #budget summary
    budget_button=Button(0, screen_height*0.4,0,0,blue, "You were left with "+str(budget)+" budget points.", True, medium_text, 'n')
    budget_button.draw()
    #temp rise summary
    sea_level_total=0
    for i in range(len(sea_levels)):
        sea_level_total+=sea_levels[i]
        
    sea_level_total=round(sea_level_total,2)

    sea_level_button=Button(0, screen_height*0.6,0,0,blue, "Sea levels rose by "+str(sea_level_total)+"m since you came to power", True, medium_text, 'n')

    sea_level_button.draw()
    
    pygame.display.update()



    
    

#start screen buttons
load_game_button=Button(0,(screen_height*0.77),0,0, green, "Load Game", False, large_text,'x')
new_game_button=Button(0,(screen_height*0.87),0,0, green, "New Game",False, large_text,'x')
help_button= Button((screen_width*0.80),(screen_height*0.1),0,0, green, "Help",False, large_text,'n')

# background image
screen.fill(blue)
background=pygame.image.load("earth.png")
background_width,background_height=background.get_size()

#Game title
title_surf= large_text.render("Earth Saver", True, (255, 255, 255))
title_width, title_height = title_surf.get_size()
title_rect = title_surf.get_rect()
title_rect.topleft = ((screen_width - title_width)/2, (screen_height-title_height)/2)


#drawing to screen
screen.blit(background, ((screen_width-background_width)/2, (screen_height-background_height)/2))
load_game_button.draw()
new_game_button.draw()
help_button.draw()
screen.blit(title_surf, title_rect)



                    
                    
pygame.init()                  
running = True
while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
                pygame.quit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if help_button.is_clicked():
                help_screen()
            elif load_game_button.is_clicked():
                load()
                if level==1:
                    level_one(main_file)
                elif level==2:
                    level_two(main_file)
                elif level==3:
                    level_three(main_file)
                else:
                    pre_test(test_list)
                    
            elif new_game_button.is_clicked():
                tutorial_screen()
                test_list=create_question_list(test_file_name)
                pre_test(test_list)
                level_one(main_file)
                level_stats(level, temps, sea_levels, time_jumps)
                level_two(main_file)
                level_stats(level, temps, sea_levels, time_jumps)
                level_three(main_file)
                post_test(test_list)
                end_screen(pre_score, post_score, temps, sea_levels, time_jumps)
    