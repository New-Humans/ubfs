# Universe Builder File System (UBFS)

Python 3 command line application. Useful for DnD worldbuilding and similar.

## Install

`pip install pyyaml`
`pip install dndice`

## Features

* Starting from a root "multiverse" entity, create planes of existance, worlds, continents, countries, buildings, people, and items.
* "Codex" display for collection of text files in `codex` directory
* DnDice library integrated

Here's the `help` output:

```
Commands:
  add    [entity] [key] Add a new entity to the current frame of reference
  update [?key]         Key optional. Update the entity
  ls     [?key]         Key optional. Show the entity
  delete [?key]         Key optional. Delete the entity
  cd     [key]          Attempt to use the given entity as the current frame of reference
  codex  [file]         Read a codex entry.
  roll   [#d#+#]        Roll some dice
  back                  Move back a context on the stack
  exit                  Save and quit.
```

## Contributing - How to add more entities

1. Create a class file in the appropriate directory (person/place/thing)
2. Copy the contents of another entity into it
3. Modify the allowed child entities array, and the related method as desired
4. Edit any existing entities such that the new entity can be created from them
5. Update the Spec class with a new ID and string


