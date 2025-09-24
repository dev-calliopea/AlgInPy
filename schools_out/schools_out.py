import sys
import os
import json

def is_validJSON(filePath):
    try:
        # Check if file exists 
        if not os.path.exists(filePath):
            print(f"Le fichier {filePath} est manquant.")
            return False

        with open(filePath, 'r') as file:
            data = json.load(file)

            # Check if empty 
            if not data:
                print(f"Le fichier {filePath} est vide.")
                return False

        return True
    
    # Check if corrupted 
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Erreur lors de la lecture du fichier {filePath}: {e}")
        return False


def get_optimal_number(data) : 
    # Sort data in ascending order based on the start time
    sorted_sessions = sorted(data, key=lambda x: x['start'])

    # Init classrooms & end_times tab 
    classrooms = []
    end_times = []

    # Go through sessions 
    for session in sorted_sessions : 
        # By default, the session can't be added to an existing classroom
        can_be_added = False

        # Go through classrooms 
        for i in range (len(classrooms)):
            # When the beginning of the session matches the time of one of the end_times : the beginning is at or after the session's end 
            if  session['start'] >= end_times[i]:
                # The end times becomes the end of the session
                end_times[i] = session['end'] 
                # The session can be added (has been added by becoming the new end_times)
                can_be_added = True
                # Stop the loop
                break
        
        # If the session can't be added to one of the classrooms 
        if not can_be_added : 
            # We add another classroom (by adding the session to the classrooms tab)
            classrooms.append(session)
            # We add another end_time to the ends_time tab (to be compared)
            end_times.append(session['end'])

    result = len(classrooms)
    # json_output = json.dumps({"optimal_classes_nb": result})
    # print(json_output) 
    print(result)


def schools_out() :
    filePath = sys.argv[1]
    validFilePath = is_validJSON(filePath)

    if (validFilePath) :
        with open(filePath, 'r') as file:
            data = json.load(file)

        get_optimal_number(data)


schools_out()