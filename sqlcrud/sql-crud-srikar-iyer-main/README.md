# SQL CRUD
## Practice CSV Links:
[https://github.com/dbdesign-assignments-spring2023/sql-crud-srikar-iyer/blob/98510a01cf6a38951c6498ba9f776a4081265675/data/posts.csv] (Posts Dataset generated from Mockaroo)
[https://github.com/dbdesign-assignments-spring2023/sql-crud-srikar-iyer/blob/98510a01cf6a38951c6498ba9f776a4081265675/data/restaurants.csv] (Restaurants Dataset generated from Mockaroo)
[https://github.com/dbdesign-assignments-spring2023/sql-crud-srikar-iyer/blob/98510a01cf6a38951c6498ba9f776a4081265675/data/users.csv] (Users Dataset generated from Mockaro0)
## Restaurant Finder
### Code to create Tables

```
CREATE TABLE restaurants (
  id INTEGER PRIMARY KEY,
  name TEXT,
  category TEXT,
  price_tier TEXT,
  neighborhood TEXT,
  opening_hours TEXT,
  average_rating INTEGER,
  good_for_kids BOOLEAN,
  created DATETIME DEFAULT CURRENT_TIMESTAMP);
```

This creates the restaurants table with the required parameters to query, those including common identifiers such as name and neighborhood, as well as opening_hours
and a real-time indicator to track when a restaurant is open.

```
CREATE TABLE reviews (
  id INTEGER PRIMARY KEY,
  restaurant_id INTEGER,
  rating INTEGER,
  comment TEXT,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (restaurant_id) REFERENCES restaurants(id)
  );
```

This creates the reviews table that refers to the restaurants table with a foreign key and contains the required and some additional ones.

### Code to import CSV data files

```
    .mode csv
    .import C:/srikar/Learning/NYU/Database/sql-crud-srikar-iyer/data/restaurants.csv restaurants
```

### SQL Queries

1. Find all cheap restaurants in a particular neighborhood (pick any neighborhood as an example).

```
    SELECT name FROM restaurants WHERE price_tier = 'cheap' AND neighborhood = 'Greenpoint';
```

2. Find all restaurants in a particular genre (pick any genre as an example) with 3 stars or more, ordered by the number of stars in descending order.

```
    SELECT name FROM restaurants WHERE category = 'Italian' AND average_rating >= 3 ORDER BY average_rating DESC;
```

3. Find all restaurants that are open now (see hint below).

```
    SELECT name from restaurants where strftime('%H:%M',datetime(strftime('%H:%M', 'now'),'localtime')) - opening_hours >=0;
```

4. Leave a review for a restaurant (pick any restaurant as an example).

```
    INSERT INTO reviews (id,restaurant_id, rating, comment) VALUES (1, 6679308429, 4.5, 'Great food and filling calzones!');
```

5. Delete all restaurants that are not good for kids.

```
    DELETE FROM restaurants WHERE good_for_kids = 'false';
```

6. Find the number of restaurants in each NYC neighborhood.

```
    SELECT neighborhood, COUNT(*) as num_restaurants FROM restaurants GROUP BY neighborhood;
```

## Social Media App
### Code to create Tables

```
CREATE TABLE users (
  id INTEGER PRIMARY KEY,
  email TEXT,
  password TEXT,
  handle TEXT
);
```

This creates a simple user table, with the essentials for a social media account.

```
CREATE TABLE posts (
  id INTEGER PRIMARY KEY,
  type TEXT,
  from_user INTEGER,
  to_user INTEGER,
  content TEXT,
  visible BOOLEAN,
  created DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (from_user ) REFERENCES users(id),
 FOREIGN KEY (to_user ) REFERENCES users(id)
);
```

This table handles task for each user, utilizing two foreign keys to utilize 
the data in the users table. Posts keeps track of who sends and takes in the message, time when message sare sent, and what format (messages or stories) text is being posted. It also keeps posts 'invisible' after time but actually hides it from users.


### Code to import CSV data files

```
    .mode csv
    .import C:/srikar/Learning/NYU/Database/sql-crud-srikar-iyer/data/users.csv users
    .import C:/srikar/Learning/NYU/Database/sql-crud-srikar-iyer/data/posts.csv posts
```

### SQL Queries


1. Register a new User.

```
    INSERT INTO users (id,email, password, handle) VALUES (12345,'newuser@example.com', 'password123', 'newuser');
```

2. Create a new Message sent by a particular User to a particular User (pick any two Users for example).

```
    INSERT INTO posts (id, type, from_user, to_user, content, visible) VALUES (98765, ‘message’, 6293643321, 12345,  'Hey there!', ‘TRUE’);
```

3. Create a new Story by a particular User (pick any User for example).

```
    INSERT INTO posts (id, type, from_user, content, visible) VALUES (98764, ‘story’, 12345, 'Hi I am a new user here!', ‘TRUE’);
```

4. Show the 10 most recent visible Messages and Stories, in order of recency.

```
    select id, type, created, visible from posts where visible = 'TRUE' order by ROUND((JULIANDAY('now') - JULIANDAY(created)) * 24) limit 10;
```

5. Show the 10 most recent visible Messages sent by a particular User to a particular User (pick any two Users for example), in order of recency.


```
    select id, content, created from posts where type='message' and from_user=9400746040 and to_user=92359957 and visible = 'TRUE' order by ROUND((JULIANDAY('now') - JULIANDAY(created)) * 24) limit 10;
```

6. Make all Stories that are more than 24 hours old invisible.

```
    update posts set visible = 'FALSE' where type='story' and ROUND((JULIANDAY('now') - JULIANDAY(created))) > 1;
```

7. Show all invisible Messages and Stories, in order of recency.

```
    select id,type,content,created from posts where visible = 'FALSE' order by ROUND((JULIANDAY('now') - JULIANDAY(created)));
```

8. Show the number of posts by each User.

```
    select from_user,count(*) from posts group by from_user;
```

9. Show the post text and email address of all posts and the User who made them within the last 24 hours

```
    select from_user, type, email from posts, users where posts.from_user = users.id and JULIANDAY('now') - JULIANDAY(created) < 1;
```

10. Show the email addresses of all Users who have not posted anything yet.

```
    select email from users left join posts on posts.from_user=users.id where posts.from_user is null;
```