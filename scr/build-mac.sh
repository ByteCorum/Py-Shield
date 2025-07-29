#!/bin/bash

python -m nuitka \
    --quiet \
    --follow-imports \
    --remove-output \
    --onefile \
    --output-filename=py-shield \
    --company-name="ByteCorum" \
    --product-name="Py-Shield" \
    --file-version=3.0.0.0 \
    --product-version=3.0.0.0 \
    --file-description="Program/Library for Python created to protect your code from decompilation and detection by antiviruses" \
    --copyright="https://github.com/ByteCorum/Py-Shield/blob/main/LICENSE" \
    main.py

echo "Build completed. Press any key to continue..."
read -n 1