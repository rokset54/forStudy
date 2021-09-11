from bottle import post, request, template

#Считывает и преобразует матрицу к нужному виду
@post('/Hamiltonov_path', method='post')
def main():
    inmatrix = request.forms.get('matrix').splitlines()
    matrix = parseText(inmatrix)
    path1 = hamilton(matrix, len(matrix), 1)
    ans = str(path1).strip(';')
    return template('index.tpl', title='Hamiltonov path', year="2021", answer= "Your Hamiltonian path: " + ans) 

def parseText(inmatrix):
    matrixTxt = inmatrix
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
    return matrix
    
    
    
    
#Вычисляет Гамильтонов путь
def hamilton(G, size, pt, path=[]):
    if pt not in set(path): #проверяет есть ли текущее значение точки в массиве
        path.append(pt)
        if len(path)==size: #проверка длины пути
            return path
        for pt_next in G.get(pt, []): #выбор следующей точки
            res_path = [i for i in path] #сохранение текущего пути на случай если догадка не правильна
            candidate = hamilton(G, size, pt_next, res_path) 
            if candidate is not None:  # skip loop or dead end
                return candidate
    
