from app.utils import logger, settings


def main():
    logger.info(f"Hello, {settings.PROJECT_NAME}!")


if __name__ == "__main__":
    main()
