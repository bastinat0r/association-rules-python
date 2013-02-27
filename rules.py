

"""
assosciaton rules with min confidence and support and the form d1 -> x as (d1, d2) where d1 is the rule-base, d2 (d1 | {x})
"""

def confidence(d1, d2, data):
    return support(d2, data) / support(d1, data)

def support(d, data):
    n = 0
    for x in data:
        if set(d) <= set(x):
            n += 1
    return n / len(data)

def frequent_sets(data, min_support):
    items = set([x for d in data for x in d])
    sets = set([frozenset([i]) for i in items if support(set([i]), data) > min_support])
    finished_sets = set()
    while len(sets) > 0:
        finished_sets = finished_sets | sets
        sets = set([
            frozenset(s | set([i]))
            for s in sets
            for i in items
                if i not in s
                    and support((s | set([i])), data) > min_support
        ])
    return finished_sets

def confident_rules(data, sets, min_confidence):
    rules = [];
    s = [(x, y) for x in sets for y in sets if x < y and confidence(x, y, data) > min_confidence]
    return s;

if __name__ == "__main__":
    data = [[1,2],[1],[2],[3],[1,2],[1],[1,2,3],[2,3],[4], [1,2], [1,2], [1], [1], [1], [1,2], [1,2,3], [1,3]]
    sets = frequent_sets(data, 0.1)
    print("\nFrequent Sets:")
    for s in sets:
        print("%s :\t%.2f" %(set(s), support(s, data)))
    cr = confident_rules(data, sets, 0.5)
    print("\nCondident Rules:")
    for r in cr:
        print("%s -> %s :\t%.2f" %(set(r[0]), set(r[1] - r[0]), confidence(r[0], r[1], data)))
