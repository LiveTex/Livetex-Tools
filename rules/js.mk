
SOURCE_PATH ?= ./lib
BUILD_PATH ?= ./bin
HEADERS_BUILD_PATH ?= ./externs
DEPS_PATH ?= ./node_modules
CONFIG_PATH ?= ./etc
INCLUDE_PATH ?= ./include


TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools


JS_ENVIRONMENT ?= node

JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
		--warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT \
		--compilation_level ADVANCED_OPTIMIZATIONS \
		--debug --formatting=PRETTY_PRINT

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		--strict --custom_jsdoc_tags="namespace, event"

JS_HEADERS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor/externsExtractor.py


vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)


all: index-externs.js index.js

publish: index-externs.js index.js
	npm version patch
	npm publish

%.js-run: %.js
	node $(BUILD_PATH)/$<


%.js-compile: %.jso %.jsh
	$(JS_COMPILER) --js $< \
	               --externs `echo "$^" | cut -d " " -f2-`


%.js-lint: %.jso
	 $(JS_LINTER) $^


%.js-check: %.js-compile %.js-lint
	

%.js-clean:
	rm -rf $(BUILD_PATH)/*


%-externs.js: %.jso
	mkdir -p $(HEADERS_BUILD_PATH)
	$(JS_HEADERS_EXTRACTOR)


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
