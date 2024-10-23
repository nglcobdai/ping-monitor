import subprocess
from pathlib import Path

from nglcobdai_utils import RotatingFileHandlerInfo, StringHandlerInfo, get_logger
from pydantic import BaseModel

from app.src import settings, slack


def monitoring(info):
    monitor = Monitor(info)
    monitor()


class Monitor:
    """Monitor the IP address and send a message to Slack."""

    def __init__(self, monitor_info):
        """Initialize the Monitor class.

        Args:
            monitor_info (MonitorInfo): The information of the monitor.
        """
        self.ip_address = monitor_info.ip_address

        fh = RotatingFileHandlerInfo(
            log_level=settings.LOG_LEVEL,
            filename=monitor_info.log_root_dir / "monitoring.log",
            max_bytes=settings.MAX_BYTES,
            backup_count=settings.BACKUP_COUNT,
        )
        sh = StringHandlerInfo(log_level="INFO")
        self.logger = get_logger(settings.IP_ADDRESS, fh_info=fh, sh_info=sh)

    def __call__(self):
        """Monitor the IP address and send a message to Slack."""
        self.logger.info("Start monitoring...")
        try:
            result = self.ping(self.ip_address)

            if result.returncode != 0:
                self.logger.warning(f"Warning: {self.ip_address} is Unreachable.")
                slack.post_text(
                    channel=settings.SLACK_CHANNEL,
                    text=self.logger.get_log_message(),
                )
            else:
                self.logger.info(f"Success: {self.ip_address} is Reachable.")

        except Exception as e:
            self.logger.error(f"Error: {e}")
            slack.post_text(
                channel=settings.SLACK_CHANNEL,
                text=self.logger.get_log_message(),
            )
        self.logger.info("End monitoring...")

    @staticmethod
    def ping(ip_address):
        """Ping the IP address.

        Args:
            ip_address (str): The IP address to ping.

        Returns:
            CompletedProcess: The result of the ping command.
        """
        return subprocess.run(
            ["ping", "-c", "1", ip_address],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )


class MonitorInfo(BaseModel):
    """The information of the monitor."""

    ip_address: str
    log_root_dir: Path
