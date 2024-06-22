import os
import abc
from WallpaperChanger import *


class KDEWallpaperChanger(WallpaperChanger):
    def __init__(self, ini_config):
        super().__init__(ini_config)
        self.desktop_wallpaper_plugin = ini_config.get("KDEDesktop", "WallpaperPlugin", fallback="org.kde.image")
        self.change_desktop_wallpaper_command = r"""qdbus org.kde.plasmashell /PlasmaShell org.kde.PlasmaShell.evaluateScript '
            var allDesktops = desktops(); 
            for (i=0;i<allDesktops.length;i++) {{ 
                d = allDesktops[i]; 
                d.wallpaperPlugin = "%s"; 
                d.currentConfigGroup = Array("Wallpaper", "org.kde.image", "General"); 
                d.writeConfig("Image", "%s") 
            }} '
        """

        self.change_lock_screen_wallpaper_command = (
            "kwriteconfig5 --file kscreenlockerrc --group Greeter --group Wallpaper "
            "--group org.kde.image --group General --key Image \"%s\"")

    def _change_desktop_wallpaper_impl(self, image_path):
        os.system(self.change_desktop_wallpaper_command % (self.desktop_wallpaper_plugin, image_path))

    def _change_lock_screen_wallpaper_impl(self, image_path):
        os.system(self.change_lock_screen_wallpaper_command % image_path)
