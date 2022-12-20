# Improving interoperability support for authoring, editing and conversion of mzTab-M for Lipidomics Tools (and Metabolomics)

This page describes the "Improving interoperability support for authoring, editing and conversion of mzTab-M for Lipidomics (and Metabolomics) Tools" project for the 1st de.NBI /
ELIXIR Germany BioHackathon.

## Abstract

mzTab-M is a HUPO-PSI standard for the description of quantitative mass spectrometry analysis results of small molecules [Neumann, S. et al. mzTab-M: a data standard for sharing quantitative results in mass spectrometry metabolomics. Anal. Chem. (2019). doi:10.1021/acs.analchem.8b04310]. It has been implemented as an input format already by MetaboAnalyst and the GNPS repository and is produced by multiple softwares, such as LipidDataAnalyzer, MZmine 3 and MS-DIAL 4. However, authoring an mzTab-M file is still challenging due to the lack of a user-interface to produce a skeleton structure containing the experiment metadata and summary information.

## Topics

Provide a list of topics of your project

* mass spectrometry
* small molecules
* FAIR
* minimal information
* interoperability

## Expected audience

* Bioinformaticians with an interest in data formats, standardization, FAIR, interoperability
* Biologists / Chemists with a background in mass spectrometry of small molecules

## Hacking topics

Within the scope of the biohackathon, our main goals are to:

* Provide a first version of a user interface in lxPostman to define and create a study design and metadata, backed by controlled vocabularies, as a template mzTab-M and combine it with the output of LipidXplorer.
* Align information that is reported within the mzTab-M file with the recently published Lipidomics Checklist [Mcdonald, J. G. et al. Introducing the Lipidomics Minimal Reporting Checklist. doi:10.1038/s42255-022-00628-3]
* Verify interoperability of the generated mzTab-M with the data submission and import workflow of the LipidCompass quantitative lipidomics reference database and other tools that already support the format.
* Convert mzTab-M into the ISA-Tab format to allow easier submission of lipidomics mass spectrometry results to the EBI MetaboLights database.

## Communication

Contact information / project coordination:

* Eduardo Jacobo Miranda Ackerman <mirandaa@mpi-cbg.de>
* Daniel Krause <dkrause@fz-borstel.de>
* Nils Hoffmann <n.hoffmann@fz-juelich.de>

## Possible outcomes

* We aim to prepare a manuscript on lxPostman + mzTab-M support within one year after the Biohackathon.
* As stretch goals, depending on available support by co-hackers, we want to explore the possibility of generating an mzTab-M file from Skyline, another software that is often used to run targeted lipidomics experiments, and to improve support for mzTab-M within MZmine 3 to support different peak detection and identification workflows.

The [de.NBI / ELIXIR-DE BioHackathon IP disclaimer][ip] applies.

[docs]: <https://github.com/HUPO-PSI/mzTab>

