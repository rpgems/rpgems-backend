# RPGems

This is a platform to define the resources for your RPG game.
You can also use it to play an RPG game after you define it.

## Definitions

### About the game

The idea is to create a system where you can define:
 - a character
 - a story
 - a game that is composed by a story and a group of characters and the rules of the game
 - a session that is the execution of the game by the players

The users in this system could define the characters, the stories, create a game, and create a session to play the game.
In the following sections, we will provide an in depth definition of each one of these elements.

#### Character

In an RPG game, the character will be an entity with two common attributes: a class and experience points.
Each character class will have extended attributes that will define the way you'll play it.
(e.g. strengthen, agility, magical power, etc.)

#### Story

In an RPG game, the story is a set of events that the characters will face.
These events will have three common features: a description, a requirement and a consequence
The description is related to the way the story progress (e.g. You're entering a mystical forest)
A requirement could be a character attribute or something related to the group of characters 
(e.g. you need a healer in order to enter this area; or your guild need to have a total XP of 3000)

#### Game

The game is the composed by the story and a group of characters that could be used in the story.
The main feature of a game is the title, the story used and the list of characters available to play.

#### Session

The session is the moment you can actually play the game.
You will have players that will choose a game, and the features of a session are: 

 - the start time, 
 - a history of the game progression
 - the players in the game with: character assignment and character history
 - the status of game (e.g. started, in progress, finished)

### About the tech stack

This system will be composed by three components:

 - a relational database: to store the definitions related to the characters, story, game and session
 - a backend service: to act as an API, so you can offer a UI to the player and provide a way to interact with the DB
 - a frontend service: to act as an interface so the player can interact with the system

#### Relational database

The relational database used for this system will be (Postgres? MySQL?).
The following [dbdiagram](https://dbdiagram.io/d/RPGems-66e8be246dde7f41494c2da8
) will be used to store the definitions.

#### Backend service

The backend service will be a REST api using [Python](https://www.python.org/) as programming language
and [FastAPI](https://fastapi.tiangolo.com/) as a framework.

#### Fronted service

The fronted service will be using [Typescript](https://www.typescriptlang.org/)
and the following framework: TBD

In the other pages of this folder, we'll provide a technical definition of each element presented here.

Next: [Stack Definition](stack_definition.md)