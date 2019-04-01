from enum import Enum


class Relationship(Enum):
    EXTENSION = ' extension '
    COMPOSITION = ' composition '
    AGGREGATION = ' aggregation '
    INHERITANCE = ' inheritance '
    ASSOCIATION = ': '
    DIRECTED_ASSOCIATION = ' directed association '
    DEPENDENCY = ' dependency '
    IMPLEMENTATION = ' implementation '
    COMPOSITION_ASSOCIATION = ' composition association '
    CONTAINMENT = ' containment '
    CROWS_FEET = ' crows feet '
    INTERFACE = ' interface '
