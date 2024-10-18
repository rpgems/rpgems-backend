# Game definition

A game definition is a requirement for a game session.
In the definition, you will need the following attributes:

 - title (string): specify the game definition game
 - story (story identifier): specify the story to use
 - characters_available (list of characters): specify the character that a player could use in the game session

## Database definition

We will have two tables (details in the db diagram):

 - game_definition (specifying the title and attaching a story)
 - game_definition_character (attaching the character to a game_definition)

## API actions

The system API should be able to execute the following actions:

 - Create a game definition
 - Modify a game definition
 - delete a game definition
 - list all game definitions
 - search for a game definition
 - Attach a character to a game definition
 - Remove a character from a game definition
 - List all characters attached to a game definition
 - Search a character attached to a game definition