from copy import deepcopy
from reference import top_k

from fuzzingbook.Grammars import is_valid_grammar
from fuzzingbook.Grammars import convert_ebnf_grammar
from fuzzingbook.Grammars import Grammar

input_grammar: Grammar = convert_ebnf_grammar({
    "<start>": ["(<integer>,[<integer>(,<integer>)*])"],
    "<integer>": ["<nzdigit><digit>*"],
    "<nzdigit>":[str(x) for x in range(1,10)], 
    "<digit>": [str(x) for x in range(10)]
})

assert is_valid_grammar(input_grammar)

def entrypoint(s: str):
    if s is None:
        return -1

    k,l = eval(s)
    k = k % len(l)
    return (deepcopy(l),k, top_k(l,k))
