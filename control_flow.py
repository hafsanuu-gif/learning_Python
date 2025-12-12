grade =75

if grade >= 90:
    #This only runs if grade is 90 or more
    print("Grade: A")
elif grade >= 80:
        #This only runs if grade is 80-89
    print("Grade: B")
elif grade >= 70:
    # This only runs if grade is 70-79 (This is the path our '75' grade takes!)
    print("Grade: C")
    
else:
    #This is the catch -all if none of the above are true
    print("Grade: F")    
