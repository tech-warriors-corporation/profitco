months = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

def print_space():
    print("")

def print_bar():
    print_space()
    print("------------------------------------------------------------------------------")
    print_space()

def format_money_value(value):
    return "R$ {:.2f}".format(value)

def calculate_total_of_months(data, key):
    total = 0

    for month in months:
        total += data[month][key]

    return total

def calculate_price_media_of_months(data, key):
    total = calculate_total_of_months(data, key)
    media = total / len(months)

    return media

def is_it_profit_or_loss(value):
    return ('prejuízo', 'lucro')[value >= 0]
