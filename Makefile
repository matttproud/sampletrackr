THIRD_PARTY=$(PWD)/third-party
NONDEPLOYMENT=$(THIRD_PARTY)/nondeployment
DEPLOYMENT=$(THIRD_PARTY)/deployment
MOX_HOME=$(NONDEPLOYMENT)/mox-0.5.1
GAE_HOME=$(NONDEPLOYMENT)/google_appengine-1.3.0

PATH += $(GAE_HOME)

PYTHON ?= python2.5
PYTHONHOME ?= $(MOX_HOME):$(GAE_HOME)

all: test

test: builtin_tests third_party_tests

builtin_tests:

third_party_tests:
	$(PYTHON) $(MOX_HOME)/mox_test.py

development_server:
	$(PYTHON) $(GAE_HOME)/dev_appserver.py . >/dev/null 2>&1

.PHONY: test builtin_tests third_party_tests development_server

