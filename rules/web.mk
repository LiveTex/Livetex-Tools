
SOURCE_PATH ?= ./lib
BUILD_PATH ?= ./public/js
CONFIG_PATH = $(shell test -d etc/build && echo etc/build || echo ./etc)
DEPS_PATH ?= node_modules
HEADERS_BUILD_PATH ?= ./externs

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

JS_ENVIRONMENT ?= node

vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)

JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
		--warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT \
		--compilation_level ADVANCED_OPTIMIZATIONS \
		--debug --formatting=PRETTY_PRINT

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		--strict --custom_jsdoc_tags="namespace, event"

JS_HEADERS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor/externsExtractor.py

TEMPLATER = $(TOOLS_HOME)/tools/templater.py -o $(BUILD_PATH) -s $(SOURCE_PATH)


all: install


install: index.js


%.js-compile: %.js-lint
	$(JS_COMPILER) --js $< \
	               --externs `echo "$^" | cut -d " " -f2`


%.js-lint:
	$(JS_LINTER) $(foreach FILE, \
	$(shell cat $(CONFIG_PATH)/content.d < /dev/null), $(SOURCE_PATH)/$(FILE))


%.js-check: %.js-compile %.js-lint


%.js-clean:
	if [ -e $(BUILD_PATH)/$*.js ]; then \
	rm -rf $(BUILD_PATH)/$*.js; \
	fi;


%-externs.js: %.jso
	mkdir -p $(HEADERS_BUILD_PATH)
	$(JS_HEADERS_EXTRACTOR)


%.js: %.jst
	mkdir -p $(BUILD_PATH)
	$(TEMPLATER) $<

