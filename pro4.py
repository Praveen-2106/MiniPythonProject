 # Feedback Rating Analyzer

feedback = str(input("FEEDBACK :"))
ratings = [4, 5, 2, 5, 4.3, 3., 5]

#oprations

convert = feedback.lower()
total = sum(ratings)
avg = total / 7 

print("Thanks for your feedback!", "\n", "Feedback ",feedback, "\n", "Ratings",ratings, "\n", "Average ",round(avg))