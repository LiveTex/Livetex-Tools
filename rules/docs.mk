
DEPS_PATH ?= ./node_modules
CONFIG_PATH ?= ./etc

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

DOCS_GENERATOR ?= $(TOOLS_HOME)/tools/Jstuff/jstuff/jstuff.py \
		--config $(CONFIG_PATH)/config.json \
		--result docs

%.doc:
	$(DOCS_GENERATOR)

