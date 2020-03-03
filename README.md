# Setup

1. Install pipenv if not already installed. 

`brew install pipenv`

2. Install project dependencies

`pipenv install`

3. Create database tables 

`pipenv run ./manage.py migrate`

4. Load some dummy users into the DB

`pipenv run ./manage.py loaddata users`

This creates users with usernames `bob` and `emily`

5. Run the server

`pipenv run ./manage.py runserver`

6. Open `http://127.0.0.1:8000/graphql/` in browser to make sure everything is working

try creating a comment with 

```
mutation CreateComment($commentText: String!) {
  createComment(input: {text: $commentText}) {
    comment {
      text
    }
  }
}

variables: {"commentText": "hey @bob do we have an estimate yet?"}

```

6. Open `comments/schema/comment.py` to begin the exercise 





