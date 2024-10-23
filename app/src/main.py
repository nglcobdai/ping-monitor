from app.src import settings, logger, datadrive
from app.src.monitor import monitoring, MonitorInfo


def main():
    logger.info(f"Start {settings.PROJECT_NAME}...")

    log_root_dir = datadrive / settings.IP_ADDRESS
    log_root_dir.mkdir(parents=True, exist_ok=True)
    info = MonitorInfo(ip_address=settings.IP_ADDRESS, log_root_dir=log_root_dir)
    monitoring(info)

    logger.info(f"End {settings.PROJECT_NAME}...")


if __name__ == "__main__":
    main()
