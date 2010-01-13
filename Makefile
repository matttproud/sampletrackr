DATASTORE=$(PWD)/datastore
NONDEPLOYMENT=$(PWD)/non-deployment
DEPLOYMENT=$(PWD)/deployment
MOX_HOME=$(NONDEPLOYMENT)/third-party/mox-0.5.1
GAE_HOME=$(NONDEPLOYMENT)/third-party/google_appengine-1.3.0

PATH += $(GAE_HOME)

FIND ?= find
MKDIR ?= mkdir
PYTHON ?= python2.5
RM ?= rm

export PYTHONPATH ?= $(MOX_HOME):$(GAE_HOME)

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
	$(PYTHON) $(GAE_HOME)/appcfg.py update $(DEPLOYMENT)

.PHONY: test builtin_tests third_party_tests development_server clean

