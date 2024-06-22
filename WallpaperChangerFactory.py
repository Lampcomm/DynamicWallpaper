import platform

from WindowsWallpaperChanger import *
from KDEWallpaperChanger import *


def create_wallpaper_changer(ini_config):
    platform_name = platform.system()
    if platform_name == 'Windows':
        return WindowsWallpaperChanger(ini_config)
    elif platform_name == 'Linux':
        return KDEWallpaperChanger(ini_config)

    return None
