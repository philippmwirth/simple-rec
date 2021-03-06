# Simple Rec

Simple Rec is a light-weight collection of simple recommender systems.

This is a personal project to highlight how easy it is to predict the 
preferences and behavior of a user in a system. With Simple Rec, a few lines of code suffice to make accurate predictions about a user. As a consequence, a user can be targeted by advertisments, manipulated, and exploited by the service provider.


## Installation

### Installation from PyPI:
```bash
pip3 install simple-rec
```

### Installation from source:
```bash
git clone https://github.com/philippmwirth/simple-rec.git
cd simple-rec
pip3 install .
```

### Requirements
The only requirements are [Numpy](https://numpy.org/) and Python3.

## Methods

### Collaborative Filtering
Collaborative Filtering is a technique used by recommender systems. The idea is based on the assumption that people who agreed in the past will also agree in the future. Hence, users and items can be grouped by similar rating history. The implementation in Simple Rec relies on a matrix factorization of the sparse user-item matrix.

### Content-based Filtering
Coming soon!

## Examples
All the examples shown below can be found in `examples/`.

### Collaborative Filtering

**Item to User: Targeted Advertising**

This example highlights how any user can become the target of an advertising strategy even if the user has never had any interest in the product being advertised.

```python
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

```

Output:
```
Ferrari should target: ['Bob', 'Alice']
```

**User to Item: Movie Ratings**

A classic example is a database of user-movie ratings. The following code provides movie recommendations to a user based on his or her preferences in the past.

```python
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

```
Output:
```
> Recommended Movies:
> Alice:   Goldfinger, Die Another Day, Skyfall
> Bob:     Skyfall, Die Another Day, Goldfinger
```

**User to User: A Simple Dating App**

A simple dating app could match users based on their taste and preferences. For example, each user could be asked to fill out a questionnaire to get the necessary information. However, the information could also be extracted from
other data, like images posted on the internet or from geotracking data.

```python
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
```

Output:
```
> Matches:
> Alice <--90%--> Carol
> Bob   <--29%--> Dan
> Carol <--90%--> Alice
> Dan   <--83%--> Carol
```
