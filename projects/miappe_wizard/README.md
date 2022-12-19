# MIAPPE Wizard

This page describes the "MIAPPE Wizard: Enabling easy creation of MIAPPE-compliant ISA metadata for Plant Phenotyping Experiments" project for the 1st de.NBI /
ELIXIR Germany BioHackathon.

## Abstract

Experimental data are only useful to other researchers if they are findable, accessible, interoperable, and reusable (FAIR). The ISA framework allows scientists to publish metadata about their experiments in a machine-readable plain text format designed to provide this interoperability and reusability. Furthermore, the MIAPPE standard (Papoutsoglou et al. 2020) defines a minimal checklist for metadata that has to be included for describing plant phenotyping experiments.
Toolkits like isa4j (Psaroudakis et al. 2020) or isatools (Johnson et al. 2021) have been developed for the programmatic creation of these metadata files but MIAPPE-compliant datasets are still scarce. The hurdle for biologists to capture and maintain such metadata that actually perform plant phenotyping experiments is high due to lack of programming experience, diverse tooling for metadata capturing, complexity in concept mapping to ontologies, and also because data stewardship infrastructures are still not common at many research institutes to support them. We therefore propose to develop an intuitive step-by-step wizard which guides users through the creation of metadata for their experiments by asking clear and specific questions tailored to the MIAPPE case. This would be supported by intelligent content recommendations, for example querying ontologies, pre-filling empty data
fields when uploading documents (e.g. study titles, etc.) and taking care of the appropriate formatting in the background, without the need to be familiar with the ISA concept or MIAPPE standard.
Leveraging isa4j’s MIAPPE extension developed during BioHackathon Europe 2021, we will create an easy-to-use web application which outputs ISA-Tab and ISA-JSON and set-up a publicly available instance to use free of charge, installation or registration. The software will be designed in a way which also allows it to be integrated as a Module/Plug-In in custom workflows and can thereby serve as an input interface to any existing or upcoming ISA consumer.

## Topics

* Plant Sciences
* Data formats
* MIAPPE
* ISA
* ARC
* web app

## Expected audience

* Bioinformaticians with an interest in plant sciences, ontologies, web technologies, and javascript.
* Biologists with a background in phenotyping.

## Hacking topics

Add your hacking topics here.

* Topic 1

## Communication

* Slack channel: #web_browser_tool_miappe
* Project lead: Sebastian Beier <s.beier@fz-juelich.de>
* Project lead: Daniel Arend <arendd@ipk-gatersleben.de>

## Possible outcomes

* Add possible outputcomes here 

The [de.NBI / ELIXIR-DE BioHackathon
IP disclaimer][ip] applies.

[docs]: <https://denbi.de>

