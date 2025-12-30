# Auto generated from person_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2025-12-30T13:42:45
# Schema: PersonSchema
#
# id: http://example.org/person
# description:
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Integer, String

metamodel_version = "1.7.0"
version = None

# Namespaces
EX = CurieNamespace('ex', 'http://example.org/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
DEFAULT_ = EX


# Types

# Class references



@dataclass(repr=False)
class Person(YAMLRoot):
    """
    A simple person
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["Person"]
    class_class_curie: ClassVar[str] = "ex:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = EX.Person

    name: str = None
    age: Optional[int] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.name):
            self.MissingRequiredField("name")
        if not isinstance(self.name, str):
            self.name = str(self.name)

        if self.age is not None and not isinstance(self.age, int):
            self.age = int(self.age)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PersonCollection(YAMLRoot):
    """
    A container for multiple persons
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = EX["PersonCollection"]
    class_class_curie: ClassVar[str] = "ex:PersonCollection"
    class_name: ClassVar[str] = "PersonCollection"
    class_model_uri: ClassVar[URIRef] = EX.PersonCollection

    persons: Optional[Union[Union[dict, Person], list[Union[dict, Person]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.persons, list):
            self.persons = [self.persons] if self.persons is not None else []
        self.persons = [v if isinstance(v, Person) else Person(**as_dict(v)) for v in self.persons]

        super().__post_init__(**kwargs)


# Enumerations


# Slots
class slots:
    pass

slots.person__name = Slot(uri=EX.name, name="person__name", curie=EX.curie('name'),
                   model_uri=EX.person__name, domain=None, range=str)

slots.person__age = Slot(uri=EX.age, name="person__age", curie=EX.curie('age'),
                   model_uri=EX.person__age, domain=None, range=Optional[int])

slots.personCollection__persons = Slot(uri=EX.persons, name="personCollection__persons", curie=EX.curie('persons'),
                   model_uri=EX.personCollection__persons, domain=None, range=Optional[Union[Union[dict, Person], list[Union[dict, Person]]]])

