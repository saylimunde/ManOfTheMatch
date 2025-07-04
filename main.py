from points_module import batting_points,bowling_points,fielding_points

players = [{'name':'Virat Kohli','role':'bat','runs':112,'fours':10,'sixes':0,'balls':119,'field':0,'wickets':0,'overs':0,'catches':0,'stumpings':0,'runout':0},
           {'name':'du Plessis','role':'bat','runs':120,'fours':11,'sixes':2,'balls':112,'field':0,'wickets':0,'overs':0,'catches':0,'stumpings':0,'runout':0},
           {'name':'Bhuvneshwar Kumar','role':'bowl','wickets':1,'overs':10,'runs':71,'field':1,'catches':0,'stumpings':0,'runout':0,'balls':0,'fours':0,'sixes':0},
           {'name':'Yuzvendra Chahal','role':'bowl','wickets':2,'overs':10,'runs':45,'field':0,'catches':0,'stumpings':0,'runout':0,'balls':0,'fours':0,'sixes':0},
           {'name':'Kuldeep Yadav','role':'bowl','wickets':3,'overs':10,'runs':34,'field':0,'catches':0,'stumpings':0,'runout':0,'balls':0,'fours':0,'sixes':0}]

highest_points = 0
man_of_match = ""

for p in players:
    bat_pts = batting_points(p['runs'],p['balls'],p['fours'],p['sixes'])
    bowl_pts = bowling_points(p['wickets'],p['runs'],p['overs'])
    field_pts = fielding_points(p['catches'],p['stumpings'],p['runout'])

    # total = bat_pts + bowl_pts + field_pts

    print(f"{p['name']} - Batting: {bat_pts}, Bowling: {bowl_pts}, Fielding: {field_pts}") #Total: {total}")
  


#     if total > highest_points:
#         highest_points = total
#         man_of_match = p["name"]


# print(f"\n🏆 Man of the Match: {man_of_match} with {highest_points} points")
