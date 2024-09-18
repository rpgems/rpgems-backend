# Session definition

The session definition is the entity responsible to provide the actual game play of a game definition.
In the session definition, we will have the following attributes:

 - Start time (date): when the session started
 - Game used (game_definition): the game definition used in this session
 - List of players (list of users): the users connected to the session
 - Character assignment list (list of assignment): for each player in the session, which character they're using in the session
 - Current status of each character (list of events): for each character in the session, which is the event they're currently in.
 - History of each character (list of past events): for each character in the session, 
which were the past events they were in and which consequences they faced.
 - Status of the game (string): status of the game. It could be the following status: `Not started`, `In progress` and `Finished`

## Database definition

We will have three tables (details in the db diagram):

 - session_definition (attaching a game definition and specifying a start_time and session status)
 - session_definition_character_assigment (attach a user to a character defined in the game definition)
 - character_history (define an action id an assigned character) (you can get the history and current status of the character from this table)

## API actions

The system API should be able to execute the following actions:

 - create a session definition
 - start the session definition
 - update the session definition status
 - assign a user to a character available in the game definition
 - get the character current status
 - get the character history
 - get the whole game status
 - get the whole game history
 - add an entry to the character history