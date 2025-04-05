#!/bin/bash
pytest unit_test.py
pytest --cov=. ./
pylint ./*.py
python3 scraper.py