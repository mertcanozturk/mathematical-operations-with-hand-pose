import keyboard
import math

def generate(distances):
    print("yaziliyor")
    with open("letter.csv", "a") as myfile:
        myfile.write(str(distances))

def GetDistance(point1,point2):
    return math.sqrt((point2[0]-point1[0])**2 + (point2[1]-point1[1])**2)

def calculate_str_distance(letter,joint_coords):
    distances = '\n'+letter+','+ str(GetDistance(joint_coords[20],joint_coords[16])) + ','  #20 serçe 4 baş 0 avuç
    distances +=(str(GetDistance(joint_coords[16],joint_coords[12]))+',')
    distances +=(str(GetDistance(joint_coords[12],joint_coords[8]))+',')
    distances +=(str(GetDistance(joint_coords[8],joint_coords[4]))+',')
    distances +=(str(GetDistance(joint_coords[0],joint_coords[20]))+',')
    distances +=(str(GetDistance(joint_coords[0],joint_coords[16]))+',')
    distances +=(str(GetDistance(joint_coords[0],joint_coords[12]))+',')
    distances +=(str(GetDistance(joint_coords[0],joint_coords[8]))+',')
    distances +=(str(GetDistance(joint_coords[0],joint_coords[4])))
    return distances

def KeyboardEvents(joint_coords):
    try:
        if keyboard.is_pressed('1'):  
            generate(calculate_str_distance('1',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('2'):   
            generate(calculate_str_distance('2',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('3'):  
            generate(calculate_str_distance('3',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('4'):  
            generate(calculate_str_distance('4',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('5'):  
            generate(calculate_str_distance('5',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('6'):   
            generate(calculate_str_distance('6',joint_coords))
    except:
        pass
    try:
        if keyboard.is_pressed('7'):  
            generate(calculate_str_distance('7',joint_coords))
    except:
        pass