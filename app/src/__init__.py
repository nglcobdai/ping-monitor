from pathlib import Path

from nglcobdai_utils import (
    RotatingFileHandlerInfo,
    Settings,
    Slack,
    get_logger,
)

settings = Settings()
slack = Slack(token=settings.SLACK_API_TOKEN)

datadrive = Path(settings.DATADRIVE)

log_root_dir = datadrive / "main"
log_root_dir.mkdir(parents=True, exist_ok=True)
fh = RotatingFileHandlerInfo(
    log_level=settings.LOG_LEVEL,
    filename=log_root_dir / "application.log",
    max_bytes=settings.MAX_BYTES,
    backup_count=settings.BACKUP_COUNT,
)
logger = get_logger(settings.PROJECT_NAME, fh_info=fh)
