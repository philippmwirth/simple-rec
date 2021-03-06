import simple_rec

users = []
items = []
ratings = []

def add_rating(user, item, rating):
    """Adds a (user, activity, rating) triple to the lists.

    """
    users.append(user)
    items.append(item)
    ratings.append(rating)

# say Alice, Bob, and Carol have participated in a
# questionnaire about ice cream

# Alice likes Strawberry and Chocolate
add_rating('Alice', 'Strawberry', 1.)
add_rating('Alice', 'Chocolate', 1.)

# Bob also likes Strawberry and Chocolate
add_rating('Bob', 'Strawberry', 0.8)
add_rating('Bob', 'Chocolate', 1.)

# Carol likes Vanilla and finds Chocolate disgusting
add_rating('Carol', 'Vanilla', 1.)
add_rating('Carol', 'Chocolate', 0.)

# now, Bob, completely unrelated, decides to buy a new car
add_rating('Bob', 'Ferrari', 1.)

# since Alice and Bob had a similar taste before, Alice 
# can now be targeted by an advertisment company for cars
recommender = simple_rec.CollaborativeFilter(users, items, ratings)
recommender.fit()

who_to_target, _ = recommender.item_to_user('Ferrari', top=2)
print('Ferrari should target:', who_to_target)