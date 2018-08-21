SHELL := /bin/bash
develop:
	source /home/sdg/miniconda3/etc/profile.d/conda.sh && \
	conda env update -f requirements.yml && \
	conda activate poc_ml_versioning && \
	pip install dvc && \
	pip install mlflow && \
	pip install -e .
