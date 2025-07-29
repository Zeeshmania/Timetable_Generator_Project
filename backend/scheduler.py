from datetime import datetime, timedelta

#the input is an array of dictionaries and integers, an example of which is shown below. The typical input is [dictionary, dictionary, string, dictionary]


# First is a dictionary for available dates and times
example_availabilities = {
        "Monday": ["16:00-18:00", "18:30 - 20:30"], 
        "Tuesday": ["17:00-18:00", "19:00 - 20:15"], 
        "Wednesday": [], 
        "Thursday": ["16:00-18:00", "18:30 - 20:30"], 
        "Friday": ["16:00-18:00", "18:30 - 20:30"], 
        "Saturday": ["11:00-13:00", "13:30 - 15:00", "16:00 - 19:00", "19:30 - 21:00"], 
        "Sunday": [], 

    }

# Then is a dictionary for subjects and confidence levels
example_subjects = {
        "Maths": 9,
        "English": 7,
        "Science": 3,
    }

# Next is the "Breaks" parameter, which will have two values, stored in a dictionary. If the user takes no breaks, the default value will be None.
example_breaks = {"frequency": 30, "length": 5}


example_input = [example_availabilities, example_subjects, "2026-07-21", example_breaks, False]




# function returns an int
def calculate_total_available_time(availability_dict):
    total_minutes = 0

    for day, intervals in availability_dict.items():
        for interval in intervals:
            # Normalize spacing
            interval = interval.replace(" ", "")
            start_str, end_str = interval.split("-")
            start = datetime.strptime(start_str, "%H:%M")
            end = datetime.strptime(end_str, "%H:%M")
            duration = end - start
            total_minutes += duration.total_seconds() / 60
    total_hours = total_minutes / 60
    return total_hours



def calculate_weighted_scores(subject_dict):
    weights = {}
    total = 0

    for confidence in subject_dict.values():
        total += confidence

    for subject, confidence in subject_dict.items():
        weights[subject] = confidence/total

    return weights

# Inputs should be an int for time, and a dictionary for weightings.
def calculate_time_per_subject(total_time_revised, weightings):
    times = {}

    for subject, time in weightings.items():
        times[subject] = time * total_time_revised

    return times

total_time = calculate_total_available_time(example_availabilities) # returns an int
weightings = calculate_weighted_scores(example_subjects) # returns a dict
times_per_subject = calculate_time_per_subject(total_time, weightings) # returns a dict

print(f"Times for each subject {times_per_subject}")
