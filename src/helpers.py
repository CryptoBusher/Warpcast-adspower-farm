busher_logo = """
██████╗░██╗░░░██╗░██████╗██╗░░██╗███████╗██████╗░
██╔══██╗██║░░░██║██╔════╝██║░░██║██╔════╝██╔══██╗
██████╦╝██║░░░██║╚█████╗░███████║█████╗░░██████╔╝
██╔══██╗██║░░░██║░╚═══██╗██╔══██║██╔══╝░░██╔══██╗
██████╦╝╚██████╔╝██████╔╝██║░░██║███████╗██║░░██║
╚═════╝░░╚═════╝░╚═════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝
"""

social_links = """
Telegram channel: @CryptoKiddiesClub
Telegram chat: @CryptoKiddiesChat
Twitter: @CryptoBusher
"""


def remove_line(file_path: str, line_to_remove: str):
    with open(file_path, "r") as _file:
        lines = [i.strip() for i in _file]

    with open(file_path, "w") as _file:
        for line in lines:
            if line != line_to_remove:
                _file.write(line)
