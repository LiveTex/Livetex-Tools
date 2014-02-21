


################################################################################
# VARIABLES
################################################################################


# PATHS ########################################################################


PROJECT_PATH        ?= $(shell pwd)
CONFIG_PATH         ?= $(PROJECT_PATH)/etc/build
TEMPLATES_PATH      ?= $(CONFIG_PATH)/templates
SOURCES_LISTS_PATH  ?= $(CONFIG_PATH)/sources-lists
INCLUDES_PATH       ?= $(PROJECT_PATH)/include
JS_BUILD_PATH       ?= $(PROJECT_PATH)/bin
JS_EXTERNS_PATH     ?= $(PROJECT_PATH)/externs
JS_SOURCES_PATH     ?= $(PROJECT_PATH)/lib
MODULES_PATH        ?= $(PROJECT_PATH)/node_modules
TOOLS_PATH          ?= $(MODULES_PATH)/livetex-tools
ENV_EXTERNS_PATH    ?= $(TOOLS_PATH)/externs


# TOOLS ########################################################################


JS_COMPILER ?= java -jar $(TOOLS_PATH)/tools/compiler.jar \
                --warning_level     VERBOSE \
                --language_in       ECMASCRIPT5_STRICT


JS_LINTER ?= $(TOOLS_PATH)/tools/gjslint/closure_linter/gjslint.py \
		            --strict \
		            --custom_jsdoc_tags "namespace, event"


JS_EXTERNS_EXTRACTOR ?= $(TOOLS_PATH)/tools/externs-extractor/externsExtractor.py


TEMPLATER ?= $(TOOLS_PATH)/tools/templater.py


# ENVIRONMENT ##################################################################


JS_ENVIRONMENT ?= node


# PREREQUISITES PATHS ##########################################################


vpath %.jst $(TEMPLATES_PATH)/js
vpath %.jsd $(SOURCES_LISTS_PATH)/js
vpath %.js  $(JS_BUILD_PATH)


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


%.js-compile: %.jsd
	@cat $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE))


%.js-compile-compressed: %.jsd
	@$(JS_COMPILER) \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \


# COMPILATIONS WITH EXTERNS ####################################################


%.js-externs-compile: %.jsd %.jsh
	$(JS_COMPILER) \
	--formating PRETTY_PRINT \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


%.js-externs-compile-compressed: %.jsd%.jsh
	@$(JS_COMPILER) \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


# ADVANCED COMPILATION #########################################################


%.js-externs-compile-advanced: %.jsd %.jsh
	$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


################################################################################
# MAIN RULES
################################################################################


%.js-lint: %.jsd
	@$(JS_LINTER) $(foreach FILE, $(shell cat $^), $(JS_SOURCES_PATH)/$(FILE))


%.js-check: %.jst
	@$(TEMPLATER) -a True $< > /dev/null


%.js-assemble: %.jst
	@mkdir -p $(JS_BUILD_PATH)
	$(TEMPLATER) $< > \
	$(shell echo $(JS_BUILD_PATH)/$(shell basename $<) | cut -d '.' -f 1).js


%.js-extract-externs: %.js
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(JS_EXTERNS_EXTRACTOR) $^ > \
	$(JS_EXTERNS_PATH)/$(shell echo $@ | cut -d '.' -f 1).js


################################################################################
# GENERAL RULES
################################################################################


js: js-clean js-check js-build
	@echo $@: DONE


js-lint:
	@$(foreach DFILE, $(shell cat $(CONFIG_PATH)/js.lint), \
	make -s $(shell echo $(DFILE) | cut -d '.' -f 1).js-lint > /dev/null)
	@echo $@: DONE


js-check: js-lint
	@$(foreach TEMPLATE, $(TEMPLATES_PATH)/js/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | cut -d '.' -f 1).js-check)
	@echo $@: DONE


js-clean:
	@rm -rf $(JS_BUILD_PATH) $(JS_EXTERNS_PATH)
	@rm -rf $(shell find $(MODULES_PATH) -maxdepth 1 \
	-not -name livetex-tools -not -name node_modules)
	@echo $@: DONE


js-build: js-clean js-check
	@mkdir -p $(JS_BUILD_PATH)
	@$(foreach TEMPLATE, $(TEMPLATES_PATH)/js/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | cut -d '.' -f 1).js-assemble)
	@$(foreach TEMPLATE, $(TEMPLATES_PATH)/js/*, make -s $(shell echo \
	$(TEMPLATE) | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js-extract-externs)
	@echo $@: DONE


publish: js-build
	@npm publish
	@echo $@: DONE
