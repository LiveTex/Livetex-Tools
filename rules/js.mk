

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
vpath %.js $(BUILD_PATH)


################################################################################
# AUX RULES
################################################################################


# HEADERS ######################################################################


%.jsh: %.js-env-headers %.js-custom-headers %.js-headers
	@cat `cat $^ < /dev/null` > $@


%.js-headers:
	@echo $(foreach DIR, $(MODULES_PATH)/*, $(wildcard $(DIR)/externs/*.js)) > $@


%.js-custom-headers:
	@echo $(foreach DIR, $(INCLUDES_PATH), $(wildcard $(DIR)/*.js)) > $@


%.js-env-headers:
	@echo $(foreach DIR, $(ENV_EXTERNS_PATH)/$(JS_ENVIRONMENT), \
	$(wildcard $(DIR)/*.js)) > $@


# COMPILATIONS #################################################################


%.js-compile: %.d
	@cat $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.d
	@$(JS_COMPILER) \
	--js        $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \


# COMPILATIONS WITH EXTERNS ####################################################


%.js-externs-compile: %.d %.jsh
	$(JS_COMPILER) \
	--formating PRETTY_PRINT \
	--js        $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


%.js-externs-compile-compressed: %.d %.jsh
	@$(JS_COMPILER) \
	--js        $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


# ADVANCED COMPILATION #########################################################


%.js-externs-compile-advanced: %.d %.jsh
	$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js        $(foreach FILE, $(shell cat $<), $(SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


################################################################################
# MAIN RULES
################################################################################


%.js-lint: %.d
	$(JS_LINTER) $(foreach FILE, $(shell cat $^), $(SOURCES_PATH)/$(FILE))


%.js-check: %.jst
	@$(JS_TEMPLATER) -a True $< > /dev/null


%.js-assemble: %.jst
	@$(JS_TEMPLATER) $< > \
	$(SOURCES_PATH)/$(shell basename $< | cut -d "." -f 1).js


%.js-extract-externs: %.js
	@mkdir -p $(EXTERNS_PATH)
	@$(JS_EXTERNS_EXTRACTOR) $^ > \
	$(EXTERNS_PATH)/$(shell echo $@ | cut -d '.' -f 1).js


################################################################################
# GENERAL RULES
################################################################################


lint:
	@$(foreach DFILE, $(shell cat $(CONFIG_PATH)/content.lint), \
	make -s $(shell echo $(DFILE) | cut -d '.' -f 1).js-lint)


check: lint
	@$(foreach TEMPLATE, $(CONFIG_PATH)/templates/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | cut -d '.' -f 1).js-check)


build: check
	@mkdir -p $(BUILD_PATH)
	@$(foreach TEMPLATE, $(CONFIG_PATH)/templates/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | cut -d '.' -f 1).js-assemble > \
	$(BUILD_PATH)/$(shell echo $(TEMPLATE) | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js)
	@$(foreach TEMPLATE, $(CONFIG_PATH)/templates/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js-extract-externs)
