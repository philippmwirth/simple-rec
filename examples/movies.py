import simple_rec

users = []
movies = []
ratings = []


def add_rating(user, movie, rating):
    """Adds a (user, movie, rating) triple to the lists.

    """
    users.append(user)
    movies.append(movie)
    ratings.append(rating)


# Alice liked "Goldfinger" but was not a fan of "Finding Nemo"
add_rating('Alice', 'Goldfinger', 1.0)
add_rating('Alice', 'Finding Nemo', 0.1)

# Bob has only watched "Skyfall" - he loved it!
add_rating('Bob', 'Skyfall', 0.9)

# Carol is a huge James Bond Fan
add_rating('Carol', 'Skyfall', 1.0)
add_rating('Carol', 'Goldfinger', 1.0)
add_rating('Carol', 'Die Another Day', 1.0)

# Initialize and fit collaborative filter
recommender = simple_rec.CollaborativeFilter(users, movies, ratings)
recommender.fit()

# Show recommended movies
movies_for_alice, _ = recommender.user_to_item('Alice', top=3)
movies_for_bob, _ = recommender.user_to_item('Bob', top=3)

print('Recommended Movies:')
print('Alice:   ' + ', '.join(movies_for_alice))
print('Bob:     ' + ', '.join(movies_for_bob))
