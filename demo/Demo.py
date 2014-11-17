from ppp_nlp_ml_standalone import ExtractTriple

if __name__ == "__main__":
    extractTriple = ExtractTriple.ExtractTriple()
    lua = False
    while True:
        s = input()
        if s is not '':
            extractTriple.change_method("PythonLinear")
            extractTriple.print_triplet(extractTriple.extract_from_sentence(s))
            if lua:
                extractTriple.change_method("LuaLinear")
                extractTriple.print_triplet(extractTriple.extract_from_sentence(s))
