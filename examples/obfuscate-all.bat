@echo off

echo onefile-legacy obfuscation test
cd "onefile-legacy"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo onefile-global obfuscation test
cd "../onefile-global"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo multifile-legacy obfuscation test
cd "../multifile-legacy"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo multifile-global obfuscation test
cd "../multifile-global"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo "done"
pause null