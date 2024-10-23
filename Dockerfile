FROM ubuntu:22.04

ENV LANG=C.UTF-8 \
    LANGUAGE=en_US \
    PYTHONPATH="/root/workspace:$PYTHONPATH" \
    DEBIAN_FRONTEND=noninteractive \
    TZ=Asia/Tokyo

# tzdataのインストールとタイムゾーンの設定
RUN apt-get update && apt-get install -y tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Pythonのインストール
RUN apt-get update && apt-get install -y python3.10 python3-pip \
    && ln -s /usr/bin/python3.10 /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /root/workspace

# Poetryのインストールと依存関係のインストール
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --upgrade poetry

# pyproject.toml、poetry.lock、poetry.tomlをコピーする
COPY pyproject.toml poetry.lock poetry.toml $WORKDIR/

# Clear cache to free up space
RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN poetry install --no-root

# cronとpingのインストール
RUN apt-get update && apt-get install -y \
    iputils-ping \
    cron \
    && rm -rf /var/lib/apt/lists/*

# cronジョブの設定
COPY app/cron_job /etc/cron.d/cron_job
RUN chmod 0644 /etc/cron.d/cron_job
RUN crontab /etc/cron.d/cron_job
