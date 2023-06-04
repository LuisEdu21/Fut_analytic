from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
import bd as ac


def buscar_HTML(Link):
    #Navegador selenium
    navegador = webdriver.Chrome()

    navegador.get(Link)

    sleep(10)

    #Transformando a Pagina em HTML document
    html = BeautifulSoup(navegador.page_source, 'html.parser')

    return html

def brasileirao_Serie_A():
    Link = 'https://www.google.com/search?gs_ssp=eJzj4tTP1TdIy8s2LzRg9OJOKkoszsxJzSxKzAcAXOUICQ&q=brasileirao&oq=Bras&aqs=chrome.1.69i57j46i39i650j69i60l2j69i65l3j69i60.2527j1j7&sourceid=chrome&ie=UTF-8#sie=lg;/g/11jspy1hvm;2;/m/0fnk7q;st;fp;1;;;'

    html = buscar_HTML(Link)

    print('Pegando o time!')

    Time = html.find_all('span',class_="ellipsisize hsKSJe")

    liga = html.find('div',class_="ofy7ae").get_text()

    print(liga)

    c = 0
    x = 0
    y = 0
    z = 0

    for Clubes in Time:
        Clube = Time[x].get_text()
        print(Clube)

        if z == 0:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc xL0E7c")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc xL0E7c")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                sleep(2)
                z = z + 1
                c = 1
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
        elif z == 19:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc bWoKCf")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc bWoKCf")
            for i in range (1):
                y = 0
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                z = z + 1
                c = 20
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
                break
        elif z < 19:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                y = y + 4
                z = z + 1
                c = c + 1 
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)       
        else:
            print("Tabela Concluida")

        x = x + 1

    return print('Brasileirao concluido...')

def brasileirao_Serie_B():
    Link = 'https://www.google.com/search?q=brasileiro+s%C3%A9rie+b&sxsrf=APwXEder5zwnicm_d0ocJUHN9w36F3wxGA%3A1685399740092&ei=vCh1ZKmjBc7O1sQP5Nqn6A8&gs_ssp=eJzj4tTP1TdIy8tOMjVg9BJOKkoszsxJzSzKVyg-vLIoM1UhCQCstwtg&oq=brasileirao+s&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgBMgUILhCABDINCC4QgwEQsQMQgAQQCjINCAAQgAQQsQMQgwEQCjIKCAAQgAQQsQMQCjIFCC4QgAQyDQgAEIAEELEDEIMBEAoyDQgAEIAEELEDEIMBEAoyDQgAEIAEELEDEIMBEAoyBQgAEIAEMgUIABCABDITCC4QgAQQlwUQ3AQQ3gQQ4AQYAjoKCAAQRxDWBBCwAzoKCAAQigUQsAMQQzoPCC4QigUQyAMQsAMQQxgBOgsILhCDARCxAxCABDoNCC4QgwEQsQMQigUQQzoLCAAQgAQQsQMQgwE6DQguEIAEELEDEIMBEAo6CAgAEIAEELEDOhkILhCDARCxAxCABBCXBRDcBBDeBBDgBBgCSgQIQRgAUPYCWPIEYJYPaAFwAXgAgAHcAYgBnAOSAQUwLjEuMZgBAKABAcABAcgBDNoBBAgBGAjaAQYIAhABGBQ&sclient=gws-wiz-serp#sie=lg;/g/11tj9phg47;2;/m/0fnkb5;st;fp;1;;;'

    html = buscar_HTML(Link)

    print('Pegando o time!')

    Time = html.find_all('span',class_="ellipsisize hsKSJe")

    liga = html.find('div',class_="ofy7ae").get_text()

    print(liga)

    c = 0
    x = 0
    y = 0
    z = 0

    for Clubes in Time:
        Clube = Time[x].get_text()
        print(Clube)

        if z == 0:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc xL0E7c")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc xL0E7c")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                sleep(2)
                z = z + 1
                c = 1
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
        elif z == 19:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc bWoKCf")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc bWoKCf")
            for i in range (1):
                y = 0
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                z = z + 1
                c = 20
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
                break
        elif z < 19:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                y = y + 4
                z = z + 1
                c = c + 1 
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)       
        else:
            print("Tabela Concluida")

        x = x + 1

    return print('Brasileirao concluido...')

def Bundesliga():
    Link = 'https://www.google.com/search?q=campeonato+alem%C3%A3o&sxsrf=AJOqlzUpjxInAiXem_x2Ar-Z-Vpw0cR45g%3A1674259262546&ei=PivLY-T3IO3b5OUPh9Og4A0&gs_ssp=eJzj4tTP1TcwNjc0szRg9BJKTswtSM3PSyzJV0jMSc09vDgfAIpjCmE&oq=campeonato+al&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAxgAMgsILhCDARCxAxCABDILCC4QgwEQsQMQgAQyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATILCAAQgAQQsQMQgwEyCwgAEIAEELEDEIMBMgsIABCABBCxAxCDATIICAAQsQMQgwEyBQgAEIAEMgUIABCABDoKCAAQRxDWBBCwAzoHCAAQsAMQQzoMCC4QyAMQsAMQQxgBOg8ILhDUAhDIAxCwAxBDGAE6BAgjECc6CgguEIMBELEDEEM6DgguEIMBENQCELEDEIAEOggIABCABBCxAzoFCC4QgAQ6CQgjECcQRhD9AToECC4QJzoKCC4QsQMQgwEQQzoLCC4QgAQQsQMQgwE6CAguEIAEENQCOggILhCABBCxA0oECEEYAEoECEYYAVDXAlihEWCsHGgBcAF4AIABvwGIAZoKkgEDMC44mAEAoAEByAETwAEB2gEGCAEQARgI&sclient=gws-wiz-serp#sie=lg;/g/11j4slbd63;2;/m/037169;st;fp;1;;;'

    html = buscar_HTML(Link)

    print('Pegando o time!')

    Time = html.find_all('span',class_="ellipsisize hsKSJe")

    liga = html.find('div',class_="ofy7ae").get_text()

    print(liga)

    c = 0
    x = 0
    y = 0
    z = 0

    for Clubes in Time:
        Clube = Time[x].get_text()
        print(Clube)

        if z == 0:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc xL0E7c")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc xL0E7c")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                sleep(2)
                z = z + 1
                c = 1
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
        elif z == 17:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc bWoKCf")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc bWoKCf")
            for i in range (1):
                y = 0
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                z = z + 1
                c = 20
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)
                break
        elif z < 17:
            Parte_1 = html.find_all('td',class_="e9fBA xkW0Cc snctkc")
            Parte_2 = html.find_all('td', class_="e9fBA xkW0Cc snctkc kRLtzc")
            for i in range (1):
                sleep(2)
                Pontuação = Parte_1[y].get_text()
                Jogos = Parte_1[y+1].get_text()
                Vitoria = Parte_1[y+2].get_text()
                Saldo_de_Gol = Parte_1[y+3].get_text()
                Empates = Parte_2[y].get_text()
                Derrota = Parte_2[y+1].get_text()
                Gols_Marcado = Parte_2[y+2].get_text()
                Gols_Contra = Parte_2[y+3].get_text()
                print(Pontuação)
                print(Jogos)
                print(Vitoria)
                print(Empates)
                print(Derrota)
                print(Gols_Marcado)
                print(Gols_Contra)
                print(Saldo_de_Gol)
                sleep(2)
                y = y + 4
                z = z + 1
                c = c + 1 
                print(c)
                ac.Inserirtime(liga,c,Clube,Pontuação,Jogos,Vitoria,Empates,Derrota,Gols_Marcado,Gols_Contra,Saldo_de_Gol)       
        else:
            print("Tabela Concluida")

        x = x + 1

    return print('Bundesliga concluido...')
