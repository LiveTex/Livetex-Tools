

SOURCE_PATH ?= ./lib
BUILD_PATH ?= ./bin
HEADERS_BUILD_PATH ?= ./externs
DEPS_PATH ?= ./node_modules
INCLUDE_PATH ?= ./include
CONFIG_PATH = $(shell test -d etc/build && echo etc/build || echo ./etc)


TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools


JS_ENVIRONMENT ?= node

JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/closure-compiler.jar \
		--warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT \
		--compilation_level ADVANCED_OPTIMIZATIONS \
		--debug --formatting=PRETTY_PRINT

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		--strict --custom_jsdoc_tags="namespace, event"

JS_HEADERS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor/externsExtractor.py


vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)


all: install


install: index.js-clean index.js index-externs.js


publish: install
	npm version patch && npm login && npm publish && git push


test-%: %.js
	node --eval "require('$(BUILD_PATH)/$^').test.run('$(names)')"



%.js-compile: %.jso %.jsh %.js-lint
	$(JS_COMPILER) --js $< \
	               --externs `echo "$^" | cut -d " " -f2`


%.js-lint: %.d
	$(JS_LINTER) $(foreach FILE, \
	$(shell cat $^ < /dev/null), $(SOURCE_PATH)/$(FILE))


%.js-check: %.js-compile %.js-lint


%.js-clean:
	if [ -e $(BUILD_PATH)/$*.js ]; then \
	rm -rf $(BUILD_PATH)/$*.js; \
	fi;

%-externs.js: %.d
	mkdir -p $(HEADERS_BUILD_PATH)
	$(JS_HEADERS_EXTRACTOR) \
	$(foreach FILE, $(shell cat $<), $(SOURCE_PATH)/$(FILE)) > \
	$(HEADERS_BUILD_PATH)/$(shell echo $< | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js


%.js: %.jso %.jst
	mkdir -p $(BUILD_PATH)
	sed -e "/%%CONTENT%%/r $<" \
	-e "//d" `echo "$^" | cut -d " " -f2-` > $(BUILD_PATH)/$(@F)


%.jso : %.d
	cat $(foreach FILE, $(shell cat $^ < /dev/null), \
	$(SOURCE_PATH)/$(FILE)) < /dev/null > $@


%.jsh : %-headers.d
	cat `cat $^ < /dev/null` $(wildcard $(INCLUDE_PATH)/*.js) < /dev/null > $@


%-headers.d :
	echo $(foreach DIR, $(DEPS_PATH)/*, $(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/*.js) \
	$(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/$(JS_ENVIRONMENT)/*.js)) > $@;