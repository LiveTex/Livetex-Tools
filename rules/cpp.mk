


################################################################################
# VARIABLES
################################################################################


# PROJECT PATHS ################################################################

PROJECT_PATH        ?= $(shell pwd)
CPP_BUILD_PATH      ?= $(PROJECT_PATH)/bin
GIP_BUILD_PATH      ?= $(PROJECT_PATH)/build
CPP_NODES_PATH      ?= $(GIP_BUILD_PATH)/Release
MODULES_PATH        ?= $(PROJECT_PATH)/node_modules
TOOLS_PATH          ?= $(MODULES_PATH)/livetex-tools
ENV_EXTERNS_PATH    ?= $(TOOLS_PATH)/externs


# ENVIRONMENT ##################################################################


# AUX VARS #####################################################################

CPP_NODES           ?= $(foreach FILE, \
                       $(shell find $(CPP_NODES_PATH) -maxdepth 1 \
                       -iname '*.node'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))


# PREREQUISITES PATHS ##########################################################


################################################################################
# TOOLS
################################################################################


################################################################################
# RULES
################################################################################

################################################################################
# AUX RULES ####################################################################

%.node:
	@mkdir -p $(CPP_BUILD_PATH)
	@cp $(GIP_BUILD_PATH)/Release/$@ $(CPP_BUILD_PATH)/$@


#################################################################### AUX RULES #
################################################################################


################################################################################
# MAIN RULES ###################################################################


################################################################### MAIN RULES #
################################################################################


################################################################################
# GENERAL RULES ################################################################


cpp: cpp-clean cpp-build
	@echo $@: DONE


cpp-build:
	@mkdir -p $(CPP_BUILD_PATH)
	@$(foreach TARGET_NAME, $(CPP_NODES), \
	$(MAKE) -s $(shell echo $(TARGET_NAME).node);)
	@rm -rf $(GIP_BUILD_PATH)
	@echo $@: DONE


cpp-clean:
	@$(foreach TARGET_NAME, $(CPP_NODES), \
	rm -f $(shell echo $(TARGET_NAME).node);)
	@echo $@: DONE


################################################################ GENERAL RULES #
################################################################################
