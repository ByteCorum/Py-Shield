#!/bin/bash

python -m nuitka \
    --follow-imports \
    --remove-output \
    --onefile \
    --assume-yes-for-downloads \
    --output-filename=py-shield \
    --linux-icon=../assets/icon.png \
    --include-package=commands \
    --company-name="ByteCorum" \
    --product-name="Py-Shield" \
    --file-version=3.0.0.0 \
    --product-version=3.0.0.0 \
    --file-description="Tool/Library for Python used to obfuscate and protect your code in static and runtime from decompilation, reverse debug, etc. Also, can prevent detection by antiviruses." \
    --copyright="https://github.com/ByteCorum/Py-Shield/blob/main/LICENSE" \
    main.py