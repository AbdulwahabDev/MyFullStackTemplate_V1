#! /usr/bin/env sh
set -e


# export all .env variables
. ./.env

# Start angular
exec ng run fuse:serve --disable-host-check --host 0.0.0.0 --poll 2000