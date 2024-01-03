from pydantic.v1 import BaseModel, Field
from typing import List


class OntologyRelation(BaseModel):
    source: str = Field(..., description="The source of the relationship")
    target: str = Field(..., description="The target of the relationship")
    relation_name: str = Field(
        ..., description="Describes the relationship between source and target"
    )


class OntologyTerm(BaseModel):
    name: str = Field(..., description="The name of the term")
    definition: str = Field(..., description="The definition of the term")


class Ontology(BaseModel):
    ontology_relations: List[OntologyRelation] = Field(
        ..., description="The list of relations in the ontology"
    )
    ontology_terms: List[OntologyTerm] = Field(
        ..., description="The list of description of each term in the ontology"
    )
