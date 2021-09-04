initProgram = int(input('Enter data? 0 - No  |  1 - Yes '))
while initProgram == 1:
    studantName = input("Studant's name: ")
    note = float(input('Final note: '))
    
    if note >= 0 and note < 3:
        grading = 'E'
    elif note >= 3 and note < 5:
        grading = 'D'
    elif note >= 5 and note < 7:
        grading = 'C'
    elif note >= 7 and note < 9:
        grading = 'B'
    elif note >= 9 and note <= 10:
        grading = 'A'
    else:
        print('[ERROR] Invalid note!')
        exit()
    
    print(f"The Studant {studantName} got the grade {note} and fits into grading system {grading}")
    
    initProgram = int(input('Do you want to leave?? 0 - Yes  |  1 - No '))
