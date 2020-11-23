# Setup

1. Install pipenv if not already installed. 

	`brew install pipenv`

2. Install pyenv if not already installed

	`brew install pyenv`

3. Install Python 3.8.0 using Pyenv

	`pyenv install 3.8.0`

	Tell Pyenv to use 3.8.0 for this project 

	`pyenv local 3.8.0`

4. Install project dependencies

	`pipenv install`

5. Create database tables 

	`pipenv run ./manage.py migrate`

6. Load some dummy users into the DB

	`pipenv run ./manage.py loaddata users`

	This creates users with usernames `bob` and `emily`

7. Run the server

	`pipenv run ./manage.py runserver`

8. Open `http://127.0.0.1:8000/graphql/` in browser to make sure everything is working

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

9. Open `comments/schema/comment.py` to begin the exercise 





