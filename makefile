default:
	cd demo && make

deploy_test:
	python setup.py register -r test
	python setup.py sdist upload -r test
	#pip install -i https://testpypi.python.org/pypi <package name>

deploy_production:
	python setup.py sdist -r pypi
	python setup.py register -r pypi
	twine upload dist/*

