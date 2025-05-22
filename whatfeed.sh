#!/bin/bash

echo "Started."
pip install -q -r requirements.txt
python -B src/reporting.py
echo "Duration: $SECONDS seconds"