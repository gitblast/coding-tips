#!/bin/bash

pip freeze | grep -v pkg-resources > requirements.txt

echo "requirements.txt updated."
