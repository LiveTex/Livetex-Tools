

################################################################################
# VARIABLES
################################################################################

# PATHS ########################################################################


PROJECT_PATH      ?= $(shell pwd)
BUILD_PATH        ?= $(PROJECT_PATH)/bin
CONFIG_PATH       ?= $(PROJECT_PATH)/etc/build
EXTERNS_PATH      ?= $(PROJECT_PATH)/externs
INCLUDES_PATH     ?= $(PROJECT_PATH)/include
MODULES_PATH      ?= $(PROJECT_PATH)/node_modules
SOURCES_PATH      ?= $(PROJECT_PATH)/lib
TOOLS_PATH        ?= $(MODULES_PATH)/livetex-tools
ENV_EXTERNS_PATH  ?= $(TOOLS_PATH)/externs


# TOOLS ########################################################################


JS_COMPILER ?= java -jar $(TOOLS_HOME)/tools/compiler.jar \
                --warning_level     VERBOSE \
                --language_in       ECMASCRIPT5_STRICT \

JS_LINTER ?= $(TOOLS_HOME)/tools/gjslint/closure_linter/gjslint.py \
		            --strict \
		            --custom_jsdoc_tags "namespace, event"

JS_EXTERNS_EXTRACTOR ?= $(TOOLS_HOME)/tools/externs-extractor/externsExtractor.py


# ENVIRONMENT ##################################################################


JS_ENVIRONMENT ?= node


# PREREQUISITES PATHS ##########################################################


vpath %.d $(CONFIG_PATH)
vpath %.jst $(CONFIG_PATH)


################################################################################
# RULES FOR FILES
################################################################################

## ПОДУМАТЬ!!!!!!!!!!!!!!!


%.js-headers: %.js-env
	cat `cat $^ < /dev/null` $(wildcard $(INCLUDE_PATH)/*.js) < /dev/null > $@


%.js-env:
	echo $(foreach DIR, $(DEPS_PATH)/*, $(wildcard $(DIR)/$(EXTERNS_PATH)/*.js) \
	$(wildcard $(DIR)/$(EXTERNS_PATH)/$(JS_ENVIRONMENT)/*.js)) > $@;


################################################################################
# AUX RULES
################################################################################


%.js-lint: %.d
	$(JS_LINTER) \
	$(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-extract-externs: %.d
	$(JS_EXTERNS_EXTRACTOR) \
	$(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE)) > $(EXTERNS_PATH)/$%.js


%.js-raw-compile: %.d
	@cat $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-compile: %.d
	$(JS_COMPILER) --formatting PRETTY_PRINT \
	--js $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-compress-compile: %.d
	$(JS_COMPILER) --js $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-externs-compile: %.d
	$(JS_COMPILER) --formatting PRETTY_PRINT \
	--js $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE)) \
	--externs $(EXTERNS_PATH)/$%.js


%.js-externs-compress-compile: %.d
	$(JS_COMPILER) --js $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE)) \
	--externs $(EXTERNS_PATH)/$%.js


%.js-assemble: %.jst
	sed -e 's/%%\(.*\)%%/$(shell $(shell cat $^ < /dev/null | grep -m 1 -o '%%\(.*\)%%' | grep -o '[^%]*' ))/' $^


################################################################################
# GENERAL RULES
################################################################################


#make
#make check
#make build
#make clean

