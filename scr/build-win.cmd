@echo off

python -m nuitka ^
    --follow-imports ^
    --remove-output ^
    --assume-yes-for-downloads ^
    --onefile ^
    --output-filename=py-shield ^
    --windows-icon-from-ico=../assets/icon.ico ^
    --include-package=commands ^
    --company-name="ByteCorum" ^
    --product-name="Py-Shield" ^
    --file-version=3.0.0.0 ^
    --product-version=3.0.0.0 ^
    --file-description="Tool/Library for Python used to obfuscate and protect your code in static and runtime from decompilation, reverse debug, etc. Also, can prevent detection by antiviruses." ^
    --copyright="https://github.com/ByteCorum/Py-Shield/blob/main/LICENSE" ^
    main.py