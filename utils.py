months = ("janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro")

def format_money_value(value):
    return "R$ {:.2f}".format(value)

def calculate_total_of_months_by_key(months_data, key):
    total = 0

    for month in months:
        total += months_data[month][key]

    return total

def calculate_media_price_of_months_by_key(months_data, key):
    total = calculate_total_of_months_by_key(months_data, key)
    media = total / len(months)

    return media

def print_space():
    print("")

def print_bar():
    print_space()
    print("==================================================================================================================")
    print_space()

def print_data(title, base_products_purchased_amount, total_spent, sold_amount, dirty_profit, total, final_quantity_of_base_products):
    print(f"Seus dados {title} são:")
    print(f"* Foram comprados {base_products_purchased_amount} produtos base;")
    print(f"* Foi gasto um total de {format_money_value(total_spent)} na compra de produtos base;")
    print(f"* Vendeu {sold_amount} produtos customizados;")
    print(f"* Teve um lucro sujo de {format_money_value(dirty_profit)};")
    print(f"* Teve um {('prejuízo', 'lucro')[total >= 0]} total de {format_money_value(total)} (essa conta é o lucro sujo subtraído pelo gasto total, pode ser positivo ou negativo, ou seja, lucro ou prejuízo);")
    print(f"* Terminou com um estoque de {final_quantity_of_base_products} produtos base;")

def print_prices(price_base_product, price_sold_product):
    print(f"* Pagou {format_money_value(price_base_product)} por cada produto base comprado;")
    print(f"* Ganhou {format_money_value(price_sold_product)} por cada produto customizado vendido;")

def print_media_prices(average_price_base_product, average_price_sale_product):
    print(f"* O preço médio dos produtos base comprados foi de {format_money_value(average_price_base_product)} cada um;")
    print(f"* O preço médio dos produtos customizados vendidos foi de {format_money_value(average_price_sale_product)} cada um;")
