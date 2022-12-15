# Towards a minimum information checklist for biomedical research projects with sensitive human data (only remote)

Please adapt the following template to your needs:

This page describes the "Towards a minimum information checklist for biomedical research projects with sensitive human data (only remote)" project for the 1st de.NBI ELIXIR Germany BioHackathon.

## Abstract

Research data from human subjects that is not of an anonymized nature is considered personal data and as such it is subject to the EU GDPR regulation. For research projects, the GDPR entails, among others, increased record keeping requirements throughout the data lifecycle, starting from data’s collection through to its deposition to repositories for secondary use – typically under controlled-access regimes. The said records are expected to contain a GDPR-oriented characterisation of data subjects and data sets, the legal grounds and the nature of data processing, the parties involved, allowed data uses and retention periods as well as logs of report-worthy activities in the data lifecycle, such as data transfers.

ELIXIR Luxembourg and ELIXIR Switzerland are two ELIXIR nodes that have developed open source tools to assist biomedical research teams with GDPR record keeping. Since a couple of years, these tools, namely DAISY and ERPA, have been in active use in respective ELIXIR nodes and some others. Despite serving a similar GDPR requirement, these two tools have different target end users and consequently differences in the information they ultimately capture. The development teams of the two tools have been in contact since early days and have been monitoring the direction each tool is taking.

In this project we propose the following:
- perform a critical and comparative review of the underlying information models of [DAISY](https://github.com/elixir-luxembourg/daisy) and [ERPA](https://gitlab.sib.swiss/clinbio/erpa-app). During this review we will take into account past experience in using our tools as well as guidelines which have shaped our tools in the first place, i.e guidance on GDPR record keeping published by relevant sector-specific, national and EU authorities.
- create a checklist for the reporting of biomedical research activities and the human datasets that they have produced. We will develop this guideline in the style of [Minimum Information Checklists](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2771753/) that researchers are already familiar with.

We foresee that the produced checklist can be used on its own for the manual reporting of projects and resulting human datasets, particularly in scenarios where the data is to be shared for secondary use. In addition, the guideline can be picked up by the developer teams of DAISY and ERPA to eventually upgrade them and introduce new interoperability features into these tools.

## Topics

Provide a list of topics of your project

* Record of Processing Activities
* Sensitive Data
* Minimal Information checklist

## Expected audience

* Research support staff responsible for GDPR compliance
* Researchers processing sensitive data
* Researchers with knowledge of JSON schema and JSON-LD
* 

## Hacking topics

* Intersaction of DAISY, ERPA, ICO and CNIL model - core model
* JSON schema of core model
* JSON-LD of core model

## Communication

Main channel: [Biohackaton Slack](https://join.slack.com/t/elixir-deworkspace/shared_invite/zt-1l6ku2o42-tqtThD8JgTYV93NaQ~SjFQ) workspace - channel **#checklist_for_human_data** 

Main contact: Vilem Ded <vilem.ded@uni.lu>

## Possible outcomes

* Minimal Information about Record Of Processing Activities (MIROPA)

The [de.NBI / ELIXIR-DE BioHackathon
IP disclaimer][ip] applies.

[docs]: <https://denbi.de>
