months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def show_space():
    print("")

def show_bar():
    show_space()
    print("------------------------------------------------------------------------------")
    show_space()

def format_value(value):
    return "R$ {:.2f}".format(value)
