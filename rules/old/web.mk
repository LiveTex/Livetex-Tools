
SOURCE_PATH ?= ./lib
BUILD_PATH ?= $(shell test -d public/js && echo public/js || echo ./js)
CONFIG_PATH = $(shell test -d etc/build && echo etc/build || echo ./etc)
DEPS_PATH ?= node_modules
HEADERS_BUILD_PATH ?= ./externs

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

JS_ENVIRONMENT ?= node


JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
		--warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		--strict --custom_jsdoc_tags="namespace, event"

TEMPLATER = $(TOOLS_HOME)/tools/templater.py -o $(BUILD_PATH) -s $(SOURCE_PATH)


vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)


%.js-compile: %.jso %.jst
	$(foreach FILE, $(shell cat $(CONFIG_PATH)/*.jso < /dev/null), $(JS_COMPILER) --js $(CONFIG_PATH)/$(FILE))
	$(TEMPLATER) %.jst


%.js-lint: %.jso
	$(JS_LINTER) $(foreach FILE, $(shell cat $(CONFIG_PATH)/$< < /dev/null), $(FILE))
	rm $(CONFIG_PATH)/*.jso


%.js-check: %.js-compile %.js-lint


%.js-clean:
	if [ -e $(BUILD_PATH)/$*.js ]; then \
	rm -rf $(BUILD_PATH)/$*.js; \
	fi;


%.js: %.jst
	mkdir -p $(BUILD_PATH)
	$(TEMPLATER) $<


%.jso: %.jst
	$(TEMPLATER) -l $(CONFIG_PATH)/$@  $^


%.jsh : %-headers.d
	cat `cat $^ < /dev/null` $(wildcard $(INCLUDE_PATH)/*.js) < /dev/null > $@


%-headers.d :
	echo $(foreach DIR, $(DEPS_PATH)/*, $(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/*.js) \
	$(wildcard $(DIR)/$(HEADERS_BUILD_PATH)/$(JS_ENVIRONMENT)/*.js)) > $@;
