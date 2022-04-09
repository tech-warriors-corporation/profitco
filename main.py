from utils import months, calculate_media_price_of_months_by_key, calculate_total_of_months_by_key, print_space, print_bar, print_data, print_media_prices, print_prices

quantity_of_base_products_purchased = 0
current_quantity_of_base_products = 0
minimum_quantity = 1000
months_data = {}

print("Bem-vindo a solução real dos seus problemas, esse é o algoritmo Simple Solution do projeto ProfitCo da equipe Tech Warriors, responsável por ajudar sua empresa na parte financeira! A seguir pediremos algumas informações.")
print_bar()

for month in months:
    print(f"No mês de {month} sua empresa:")

    base_products_should_i_buy = minimum_quantity - current_quantity_of_base_products
    current_quantity_of_base_products += base_products_should_i_buy
    quantity_of_base_products_purchased += base_products_should_i_buy
    price_base_product = float(input("- Pagou quanto por cada produto base nesse mês? R: "))
    price_sold_product = float(input("- Vendeu por quanto cada produto customizado nesse mês? R: "))
    sold_amount = int(input("- Vendeu quantos produtos customizados nesse mês? R: "))
    total_spent = base_products_should_i_buy * price_base_product
    dirty_profit = price_sold_product * sold_amount
    total = dirty_profit - total_spent
    current_quantity_of_base_products -= sold_amount

    months_data[month] = {
        "price_base_product": price_base_product,
        "base_products_should_i_buy": base_products_should_i_buy,
        "total_spent": total_spent,
        "price_sold_product": price_sold_product,
        "sold_amount": sold_amount,
        "dirty_profit": dirty_profit,
        "total": total,
        "final_stock": current_quantity_of_base_products
    }

    print_space()
    print_data(f"no mês de {month}", base_products_should_i_buy, total_spent, sold_amount, dirty_profit, total, current_quantity_of_base_products)
    print_prices(price_base_product, price_sold_product)
    print_bar()

print_data(
    "no final do ano",
    quantity_of_base_products_purchased,
    calculate_total_of_months_by_key(months_data, "total_spent"),
    calculate_total_of_months_by_key(months_data, "sold_amount"),
    calculate_total_of_months_by_key(months_data, "dirty_profit"),
    calculate_total_of_months_by_key(months_data, "total"),
    current_quantity_of_base_products
)

print_media_prices(
    calculate_media_price_of_months_by_key(months_data, "price_base_product"),
    calculate_media_price_of_months_by_key(months_data, "price_sold_product")
)
