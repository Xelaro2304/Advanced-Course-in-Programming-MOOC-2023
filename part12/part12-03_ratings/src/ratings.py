# TEE RATKAISUSI TÄHÄN:
def sort_by_ratings(items: list):
    def order_by_seasons(item):
        return item["rating"]

    return sorted(items, key=order_by_seasons, reverse = True)