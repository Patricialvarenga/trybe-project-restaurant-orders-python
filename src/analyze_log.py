import csv
# https://docs.python.org/3/library/statistics.html
from statistics import mode


def maria_eats(path_to_file, customer_match="maria"):
    dish_most_ordered_per_maria = []
    with open(path_to_file, "r") as file:
        orders = csv.reader(file)

        for order in orders:
            if customer_match in order:
                dish_most_ordered_per_maria.append(order[1])
    return mode(dish_most_ordered_per_maria)


def arnaldo_ask_hamburguer(
    path_to_file, customer_match="arnaldo", dish_match="hamburguer"
        ):
    counter = 0
    with open(path_to_file, "r") as file:
        orders = csv.reader(file)

        for order in orders:
            if customer_match in order and dish_match in order:
                counter += 1
    return counter


def joao_never_ask(path_to_file, customer_match="joao"):
    all_dishes = set()
    joao_dishes = set()
    with open(path_to_file, "r") as file:
        orders = csv.reader(file)

        for order in orders:
            all_dishes.add(order[1])
            if customer_match in order:
                joao_dishes.add(order[1])
    return all_dishes.difference(joao_dishes)


def joao_never_went(path_to_file, customer_match="joao"):
    all_days = set()
    joao_days = set()
    with open(path_to_file, "r") as file:
        orders = csv.reader(file)

        for order in orders:
            all_days.add(order[2])
            if customer_match in order:
                joao_days.add(order[2])
    return all_days.difference(joao_days)


def analyze_log(path_to_file):
    if path_to_file.endswith(".csv"):
        try:
            rows = [
                f"{maria_eats(path_to_file)}\n",
                f"{arnaldo_ask_hamburguer(path_to_file)}\n",
                f"{joao_never_ask(path_to_file)}\n",
                f"{joao_never_went(path_to_file)}",
            ]

            with open("./data/mkt_campaign.txt", mode="w") as file:
                file.writelines(rows)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
    else:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
