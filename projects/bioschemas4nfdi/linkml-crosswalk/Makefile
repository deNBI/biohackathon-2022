NAME=crosswalk
ENV=conda run -n $(NAME)

all: run

.env_created:
	conda env create -n $(NAME) -f environment.yaml
	touch .env_created

schema.yaml: .env_created
	$(ENV) wget https://raw.githubusercontent.com/sbilge/biohackathon-2022/exact_mappings/projects/bioschemas4nfdi/linkml-crosswalk/schema.yaml

.PHONY:run
run: schema.yaml .env_created
	$(ENV) ./translate.py schema.yaml test.ttl

.PHONY:clean
clean:
	conda env remove -n $(NAME)
	rm schema.yaml .env_created
