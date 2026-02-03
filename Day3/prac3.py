'''
# Problem Statement: Shopping Cart Price Engine
def calculate_cart_total(*prices):
    #total = sum(prices)
    total = 0
    for i in prices:
        total += i
    if total > 5000:
        total *= 0.95
        # discount = total * 0.05
        # total -= discount
    return total

print(calculate_cart_total(1200,800,2500,900))
'''

'''
# Problem Statement: User Profile Updater
def update_profile(user_id, **details):
    profile = {"user_id": user_id}
    profile.update(details)
    return profile

print(update_profile(101, name="Mohit", email="mohit@gmail.com", city="ldh", phone=1234567890))
'''

'''
# Problem Statement: Job Portal Backend Utility
c1 = {"name":"Mohit","experience":2,"skills":["Python","Django"]}
c2 = {"name":"Ravi","experience":5,"skills":["JavaScript","React"]}
c3 = {"name":"Ankit","experience":3,"skills":["Java"]}
c4 = {"name":"Suraj","experience":4,"skills":["Python","Flask","React"]}

def process_applications(*candidates, **criteria):
    min_exp = criteria.get("min_experience", 0)
    req_skills = criteria.get("skills", 0)
    final = []
    for candidate in candidates:
        if candidate["experience"] >= min_exp and req_skills in candidate["skills"]:
            final.append(candidate['name'])
    return final
print(process_applications(c1, c2, c3, c4, min_experience=2, skills="Python"))
'''

#Problem Statement: Student Result Analyzer
from functools import reduce
marks = [45, 78, 90, 32, 67, 88, 54]

res = list(filter(lambda x: x>=40, marks))
print(res)

grace_marks = list(map(lambda x: x + 5, marks))
print(grace_marks)

total_marks = reduce(lambda a,b: a + b, marks)
print(total_marks)