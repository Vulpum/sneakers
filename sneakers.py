from pprint import pprint


def get_sneakers():
    sneakers = []
    with open('sneakers.csv', 'r', encoding='utf-8') as file:
        for line in list(file)[1:]:
            line = line.split(',')
            sneakers.append({
                'title': line[0],
                'color': line[1],
                'full_price': float(line[2]),
                'current_price': float(line[3]),
                'publish_date': line[4][:10]
            })
    return sneakers


def main():
    sneakers = get_sneakers()
    print('Válassz, melyik szempont alapján rendezzem a cipőket?\n1 - title\n2 - color\n3 - full price\n4 - current price\n5 - publish date')
    order_by = int(input('Add meg a lehetőség számát! '))
    options = ['title', 'color', 'full_price', 'current_price', 'publish_date']
    sneakers.sort(key=lambda sneaker: sneaker[options[order_by - 1]])
    print('')
    pprint(sneakers, indent=1)


main()
