#! /usr/bin/env sh

export DB_USER=torrent-sniff
export DB_PASS=torrent-sniff
export DB_NAME=torrent-sniff
export DB_PORT=5432

box stop ./database.json
box delete ./database.json
box create ./database.json
box start ./database.json

sleep 3

migrate init postgres
migrate run postgres

unset DB_USER
unset DB_PASS
unset DB_NAME
unset DB_PORT
