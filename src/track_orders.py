# https://docs.python.org/3/library/statistics.html
from statistics import mode


class TrackOrders:
    # iniciamos
    def __init__(self):
        self.orders = []
    # aqui deve expor a quantidade de estoque

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        return self.orders.append({
            "customer": customer, "order": order, "day": day
        })

    def get_most_ordered_dish_per_customer(self, customer):
        all_ordered_dishes = {}
        counter = 0
        most_ordered_dish = ""
        for order in self.orders:
            if order["customer"] == customer:
                if not order["order"] in all_ordered_dishes:
                    all_ordered_dishes[order["order"]] = 1
                else:
                    all_ordered_dishes[order["order"]] += 1
                    if all_ordered_dishes[order["order"]] > counter:
                        counter = all_ordered_dishes[order["order"]]
                        most_ordered_dish = order["order"]
        return most_ordered_dish

    def get_never_ordered_per_customer(self, customer):
        all_dishes = set()
        customer_dishes = set()
        for order in self.orders:
            all_dishes.add(order["order"])
            if customer in order.values():
                customer_dishes.add(order["order"])
        return all_dishes.difference(customer_dishes)

    def get_days_never_visited_per_customer(self, customer):
        all_days = set()
        customer_days = set()
        for order in self.orders:
            all_days.add(order["day"])
            if customer in order.values():
                customer_days.add(order["day"])
        return all_days.difference(customer_days)

    def get_busiest_day(self):
        all_days = []
        for order in self.orders:
            all_days.append(order["day"])
        busiest_day = mode(all_days)
        return busiest_day

    def get_least_busy_day(self):
        frequent_days = {}

        for order in self.orders:
            if order['day'] not in frequent_days:
                frequent_days[order['day']] = 1
            else:
                frequent_days[order['day']] += 1
        for least_busy_day, count in frequent_days.items():
            if count <= 1:
                return least_busy_day
