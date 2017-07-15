CMD_PRICE = ["price", "цена"]
RSP_PRICE = "%s (%s) - %.2f"
HELP_PRICE = format("*%s* (*%s*) _<имя_компании>_ - поиск цены акции на MOEX\n" % (CMD_PRICE[0], CMD_PRICE[1]))

CMD_CAPITAL = ["capital", "капитал"]
RSP_CAPITAL = "%s : CAP %.2f : VOLUME %.2f : CAP/VOLUME %.2f"
HELP_CAPITAL = format(
    "*%s* (*%s*) _<имя_компании>_ - поиск капитализации, объема выпущенных акций"
    "и отношение капитализации к объему акций [_руб/акция_]\n" % (CMD_CAPITAL[0], CMD_CAPITAL[1]))

RSP_WAIT = "Подождите... Я уже ищу"

CMD_UPDATE = "update"
RSP_UPDATE_STOCK = "Загружены последнии версии файлов"
HELP_UPDATE = format("*%s* - обновить файлы с метаданными\n" % CMD_UPDATE)

RSP_NOF_FOUND_STOCK = "Не найдена акция %s"

CMD_MOEX = ["moex", "биржа"]
HELP_MOEX = format("*%s* (*%s*) - получить ссылку акции на бирже\n" % (CMD_MOEX[0], CMD_MOEX[1]))

CMD_HELP = ["help", "помогите", "помощь"]

RSP_HELP = "Вот чему меня научили:\n" + HELP_PRICE + HELP_CAPITAL + HELP_MOEX + HELP_UPDATE

WELCOME = format("Привет, чтобы узнать что я умею напиши одно из @portfolio *%s*, *%s*, *%s*" %
                 (CMD_HELP[0], CMD_HELP[1], CMD_HELP[2]))
