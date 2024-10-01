import os

if not os.path.exists("build"):
    os.mkdir("build")

content = """@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:something a rdfs:Class .
"""

with open("build/output.ttl", "w") as f:
    f.write(content)

print("Created file.")