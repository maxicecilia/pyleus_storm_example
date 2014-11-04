from neomodel import (StructuredNode, StringProperty, IntegerProperty,
                      RelationshipTo, RelationshipFrom)


class Actor(StructuredNode):
    name = StringProperty(unique_index=True, required=True)

    # traverse incoming IS_FROM relation, inflate to Person objects
    favorites = RelationshipFrom('Article', 'LIKES')


class Article(StructuredNode):
    name = StringProperty(unique_index=True)
    date = StringProperty()

    # traverse outgoing IS_FROM relations, inflate to Country objects
    favorited = RelationshipTo(Actor, 'LIKES')
