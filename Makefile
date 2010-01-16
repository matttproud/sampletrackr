export DATASTORE=$(PWD)/datastore
export NONDEPLOYMENT=$(PWD)/non-deployment
export DEPLOYMENT=$(PWD)/deployment
export MOX_HOME=$(NONDEPLOYMENT)/third-party/mox-0.5.1
export GAE_HOME=$(NONDEPLOYMENT)/third-party/google_appengine-1.3.0
export APPCFG=$(GAE_HOME)/appcfg.py
export PATH += $(GAE_HOME)

export FIND ?= find
export MKDIR ?= mkdir
export PYTHON ?= python2.5
export RM ?= rm

export PYTHONPATH ?= $(MOX_HOME):$(GAE_HOME):$(DEPLOYMENT)

all: test

clean:
	$(FIND) -type f -a -iname '*~' -exec $(RM) '{}' ';'
	$(FIND) -type f -a -iname '*.pyc' -exec $(RM) '{}' ';'
	$(FIND) -type f -a -iname '*.pyo' -exec $(RM) '{}' ';'

test: builtin_tests third_party_tests

builtin_tests:

third_party_tests:
	$(PYTHON) $(MOX_HOME)/mox_test.py
	$(PYTHON) *_test.py

development_server:
	$(PYTHON) $(GAE_HOME)/dev_appserver.py \
	  --datastore_path=$(DATASTORE) $(DEPLOYMENT)

remote_update:
	$(PYTHON) $(APPCFG) update $(DEPLOYMENT)

load_fixtures:
	$(MAKE) -C non-deployment/fixtures

.PHONY: test builtin_tests third_party_tests development_server clean

