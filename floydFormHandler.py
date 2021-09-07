from bottle import template, post, request
import copy
import datetime
from floyd import floyd

@post('/floyd', method='post') # Обработчик формы расчёта макимального потока
def posting():
    num = request.forms.get('CHANGE') # Получение данных с формы
    length = request.forms.get('LENGTH') # Получение данных с формы
    btn = request.forms.get('BTN') # Получение данных с формы
    graph=[] # Пустой массив для записи данных с формы, что бы сохранить данные
    if num=="": num=3 # Проверка заполенности поля
    if btn=="Enter": # 1 обработчик размерности матрицы
        for i in range(int(num)): # Создание массива массивов для отображения таблицы
            curr = []
            for j in range(int(num)):
                curr.append(0)
            graph.append(curr)
        return template('floyd.tpl',title="floyd", year="2021", graph=graph, length=num, answer="") # Возвращение страницы с таблицей, с указанной размерностью
    if btn=="Calculate": # 2 обработчик вычисления максимального потока
        inFile = "\n\n" # Запись в файл
        inFile += "the date of the: "+ datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S") # Запись даты в файл
        graph=[] # Создание пустого массива для записи данных с формы
        inFile += "\nInput data: " # Запись в файл
        for i in range(int(length)): # Цикл сбора данных с формы в массив
            inFile+="\n" # Запись в файл
            curr = []
            for j in range(int(length)):
                if not request.forms.get(str(i)+str(j))=="": 
                    inFile+=request.forms.get(str(i)+str(j))+ "  " # Запись в файл
                    curr.append(int(request.forms.get(str(i)+str(j))))
                else: 
                    curr.append(0)
                    inFile+="0  " # Запись в файл
            graph.append(curr)
        temp = copy.deepcopy(graph) # Глубокое копирование введённых данных пользователя для сохранения данных после перезагрузки, т.к. в процессе работы программы он изменится

        answer = str(floyd(graph)) # Поучение максимального потока
        ans = answer
        ans = "Answer is = " + answer # Проверка ответа для вывода соответствующего ответа пользователю
        inFile+="\n" # Запись в файл
        inFile+=ans # Запись в файл
        f = open('program_log/floyd.txt', 'a') # Открытие файла для записи в него данных
        f.write(inFile) # Запись данных
        return template('floyd.tpl',title="floyd", year="2021", graph=temp, length=length,answer=ans) # Возвращение страницы с таблицей и ответом
