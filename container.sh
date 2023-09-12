#! /usr/bin/env sh

podman build -t torrent-sniff .
podman container create --name torrent-sniff \
  -p 8080:8080/tcp \
  torrent-sniff
