#JEE percentile predictor- by jone jefri
def get_percentile (marks,difficulty):
    #data based on 2025 year
    if marks>=280:
        percentile=99.9
    elif marks>=250:
        percentile=99.5
    elif marks>=210:
        percentile=99.0
    elif marks>=180:
        percentile=98.0
    elif marks>=150:
        percentile=96.0
    elif marks>=120:
        percentile=93.0
    elif marks>=90:
        percentile=88.0
    elif marks>=60:
        percentile=80.0
    else:
        percentile=65.0
    return percentile



def get_rank(percentile, total_students):
    rank=(100 - percentile)/100*total_students
    return int(rank)

def get_college(percentile):
    if percentile>=99.5:
        return"Top IIT, NIT, IIIT chance - excellent!"
    elif percentile>= 97:
        return"Good NIT/ IIIT chance"
    elif percentile>=93:
        return"you are qualified for jee advanced"
    elif percentile>=90:
        return"Good private college, try for next attempt for best"
    else:
        return"Keep practising and never give up champ"


#how much percentile needed for IIT
def get_more(percentile):
    if (percentile<99.0):
        new_percentile=99.9-percentile
        return new_percentile

#main part
print("=== JEE percentile Predictor===") 
print("can make mistakes and information based on year 2025")   
marks= int (input("Enter your marks out of 300"))
difficulty=input("how was the shift? easy or hard").lower()
total_students=int(input("Enter how many student were written the exam in your shift"))
per=get_percentile(marks,difficulty)
rank=get_rank(per,total_students)
college=get_college(per)
new_percentile=get_more(per)
print(f"\nYour estimated percentile {per}")
print(f"Your estimated rank:{rank}")
print(f"college hint to join: {college}")
print(f"the more percentile needed to secure top orr dream IIT{new_percentile}")
print("DISCLAIMER!: this information is based on previous year data, real and accurate data will announced by NTA based on the day's shift.")