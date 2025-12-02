def check_age_group(age):
    if age < 13:
        return "Child"
    
    elif age < 18:
        return "Teenager"
    
    else: 
        return "Adult"
    

print(f"Age 10: {check_age_group(10)}")
print(f"Age 13: {check_age_group(13)}")
print(f"Age 17: {check_age_group(17)}")
print(f"Age 18: {check_age_group(18)}")
print(f"Age 40: {check_age_group(40)}")
    
