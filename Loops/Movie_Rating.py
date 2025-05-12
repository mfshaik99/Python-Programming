# List of movie names
movies = ["Inception", "Titanic", "Avatar", "The Dark Knight", "The Godfather"]

# Loop to ask for ratings for each movie
ratings = {}
for movie in movies:
    rating = int(input(f"Rate the movie {movie} out of 10: "))
    ratings[movie] = rating

print("\nMovie Ratings:")
for movie, rating in ratings.items():
    print(f"{movie}: {rating}/10")
