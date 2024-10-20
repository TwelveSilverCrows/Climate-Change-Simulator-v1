import math
def initialise():
    global year
    year=2023
    
    global albedo
    albedo = 0.30
    
    global budget
    budget=100
    
    global sea_level_rise
    sea_level_rise=0
    
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
    main_file='main-game-questions.csv'

    
    global T_cel
    T_cel=0

    global level
    level=0
    
    global temp_rise
    temp_rise=0

    
def calculate_temperature(greenhouse_effect, albedo):
    pi = 3.14159
    sigma = 5.6703e-8 # e is '10^'
    mass_of_sun = 1.989e30
    distance = 1.496e11
    greenhouse_effect-=0.0005
    print(greenhouse_effect)
    # Albedo and greenhouse_effect are the two variables that can be changed
    
    solar_luminosity = 3.846e26

    # Effective temperature
    T_eff = math.sqrt(math.sqrt((1 - albedo) * solar_luminosity / (4 * pi * sigma))) * 1 / math.sqrt(2 * distance)
    print(T_eff)
    # Equivalent temperature below, which is temperature when the system is in equilibrium (energy is balanced)
    T_eq = T_eff**4 * (1 + (0.75 * greenhouse_effect))
    print(T_eq)
    # Temperature in Kelvin
    T_kel = math.sqrt(T_eq / 0.9)
    print(T_kel)
    # Converting to Celsius
    T_cel = T_kel - 273
    print(T_cel)
    return T_cel



def calculate_sea_level(sea_level_rise,temp_changes, albedo):
    if temp_changes: #prevents function from executing when array is empty
        sea_level_rise=(temp_rise)*2.3
        albedo-=(0.005*sea_level_rise)
    return sea_level_rise, albedo

t=calculate_sea_level(0,0.7819437236698263, 0.3 )
print('t',t)
