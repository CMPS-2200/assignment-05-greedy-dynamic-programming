from main import *

# 10 pts
def test_huffman_simple():
    """ example from class """
    f = Counter(["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "C", "D"])
    T = make_huffman_tree(f)
    C = get_code(T)
    assert huffman_cost(C, f) == 17

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('relevant', 'elephant')]

# 6 pts
def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)

# 2 pts                               
def test_align_1():
    S = 'book'
    T = 'back'
    align_S, align_T = fast_align_MED(S, T)
    assert (align_S == 'book' and align_T == 'back')

# 2 pts
def test_align_2():
    S = 'kookaburra'
    T = 'kookybird'
    align_S, align_T = fast_align_MED(S, T)
    assert (align_S == 'kookaburra' 
            and (align_T == 'kookybird-' 
                 or align_T == 'kookybir-d'
                 or align_T == 'kookyb-ird'))

# 2 pts                               
def test_align_3():
    S = 'relevant'
    T = 'elephant'
    align_S, align_T = fast_align_MED(S, T)
    assert ((align_S == 'relev-ant' and align_T == '-elephant')
            or (align_S == 'rele-vant' and align_T == '-elephant'))