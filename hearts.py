from openpyxl import Workbook, load_workbook

wb = load_workbook(filename='GameGenie/Hearts.xlsx')
ws = wb["Sheet1"]

def Hearts(top, bottom, left, right, mode, target_value):
    print(top)
    print(bottom)
    print(left)
    print(right)
    top_points = 0
    bottom_points = 0
    left_points = 0
    right_points = 0
    rounds=1
    passing = ["Center","Left","Right"]

    
    while(True):
        current_pattern = passing[rounds % len(passing)]

        input("Press enter to continue...")
        #Showing Passing Order
        print(current_pattern)

        #Rounds
        print(rounds)

        temp_score = f"A{rounds}"
        top_points += int(ws[temp_score].value)
        temp_score = f"B{rounds}"
        bottom_points += int(ws[temp_score].value)
        temp_score = f"C{rounds}"
        right_points += int(ws[temp_score].value)
        temp_score = f"D{rounds}"
        left_points += int(ws[temp_score].value)

        #Showing total scores
        print(top_points)
        print(bottom_points)
        print(left_points)
        print(right_points)

        if mode:
            if (top_points >=target_value and bottom_points >=target_value and left_points >=target_value and right_points >=target_value):
                break
        else:
            if (rounds > target_value):
                break
        rounds += 1
Hearts("eli", "alex", "Grilliot", "Right",True, 10)
wb.save('GameGenie/Hearts.xlsx')