


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
BACKPORTS_PATH      ?= $(TOOLS_PATH)/rules/backports


# VARS #########################################################################


JS_LINT             ?= $(shell ls $(SOURCES_LISTS_PATH)/js)
JS_EXTERNS          ?= $(shell ls $(wildcard $(JS_BUILD_PATH)) | \
                                  rev | cut -d '/' -f 1 | rev )


# TOOLS ########################################################################


JS_COMPILER ?= java -jar $(TOOLS_PATH)/tools/closure-compiler.jar \
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


vpath %.jst   $(TEMPLATES_PATH)/js
vpath %.jsd   $(SOURCES_LISTS_PATH)/js
vpath %.js    $(JS_BUILD_PATH)


################################################################################
# AUX RULES
################################################################################


# HEADERS ######################################################################


%.jsh: %.js-env-headers %.js-custom-headers %.js-headers
	@cat `cat $^ < /dev/null` > $@


%.js-headers:
	@echo $(foreach DIR, $(wildcard $(MODULES_PATH)/*), \
	$(wildcard $(DIR)/externs/*.js)) > $@


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
	--js          $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \


# COMPRESSED COMPILATIONS ######################################################


%.js-externs-compile-compressed: %.jsd %.jsh
	@$(JS_COMPILER) \
	--js          $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs     $(shell echo "$^" | cut -d " " -f 2)


# ADVANCED COMPILATION #########################################################


%.js-externs-compile-advanced: %.jsd %.jsh
	$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js          $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs     $(shell echo "$^" | cut -d " " -f 2)


################################################################################
# MAIN RULES
################################################################################


%.js-lint: %.jsd
	@$(JS_LINTER) $(foreach FILE, $(shell cat $^), $(JS_SOURCES_PATH)/$(FILE))


%.js-check: %.jst
	@$(TEMPLATER) -a True $< > /dev/null


%.js-assemble: %.jst
	@mkdir -p $(JS_BUILD_PATH)
	@$(TEMPLATER) $< > \
	$(shell echo $(JS_BUILD_PATH)/$(shell basename $<) | cut -d '.' -f 1).js


%.js-extract-externs: %.js
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(JS_EXTERNS_EXTRACTOR) $< \
	> $(JS_EXTERNS_PATH)/$(shell echo $< | rev | cut -d '/' -f 1 | rev)


################################################################################
# GENERAL RULES
################################################################################


all:
	test -d $(TEMPLATES_PATH) || $(MAKE) -f $(BACKPORTS_PATH)/Makefile $@ && \
	exit 0


js: js-build js-externs
	@echo $@: DONE


js-lint:
	@$(foreach DFILE, $(JS_LINT), \
	$(MAKE) -s $(shell echo $(DFILE) | cut -d '.' -f 1).js-lint > /dev/null)
	@echo $@: DONE


js-check: js-lint
	@$(foreach TEMPLATE, $(wildcard $(TEMPLATES_PATH)/js/*), \
	$(shell $(MAKE) -s $(shell echo $(TEMPLATE) | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js-check))
	@echo $@: DONE


js-externs:
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(foreach FILE, $(JS_EXTERNS), $(MAKE) -s $(FILE)-extract-externs)
	@echo $@: DONE


js-build: js-clean js-check
	@mkdir -p $(JS_BUILD_PATH)
	$(foreach TEMPLATE, $(wildcard $(TEMPLATES_PATH)/js/*), \
	$(shell $(MAKE) -s $(shell echo $(TEMPLATE) | rev | cut -d '/' -f 1 | rev | \
	cut -d '.' -f 1).js-assemble))
	@echo $@: DONE


js-clean:
	@rm -rf $(wildcard $(JS_BUILD_PATH)/*.js) $(JS_EXTERNS_PATH)
	@echo $@: DONE


publish: js-build
	@npm version patch
	@npm login
	@npm publish
	@git push
	@echo $@: DONE

