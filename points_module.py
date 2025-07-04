def batting_points(runs,balls,sixes,fours):
    points = runs//2
    if runs <= 50:
        points += 5
    elif runs >= 100:
        points += 10
        
    if balls > 0:
        strike_rate = runs/balls
        if strike_rate >= 80 and strike_rate <= 100:
            points += 2
        elif strike_rate > 100:
            points += 6

    points += fours * 1
    points += sixes * 2
    return points
            
def bowling_points(wickets,runs,overs):
    points = wickets * 10
    if wickets >= 3:
        points += 5
    if wickets >= 5:
        points += 10

    if overs > 0:
        econ = runs /  overs
        if 3.5 <= econ <= 4.5:
            points += 4
        elif 2 <= econ <= 3.5:
            points += 7
        elif econ < 2:
            points += 10
    return points

def fielding_points(catches,stumpings,runout):
    return (catches+stumpings+runout) * 10
