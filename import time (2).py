import time
import random
from colorama import Fore, init

init()

player_name = ""
kitten_name = ""
found_items = []
time_left = 3

def print_slow(text, delay=0.03):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def show_status():
    print_slow(Fore.CYAN + f"\nВремя: {time_left}ч | Предметы: {len(found_items)}")

def first_scene():
    print_slow(Fore.YELLOW + "\n=== СЦЕНА 1: ТРЕВОЖНОЕ УТРО ===")
    
    print_slow(f"\n{player_name}, ты просыпаешься от солнца.")
    time.sleep(1)
    
    print_slow(Fore.RED + "\n!!! Резкий звонок телефона!")
    time.sleep(1)
    
    print_slow(Fore.CYAN + "Ты берешь трубку...")
    print_slow(Fore.RED + f"МАМА: 'Проснись! {kitten_name} пропал! Миша скоро вернется!'")
    
    time.sleep(1)
    print_slow(Fore.YELLOW + f"\nПаника! Ты вспоминаешь открытое окно...")
    print_slow(f"Всего {time_left} часа до возвращения брата!")
    
    choice = input(Fore.MAGENTA + """
1. Быстро обыскать дом
2. Позвонить за помощью
3. Проверить окно и балкон
4. Составить план поисков

Твой выбор: """)

    if choice == "1":
        search_house_fast()
    elif choice == "2":
        call_for_help()
    elif choice == "3":
        check_window_balcony()
    elif choice == "4":
        make_search_plan()
    else:
        print_slow(Fore.RED + "Нужно действовать!")
        first_scene()

def search_house_fast():
    print_slow(Fore.GREEN + "\nТы быстро осматриваешь комнаты...")
    time.sleep(1)
    
    finds = [
        f"Шерсть {kitten_name} на диване",
        "Перевернутая миска с едой", 
        "Следы лапок в коридоре",
        "Поцарапанный дверной косяк"
    ]
    
    for find in random.sample(finds, 2):
        print_slow(f"Нашел: {find}")
        time.sleep(0.5)
    
    found_items.append("Быстрый осмотр")
    show_status()
    continue_search()

def call_for_help():
    print_slow(Fore.CYAN + "\nТы звонишь друзьям...")
    time.sleep(1)
    
    friends = [
        ("Саша", "Проверь гараж и подвал!"),
        ("Маша", "Спроси соседей, они могли видеть!"),
        ("Петя", "Ищи у мусорных баков!"),
        ("Катя", "Разложи любимый корм как приманку!")
    ]
    
    for friend, advice in random.sample(friends, 2):
        print_slow(f"{friend}: {advice}")
        time.sleep(1)
    
    found_items.append("Советы друзей")
    show_status()
    continue_search()

def check_window_balcony():
    print_slow(Fore.BLUE + "\nТы идешь к окну...")
    time.sleep(1)
    
    clues = [
        "Следы лапок на подоконнике",
        "Порванная сетка на окне", 
        "Шерсть на раме",
        "Открытая балконная дверь"
    ]
    
    for clue in random.sample(clues, 2):
        print_slow(f"Обнаружено: {clue}")
        time.sleep(0.5)
    
    print_slow(Fore.YELLOW + "Ясно! Котенок сбежал через окно!")
    found_items.append("Улики у окна")
    show_status()
    continue_search()

def make_search_plan():
    print_slow(Fore.BLUE + "\nТы обдумываешь план...")
    time.sleep(1)
    
    plans = [
        f"Вспомнил: {kitten_name} любит высокие места",
        f"Знаю: {kitten_name} боится громких звуков",
        f"Помню: {kitten_name} обожает коробки",
        f"Заметил: {kitten_name} часто прячется в шкафу"
    ]
    
    for plan in random.sample(plans, 2):
        print_slow(plan)
        time.sleep(0.5)
    
    found_items.append("План поисков")
    show_status()
    continue_search()

def continue_search():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Куда направишь поиски теперь?")
    
    choice = input("""
1. Тщательно осмотреть балкон
2. Проверить вход и подъезд  
3. Выйти во двор
4. Опросить соседей
5. Обыскать гараж

Выбор: """)
    
    if choice == "1":
        search_balcony()
    elif choice == "2":
        search_entrance()
    elif choice == "3":
        search_yard()
    elif choice == "4":
        ask_neighbors()
    elif choice == "5":
        search_garage()
    else:
        print_slow(Fore.RED + "Время идет!")
        continue_search()

def search_balcony():
    print_slow(Fore.GREEN + "\nНа балконе ты находишь:")
    print_slow("Открытую дверь и свежие следы!")
    print_slow("Записку: 'Корми котенка вовремя!'")
    found_items.append("Балконные улики")
    end_scene()

def search_entrance():
    print_slow(Fore.GREEN + "\nУ входа обнаруживаешь:")
    print_slow("Царапины на двери")
    print_slow("Клочки шерсти на коврике")
    found_items.append("Улики у входа")
    end_scene()

def search_yard():
    print_slow(Fore.GREEN + "\nВо дворе ты видишь:")
    print_slow("Следы, ведущие к соседям")
    print_slow("Дети говорят, что видели котенка")
    found_items.append("Уличные улики")
    end_scene()

def ask_neighbors():
    print_slow(Fore.CYAN + "\nСоседи рассказывают:")
    print_slow("Баба Зина: 'Видела рыжего у мусорок!'")
    print_slow("Молодые соседи: 'Вчера он был на дереве!'")
    found_items.append("Рассказы соседей")
    end_scene()

def search_garage():
    print_slow(Fore.BLUE + "\nВ гараже находишь:")
    print_slow("Открытую форточку")
    print_slow("Следы на пыльном столе")
    found_items.append("Гаражные улики")
    end_scene()

def end_scene():
    print_slow(Fore.YELLOW + "\n" + "="*50)
    print_slow("=== ПЕРВАЯ СЦЕНА ЗАВЕРШЕНА ===")
    
    print_slow(Fore.CYAN + f"\nИтоги поисков:")
    print_slow(f"Собрано улик: {len(found_items)}")
    print_slow(f"Осталось времени: {time_left} часа")
    
    print_slow(Fore.MAGENTA + "\nНайденные предметы:")
    for item in found_items:
        print_slow(f"{item}")
    print_slow(Fore.YELLOW + f"\nУдачи, {player_name}! Ищи {kitten_name}!")

def start_game():
    global player_name, kitten_name
    
    print_slow(Fore.CYAN + "=== ПРОПАВШИЙ КОТЕНОК ===")
    player_name = input("Как тебя зовут?: ") or "Игрок"
    kitten_name = input("Имя котенка?: ") or "Пушистик"
    
    print_slow(f"\nПривет, {player_name}! Найди {kitten_name} за 3 часа!")
    time.sleep(1)
    first_scene()








def continue_search():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Куда направишь поиски теперь?")
    
    choice = input("""
1. Тщательно осмотреть балкон
2. Проверить вход и подъезд  
3. Выйти во двор
4. Опросить соседей

Выбор: """)
    
    if choice == "1":
        search_balcony()
    elif choice == "2":
        search_entrance()
    elif choice == "3":
        search_yard()
    elif choice == "4":
        ask_neighbors()
    else:
        print_slow(Fore.RED + "Время идет!")
        continue_search()

def search_balcony():
    print_slow(Fore.GREEN + "\n=== СЦЕНА 2: СЛЕДЫ НА БАЛКОНЕ ===")
    print_slow("\nТы тщательно осматриваешь балкон...")
    time.sleep(1)
    
    print_slow("Находишь рыжую шерсть на перилах!")
    print_slow("Следы ведут к соседскому балкону!")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\nЯсно! {kitten_name} перепрыгнул к соседям!")
    found_items.append("Шерсть на балконе")
    found_items.append("Следы к соседям")
    show_status()
    
    
    balcony_investigation()

def search_entrance():
    print_slow(Fore.GREEN + "\n=== СЦЕНА 2: ТАЙНЫ ПОДЪЕЗДА ===")
    print_slow("\nТы осматриваешь подъезд...")
    time.sleep(1)
    
    print_slow("На коврике у лифта - клочок шерсти!")
    print_slow("Соседка слышала мяуканье ночью!")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\n{player_name}, котенок где-то в подъезде!")
    found_items.append("Шерсть в подъезде")
    found_items.append("Свидетельство соседки")
    show_status()
    
    entrance_investigation()

def search_yard():
    print_slow(Fore.GREEN + "\n=== СЦЕНА 2: ПОИСКИ ВО ДВОРЕ ===")
    print_slow("\nТы выходишь во двор...")
    time.sleep(1)
    
    print_slow("Дети видели рыжего котенка у качелей!")
    print_slow("Следы ведут к детской площадке!")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\nОтлично! {kitten_name} где-то во дворе!")
    found_items.append("Рассказы детей")
    found_items.append("Следы к площадке")
    show_status()
    
    yard_investigation()

def ask_neighbors():
    print_slow(Fore.GREEN + "\n=== СЦЕНА 2: РАССКАЗЫ СОСЕДЕЙ ===")
    print_slow("\nТы опрашиваешь соседей...")
    time.sleep(1)
    
    print_slow("Баба Зина: 'Видела его у мусорок утром!'")
    print_slow("Молодые соседи: 'Он бежал в сторону парка!'")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\nВажная зацепка! {kitten_name} мог убежать в парк!")
    found_items.append("Свидетельство Бабы Зины")
    found_items.append("Направление к парку")
    show_status()
    
    neighbors_investigation()

def balcony_investigation():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Ты звонишь соседям...")
    time.sleep(1)
    
    print_slow("Соседка подтверждает:")
    print_slow("'Да, котенок был у нас! Но он убежал через открытую дверь!'")
    print_slow("'Мы видели, как он побежал в сторону парка!'")
    
    found_items.append("Подтверждение соседки")
    start_third_scene()

def entrance_investigation():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Ты спускаешься вниз по лестнице...")
    time.sleep(1)
    
    print_slow("На первом этаже встречаешь дворника:")
    print_slow("'Видел вашего котенка! Он выбежал на улицу и помчался в парк!'")
    
    found_items.append("Свидетельство дворника")
    start_third_scene()

def yard_investigation():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Ты следуешь за следами...")
    time.sleep(1)
    
    print_slow("Следы приводят тебя к калитке во двор.")
    print_slow("Охранник говорит: 'Котенок выбежал в парк через эту калитку!'")
    
    found_items.append("Подтверждение охранника")
    start_third_scene()

def neighbors_investigation():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Осталось: {time_left} часа")
    print_slow("Ты идешь по указанному направлению...")
    time.sleep(1)
    
    print_slow("По дороге встречаешь почтальона:")
    print_slow("'Видел рыжего котенка! Он бежал по аллее прямо в парк!'")
    
    found_items.append("Свидетельство почтальона")
    start_third_scene()

def start_third_scene():
    print_slow("=== СЦЕНА 3: ПОИСКИ В ПАРКЕ ===")
    
    print_slow(Fore.CYAN + f"\n{player_name}, ты в парке! Здесь много укрытий...")
    print_slow(f"Нужно найти {kitten_name} до наступления темноты!")
    
    print_slow(Fore.MAGENTA + f"\nОсталось времени: {time_left} часа")
    print_slow("С чего начнешь поиски в парке?")
    
    choice = input("""
1. Обыскать детскую площадку
2. Проверить район вокруг фонтана
3. Осмотреть кусты и газоны
4. Пройти по центральным аллеям

Выбор: """)
    
    if choice == "1":
        search_park_playground()
    elif choice == "2":
        search_park_fountain()
    elif choice == "3":
        search_park_bushes()
    elif choice == "4":
        search_park_alleys()
    else:
        print_slow(Fore.RED + "Нужно срочно начать поиски!")
        start_third_scene()

def search_park_playground():
    print_slow(Fore.GREEN + "\nТы на детской площадке...")
    time.sleep(2)
    
    print_slow("Осматриваешь горки, качели, песочницу...")
    print_slow("Дети показывают: 'Котенок прятался в домике!'")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\n{kitten_name} был здесь! Но сейчас его нет...")
    print_slow("Следы ведут дальше вглубь парка!")
    found_items.append("Следы на площадке")
    
    park_final_search()

def search_park_fountain():
    print_slow(Fore.GREEN + "\nТы у фонтана...")
    time.sleep(2)
    
    print_slow("Вода журчит, вокруг бегают голуби...")
    print_slow("Замечаешь мокрые следы на бортике!")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\n{kitten_name} пил воду здесь!")
    print_slow("Но сейчас его нигде не видно...")
    found_items.append("Следы у фонтана")
    
    park_final_search()

def search_park_bushes():
    print_slow(Fore.GREEN + "\nТы осматриваешь кусты...")
    time.sleep(2)
    
    print_slow("В густых зарослях находишь:")
    print_slow(" Примятую траву")
    print_slow("Рыжую шерсть на колючках")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\n{kitten_name} точно прятался здесь!")
    print_slow("Нужно искать дальше!")
    found_items.append("Улики в кустах")
    
    park_final_search()

def search_park_alleys():
    print_slow(Fore.GREEN + "\nТы идешь по центральным аллеям...")
    time.sleep(2)
    
    print_slow("Люди указывают направление:")
    print_slow("'Котенок бежал к старому дубу!'")
    time.sleep(1)
    
    print_slow(Fore.YELLOW + f"\n{kitten_name} активно перемещается по парку!")
    print_slow("Все ближе к развязке...")
    found_items.append("Направления от людей")
    
    park_final_search()

def park_final_search():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Остался 1 час до возвращения брата!")
    print_slow(Fore.CYAN + "\nТы нашел следы, но котенка еще нет...")
    print_slow("Вдруг слышишь тихое мяуканье из-за кустов сирени!")
    
    print_slow(Fore.YELLOW + "\nЧто будешь делать?")
    choice = input("""
1. Аккуратно подойти и посмотреть
2. Позвать котенка по имени
3. Использовать приманку (если есть)
4. Быстро пробежать через кусты

Выбор: """)
    
    
    if choice == "1":
        print_slow(Fore.BLUE + "\nТы аккуратно подходишь к кустам...")
    elif choice == "2":
        print_slow(Fore.BLUE + f"\nТы зовешь: '{kitten_name}! Иди сюда!'")
    elif choice == "3":
        print_slow(Fore.BLUE + "\nТы достаешь приманку...")
    elif choice == "4":
        print_slow(Fore.BLUE + "\nТы быстро пробираешься через кусты...")
    
    time.sleep(2)

def park_final_search():
    global time_left
    time_left -= 1
    
    print_slow(Fore.MAGENTA + f"\nПрошел 1 час. Остался 1 час до возвращения брата!")
    print_slow(Fore.CYAN + "\nТы нашел следы, но котенка еще нет...")
    print_slow("Вдруг слышишь тихое мяуканье из-за кустов сирени!")
    
    print_slow(Fore.YELLOW + "\nЧто будешь делать?")
    choice = input("""
1. Аккуратно подойти и посмотреть
2. Позвать котенка по имени
3. Использовать приманку (если есть)
4. Быстро пробежать через кусты

Выбор: """)
    
    if choice == "1":
        print_slow(Fore.BLUE + "\nТы аккуратно подходишь к кустам...")
        time.sleep(2)
        print_slow("За кустами видишь заброшенную беседку!")
        found_items.append("Обнаружена беседка")
    elif choice == "2":
        print_slow(Fore.BLUE + f"\nТы зовешь: '{kitten_name}! Иди сюда!'")
        time.sleep(2)
        print_slow("В ответ слышишь громкое мяуканье из глубины парка!")
        found_items.append("Ответный крик")
    elif choice == "3":
        print_slow(Fore.BLUE + "\nТы достаешь приманку...")
        time.sleep(2)
        print_slow("Через несколько минут слышишь шорох в траве!")
        found_items.append("Реакция на приманку")
    elif choice == "4":
        print_slow(Fore.BLUE + "\nТы быстро пробираешься через кусты...")
        time.sleep(2)
        print_slow("За кустами обнаруживаешь тропинку, ведущую к озеру!")
        found_items.append("Тропинка к озеру")
    
    time.sleep(2)
    third_scene_finale()

def third_scene_finale():
    
    
    print_slow(Fore.CYAN + f"\n{player_name}, ты нашел старую беседку в глубине парка!")
    print_slow("Внутри слышится явное движение и тихое мяуканье!")
    
    print_slow(Fore.MAGENTA + "\nОсталось всего 30 минут! Нужно действовать!")
    
    choice = input("""
1. Осторожно войти в беседку
2. Заглянуть через окно
3. Подождать у входа
4. Позвать котенка по имени

Выбор: """)
    
    if choice == "1":
        print_slow(Fore.GREEN + "\nТы медленно входишь в беседку...")
        time.sleep(2)
        print_slow("Внутри темно, пахнет сыростью и старым деревом.")
        print_slow("В углу замечаешь свернувшийся рыжий комочек!")
    elif choice == "2":
        print_slow(Fore.GREEN + "\nТы заглядываешь в окно...")
        time.sleep(2)
        print_slow("Видишь, как в луче света сидит испуганный котенок!")
        print_slow("Он смотрит на тебя большими глазами!")
    elif choice == "3":
        print_slow(Fore.GREEN + "\nТы решаешь подождать...")
        time.sleep(2)
        print_slow("Через пару минут котенок сам выходит из укрытия!")
        print_slow("Он с любопытством смотрит на тебя!")
    elif choice == "4":
        print_slow(Fore.GREEN + f"\nТы зовешь: '{kitten_name}, я здесь!'")
        time.sleep(2)
        print_slow("Котенок выбегает из беседки и останавливается перед тобой!")
    
    time.sleep(2)
    print_slow(Fore.YELLOW + f"\nЭто он! Это {kitten_name}!")
    print_slow("Он жив и невредим, хотя выглядит испуганным!")
    
    found_items.append("Котенок найден в беседке")
    start_fourth_scene()

def start_fourth_scene():
    print_slow("=== СЦЕНА 4: ВОЗВРАЩЕНИЕ ДОМОЙ ===")
    
    print_slow(Fore.CYAN + f"\n{player_name}, ты нашел {kitten_name}!")
    print_slow("Но нужно срочно возвращаться домой - брат скоро приедет!")
    
    print_slow(Fore.MAGENTA + "\nОсталось всего 15 минут! Выбери путь:")
    
    choice = input("""
1. Бежать кратчайшей дорогой через стройку
2. Идти спокойно по знакомым улицам
3. Попробовать поймать такси
4. Позвонить другу за помощью

Выбор: """)
    
    if choice == "1":
        fourth_scene_construction()
    elif choice == "2":
        fourth_scene_familiar_way()
    elif choice == "3":
        fourth_scene_taxi()
    elif choice == "4":
        fourth_scene_friend_help()
    else:
        print_slow(Fore.RED + "Нужно срочно выбирать путь!")
        start_fourth_scene()

def fourth_scene_construction():
    print_slow(Fore.GREEN + "\nТы бежишь через стройку...")
    time.sleep(2)
    
    print_slow("Путь короче, но опаснее!")
    print_slow("Нужно преодолеть несколько препятствий:")
    
    obstacles = [
        "Перелезть через забор",
        "Обойти яму с водой", 
        "Пробежать мимо стройтехники",
        "Перейти по временному мостику"
    ]
    
    for obstacle in obstacles:
        print_slow(f"~ {obstacle}")
        time.sleep(1)
    
    print_slow(Fore.YELLOW + "\nТы успешно преодолеваешь все препятствия!")
    print_slow("Вы почти у дома!")
    
    final_race_home()

def fourth_scene_familiar_way():
    print_slow(Fore.GREEN + "\nТы идешь по знакомым улицам...")
    time.sleep(2)
    
    print_slow("Путь безопасный, но длиннее.")
    print_slow("По дороге встречаешь знакомых:")
    
    encounters = [
        "Соседка с собачкой желает удачи",
        "Друг предлагает подвезти на велосипеде",
        "Продавец из магазина дает угощение для котенка",
        "Дети помогают перейти дорогу"
    ]
    
    for encounter in random.sample(encounters, 2):
        print_slow(f"~ {encounter}")
        time.sleep(1)
    
    print_slow(Fore.YELLOW + "\nВсе помогают вам добраться быстрее!")
    print_slow("Дом уже виден!")
    
    final_race_home()

def fourth_scene_taxi():
    print_slow(Fore.GREEN + "\nТы пытаешься поймать такси...")
    time.sleep(2)
    
    print_slow("Машины проезжают, но не останавливаются!")
    print_slow("Вдруг замечаешь знакомого водителя!")
    
    print_slow(Fore.CYAN + "\nВОДИТЕЛЬ: 'Садись, подвезу! Вижу, котенка нашел!'")
    print_slow("Вы быстро едете по почти пустым улицам.")
    
    print_slow(Fore.YELLOW + "\nТаксист знает короткую дорогу!")
    print_slow("Вы подъезжаете к дому!")
    
    final_race_home()

def fourth_scene_friend_help():
    print_slow(Fore.GREEN + "\nТы звонишь другу...")
    time.sleep(2)
    
    print_slow("Друг сразу выезжает на машине!")
    print_slow("Через 5 минут он уже забирает вас у парка.")
    
    print_slow(Fore.CYAN + "\nПока едете, котенок успокаивается у тебя на руках.")
    print_slow("Друг рассказывает, что тоже волновался.")
    
    print_slow(Fore.YELLOW + "\nМашина останавливается у твоего дома!")
    print_slow("Вы успеваете вовремя!")
    
    final_race_home()

def final_race_home():
    print_slow("=== ФИНАЛЬНАЯ ГОНКА ===")
    
    print_slow(Fore.CYAN + f"\n{player_name}, ты у своего дома!")
    print_slow("Но видишь, что к подъезду подъезжает машина брата!")
    
    print_slow(Fore.MAGENTA + "\nОстались считанные секунды!")
    print_slow("Что будешь делать?")
    
    choice = input("""
1. Бежать к подъезду наперерез
2. Спрятаться за углом и подождать
3. Сделать вид, что вышел погулять
4. Позвонить брату и попросить зайти в магазин

Выбор: """)
    
    if choice == "1":
        print_slow(Fore.BLUE + "\nТы бежишь к подъезду...")
        time.sleep(2)
        print_slow("Брат только что вышел из машины!")
        print_slow("Ты успеваешь зайти в подъезд первым!")
    elif choice == "2":
        print_slow(Fore.BLUE + "\nТы прячешься за углом...")
        time.sleep(2)
        print_slow("Ждешь, когда брат зайдет в подъезд.")
        print_slow("Затем быстро заскакиваешь в дом!")
    elif choice == "3":
        print_slow(Fore.BLUE + "\nТы делаешь вид, что гулял...")
        time.sleep(2)
        print_slow("'Привет! Я просто вывел котенка подышать!'")
        print_slow("Брат улыбается и ничего не замечает!")
    elif choice == "4":
        print_slow(Fore.BLUE + "\nТы звонишь брату...")
        time.sleep(2)
        print_slow("'Привет! Зайди, пожалуйста, в магазин!'")
        print_slow("Пока он в магазине, ты успеваешь зайти домой!")
    
    time.sleep(2)
    game_finale()

def game_finale():
    print_slow(" МИССИЯ ВЫПОЛНЕНА! ")
    
    time.sleep(2)
    print_slow(f"\n{player_name}, ты совершил настоящий подвиг!")
    print_slow(f"Ты нашел {kitten_name} и успел вернуться домой вовремя!")
    
    print_slow(Fore.CYAN + "\nБрат заходит в квартиру...")
    time.sleep(1)
    print_slow(f"БРАТ: 'Привет! Как поживает наш {kitten_name}?'")
    print_slow(f"{kitten_name} мурлычет у тебя на руках!")
    
    print_slow(Fore.YELLOW + "\nБрат даже не подозревает, что случилось!")
    print_slow("Ты спас ситуацию и сохранил секрет!")
   
    print_slow(Fore.MAGENTA + "\n" + "="*50)
    print_slow("=== ИТОГИ ВАШЕГО ПРИКЛЮЧЕНИЯ ===")
    print_slow("="*50)
    
    print_slow(f"\nИгрок: {player_name}")
    print_slow(f"Спасенный котенок: {kitten_name}")
    print_slow(f"Всего найдено улик: {len(found_items)}")
    print_slow(f"Оставшееся время: 0 часов (успел вовремя!)")
    
    print_slow(Fore.CYAN + "\nВесь ваш путь:")
    for i, item in enumerate(found_items, 1):
        print_slow(f"{i:2d}. {item}")
   
    score = len(found_items) * 10
    if score > 80:
        rating = "ВЕЛИКОЛЕПНО"
        comment = "Ты настоящий сыщик!"
    elif score > 60:
        rating = "ОТЛИЧНО"
        comment = "Отличная работа!"
    elif score > 40:
        rating = "ХОРОШО"
        comment = "Ты справился хорошо!"
    else:
        rating = "УДОВЛЕТВОРИТЕЛЬНО"
        comment = "Главное - котенок спасен!"
    
    print_slow(Fore.YELLOW + f"\nВаш результат: {score} очков")
    print_slow(Fore.GREEN + f"Оценка: {rating}")
    print_slow(Fore.CYAN + f"{comment}")
    
    time.sleep(2)
    print_slow(Fore.MAGENTA + "\n" + "="*50)
    print_slow(" ИСТОРИЯ ЗАКОНЧЕНА ")
    print_slow("="*50)
   
    print_slow(Fore.GREEN + f"\nСпасибо, {player_name}, за спасение {kitten_name}!")
    print_slow("Теперь котенок в безопасности, а твой секрет сохранен!")
   
    choice = input(Fore.MAGENTA + "Хочешь сыграть еще раз? (1-да, 2-нет): ")
    
    if choice == "1":
        reset_game()
    else:
        print_slow(Fore.CYAN + "\nСпасибо за игру! До новых приключений!")
        print_slow("Надеемся, тебе понравилось это приключение!")
        exit()

def reset_game():
    global player_name, kitten_name, found_items, time_left
    
    found_items = []
    time_left = 3
    
    print_slow(Fore.CYAN + "\n\n" + "="*50)
    print_slow("=== НАЧИНАЕМ НОВУЮ ИГРУ ===")
    start_game()

if __name__ == "__main__":
    start_game()