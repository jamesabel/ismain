pushd .
cd ..
call venv\Scripts\activate.bat 
mypy -m ismain
call deactivate
popd
