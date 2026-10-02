#!/usr/bin/env bash
exec python3 -m unittest discover -s tests -p "test_*.py"
echo "TESTS: $passed/$total"