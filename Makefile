.PHONY:	
	tests
	coverage

coverage:
	coverage run -m pytest --verbose
	coverage html
	coverage xml
 
tests:
	py.test --verbose
