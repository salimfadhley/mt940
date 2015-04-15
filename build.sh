source venv/bin/activate
pushd `pwd`
cd src
python setup.py bdist_wheel upload
python setup.py sdist upload
popd