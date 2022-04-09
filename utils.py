months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]

def print_space():
    print("")

def print_bar():
    print_space()
    print("------------------------------------------------------------------------------")
    print_space()

def format_money_value(value):
    return "R$ {:.2f}".format(value)
