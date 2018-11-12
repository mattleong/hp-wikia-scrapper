from bs4 import BeautifulSoup
from hpscrapper.util.pagescrapper import PageScrapper

class SpellBook(PageScrapper):
    def __init__(self):
        self.url = 'http://harrypotter.wikia.com/wiki/List_of_spells'
        self.spells = self.get_spells()

    # Parses attr element
    def processAttrs(self, el):
        attrs_el = el.find_next_sibling('dl')
        attr_els = attrs_el.find_all('dd')
        attr_data = {
            'name': el.text
        }

        for attr_el in attr_els:
            attr_str = attr_el.text.replace('\n', '')
            if 'Type: ' in attr_str:
                attr_data['type'] = attr_str[len('Type: '):len(attr_str)]
            elif 'Pronunciation: ' in attr_str:
                attr_data['pronunciation'] = attr_str[len('Pronunciation: '):len(attr_str)]
            elif 'Description: ' in attr_str:
                attr_data['description'] = attr_str[len('Description: '):len(attr_str)]
            elif 'Seen/Mentioned: ' in attr_str:
                attr_data['seen'] = attr_str[len('Seen/Mentioned: '):len(attr_str)]
            elif 'Etymology: ' in attr_str:
                attr_data['etymology'] = attr_str[len('Etymology: '):len(attr_str)]

        return attr_data

    def get_spells(self):
        html_doc = self.get_url_data(self.url)
        soup = BeautifulSoup(html_doc, 'html.parser')
        content_tab = soup.find('div', attrs={"id": "mw-content-text"})
        spell_tabs = content_tab.find_all('div', class_='tabbertab')

        # create spell book
        spell_book = []
        for spell_tab in spell_tabs:
            # spell name
            h3s = spell_tab.find_all('h3')
            for h3 in h3s:
                spell = {}
                # spell attrs are siblings
                spell_attrs = self.processAttrs(h3)
                for key, attr in spell_attrs.items():
                    spell[key] = attr

                # add spell to spell book
                spell_book.append(spell)

        self.spells = spell_book
        return self.spells
