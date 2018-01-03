Welcome to UBFS (Universe Builder File System)

Requires Python 3. Run enter.py and use 'help' to get started.

Based on a tree of contexts. Each context is an entity, but not all entities are contexts. The context tree can be traversed using a stack of contexts. Entities can be leaf nodes, but not branch nodes.

New entities should be added to the classes/custom/[person|place|thing] directory. See templates for assistance. See entity and context classes for more assistance. All non-custom classes should include docstrings denoting private/public status of members, as well as return type and parameters for methods.

New entities should assign themselves a "Spec" value, which acts as an enumeration of the entity. All entities and all contexts are enumerated within this class.
