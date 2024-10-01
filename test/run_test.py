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

    # some not very elaborate test
        error_status = True

    return error_status

def main():
    syntax_error = test_syntax()

    if syntax_error:
        raise ImportError("The syntax of the generated files is not ok.")

    meaning_error = test_meaning()
    if meaning_error:
        raise ValueError("A requirement regarding the content of the output files is not met.")
    
    print(syntax_error, meaning_error)

if __name__ == "__main__":
    main()