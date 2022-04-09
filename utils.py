months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def print_space():
    print("")

def print_bar():
    print_space()
    print("------------------------------------------------------------------------------")
    print_space()

def format_money_value(value):
    return "R$ {:.2f}".format(value)
