# Character definition

A character will be the entity immerse in the game session.
Every character will have the following attributes:

 - name (string): this will define the name of the character
 - class (string): the name of the class of this  character belongs. This will define a group of extended attributes this character will have.
 - description (string): a brief description of this character
 - experience_points (string): the amount of experience this character can start with/will have during the game session.

Depending upon the class of the character, a set of extended attributes are already defined.
Also extended attributes could be added to the character (only if the extended is not part of the class)
These extended attributes could be defined in the following way:

 - name (string): define the name of the attribute
 - description (string): specify what this skill offer to the character
 - skill_points (number): specify the level of experience in this specific skill

## Database definition

We will have four tables (details in the db diagram):

 - character (with the common attributes for every character)
 - class (with the name of the class)
 - attributes (with the definition of an extended attribute)
 - class_attribute (that will attach an attribute to a class)
 - character_attribute (that will attach an attribute to a character)

## API actions

The system API should be able to execute the following actions:

 - Add a new character
 - Modify an existing character
 - Delete an existing character
 - List all characters
 - Search a character
 - Add a new extended attribute
 - Modify an existing extended attribute
 - Delete an existing extended attribute
 - List all extended attributes
 - Search an extended attribute
 - Add an extended attribute to a character
 - Remove an extended attribute to a character