# The ELIXIR::GA4GH Cloud

This page describes the "ELIXIR::GA4GH Cloud" project for the 1st de.NBI /
ELIXIR Germany BioHackathon.

## Abstract

The Global Alliance for Genomics and Health (GA4GH), an international
standard-setting organization bringing together opinion leaders in academia and
industry, has proposed a set of community standards for data storage, transfer
and processing in the cloud. The ELIXIR Cloud & AAI community, a GA4GH Driver
Project, is developing the ELIXIR::GA4GH Cloud (EGC), a federated cloud
environment for large-scale data analysis in the life sciences.
Interoperability across services and clouds is achieved through adopting GA4GH
standards and authentication and authorization guidelines.

To find out more about the organization and the project, check out a recent
[slide deck][slides], or the corresponding [webinar][webinar] (~1 hour). We
are also working on a new [website][website] and [documentation hub][docs],
but they are still under construction.

## Topics

* Cloud
* Containers
* Workflows
* GA4GH
* Galaxy

## Expected audience

* **Bioinformaticians / data scientists**, particularly those needing to run
  different workflows on large amounts of data
* **Systems/service administrators / DevOps**, particularly those interested in
  having their nodes join the ELIXIR::GA4GH Cloud
* **(Web) developers**, particularly those interested in adopting standards and
  guidelines to make their services compatible with the EGC
* **Testers / teachers / trainers** who are interested in interoperable cloud
  solutions

## Hacking topics

Work will be organized in different topics. We will determine which topic or
topics we will follow, depending on everyone's interests. To discuss that, we
will meet online in the afternoon of the first day at 4 pm. Please check
the [Slack channel](#communication) for call details.

1. Community engagement: Liaise with interested drivers, developers & sys
   admins in and beyond de.NBI (issue label: `outreach`); we are also very
   much interested to extend our collaborations and interoperability with
   Galaxy/Pulsar!
2. Integrate the proWES gateway for workflow-level federation (issue label:
   `workflow federation`)
3. Integrate the proTES gateway for task-level federation and/or work toward
   Nextflow and/or hybrid cloud support (issue label: `task federation`)
4. Generate documentation for end users, developers & administrators (issue
   label: `documentation`)

There are will be issues associated with each of the themes - just have a look
at the [project board][project-board]. There may not be issues associated with
every theme yet, but check frequently - more issues will be added as soon as we
will know which themes we will work on.

## Communication

We will mainly use the ELIXIR Cloud & AAI Slack board (channel `#biohackathon`)
for communication, as a big part of the hackers who signed up for the project
are already members of that Slack board. Moreover, there is a whole range of
other people on that board who may be able to help us along. However, we will
also use the de.NBI BioHackathon board (channel `#elixir-ga4gh-cloud`).

* Invitation Slack board ELIXIR Cloud & AAI Slack board (channel
  `#biohackathon`):
  <https://join.slack.com/t/elixir-cloud/shared_invite/enQtNzA3NTQ5Mzg2NjQ3LTZjZGI1OGQ5ZTRiOTRkY2ExMGUxNmQyODAxMDdjM2EyZDQ1YWM0ZGFjOTJhNzg5NjE0YmJiZTZhZDVhOWE4MWM>
* Invitation Slack board de.NBI (channel `#elixir-ga4gh-cloud`):
  <https://join.slack.com/t/elixir-deworkspace/shared_invite/zt-1l6ku2o42-tqtThD8JgTYV93NaQ~SjFQ>
* Project lead: Alex Kanitz <alexander.kanitz@unibas.ch>

## Possible outcomes

* New driver projects or collaborators found and/or additional use cases for
  the ELIXIR::GA4GH Cloud defined
* Additional computing centers and data portals represented by the BioHackathon
  community integrated into the EGC
* New services for workflow and task federation integrated into the EGC
* Improved website and/or documentation

Note that all outputs will be added to the appropriate repositories, generally
available on the [ELIXIR Cloud & AAI GitHub organization][gh-org]. Free and
Open Source licenses are available for all repositories, usually Apache 2.0 for
code and CC0 or CC-BY for documentation. The [de.NBI / ELIXIR-DE BioHackathon
IP disclaimer][ip] applies.

[docs]: <https://elixir-cloud-aai.github.io/>
[gh-org]: <https://github.com/elixir-cloud-aai>
[ip]: <https://github.com/deNBI/biohackathon-2022/blob/f0c50fa3a42440da64e5adc51ad474029fc50c5c/README.md#biohackathon-ip-disclaimer>
[project-board]: <https://github.com/orgs/elixir-cloud-aai/projects/7>
[slides]: <https://docs.google.com/presentation/d/1DyrwN6HhJ-Tz6mh_QBObFQruWr7zCOL-BIn17Zjlqk4/edit?usp=sharing>
[webinar]: <https://www.pistoiaalliance.org/pistoia-webinars/the-elixirga4gh-cloud-towards-a-federated-fair-life-science-analytics-infrastructure/>
[website]: <https://elixir-cloud.dcc.sib.swiss/>
