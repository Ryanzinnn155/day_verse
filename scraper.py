from bs4 import BeautifulSoup
from selenium.webdriver import Chrome


class Scrapper:
    def __init__(self):
        # Log in to Selenium, opening a Tab in Google Chrome, with the website link 'Biblia Online'
        self.session = Chrome()
        self.session.get('https://www.bibliaon.com/versiculo_do_dia/')

    def get_html(self,):
        # Get the HTML of the Page
        html = self.session.page_source
        html = BeautifulSoup(html, 'html.parser')
        return html

    def get_verse_day(self):
        html = self.session.page_source
        html = BeautifulSoup(html, 'html.parser')
        title = html.select_one('h2.v_title').text
        date = html.select_one('h4.v_date').text
        verse = html.select_one('p.destaque').text.strip()
        print(f'''{title}
Data: {date}
Versículo: {verse}
        ''')

    def get_yesterday_verse(self):
        html = self.session.page_source
        html = BeautifulSoup(html, 'html.parser')
        title = html.select_one('h3.v_title').text
        verse = html.select_one('div.v_ontem > div.color-box > p.destaque')
        print(f'''{title}
{verse.text.strip()}''')


scrapper = Scrapper()
scrapper.get_verse_day()
escolha = input('Quer Ler o Versiculo de Ontem? ').upper()
if escolha == 'S':
    scrapper.get_yesterday_verse()

elif escolha == 'N':
    print('Blz, Tenha um Bom dia Ryan! TENHA FOCO no seu Objetivo!')



