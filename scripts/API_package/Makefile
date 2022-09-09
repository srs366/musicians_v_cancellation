run_get_token:
	python -c 'from chartmetric.Chartmetric_API_token.get_token import get_API_token ; get_API_token()'

run_setup:
	python -c 'from chartmetric.interface.main import setup; setup()'

run_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline; dataframe_pipeline()'

run_setup_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline, setup; dataframe_pipeline(setup())'

run_all: run_setup run_df run_pred
