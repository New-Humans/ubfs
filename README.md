Hello! Welcome to the universe builder file system.

This project depends on a contextual heirarchy. All things in creation are defined relative to their context. As such, representing the context between entities is very important. This is what the UBFS tries to address - contextual heirarchy between entities.

Each directory will contain the an "entity_meta.yaml". It contains information specific to the entity.

Directories within the entitity are considered to be context-specific entities within the current entity.

Different entities have different properties. Custom properties can be added to any entity.

You can use the ubfs.py script to interact with your project. It just reads the file system and handles directory/file creation and deletion.

ubfs_generate_html.py will generate a visualization of the project.

ubfs_browse.py will allow you to browse your universe via text.
