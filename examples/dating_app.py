import simple_rec

users = []
activities = []
ratings = []

def add_rating(user, activity, rating):
    """Adds a (user, activity, rating) triple to the lists.

    """
    users.append(user)
    activities.append(activity)
    ratings.append(rating)

# Alice likes to play Volleyball but cannot stand Boardgames
add_rating('Alice', 'Volleyball', 5)
add_rating('Alice', 'Boardgames', 1)

# Bob loves Boardgames and Hiking
add_rating('Bob', 'Boardgames', 5)
add_rating('Bob', 'Hiking', 5)

# Carol finds Boardgames OK, Volleyball is her passion
add_rating('Carol', 'Volleyball', 5)
add_rating('Carol', 'Boardgames', 3)
add_rating('Carol', 'Hiking', 1)

# Dan likes sports in general and doesn't hate Boardgames
add_rating('Dan', 'Volleyball', 4)
add_rating('Dan', 'Boardgames', 3)
add_rating('Dan', 'Football', 5)

# Initialize and fit collaborative filter
recommender = simple_rec.CollaborativeFilter(users, activities, ratings)
recommender.fit()

# Show best matches
match_for_alice = recommender.user_to_user('Alice', top=1)
match_for_bob = recommender.user_to_user('Bob', top=1)
match_for_carol = recommender.user_to_user('Carol', top=1)
match_for_dan = recommender.user_to_user('Dan', top=1)

print('Matches:')
print(f'Alice <--{100*match_for_alice[1][0]:.0f}%--> {match_for_alice[0][0]}')
print(f'Bob   <--{100*match_for_bob[1][0]:.0f}%--> {match_for_bob[0][0]}')
print(f'Carol <--{100*match_for_carol[1][0]:.0f}%--> {match_for_carol[0][0]}')
print(f'Dan   <--{100*match_for_dan[1][0]:.0f}%--> {match_for_dan[0][0]}')
