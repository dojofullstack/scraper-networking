#!/bin/sh
find . -name '*.pyc' -exec rm -f {} +
find . -name '*.pyo' -exec rm -f {} +
find . -name '*~' -exec rm -f {} +
rm db.sqlite3 ;
rm -rf app/migrations/* ;
echo '' > app/migrations/__init__.py ;
