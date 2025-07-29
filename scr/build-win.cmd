@echo off

python -m nuitka ^
    --follow-imports ^
    --remove-output ^
    --assume-yes-for-downloads ^
    --onefile ^
    --output-filename=py-shield ^
    --windows-icon-from-ico=../assets/icon.ico ^
    --company-name="ByteCorum" ^
    --product-name="Py-Shield" ^
    --file-version=3.0.0.0 ^
    --product-version=3.0.0.0 ^
    --file-description="Program/Library for Python created to protect your code from decompilation and detection by antiviruses" ^
    --copyright="https://github.com/ByteCorum/Py-Shield/blob/main/LICENSE" ^
    main.py