config = {
    # General settings | Общие настройки
    "threads": 10,                              # threads amount | количество потоков | (1+)
    "delay_before_first": True,                 # delay before first account in thread | пауза перед первым аккаунтом в потоке | (True / False)
    "headless": False,                          # run browser window in headless mode | запускать браузер в скрытом режиме | (True / False)
    "profiles_to_farm": 10,                     # how much profiles to warmup | сколько профилей прогреть | (1+)
    "farm_running_profiles": True,              # farm already opened profiles | работать с уже открытыми профилями | (True / False)
    "close_running_profiles": False,            # close profiles that were already opened | закрывать ли те профиля, которые уже были открыты | (True / False)
    "close_all_other_tabs": False,              # close all other tabs | закрывать ли лишние вкладки | (True / False)
    "show_debug_logs": False,                   # show debug log, for developers | показывать дебаг лог, для разработчиков | (True / False)
    "highlight_elements": False,                # higlight some elements for debug purposes | подсвечивать некоторые элементы для дебаггинга | (True / False)
    "element_wait_sec": 60,                     # how long bot should wait for an element before throwing an error, seconds | как долго ждать подгрузки элемента перед фейлом, секунд | (1+)
    "adspower_debug_port": 50325,               # можно найти в Adspower -> Automation -> API -> Connection

    # Module switches | Свичи модулей
    "module_switches": {
        "cast_on_homepage": True,
        "surf_feed": True,
        "subscribe_to_users_via_explore": True,
        "subscribe_to_channels_via_explore": True,
        "subscribe_to_authors_via_search": True,
        "subscribe_to_channels_via_search": True,
        "subscribe_to_users_via_search": True,
        "subscribe_to_mandatory_users": True,
        "subscribe_to_mandatory_channels": True,
        "connect_metamask": True
    },

    # Module settings | Настройки модулей
    "cast_on_homepage": {
        "use_module_probability": 0.5,          # casting (home) probability | вероятность поста каста (home) | (0 - 1)
        "keep_order": True,                     # keep casts order from txt file | сохранять порядок кастов для аккаунта как в текстовике | (True / False)
        "emojis": {
            "use_probability":  0.5,            # pick emoji from context menu probability | вероятность добавления эмодзи из контекстного меню | (0 - 1)
            "max_dev_from_result": 1,           # maximum deviation from the first emoji after search | максимальное отклонение от первого эмодзи в поиске | (0+)
            "max_repeat": 2                     # maximum amount of clicks on emoji (spam emoji) | максимальное количество кликов по одному эмодзи | (1+)
        },
        "images": {
            "use_from_random_probability": 0.5  # random media usage probability (from "all" folder) | вероятность добавления случайного медиа файла (из папки "all") | (0 - 1)
        }
    },
    "surf_feed": {
        "use_module_probability": 0.5,          # feed surfing probability | вероятность серфинга по ленте | (0 - 1)
        "min_scroll_episodes": 2,               # minimum amount of feed scroll episodes | минимальное количество эпизодов прокрутки ленты | (1+)
        "max_scroll_episodes": 5,               # maximum amount of feed scroll episodes | максимальное количество эпизодов прокрутки ленты | (1+)
        "recast_probability": 0.4,              # random repost probability for specific scroll episode | вероятность репоста в рамках эпизода прокрутки | (0 - 1)
        "like_probability": 0.7                 # random like probability for specific scroll episode | вероятность лайка в рамках эпизода прокрутки | (0 - 1)
    },
    "subscribe_via_explore": {
        "to_users_probability": 0.3,            # follow users via explore probability | вероятность подписки на пользователей из рекомендаций | (0 - 1)
        "to_channels_probability": 0.3,         # follow channels via explore probability | вероятность подписки на каналы из рекомендаций | (0 - 1)
        "min_scroll_episodes": 1,               # minimum amount of list scroll episodes | минимальное количество эпизодов прокрутки списка | (1+)
        "max_scroll_episodes": 4,               # maximum amount of list scroll episodes | максимальное количество эпизодов прокрутки списка | (1+)
        "min_subscribes_per_episode": 0,        # minimum amount of follows for specific scroll episode | минимальное количество подписок в рамках эпизода прокрутки (0+)
        "max_subscribes_per_episode": 2,        # maximum amount of follows for specific scroll episode | максимальное количество подписок в рамках эпизода прокрутки (0+)
    },
    "subscribe_to_authors_via_search": {
        "use_module_probability": 0.1,          # follow cast authors via search probability | вероятность подписки на авторов постов через поиск по запросу | (0 - 1)
        "remove_text_from_base": False,         # remove used search text from txt file | удалить из базы текст, использованный для поиска | (True / False)
        "use_scrolling_probability": 0.5,       # scroll feed probability (scroll mode / no scroll mode) | вероятность того, что скрипт будет скроллить ленту | (0 - 1)
        "keep_order_probability": 0.5,          # keep order during subscribing in no scroll mode (top -> bottom) | вероятность соблюдения порядка при подписках без скролла | (0 - 1)
        "min_subscribes": 1,                    # minimum amount of subscriptions in no scroll mode | минимальное количество подписок без скролла | (0+)
        "max_subscribes": 2,                    # maximum amount of subscriptions in no scroll mode | максимальное количество подписок без скролла | (0+)
        "min_scroll_episodes": 1,               # minimum amount of feed scroll episodes | минимальное количество эпизодов прокрутки | (1+)
        "max_scroll_episodes": 2,               # maximum amount of feed scroll episodes | максимальное количество эпизодов прокрутки | (1+)
        "min_subscribes_per_episode": 0,        # minimum amount of follows for specific scroll episode | минимальное количество подписок в рамках эпизода прокрутки (0+)
        "max_subscribes_per_episode": 3         # maximum amount of follows for specific scroll episode | максимальное количество подписок в рамках эпизода прокрутки (0+)
    },
    "subscribe_to_channels_via_search": {
        "use_module_probability": 0.1,          # follow channels via search probability | вероятность подписки на каналы через поиск по запросу | (0 - 1)
        "remove_text_from_base": False,         # remove used search text from txt file | удалить из базы текст, использованный для поиска | (True / False)
        "use_scrolling_probability": 0.5,       # scroll feed probability (scroll mode / no scroll mode) | вероятность того, что скрипт будет скроллить ленту | (0 - 1)
        "keep_order_probability": 0.5,          # keep order during subscribing in no scroll mode (top -> bottom) | вероятность соблюдения порядка при подписках без скролла | (0 - 1)
        "min_subscribes": 1,                    # minimum amount of subscriptions in no scroll mode | минимальное количество подписок без скролла | (0+)
        "max_subscribes": 2,                    # maximum amount of subscriptions in no scroll mode | максимальное количество подписок без скролла | (0+)
        "min_scroll_episodes": 1,               # minimum amount of feed scroll episodes | минимальное количество эпизодов прокрутки | (1+)
        "max_scroll_episodes": 2,               # maximum amount of feed scroll episodes | максимальное количество эпизодов прокрутки | (1+)
        "min_subscribes_per_episode": 0,        # minimum amount of follows for specific scroll episode | минимальное количество подписок в рамках эпизода прокрутки | (0+)
        "max_subscribes_per_episode": 3         # maximum amount of follows for specific scroll episode | максимальное количество подписок в рамках эпизода прокрутки | (0+)
    },
    "subscribe_to_users_via_search": {
        "use_module_probability": 1.0,          # follow users via search probability | вероятность подписки на пользователей через поиск по запросу | (0 - 1)
        "remove_text_from_base": False,         # remove used search text from txt file | удалить из базы текст, использованный для поиска | (True / False)
        "use_scrolling_probability": 0.5,       # scroll feed probability (scroll mode / no scroll mode) | вероятность того, что скрипт будет скроллить ленту | (0 - 1)
        "keep_order_probability": 0.5,          # keep order during subscribing in no scroll mode (top -> bottom) | вероятность соблюдения порядка при подписках без скролла | (0 - 1)
        "min_subscribes": 1,                    # minimum amount of subscriptions in no scroll mode | минимальное количество подписок без скролла | (0+)
        "max_subscribes": 2,                    # maximum amount of subscriptions in no scroll mode | максимальное количество подписок без скролла | (0+)
        "min_scroll_episodes": 1,               # minimum amount of feed scroll episodes | минимальное количество эпизодов прокрутки | (1+)
        "max_scroll_episodes": 2,               # maximum amount of feed scroll episodes | максимальное количество эпизодов прокрутки | (1+)
        "min_subscribes_per_episode": 0,        # minimum amount of follows for specific scroll episode | минимальное количество подписок в рамках эпизода прокрутки | (0+)
        "max_subscribes_per_episode": 3         # maximum amount of follows for specific scroll episode | максимальное количество подписок в рамках эпизода прокрутки | (0+)
    },
    "subscribe_to_mandatory_users": {
        "use_module_probability": 1.0,          # follow mandatory users from list probability | вероятность подписки на юзеров из предоставленного списка | (0 - 1)
        "use_direct_link_probability": 0.0,     # visit user page via direct link probability | вероятность перехода на страницу юзера по ссылке (а не через поиск) | (0 - 1)
        "surf_user_feed_probability": 1.0,      # surf user home page before subscribing (not yet implemented) | вероятность серфинга стены юзера перед подпиской на него (еще не реализованно) | (0 - 1)
        "min_subscribes_per_run": 1,            # minimum amount of follows for a single run | минимальное количество подписок в рамках выполнения модуля | (1+)
        "max_subscribes_per_run": 3             # maximum amount of follows for a single run | максимальное количество подписок в рамках выполнения модуля | (1+)
    },
    "subscribe_to_mandatory_channels": {
        "use_module_probability": 1.0,          # follow mandatory channels from list probability | вероятность подписки на каналы из предоставленного списка | (0 - 1)
        "min_subscribes_per_run": 1,            # minimum amount of follows for a single run | минимальное количество подписок в рамках выполнения модуля | (1+)
        "max_subscribes_per_run": 3             # maximum amount of follows for a single run | максимальное количество подписок в рамках выполнения модуля | (1+)
    },
    "connect_metamask": {
        "use_module_probability": 0.5           # connect metamask probability | вероятность подключения метамаска | (0 - 1)
    },

    # Delays | Задержки
    "delays": {
        "min_activity_sec": 5,                  # minimum delay between modules, seconds | минимальная задержка между модулями, секунды | (0+)
        "max_activity_sec": 15,                 # maximum delay between modules, seconds | максимальная задержка между модулями, секунды | (0+)
        "min_subactivity_sec": 1,               # minimum delay between activities within the module, seconds | минимальная задержка между действиями внутри модуля, секунды | (0+)
        "max_subactivity_sec": 4,               # minimum delay between activities within the module, seconds | максимальная задержка между действиями внутри модуля, секунды | (0+)
        "min_typing_sec": 0.02,                 # minimum delay between chars input (typing delay), seconds | минимальная пауза между вводами символов при печати, секунды | (0+)
        "max_typing_sec": 0.2,                  # maximum delay between chars input (typing delay), seconds | максимальная пауза между вводами символов при печати, секунды | (0+)
        "min_idle_minutes": 3,                  # minimum delay between accounts, minutes | минимальная задержка между аккаунтами, минуты | (0+)
        "max_idle_minutes": 5,                  # maximum delay between accounts, minutes | максимальная задержка между аккаунтами, минуты | (0+)
    },

    # Mouse scroll settings | Настройки скролла
    "pixels_per_scroll_tick": 100,              # how mush pixels are scrolled by one mouse tick, pixels | сколько пикселей прокручивает один тик колеса мыши, пиксели | (1+)
    "min_ticks_per_scroll": 6,                  # minimum amount of ticks per scroll episode | минимальное количество тиков за эпизод прокрутки | (1+)
    "max_ticks_per_scroll": 12,                 # maximum amount of ticks per scroll episode | максимальное количество тиков за эпизод прокрутки | (1+)
    "min_delay_between_scroll_ticks_sec": 0.05, # minimum delay between ticks withing scroll episode, seconds | минимальная задержка между тиками в рамках эпизода прокрутки, секунды | (0+)
    "max_delay_between_scroll_ticks_sec": 0.5,  # maximum delay between ticks withing scroll episode, seconds | максимальная задержка между тиками в рамках эпизода прокрутки, секунды | (0+)

    # Mouse click deviations | Отклонения при кликах
    "max_click_height_deviation": 0.1,          # maximum vertical deviation from the center of the object when clicked | максимальное вертикальное отклонение от центра объекта при нажатии | (0 - 1)
    "max_click_width_deviation": 0.1,           # maximum horizontal deviation from the center of the object when clicked | максимальное горизонтальное отклонение от центра кнопки при нажатии | (0 - 1)

    # Popup dodge settings (profile info popups) | Настройки доджа попапов (всплывающая информация профиля)
    "popup_dodge": {
        "min_tries": 6,                         # minimum amount of popup dodge tries | минимальное количество попыток увернуться от попапа | (0+)
        "max_tries": 10,                        # maximum amount of popup dodge tries | максимальное количество попыток увернуться от попапа | (0+)
        "min_height_deviation_px": 10,          # minimum mouse vertical shift, pixels | минимальный сдвиг мыши по вертикали, пиксели | (0+)
        "max_height_deviation_px": 200,         # maximum mouse vertical shift, pixels | максимальный сдвиг мыши по вертикали, пиксели  | (0+)
        "min_width_deviation_px": 10,           # minimum mouse horizontal shift, pixels | минимальный сдвиг мыши по горизонтали, пиксели | (0+)
        "max_width_deviation_px": 200,          # maximum mouse horizontal shift, pixels | максимальный сдвиг мыши по горизонтали, пиксели | (0+)
    }
}
