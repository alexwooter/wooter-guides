#!/bin/sh
# Rebuilds every sites/*.json from the batch files, then the static output. Run from the repo root.
set -e
python3 tools/batch1.py
python3 tools/facts.py
for f in tools/batch2_basketball.py tools/batch3_diamond.py tools/batch4_field.py tools/batch5_specialty.py tools/batch6_general.py tools/batch7_tools.py; do python3 "$f"; done
python3 tools/related.py
python3 tools/timing.py
node build.mjs > /dev/null
echo "built $(ls dist | grep -c '\.com$') sites"
