#!/usr/bin/env python

import click
from click_loglevel import LogLevel
import logging

from linkml_runtime.utils.schemaview import SchemaView


from rdflib import Graph, URIRef
from json import dumps


@click.command()
@click.argument("model", type=click.Path(exists=True))
@click.argument("data", type=click.Path(exists=True))
@click.option("-p", "--prefix", type=str, default="bioschemas")
@click.option("-i", "--indent", type=int, default=4)
@click.option("-l", "--log-level", type=LogLevel(), default=logging.ERROR)
def dump(model, data, prefix, indent, log_level):

    logging.basicConfig(level=log_level)

    mappings = {}

    sv = SchemaView(str(model))
    ns = sv.namespaces()
    for ckey, cvalue in sv.schema.classes.items():
        for skey, svalue in cvalue.slot_usage.items():
            for mapping in svalue.exact_mappings:
                logging.debug(ckey, skey, "->", mapping)
                uri = sv.get_uri(svalue)
                if not mapping.startswith(prefix):
                    logging.info("Skipping prefix: %s!=%s", mapping, prefix)
                    continue
                if ":" in uri:
                    first, second = uri.split(":")
                    uri = f"{ns[first]}{second}"
                if ":" in mapping:
                    first, second = mapping.split(":")
                    mapping = f"{ns[first]}{second}"
                mappings[uri] = mapping

    graph = Graph().parse(data)
    output = Graph()
    for s, p, o in graph:
        logging.debug("INPUT:" + "%s"*3, s, p, o)
        lookup = mappings.get(str(p))
        if lookup:
            output.add((s, URIRef(lookup), o))

    jsonld = {
        "@context": "http://schema.org",
        "@type": "Dataset",
    }
    for s, p, o in output:
        logging.debug("OUTPUT:" + "%s"*3, s, p, o)

        # Without json-ld framing, it's unclear how
        # best to go from these triples to a desired
        # block of JSON-LD.
        key = str(p).split("/")[-1]
        jsonld[key] = str(o)

    print(dumps(jsonld, indent=indent, sort_keys=True))


if __name__ == "__main__":
    dump()
