# Simple Rec

## Installation

### Installation from PyPI:
```bash
pip install simple-rec
```

## Methods

### Collaborative Filtering
To Do.

## Examples
All the examples shown below can be found in `examples/`.

### Collaborative Filtering

**User to Item: Movie Ratings**

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

**Item to User: TODO**
E.g. for a given topic, find users which might be interested.

**Item to Item: TODO**
E.g. based on your interest in X present Y (maybe FPL players).