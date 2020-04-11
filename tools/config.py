import configparser

def main():
    config = configparser.ConfigParser()
    project_config = config.read('../config.ini')

    return project_config


if __name__ == '__main__':
    main()