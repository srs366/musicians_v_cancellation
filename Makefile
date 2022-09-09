# ----------------------------------
#          INSTALL & TEST
# ----------------------------------
install_requirements:
	@pip install -r requirements.txt

check_code:
	@flake8 scripts/* musicians_v_cancellation/*.py

black:
	@black scripts/* musicians_v_cancellation/*.py

test:
	@coverage run -m pytest tests/*.py
	@coverage report -m --omit="${VIRTUAL_ENV}/lib/python*"

ftest:
	@Write me

clean:
	@rm -f */version.txt
	@rm -f .coverage
	@rm -fr */__pycache__ */*.pyc __pycache__
	@rm -fr build dist
	@rm -fr musicians_v_cancellation-*.dist-info
	@rm -fr musicians_v_cancellation.egg-info

install:
	@pip install . -U

all: clean install test black check_code

count_lines:
	@find ./ -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./scripts -name '*-*' -exec  wc -l {} \; | sort -n| awk \
		        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''
	@find ./tests -name '*.py' -exec  wc -l {} \; | sort -n| awk \
        '{printf "%4s %s\n", $$1, $$2}{s+=$$0}END{print s}'
	@echo ''

# ----------------------------------
#      UPLOAD PACKAGE TO PYPI
# ----------------------------------
PYPI_USERNAME=<AUTHOR>
build:
	@python setup.py sdist bdist_wheel

pypi_test:
	@twine upload -r testpypi dist/* -u $(PYPI_USERNAME)

pypi:
	@twine upload dist/* -u $(PYPI_USERNAME)

#API Run
run_get_token:
	python -c 'from chartmetric.Chartmetric_API_token.get_token import get_API_token ; print(get_API_token())'

run_setup:
	python -c 'from chartmetric.interface.main import setup; print(setup())'

run_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline; dataframe_pipeline()'

run_setup_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline, setup; dataframe_pipeline(setup())'

run_all: run_setup run_df run_pred

#Tweet Run
run_tweet_setup:
	python -c 'from twitter_scraping.twitter.interface.main import setup; print(setup())'

run_tweet_df:
	python -c 'from twitter_scraping.twitter.interface.main import dataframe_pipeline; dataframe_pipeline()'

run_tweet_setup_df:
	python -c 'from twitter_scraping.twitter.interface.main import dataframe_pipeline, setup; dataframe_pipeline(setup())'
