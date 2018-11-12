from hpscrapper.spellbook import SpellBook

def main():
    spell_book = SpellBook()
    for spell in spell_book.spells:
        print('Name: ', spell['name'])
        if 'type' in spell:
            print('Type: ', spell['type'])
        if 'pronunciation' in spell:
            print('Pronunciation: ', spell['pronunciation'])
        if 'description' in spell:
            print('Description: ', spell['description'])
        if 'seen' in spell:
            print('Seen/Mentioned: ', spell['seen'])
        if 'etymology' in spell:
            print('Etymology: ', spell['etymology'])
        print('\n')

if __name__ == "__main__":
    main()
