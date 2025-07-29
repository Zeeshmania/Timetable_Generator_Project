# Inputs

An array consisting of:

1. A dictionary with days as keys and times as values. Times are in 24-hour format, represented as: "11:11 - 12:22". 
2. A dictionary containing an subject names as keys and integers representing confidence levels as values.
3. A string representing an ending date, selecting from a calendar pop-up (in YYYY-MM-DD format).

For example:

[
    {
        "Monday": ["16:00-18:00", "18:30 - 20:30"], 
        "Tuesday": ["17:00-18:00", "19:00 - 20:15"], 
        "Wednesday": [], 
        "Thursday": ["16:00-18:00", "18:30 - 20:30"], 
        "Friday": ["16:00-18:00", "18:30 - 20:30"], 
        "Saturday": ["11:00-13:00", "13:30 - 15:00", "16:00 - 19:00", "19:30 - 21:00"], 
        "Sunday": [], 

    }
        
    {
        "Maths": 9,
        "English": 7,
        "Science": 3
    }

    4
        ]


Suppose the user suppliess the following information:

## Availabilities: 

1. Monday
 * 16:00 - 18:00
 * 18:30 - 20:30

2. Tuesday
 * 17:00 - 18:00
 * 19:00 - 20:15

3. Wednesday
 * N/A

4. Thursday
 * 16:00 - 18:00
 * 18:30 - 20:30

5. Friday
 * 16:00 - 18:00
 * 18:30 - 20:30

6. Saturday
 * 11:00 - 13:00
 * 13:30 - 15:00
 * 16:00 - 19:00
 * 19:30 - 21:00

7. Sunday
 * N/A


## Subjects: 
1. Maths (9/10)

2. English (7, 10)

3. Science (3/10)

## Additional Options


1. Include Breaks?
 * Yes (30 minutes)
2. Include Recall?
 * NO



In this case, we have 22.25 hours of revision time per week, and 3 subjects to study. Priority should be given according to the user's proficiency in each area. Obtain a weighted score by dividing the score in a subject by the sum of the user-inputted scores (so Maths would have a weighting of 9/(9 + 7 + 3) = 9/19). Multiply the weighted score by the total number of hours to be obtain an estimate for the time spent on each subject per week. In this case, it would be:

1. Maths: 11 hours (rounded up)
2. English: 8 hours (rounded down)
3. Science: 3.25 hours (rounded down)

Now, we just need to assign each study period a subject. Just keep a counter for how many hours of study are left in a subject, and subtract for each assignment.


1. Monday
 * 16:00 - 18:00 (MATHS)
 * 18:30 - 20:30 (ENGLISH)

2. Tuesday
 * 17:00 - 18:00 (SCIENCE)
 * 19:00 - 20:15 (ENGLISH)


... and so on.

The program should:

 * Calculate the total number of hours available to revise.
 * Calculate the weightings for each subject
 * Calculate the number of hours to be revised for each subject

