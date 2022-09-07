run_setup:
	python -c 'from chartmetric.interface.main import setup; print(setup())'

run_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline; dataframe_pipeline()'

run_setup_df:
	python -c 'from chartmetric.interface.main import dataframe_pipeline, setup; dataframe_pipeline(setup())'

run_all: run_setup run_df run_pred
