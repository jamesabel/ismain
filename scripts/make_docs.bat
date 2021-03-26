REM jca
REM https://sphinx-rtd-tutorial.readthedocs.io/en/latest/build-the-docs.html
REM
pushd .
cd ..
call venv\Scripts\activate.bat
call make clean
call sphinx-apidoc -o ./source sundry
call make html
deactivate
popd
