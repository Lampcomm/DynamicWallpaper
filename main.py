import sys
import configparser
import WallpaperChangerFactory


def main():
    wallpaperChanger = WallpaperChangerFactory.create_wallpaper_changer(get_config())
    while True:
        wallpaperChanger.try_change_wallpaper()


def get_config():
    config_path = "config.ini"
    if len(sys.argv) > 1:
        config_path = sys.argv[1]

    config_parser = configparser.ConfigParser()
    config_parser.read(config_path)
    return config_parser


if __name__ == "__main__":
    main()
