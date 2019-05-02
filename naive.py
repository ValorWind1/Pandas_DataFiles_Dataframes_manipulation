#a hamilton cycle through a graph that visits each node exactly once
def hamilton(G, size, pt, path=[]):  # pt = staring point , path = previously traversed vertices.
    print('hamilton called with pt={}, path={}'.format(pt, path))
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
        print('path {} is a dead end'.format(path))
    else:
        print('pt {} already in path {}'.format(pt, path))

G = {1:[4,14,20,24], 2:[0,3,9,17,21], 3:[6,18], 4:[7,11,22,24],5:[3,8,13,15,17]}
hamilton(G, 5, 1) 