import loader_from_file


def get_url(words):
    company = words[1]
    stock = loader_from_file.load_one_stock(company)
    return loader_from_file.url_board(stock.trade_code)