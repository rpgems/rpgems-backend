# Story definition

A story is a set of events that will make the characters progress in the game.
A story will have the following attributes:

 - Title (string): the story's title
 - Description (string): a brief description for the story

Each story event is composed of the following attributes:

 - Location (string): the current location of the character(s).
 - Description (string): specify what would happen in the current location

Each event will have a list of actions that the character would take.
These actions will have the following attributes:

 - current event (number): specify the id for the current event
 - requirement (string): specify the requirement to execute the action
 - consequence (string): specify what the character could earn from executing this action
 - next event (number): specify the id for the next event

## Database definition

We will have three tables (details in the db diagram):

 - story (with the title and description)
 - event (with the specified attributes)
 - action (that will link a current event to the next event)

## API actions

The system API should be able to execute the following actions:

 - Create a new story
 - Modify an existing story
 - Delete an existing story
 - List all stories
 - Search for a story
 - Create an event
 - Modify an event
 - Delete an event
 - List all events
 - Search an event
 - Create an action
 - Modify an action
 - Delete an action
 - List all actions
 - Search for an action