#!/usr/bin/env bash

set -eu

curr_dir=$(cd "$(dirname $0)";pwd)
script_dir="$HOME/Library/ApplicationSupport/iTerm2/Scripts/AutoLaunch"
scripts=vagrant-counter.py

mkdir -p "$script_dir"

for script in $scripts
do
    if [ ! -h "$script_dir"/$script ]; then
        ln -s "$curr_dir"/$script "$script_dir"/$script
    fi
done

exit 0
