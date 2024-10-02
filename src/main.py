import os

if not os.path.exists("build"):
    os.mkdir("build")

content = """@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix ex: <http://example.org/> .

ex:something a rdfs:Class .
"""

with open("build/output.ttl", "w") as f:
    f.write(content)

release_notes = """# A new release from this demo repo

Could link some ideas here.

## Changelog

not implemented

## Coffee

Yes, please.
"""

with open("build/release_note.md", "w") as f:
    f.write(release_notes)


print("Created file.")