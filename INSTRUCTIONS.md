We want to create a system for creating comments and parsing @mentions

A comment includes text and the author (user)
A mention joins a user to a comment

Start with basic @mentions where all we need is an email to go out

If that gets implemented, discuss how the FE needed to know which attempted mentions actually resulted in a notification


1. create a comment model 
2. create a mention model
3. create a gql schema for user
4. create a gql schema for comment, include a mentions field
5. write a resolver for getting all mentions
6. create mutation for creating a comment
7. extract from the input.text a list of all users who were @mentioned 
8. for each @mention, create and insert a Mention (which just joins Comment to User) into DB
9. return a CreateCommentResponse with the comment
