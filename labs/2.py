def check_age_group(age):
    if age < 13:
        return "child"
    elif 13 <= age <= 19:
        return "teenager"
    elif 20 <= age <= 59:
        return "adult"
    else:
        return "senior"
    
ages = [10,16,25,65]
for a in ages:
    print(f"Age {a} = {check_age_group(a)}")