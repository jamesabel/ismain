del /Q ismain.egg-info\*.*
del /Q build\*.*
del /Q dist\*.*
copy /Y LICENSE LICENSE.txt
REM copy /Y docs\source\readme.rst readme.rst
REM copy /Y docs\source\readme.rst ismain\readme.rst
call venv\Scripts\activate.bat
python.exe setup.py bdist_wheel
twine upload dist/*
deactivate
