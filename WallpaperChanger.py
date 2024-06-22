import os
from abc import ABC, abstractmethod
import SystemClockFactory


class WallpaperChanger(ABC):
    def __init__(self, ini_config):
        self.prev_hour = -1
        self.curr_hour = -1
        self.desktop_wallpaper_path = ini_config.get("Desktop", "WallpaperPath", fallback="")
        self.lock_screen_wallpaper_path = ini_config.get("LockScreen", "WallpaperPath", fallback="")
        self.system_clock = SystemClockFactory.create_system_clock()

    def try_change_wallpaper(self):
        if not self.__need_change_wallpaper():
            return

        if self.__need_change_desktop_wallpaper():
            self.__change_desktop_wallpaper()

        if self.__need_change_lock_screen_wallpaper():
            self.__change_lock_screen_wallpaper()

    def __change_desktop_wallpaper(self):
        self._change_desktop_wallpaper_impl(self.__get_image_path(self.desktop_wallpaper_path))

    def __change_lock_screen_wallpaper(self):
        self._change_lock_screen_wallpaper_impl(self.__get_image_path(self.lock_screen_wallpaper_path))

    @abstractmethod
    def _change_desktop_wallpaper_impl(self, image_path):
        pass

    @abstractmethod
    def _change_lock_screen_wallpaper_impl(self, image_path):
        pass

    def __need_change_wallpaper(self):
        self.curr_hour = self.system_clock.now().hour
        if self.curr_hour != self.prev_hour:
            self.prev_hour = self.curr_hour
            return True

        return False

    def __need_change_desktop_wallpaper(self):
        return self.desktop_wallpaper_path != ""

    def __need_change_lock_screen_wallpaper(self):
        return self.lock_screen_wallpaper_path != ""

    def __get_image_path(self, images_paths):
        image_index_str = str(self.curr_hour)
        for image_name in os.listdir(images_paths):
            if image_index_str in image_name:
                return os.path.join(images_paths, image_name)
