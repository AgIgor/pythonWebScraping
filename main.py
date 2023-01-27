import requests
import time
from bs4 import BeautifulSoup
import datetime
from telebot import TeleBot

app = TeleBot(__name__)

lista_jogos = ['https://www.google.com.br/search?q=cota%C3%A7%C3%A3o+dolar&sxsrf=AJOqlzVtQd4x4pmItN7JXTkKjPKn8YYjyw%3A1674780358325&source=hp&ei=xh7TY_-pEZDC5OUPyKq-uAI&iflsig=AK50M_UAAAAAY9Ms1sm86vAZDExU3C5rSgF0KmfwrV5K&oq=cot&gs_lcp=Cgdnd3Mtd2l6EAMYADIECCMQJzIGCCMQJxATMgQIIxAnMg0IABCABBCxAxCDARAKMg0IABCABBCxAxCDARAKMg0ILhCABBCxAxCDARAKMgoIABCxAxCDARBDMgcIABCABBAKMhAILhCABBCxAxDHARDRAxAKMg0IABCABBCxAxCDARAKOgcIIxDqAhAnOg0ILhDHARCvARDqAhAnOgQIABBDOg0ILhCxAxDHARDRAxBDOgsIABCABBCxAxCDAToLCC4QgAQQsQMQgwE6BQgAEIAEOgcIABCxAxBDOggIABCABBCxAzoICC4QgAQQsQNQiiVYtDBg6DZoAnAAeACAAYABiAHSA5IBAzAuNJgBAKABAbABCg&sclient=gws-wiz']


def busca_preco(url):
    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    print(soup.prettify())
    price = soup.find("span", class_="DFlfde SwHCTb")
    name = soup.find("span", class_="MWvIVe nGP2Tb")
    print(name, price)
    return [price.string, name.string]


@app.route('/busca ?(.*)')
def busca(message, cmd):
    chat_dest = message['chat']['id']
    # msg = f"Recebido: {cmd} \nId: {chat_dest}"

    for i in lista_jogos:

        preco, nome = (busca_preco(i))
        msg = f"{nome}\n{preco}"
        time.sleep(1)
        app.send_message(chat_dest, msg)


@app.route('(?!/).+')
def parrot(message):
    chat_dest = message['chat']['id']
    user_msg = message['text']
    msg = f"Parrot Says: {user_msg} \nId: {chat_dest}"
    app.send_message(chat_dest, msg)


if __name__ == '__main__':
    app.config['api_key'] = '5597021264:AAFe2sbR0Z_F42yVuoaDJxHCoGRvskIq3xw'
    app.poll(debug=True)












# while True:
# date = datetime.datetime.now()
# time.sleep(5)
# print(date.strftime("%X"))
# hour = int(date.strftime("%H"))
# if hour % 4 == 0 and hour in range(8,20):

# if True:
#     data = date.strftime("%x")
#     hora = date.strftime("%X")
#     print("Enviando")
#     bot.send_message(5510367423, data)
#     for i in lista_jogos:
#         busca_preco(i)
#         time.sleep(1)


# # 'chat': {'id': 5510367423,
# # url = "https://www.xbox.com/pt-BR/games/store/call-of-duty-modern-warfare-edicao-digital-padrao/9NVQBQ3F6W9W"
# # pagina = requests.get(url)
# # time.sleep(0.5)
# # payload = pagina.text
# # inicio = payload.find("R$")
# # fim = payload.find("<", inicio)
# # valor = payload[inicio:fim]
#
#
#
# # @bot.message_handler(commands=["MW"])
# # def busca1(mensagem):
# #     pass
#
# # @bot.message_handler(commands=["MW2"])
# # def busca1(mensagem):
# #     pass
#
# # def verificar(mensagem):
# #     return True
# # @bot.message_handler(func=verificar)
# # def responder(mensagem):
# #     print(mensagem)
# #     opcoes = '''
# #     Clique em um jogo!
# #     👉🏽 /MW
# #     👉🏽 /MW2
# #     '''
# #     bot.send_message(mensagem.chat.id,opcoes)
# # #
# # bot.polling()
# time.sleep(1)
