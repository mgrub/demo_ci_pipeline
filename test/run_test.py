import rdflib

def test_syntax():
    error_status = False

    try:
        g = rdflib.Graph()
        g.parse("build/output.ttl")
    except SyntaxError as e:
        error_status = True
    
    return error_status

def test_meaning():

    error_status = False

    g = rdflib.Graph()
    g.parse("build/output.ttl")

    if len(list(g.triples((None, None, None)))) == 0:
        error_status = True

    return error_status

def main():
    syntax_error = test_syntax()

    if syntax_error:
        raise ImportError()

    meaning_error = test_meaning()
    if meaning_error:
        raise ValueError()
    
    print(syntax_error, meaning_error)

if __name__ == "__main__":
    main()