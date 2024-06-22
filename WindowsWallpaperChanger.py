import os
from WallpaperChanger import *


class WindowsWallpaperChanger(WallpaperChanger):
    def __init__(self, ini_config):
        super().__init__(ini_config)

    def _change_desktop_wallpaper_impl(self, image_path):
        pass

    def _change_lock_screen_wallpaper_impl(self, image_path):
        pass
