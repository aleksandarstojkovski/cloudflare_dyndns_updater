#!/bin/bash

SCRIPT=$(realpath -s "$0")
SCRIPTPATH=$(dirname "$SCRIPT")

cd "$SCRIPTPATH"

if [[ -f pid ]]; then
  kill -9 $(cat pid)
  rm -f pid
fi

if [[ ! -f pid ]]; then
  nohup python3 -u main.py  > log.log 2>&1 &
  echo $! > pid
else
  echo "process already started, pid: $(cat pid)"
fi
