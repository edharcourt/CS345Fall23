from typing import Tuple, List, Set


def attr_closure(F: Set[Tuple[Set[str], Set[str]]], X: Set[str]) -> Set[str]:
    """Compute the closure of X under F."""
    result = X.copy()
    done = False

    while not done:
        before = len(result)
        for (beta, gamma) in F:
            if beta.issubset(result):
                result = result.union(gamma)
        if len(result) == before:
            done = True
    return result

if __name__ == '__main__':
    F = [
        ({'a'}, {'b'}),       # a --> b
        ({'a'}, {'c'}),       # a --> c
        ({'c', 'g'}, {'h'}),  # cg --> h
        ({'c', 'g'}, {'i'}),  # cg --> i
        ({'b'}, {'h'})        # b --> h
    ]

    print(attr_closure(F, {'a'}))  # {'b', 'c', 'h', 'i'}
    print(attr_closure(F, {'b'}))  # {'b', 'h'}