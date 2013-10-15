
BUILD_PATH ?= ./bin
HEADERS_PATH ?= ./externs
DEPS_PATH ?= ./node_modules

TOOLS_HOME ?= $(shell pwd)/$(DEPS_PATH)/livetex-tools

JS_ENVIRONMENT ?= node

JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
                --warning_level VERBOSE --language_in=ECMASCRIPT5_STRICT \
                --compilation_level ADVANCED_OPTIMIZATIONS \
                --debug --formatting=PRETTY_PRINT

JS_LINTER ?= gjslint --strict --custom_jsdoc_tags="namespace,event"

JS_HEADERS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor


%.js-compile: %.jso %.jsh
	$(JS_COMPILER) --js $< \
	               --externs `echo "$^" | cut -d " " -f2-`


%.js-lint: %.jso
	 $(JS_LINTER) $^


%.js: %.jso %.jst
	$(JS_HEADERS_EXTRACTOR) $< > $(HEADERS_PATH)/$(@F); \
  sed -e "/%%CONTENT%%/r $<" \
      -e "//d" `echo "$^" | cut -d " " -f2-` > $(BUILD_PATH)/$(@F)


%.jso : %.d
	cat $(foreach FILE, $(shell cat $^), $(<D)/$(FILE)) > $@


%.jsh : %.hd
	cat `cat $^ || echo "/dev/null"` > $@


%.hd :
	echo $(foreach DIR, $(DEPS_PATH)/*, $(wildcard $(DIR)/$(HEADERS_PATH)/*.js) \
	  $(wildcard $(DIR)/$(HEADERS_PATH)/$(JS_ENVIRONMENT)/*.js)) > $@;
