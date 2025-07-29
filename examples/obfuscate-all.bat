@echo off

echo onefile-legacy obfuscation test
cd "onefile-legacy"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo onefile obfuscation test
cd "../onefile"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo multifile-legacy obfuscation test
cd "../multifile-legacy"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo multifile obfuscation test
cd "../multifile"
rmdir /s /q "obfuscated"
start cmd /c "obfuscate.bat"

echo "done"
pause null