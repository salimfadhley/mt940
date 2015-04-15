source venv/bin/activate
pushd `pwd`
cd src
python setup.py clean bdist_wheel upload
python setup.py clean sdist upload
popd
