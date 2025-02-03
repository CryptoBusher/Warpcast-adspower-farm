# 🚀 Warpcast adspower farm

## 🌎 English
Why the fuck am I sharing this? This script will save you a ton of time. It works with Warpcast profiles that are imported into [AdsPower](https://share.adspower.net/Btc9YYgpiyJxhmW). I've struggled with randomization, so you can sleep soundly.

<i>Contact developer: https://t.me/CryptoBusher</i> <br>
<i>For Twitter guys: https://twitter.com/CryptoBusher</i> <br>

<i>Join my Telegram channel and get more bots / smart ideas: https://t.me/CryptoKiddiesClub</i> <br>
<i>Join our Telegram chat and communicate with Russian sybils: https://t.me/CryptoKiddiesChat</i> <br>

## 🔥 Latest updates
- [x] 28.05.2024 - Follow users from list via direct link or search
- [x] 28.05.2024 - Follow channels from list via direct link
- [x] 28.05.2024 - [How to set up the script? Video guide](https://t.me/CryptoKiddiesClub/513)
- [x] 29.05.2024 - Module switches in config for convenience
- [x] 29.05.2024 - Fixed minor bugs, added debug log to "data/debug_log.log"
- [x] 01.06.2024 - Fixed minor bugs
- [x] 01.06.2024 - Connect Metamask (see additional information)
- [x] 04.06.2024 - Fixed minor bugs (search input clearing)
- [x] 07.06.2024 - Multi-line casts, casts with emojis
- [x] 13.06.2024 - Images in casts (explicit or random)
- [x] 16.06.2024 - Multithreading
- [x] 01.07.2024 - Fixed minor bugs, fixed "Error retrieving data. Please try again."
- [x] 01.07.2024 - Added "adspower_debug_port" to config
- [x] 12.07.2024 - Fixed errors during selecting emoji from menu, shifted error stack traces to debug log
- [x] 03.08.2024 - Readme and config have been translated into English
- [x] 03.02.2025 - Updated selectors, tested all methods, added "highlight_elements" to config, removed bookmark feature in "surf feed" module

## ⌛️ Next in line
- Casts in channels according to a given scenario
- Activities in top projects

## ⚙️ Functionality
1. Casts (home)
2. Follow random users from "explore" (scroll + subscribe)
3. Follow random channels from "explore" (scroll + subscribe)
4. Surfing the feed including:
   1. Scroll feed
   2. Random likes
   3. Random recasts
   4. Random bookmarks
5. Use search to:
   1. Randomly follow authors of casts based on search results
   2. Randomly follow channels based on search results
   3. Randomly follow users based on search results
6. Follow users from list via direct link or search
7. Follow channels from list via direct link
8. Connect Metamask

## 🤔 Advantages
1. Maximum possible randomization:
   1. Module execution sequence
   2. Activities within the module (number of interactions, execution speed)
   3. Randomization is based on probabilities
   4. Button click coordinates
   5. Typing delays
   6. Feed scrolling
2. Farming via [AdsPower](https://share.adspower.net/Btc9YYgpiyJxhmW)
3. Headless mode
4. Ability to farm already opened AdsPower profiles
5. Selecting emojis from built-in menu
6. Media in casts (images / GIFs etc.)
7. Multithreading

## 📚 First start
1. Install [Python 3.12](https://www.python.org/downloads/).
2. Download the repository, navigate to the project folder using terminal and enter the command "pip install -r requirements.txt" to install all dependencies.
3. Rename folder "_data" to "data".
4. Open the file "data/profile_ids.py" and fill in your profiles as in the example ("name":"AdsPower ID"). The name should match the names in the file "data/farm_data/casts.txt". The best way to name profiles in numerical order.
5. Open the file "data/config.py" and fill in the settings. You can get support in our [chat](https://t.me/CryptoKiddiesChat).
6. Open the file "data/farm_data/casts.txt" and enter texts for casts, each on a new line using the format "acc_name|cast_text". For each account, you need to provide your own text for the cast, you can enter many texts for one account, the script will select next / random text for the account, depending on the settings. The cast text can contain emojis and line breaks ('\n).
7. Open the file "data/farm_data/emoji_names.txt" and enter the titles of emojis for searching them in the Warpcast context menu.
8. Open the file "data/farm_data/search_authors.txt" and enter the keywords for searching posts and further random subscription to authors.
9. Open the file "data/farm_data/search_channels.txt" and enter the keywords for searching channels and further random subscription to them.
10. Open the file "data/farm_data/search_users.txt" and enter the keywords for searching users and further random subscription to them.
11. Open the file "data/farm_data/subscribe_to_users.txt" and enter the mandatory usernames that you are going to follow (the number of subscriptions at a time is specified in the config).
12. Open the file "data/farm_data/subscribe_to_channels.txt" and enter the mandatory channel names that you are going to follow (the number of subscriptions at a time is specified in the config).
13. Open the folder "data/images_for_casts/random" and upload any media files with any names. These files will be randomly added to casts.
14. Open the folder "data/images_for_casts/specific" and upload any media files. These files will be attached to specific casts (we specify the link to the media file explicitly in the cast text). To attach media file to a cast you need to specify a link in the cast text using the format <image_name.type>, for example "1|ZkSync assholes<example_123.png>". You can insert the link anywhere in the cast text (anywhere after "|", for example "1|ZkSync <example_123.png>assholes or "1|<example_123.png>ZkSync assholes", but <b>not</b> like this "<example_123.png>1|ZkSync assholes"). Images are deleted after use. Do not forget to specify the image extension, it may differ (jpg, png, etc.). In general, any file that is supported by Warpcast will work here.
15. Open the file "data/sensitive_data/metamask_passwords.txt" and enter the Metamask passwords, each on a new line using the format "acc_name|metamask_password" in case you are going to use the metamask connection module (connect_metamask).
16. Launch AdsPower and log into your account.
17. Use terminal to navigate to the project folder, enter the command "python3 farm_warpcast.py" and press ENTER.

## 🌵 Additional information
- I am not responsible for your accounts (ban, shadowban). However, this approach was tested by the community (check out my [Twitter bot](https://github.com/CryptoBusher/Adspower-twitter-warmup)). I have also improved some algorithms.
- If you find any bugs, I would appreciate your feedback.
- In order for the metamask connection module (connect_metamask) to work, you must have LavaMoat disabled. If you don't know how to do this, you can use, for example, [this version of metamask](https://github.com/MetaMask/metamask-extension/releases/tag/v10.25.0), or process this activity manually. Seeds must already be imported into metamask.

## 💴 Donate
Support my channel by donating on any EVM chain
<b>0x77777777323736d17883eac36d822d578d0ecc80</b>

## 🌏 Russian
Нахуй я этим делюсь? Этот скрипт поможет сэкономить бешеное количество времени. Он работает с профилями Warpcast, которые импортированны в [AdsPower](https://share.adspower.net/Btc9YYgpiyJxhmW). Заебался с рандомизацией, так что можешь спать спокойно.

<i>Связь с создателем: https://t.me/CryptoBusher</i> <br>
<i>Если ты больше по Твиттеру: https://twitter.com/CryptoBusher</i> <br>

<i>Залетай сюда, чтоб не пропускать дропы подобных скриптов: https://t.me/CryptoKiddiesClub</i> <br>
<i>И сюда, чтоб общаться с крутыми ребятами: https://t.me/CryptoKiddiesChat</i> <br>

## 🔥 Последние обновления
- [x] 28.05.2024 - Подписка на юзеров из списка через прямую ссылку и поиск
- [x] 28.05.2024 - Подписка на каналы из списка только через прямую ссылку
- [x] 28.05.2024 - [Видео - гайд по настройке](https://t.me/CryptoKiddiesClub/513)
- [x] 29.05.2024 - Свичи модулей в конфиге для удобства
- [x] 29.05.2024 - Фикс мелких багов, добавлен дебаг лог в файл "data/debug_log.log"
- [x] 01.06.2024 - Фикс мелких багов
- [x] 01.06.2024 - Привязка Metamask (см. дополнительную информацию)
- [x] 04.06.2024 - Фикс мелких багов (добавлена очистка поля поиска)
- [x] 07.06.2024 - Многострочные касты, поддержка emoji, указанных в тексте кастов
- [x] 13.06.2024 - Изображения в кастах (указанные явно или рандомные)
- [x] 16.06.2024 - Многопоточность
- [x] 01.07.2024 - Фикс багов, фикс проблемы "Error retrieving data. Please try again."
- [x] 01.07.2024 - Добавлен параметр "adspower_debug_port" в конфиг
- [x] 12.07.2024 - Отловилены ошибки при выборе emoji для каста, убраны stack traces в дебаг лог
- [x] 03.08.2024 - Readme и config переведены на Английский
- [x] 03.02.2025 - Обновилены селекторы, оттестированы все методы, добавлены "highlight_elements" в конфиг, удалена функция "bookmark" из модуля "surf feed"

## ⌛️ На очереди
- Касты в каналах по заданному сценарию
- Активности в топовых проектах 

## ⚙️ Функции
1. Касты (home)
2. Подписка на рандомных юзеров из рекомендаций (скроллит и подписывается)
3. Подписка на рандомные каналы из рекомендаций (скроллит и подписывается)
4. Серфинг ленты, включая:
   1. Скролл ленты
   2. Рандомные лайки
   3. Рандомные рекасты
   4. Рандомные букмарки
5. Использование поиска и:
   1. Рандомная подписка на авторов постов из результатов поиска
   2. Рандомная подписка на каналы из результатов поиска 
   3. Рандомная подписка на юзеров из результатов поиска
6. Подписка на юзеров из списка через прямую ссылку и поиск
7. Подписка на каналы из списка только через прямую ссылку
8. Подключение метамаска

## 🤔 Преимущества
1. Максимально - возможная рандомизация:
   1. Последовательность выполнения модулей
   2. Активности в рамках модуля (количество interactions, скорость выполнения)
   3. Рандомизация основанна на вероятностях
   4. Координаты, по которым производится клик по кнопке
   5. Задержки при вводе текста
   6. Скролл ленты
2. Работа через [AdsPower](https://share.adspower.net/Btc9YYgpiyJxhmW)
3. Headless mode
4. Возможность работать с уже открытыми профилями AdsPower
5. Использования меню Emoji при касте
6. Медиа в кастах (изображения / GIF итд.)
7. Многопоточность

## 📚 Первый запуск
1. Устанавливаем [Python 3.12](https://www.python.org/downloads/).
2. Скачиваем проект, в терминале, находясь в папке проекта, вписываем команду "pip install -r requirements.txt" для установки всех зависимостей.
3. Переименовываем папку "_data" в "data".
4. Открываем файл "data/profile_ids.py" и забиваем свои профиля как в примере ("название":"ID из AdsPower"). Название должно мэтчиться с названиями в файле "data/farm_data/casts.txt". Проще всего пронумеровать, как в примере.
5. Открываем файл "data/config.py" и забиваем настройки. Можно написать в наш [чат](https://t.me/CryptoKiddiesChat) для уточнения каких - либо моментов.
6. Открываем файл "data/farm_data/casts.txt" и вбиваем текста для постов, каждый с новой строки в формате "acc_name|cast_text". Для каждого аккаунта надо предоставлять свои текста для постов, можно вбивать много текстов для одного аккаунта, скрипт будет выбирать рандомно текста для акка или по - порядку, в зависимости от настроек. Текст каста может содержать emojis и переносы строк ('\n).
7. Открываем файл "data/farm_data/emoji_names.txt" и вбиваем туда названия emoji, по которым будет производиться поиск в контекстном меню, если в настройках вы активировали данную функцию.
8. Открываем файл "data/farm_data/search_authors.txt" и вбиваем туда строки, по которым будет происходить поиск постов для последующей подписки на их авторов.
9. Открываем файл "data/farm_data/search_channels.txt" и вбиваем туда строки, по которым будет происходить поиск каналов для последующей подписки на них.
10. Открываем файл "data/farm_data/search_users.txt" и вбиваем туда строки, по которым будет происходить поиск юзеров для последующей подписки них.
11. Открываем файл "data/farm_data/subscribe_to_users.txt" и вбиваем туда список юзернеймов, на которые обязательно надо подписываться (количество подписок за раз указывается в конфиге).
12. Открываем файл "data/farm_data/subscribe_to_channels.txt" и вбиваем туда список каналов, на которые обязательно надо подписываться (количество подписок за раз указывается в конфиге).
13. Открываем папку "data/images_for_casts/random" и закидываем любые картинки с любыми названиями, которые хотим рандомно добавлять к постам согласно вероятности в конфиге.
14. Открываем папку "data/images_for_casts/specific" и закидываем картинки, которые хотим прикладывать к определенным кастам (указываем ссылку на картинку явно в тексте каста). Чтоб прикрепить эту картинку к касту, надо в тексте каста указать ссылку в формате <image_name.type>, например "1|ZkSync pidarasi<example_123.png>", можно вставлять ссылку в любом месте текста каста (в любом месте после **|**, например так: "1|ZkSync <example_123.png>pidarasi": или так "1|<example_123.png>ZkSync pidarasi", но не так: "<example_123.png>1|ZkSync pidarasi"). Изображения удаляются после использования. Не забывайте указать расширение изображения, оно может отличаться (jpg, png и тд.). Вообще, тут будет работать любой поддерживаемый Варпкастом файл.
15. Открываем файл "data/sensitive_data/metamask_passwords.txt" и вбиваем туда список паролей от метамасков, каждый с новой строки в формате "acc_name|metamask_password", если хотите использовать модуль подключения метамаска (connect_metamask).
16. Запускаем AdsPower и логинимся в свой аккаунт.
17. В терминале, находясь в папке проекта, вписываем команду "python3 farm_warpcast.py" и жмем ENTER.

## 🌵 Дополнительная информация
- Я не несу ответственность за ваши аккаунты (ban, shadowban). Однако данный подход был оттестирован комьюнити (на примере [Twitter бота](https://github.com/CryptoBusher/Adspower-twitter-warmup)). Я доработал некоторые алгоритмы.
- Если нашли баги - буду благодарен за обратную связь.
- Для того, чтоб работал модуль подключения метамаска (connect_metamask) работал, у тебя должен быть отключен LavaMoat. Если не знаешь, как это сделать - можешь использовать, например, [эту версию метамаска](https://github.com/MetaMask/metamask-extension/releases/tag/v10.25.0), либо подключай руками. Сидки должны быть уже импортированны в метамаск. 

## 💴 Донат
Поддержи мой канал донатом в любой EVM сети
<b>0x77777777323736d17883eac36d822d578d0ecc80</b>
