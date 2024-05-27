from sys import stderr
from random import randint, choice, shuffle, uniform
from time import sleep

from loguru import logger

from src.helpers import *
from src.WarpcastProfile import WarpcastProfile
from data.profile_ids import profile_ids
from data.config import config

logger.remove()
logger_level = "DEBUG" if config['show_debug_logs'] else "INFO"
logger.add(stderr, level=logger_level, format="<white>{time:HH:mm:ss}</white> | <level>{level: <8}</level> | <white>{"
                                              "message}</white>")

print(busher_logo)
print(social_links)

def start_farm(_account: WarpcastProfile):
    actions_list = {
        _account.cast_on_homepage: {
            "probability": config['cast_on_homepage']['use_module_probability'],
            "name": "cast on homepage"
        },
        _account.subscribe_to_users: {
            "probability": config['subscribe_via_explore']['to_users_probability'],
            "name": "subscribe to users"
        },
        _account.subscribe_to_channels: {
            "probability": config['subscribe_via_explore']['to_channels_probability'],
            "name": "cast on channels"
        },
        _account.surf_feed: {
            "probability": config['surf_feed']['use_module_probability'],
            "name": "surf feed"
        },
        _account.subscribe_to_authors_via_search: {
            "probability": config['subscribe_to_authors_via_search']['use_module_probability'],
            "name": "subscribe to authors via search"
        },
        _account.subscribe_to_channels_via_search: {
            "probability": config['subscribe_to_channels_via_search']['use_module_probability'],
            "name": "subscribe to channels via search"
        },
        _account.subscribe_to_users_via_search: {
            "probability": config['subscribe_to_users_via_search']['use_module_probability'],
            "name": "subscribe to users via search"
        }
    }

    all_actions = list(actions_list.keys())
    shuffle(all_actions)

    logger.info(f'{_account.profile_name} - opening adspower profile')
    _account.open_profile(config['headless'])
    sleep(5)
    _account.driver.maximize_window()

    logger.info(f'{_account.profile_name} - opening warpcast homepage')
    _account.visit_warpcast()
    _account.random_activity_sleep()

    for action in all_actions:
        if uniform(0, 1) < actions_list[action]["probability"]:
            logger.info(f'{_account.profile_name} - performing activity "{actions_list[action]["name"]}"')
            try:
                action()
            except Exception as _err:
                logger.error(f'{_account.profile_name} - failed to perform activity, reason: {_err}')
            finally:
                _account.random_activity_sleep()

    if not _account.profile_was_running:
        logger.info(f'{_account.profile_name} - closing profile')
        try:
            _account.close_profile()
        except Exception as _err:
            logger.error(f'{_account.profile_name} - failed to close profile, reason: {_err}')
    else:
        logger.info(f'{_account.profile_name} - profile was running before farm, leaving it opened')


if __name__ == "__main__":
    warpcast_accounts = []
    for i, (profile_name, profile_id) in enumerate(profile_ids.items()):
        warpcast_accounts.append(WarpcastProfile(profile_name, profile_id))

    if config["profiles_to_farm"] > len(warpcast_accounts):
        logger.info(f"Amount of profiles to farm > total amount of profiles, adjusted")
        config["profiles_to_farm"] = len(warpcast_accounts)

    # for debugging
    # self = warpcast_accounts[0]
    # self.open_profile()

    for i in range(config["profiles_to_farm"]):
        account = warpcast_accounts.pop(randint(0, len(warpcast_accounts) - 1))

        try:
            logger.info(f'{account.profile_name} - starting farm')
            start_farm(account)
            logger.success(f'{account.profile_name} - finished farm')
        except Exception as err:
            logger.error(f'{account.profile_name} - failed to farm, reason: ${err}')

        idle_time_sec = randint(config["delays"]["min_idle_minutes"] * 60, config["delays"]["max_idle_minutes"] * 60)
        logger.info(f'Sleeping {round(idle_time_sec / 60, 1)} minutes')
        sleep(idle_time_sec)
