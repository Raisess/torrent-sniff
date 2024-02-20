#! /usr/bin/env sh

podman build -t torrent-sniff .
podman container create --name torrent-sniff \
  -p 8090:8080/tcp \
  torrent-sniff
