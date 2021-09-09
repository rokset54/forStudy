from bottle import post, request, template



@post('/Hamiltonov_path', method='post')
def parseText():
    matrixTxt = request.forms.get('matrix').splitlines()
    for i in range(len(matrixTxt)):
        matrixTxt[i] = str(str(matrixTxt[i]).replace(",",""))
    j = 1
    i = 0
    k = 0
    leen = len(matrixTxt)
    tmp = []
    matrix = {a: a for a in range(1, leen + 1)}
    while i < leen:
        while k < leen:
            if matrixTxt[i][k] == "1":
                tmp.append(k + 1)
            k += 1
        matrix[j] = tmp
        tmp =[]
        k = 0
        i += 1
        j += 1
    path1 = hamilton(matrix, leen, 1)
    ans = str(path1).strip(';')
    
    return template('index.tpl', title='Hamiltonov path', year="2021", answer= "Your Hamiltonian path: " + ans)
    

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
    
