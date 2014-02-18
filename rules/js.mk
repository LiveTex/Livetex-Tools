

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


JS_COMPILER ?= java -jar $(TOOLS_PATH)/tools/compiler.jar \
                --warning_level     VERBOSE \
                --language_in       ECMASCRIPT5_STRICT

JS_LINTER ?= $(TOOLS_PATH)/tools/gjslint/closure_linter/gjslint.py \
		            --strict \
		            --custom_jsdoc_tags "namespace, event"

JS_EXTERNS_EXTRACTOR ?= $(TOOLS_PATH)/tools/externs-extractor/externsExtractor.py

JS_TEMPLATER ?= $(TOOLS_PATH)/tools/templater.py


# ENVIRONMENT ##################################################################


JS_ENVIRONMENT ?= node


# PREREQUISITES PATHS ##########################################################


vpath %.d $(CONFIG_PATH)/sources-lists
vpath %.jst $(CONFIG_PATH)/templates


################################################################################
# AUX RULES
################################################################################


%.jsh: %.js-env-headers %.js-custom-headers %.js-headers
	@cat `cat $^ < /dev/null` > $@


%.js-headers:
	@echo $(foreach DIR, $(MODULES_PATH)/*, $(wildcard $(DIR)/externs/*.js)) > $@


%.js-custom-headers:
	@echo $(foreach DIR, $(INCLUDES_PATH), $(wildcard $(DIR)/*.js)) > $@


%.js-env-headers:
	@echo $(foreach DIR, $(ENV_EXTERNS_PATH)/$(JS_ENVIRONMENT), \
	$(wildcard $(DIR)/*.js)) > $@


################################################################################
# MAIN RULES
################################################################################


%.js-lint: %.d
	$(JS_LINTER) \
	$(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-extract-externs: %.d
	@mkdir -p $(EXTERNS_PATH)
	@$(JS_EXTERNS_EXTRACTOR) \
	$(foreach FILE, $(shell cat $^), \
	$(SOURCES_PATH)/$(FILE)) > $(EXTERNS_PATH)/$(shell echo $@ | cut -d '.' -f 1).js


%.js-assemble: %.jst
	@$(JS_TEMPLATER) $< > $(SOURCES_PATH)/$(shell basename $< | cut -d "." -f 1).js


# COMPILATIONS #################################################################


%.js-advanced-compile: %.d %.jsh
	$(JS_COMPILER) \
	--formatting PRETTY_PRINT \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \
	--externs $(shell echo "$^" | cut -d " " -f 2)


%.js-compress-compile: %.d %.jsh
	@$(JS_COMPILER) \
	--js $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \
	--externs $(shell echo "$^" | cut -d " " -f 2)


%.js-raw-compile: %.d
	@cat $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE))

