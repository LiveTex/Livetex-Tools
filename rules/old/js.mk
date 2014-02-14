

SOURCE_PATH ?= ./lib
BUILD_PATH ?= ./bin
HEADERS_BUILD_PATH ?= ./externs
DEPS_PATH ?= ./node_modules
INCLUDE_PATH ?= ./include
CONFIG_PATH = $(shell test -d etc/build && echo etc/build || echo ./etc)


TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools


JS_ENVIRONMENT ?= node


JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
		--warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		--strict --custom_jsdoc_tags="namespace, event"

JS_HEADERS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor/externsExtractor.py

TEMPLATER = $(TOOLS_HOME)/tools/templater.py -o $(BUILD_PATH) -s $(SOURCE_PATH)


vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)


all: install


install: index.js-clean index.js index-externs.js


publish: install
	npm version patch && npm login && npm publish && git push


test-%: %.js
	node --eval "require('$(BUILD_PATH)/$^').test.run('$(names)')"



%.js-compile: %.js %.jsh %.js-lint
	$(JS_COMPILER) --js $(BUILD_PATH)/$< \
	               --externs `echo "$^" | cut -d " " -f2`


%.js-lint:
	$(JS_LINTER) $(foreach FILE, \
	$(shell cat $(CONFIG_PATH)/content.d < /dev/null), $(SOURCE_PATH)/$(FILE))


%.js-check: %.js-compile %.js-lint
	

%.js-clean:
	if [ -e $(BUILD_PATH)/$*.js ]; then \
	rm -rf $(BUILD_PATH)/$*.js; \
	fi;


%-externs.js: %.js
	mkdir -p $(HEADERS_BUILD_PATH)
	$(JS_HEADERS_EXTRACTOR) -i $^


%.js: %.jst
	mkdir -p $(BUILD_PATH)
	$(TEMPLATER) $<


%.jso: %.jst

	cat $(foreach FILE, $(shell cat $^ < /dev/null), \
	$(SOURCE_PATH)/$(FILE)) < /dev/null > content.d


%.jsh: %-headers.d
	cat `cat $^ < /dev/null` $(wildcard $(INCLUDE_PATH)/*.js) < /dev/null > $@


%-headers.d :
	echo $(foreach DIR, $(DEPS_PATH)/*, $(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/*.js) \
	$(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/$(JS_ENVIRONMENT)/*.js)) > $@;
