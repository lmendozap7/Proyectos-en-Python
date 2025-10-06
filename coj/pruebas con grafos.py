N = {
    'a': set('bcdef'),
    'b': set('ce'),
    'c': set('d'),
    'd': set('e'),
    'e': set('f'),
    'f': set('cgh'),
    'g': set('fh'),
    'h': set('fg')
}


def walk(G, s, S=set()):  # Walk the graph from node s
    P, Q = dict(), set()  # Predecessors + "to do" queue
    P[s] = None  # s has no predecessor
    Q.add(s)  # We plan on starting with s
    while Q:  # Still nodes to visit
        u = Q.pop()  # Pick one, arbitrarily
        for v in G[u].difference(P, S):  # New nodes?
            Q.add(v)  # We plan to visit them!
            P[v] = u  # Remember where we came from
    return P  # The traversal tree


def components(G):  # The connected components
    comp = []
    seen = set()  # Nodes we've already seen
    for u in G:  # Try every starting point
        if u in seen: continue  # Seen? Ignore it
        C = walk(G, u)  # Traverse component
        seen.update(C)  # Add keys of C to seen
        comp.append(C)  # Collect the components
    return comp


print components(N)
