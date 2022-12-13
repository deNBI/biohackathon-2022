NAME=crosswalk
ENV=conda run -n $(NAME)

all: run

.env_created:
	conda env create -n $(NAME) -f environment.yaml
	touch .env_created

ghga.yaml: .env_created
	$(ENV) wget https://raw.githubusercontent.com/ghga-de/ghga-metadata-schema/main/src/schema/ghga.yaml
	patch ghga.yaml < ghga.patch

.PHONY:run
run: ghga.yaml .env_created
	$(ENV) ./translate.py ghga.yaml test.ttl UNUSED

.PHONY:clean
clean:
	conda env remove -n $(NAME)
	rm ghga.yaml .env_created
