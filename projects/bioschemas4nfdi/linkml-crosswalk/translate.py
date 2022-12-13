#!/usr/bin/env python

import click
from click_loglevel import LogLevel
import logging

from linkml_runtime.utils.schemaview import SchemaView


from rdflib import Graph, URIRef


@click.command()
@click.argument("model", type=click.Path(exists=True))
@click.argument("data", type=click.Path(exists=True))
@click.argument("mapping", type=str)
@click.option("-l", "--log-level", type=LogLevel(), default=logging.INFO)
def dump(model, data, mapping, log_level):

    logging.basicConfig(level=log_level)

    mappings = {}

    sv = SchemaView(str(model))
    ns = sv.namespaces()
    for ckey, cvalue in sv.schema.classes.items():
        for skey, svalue in cvalue.slot_usage.items():
            for mapping in svalue.exact_mappings:
                print(ckey, skey, "->", mapping)
                uri = sv.get_uri(svalue)
                if ":" in uri:
                    first, second = uri.split(":")
                    uri = f"{ns[first]}{second}"
                if ":" in mapping:
                    first, second = mapping.split(":")
                    mapping = f"{ns[first]}{second}"
                mappings[uri] = mapping

    graph = Graph().parse(data)
    output = Graph()
    print("INPUT")
    for s, p, o in graph:
        print(s, p, o)
        lookup = mappings.get(str(p))
        if lookup:
            output.add((s, URIRef(lookup), o))
    print("OUTPUT")
    for s, p, o in output:
        print(s, p, o)


if __name__ == "__main__":
    dump()
