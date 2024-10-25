# pint-monitor

`ping-monitor` is a tool to monitor the availability of a server by pinging it.

|                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **License**     | ![LICENSE](https://img.shields.io/badge/license-MIT-blue.svg?style=flat)                                                                                                                                                                                                                                                                                                                                                                                                           |
| **Environment** | ![Ubuntu](https://img.shields.io/badge/-Ubuntu_22.04_LTS-fad9c1.svg?logo=ubuntu&style=flat) <br> ![Docker](https://img.shields.io/badge/-Docker_v26.0.2-0055a4.svg?logo=docker&style=flat) ![Docker Compose](https://img.shields.io/badge/-Docker_Compose_v2.22.0-0055a4.svg?logo=docker&style=flat) <br> ![Python](https://img.shields.io/badge/-Python_3.10-F9DC3E.svg?logo=python&style=flat) ![Poetry](https://img.shields.io/badge/-Poetry-2c2d72.svg?logo=python&style=flat) |
| **Technology**  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                 |

## Requirements

- Docker and docker-compose are required. The versions are as follows.
  - Docker: v26.0.2
  - Docker Compose: v2.22.0

## Getting Started

### 1. Clone Repository

```sh
$ git clone git@github.com:nglcobdai/ping-monitor.git
$ cd ping-monitor
```

### 2. Create .env file

#### 2.1. copy .env.example to .env

```sh
$ cp .env{.example,}
```

#### 2.2. edit .env

| Key             | Description                                                                        |
| --------------- | ---------------------------------------------------------------------------------- |
| IP_ADDRESS      | IP address to ping                                                                 |
| SLACK_API_TOKEN | [Slack API Token](https://nglcobdai.github.io/nglcobdai-utils/Installation/Slack/) |
| SLACK_CHANNEL   | [Slack Channel](https://nglcobdai.github.io/nglcobdai-utils/Installation/Slack/)   |
| DATADRIVE       | project directory for output log                                                   |

### 3. Docker Build

```sh
$ docker-compose build --no-cache
```

### 4. cron start

pint-monitor is running on background by cron.

```sh
$ docker-compose up -d
```
