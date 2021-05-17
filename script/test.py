from lib.file_io import YamlIO, DISPLAY_PATH


def main():
    yaml_display = YamlIO(DISPLAY_PATH)
    data = yaml_display.load()
    yaml_display.dump(data)


if __name__ == "__main__":
    main()
