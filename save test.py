#new section 2
def save():

        #ask for name
        #check for no special chars
        #save file with current vars
        #display success message
        #name is passed as parameter
#need to save level?

    
    reject=False
    special_chars = ["'", '"', ".", "£"]
    while special_chars in name:
        reject=True
    name=str(name)
    if reject == False:
        with open(name+'.txt','w') as file:
            file.write(year+"\n")
            file.write(greenhouse_effect)
            file.write(temps)
            file.write(temp_changes)
            file.write(sea_level_rise)
            file.write(total_temp_rise)
            file.write(question_number)
            file.close()
            print("Success!")
            
            
        '''screen.fill(blue)
        save_button=(0,0,0,0,blue, "Save game?", True, large_text, 'c')
        save_button.draw()
        yes_button=Button(screen_width*0.2, screen_height*0.7, 100,100, "Yes", True, small_text, 'n')'''
            
        ''' #display success message
        screen.fill(blue)
        success_button = Button(0, 0, 300, 250, green, "Save successful! Quitting now",True, medium_text, 'c')
        success_button.draw()
        time.sleep()
        pygame.quit()'''

def validation(name):
    #avoid type error
    name=str(name)
    special_chars = [ '\\', '/', ':', '*', '?', '"', '<', '>', '|', '.', ',','!' ]
    valid=False
    for char in special_chars:
        if char in name:
            valid= False
            break
        else:
            valid= True
            
    return valid





def save():

    #clear screen
    screen.fill((255,255,255))
    pygame.display.update()

    #initialise font and colours for text and box
    font = pygame.font.Font(None, 32)
    box_colour = pygame.Color('gray')
    text_colour = pygame.Color('black')

    input_text = ""
    active = False
    cursor_pos = 0

    box_width = 200
    box_height = 32
    box_rect = pygame.Rect((screen_width - box_width) // 2, (screen_height - box_height) // 2, box_width, box_height)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.pos[0] >= box_rect.left and event.pos[0] <= box_rect.right and event.pos[1] >= box_rect.top and event.pos[1] <= box_rect.bottom:
                    active = not active
            elif event.type == pygame.KEYDOWN and active:
                if event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                    cursor_pos -= 1
                   #TEST CODE 
                elif event.key == pygame.K_RETURN:
                    print(f"Input: {input_text}")
                    input_text = ""
                else:
                    input_text = input_text[:cursor_pos] + event.unicode + input_text[cursor_pos:]
                    cursor_pos += 1


        text_surface = font.render(input_text, True, text_colour)
        screen.fill(box_colour, box_rect)
        screen.blit(text_surface, (box_rect.x + 5, box_rect.y + 5))

        if active:
            cursor_x = box_rect.x + font.size(input_text[:cursor_pos])[0] + 5
            pygame.draw.line(screen, text_colour, (cursor_x, box_rect.y + 5), (cursor_x, box_rect.y + box_height - 5), 2)

        pygame.display.flip()

file_name=str("hi").strip("''")
print(file_name)
