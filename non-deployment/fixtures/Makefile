all: content_classifications \
	sample_sources \
	cue_classifications \
	sample_consumers \
	samples

include ../../Makefile

content_classifications:
	$(APPCFG) upload_data --config_file ../tools/bulk_loaders.py \
	--filename=content_classifications.csv --kind=ContentClassification \
	--url=http://localhost:8080/remote_api $(DEPLOYMENT)

sample_sources: content_classifications
	$(APPCFG) upload_data --config_file ../tools/bulk_loaders.py \
	--filename=sample_sources.csv --kind=SampleSource \
	--url=http://localhost:8080/remote_api $(DEPLOYMENT)

cue_classifications:
	$(APPCFG) upload_data --config_file ../tools/bulk_loaders.py \
	--filename=cue_classifications.csv --kind=CueClassification \
	--url=http://localhost:8080/remote_api $(DEPLOYMENT)

sample_consumers:
	$(APPCFG) upload_data --config_file ../tools/bulk_loaders.py \
	--filename=sample_consumers.csv --kind=SampleConsumer \
	--url=http://localhost:8080/remote_api $(DEPLOYMENT)

samples:
	$(APPCFG) upload_data -v --noisy --config_file ../tools/bulk_loaders.py \
	--filename=samples.csv --kind=Sample \
	--num_threads=1 --batch_size=1 --http_limit 1 --insecure \
	--url=http://localhost:8080/remote_api $(DEPLOYMENT)

.PHONY: content_classifications sample_sources cue_classifications \
	sample_consumers samples