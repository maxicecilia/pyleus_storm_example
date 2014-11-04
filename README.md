Pyleus-Storm Example
====================

A quick test of what can be done using apache storm + pyleus + neo4j.

What you need:
* Apache Storm (installed as release)
* Pyleus (pip install pyleus)
* Neo4j (assume to be in the default host/port)

To run:
```
$ pyleus build storm_py.yaml
$ pyleus local storm_py.jar -d
```
