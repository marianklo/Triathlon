# THe program will determines the award a person competing in a triathlon will receive.
# The program will read in the times (in minutes) for all three events of a triathlon, namely "swimming", "cycling", and "running", and then calculate and display the total.
# The award a participant receives is based on the total time taken to complete the triathlon. The qualifying time for awards is 100 minutes.
# The award that the participant will receive is based on the following criteria:
# Within qualifying time. Provincial Colours
# Within 5 minutes of qualifying time. "Provincial Half Colours"
# Within 10 minutes of qualifying time. "Provincial Scroll"
# More than 10 minutes of qualifying time. "No award"

print("Please enter the timming in munutes for the following events.")
swimming = int(input("What time have you score for swimming :"))
cycling = int(input("What time have you scored for cyclinng :"))
running = int(input("What time have you score for running :"))
total = swimming + cycling + running


# After finding how much a person scored for each event and the total of points/score, if statement will be used
# With if statement we can determine based on points/score what the award is for that person.


print(f"The total score you have completed the triathlon is : {total} minutes")
if total == 100 :
    print("The award you have achieved is PROVINCIAL COLOURS")
elif total >= 95 and total <= 100 :
    print ("The award you have achieved is PROVINCIAL HALF COLOURS")
elif total >= 90 and total <= 95 :
    print ("The award you have achieved is PROVINCIAL SCROLL")
elif total > 110 :
    print ("You have received no award")
else :
    print ("You have received no award")