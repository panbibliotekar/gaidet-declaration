# /// script
# requires-python = ">=3.10"
# dependencies = [
#     "bioregistry",
#     "click",
#     "pyobo>=0.12.6",
#     "pyyaml",
# ]
# ///

"""Generate ontology artifacts for GAIDeT."""

from pathlib import Path

import bioregistry
import click
import yaml

from pyobo import Reference, Term, build_ontology
from pyobo.struct.typedef import exact_match, has_ontology_root_term

HERE = Path(__file__).parent.resolve()
TERMS_PATH = HERE.joinpath("_data", "terms.yml")
OBO_PATH = HERE.joinpath("gaidet.obo")
OWL_PATH = HERE.joinpath("gaidet.owl")

CURIE_PREFIX = "gaidet"
URI_PREFIX = "https://w3id.org/gaidet/"  # TODO need PURL scheme

NAME = "Generative Artificial Intelligence Delegation Taxonomy"
DESCRIPTION = "An extension/complement to Contributor Roles Taxonomy and the Contributor Roles Ontology for generative artificial intelligence."
REPOSITORY = "https://github.com/panbibliotekar/gaidet-declaration"
ROOT = Reference(prefix="cro", identifier="0000000", name="contributor role")


def _annotate_mappings(term: Term, record) -> None:
    for mapping in record.get("mappings", []):
        predicate = Reference.from_curie(mapping["predicate"])
        obj = Reference.from_curie(mapping["object"])
        term.annotate_object(predicate, obj)


@click.command()
def main() -> None:
    """Generate ontology artifacts for GAIDeT."""
    bioregistry.add_resource(
        bioregistry.Resource(
            prefix=CURIE_PREFIX,
            uri_format=URI_PREFIX + "$1",
            repository=REPOSITORY,
            description=DESCRIPTION,
        )
    )

    records = yaml.safe_load(TERMS_PATH.read_text())
    terms = [Term(reference=ROOT)]
    for record in records.values():
        term = Term(
            reference=Reference(prefix=CURIE_PREFIX, identifier=record["id"], name=record["label"])
        )
        term.append_parent(ROOT)
        # TODO add ukranian label
        _annotate_mappings(term, record)
        terms.append(term)

        for child in record["terms"]:
            child_term = Term.from_triple(
                prefix=CURIE_PREFIX, identifier=child["id"], name=child["label"]
            )
            child_term.append_parent(term)
            _annotate_mappings(child_term, child)
            terms.append(child_term)

    ontology = build_ontology(
        prefix=CURIE_PREFIX,
        terms=terms,
        typedefs=[exact_match, has_ontology_root_term],
        root_terms=[ROOT],
    )
    ontology.write_obo(OBO_PATH)
    ontology.write_owl(OWL_PATH)


if __name__ == "__main__":
    main()
