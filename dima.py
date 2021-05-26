from bottle import post, request

@post('/home', method='post')
def parseText():
    matrixTxt = request.forms.get('matrix')
    return matrixTxt

def hamilton(G, size, pt, path=[]):
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  # skip loop or dead end
                return candidate
