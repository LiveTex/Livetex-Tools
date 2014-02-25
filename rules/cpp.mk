


################################################################################
# VARIABLES
################################################################################


# PATHS ########################################################################


PROJECT_PATH      ?= $(shell pwd)
CPP_BUILD_PATH    ?= $(PROJECT_PATH)/bin
GIP_BUILD_PATH    ?= $(PROJECT_PATH)/build
CPP_NODES_PATH    ?= $(GIP_BUILD_PATH)/Release
MODULES_PATH      ?= $(PROJECT_PATH)/node_modules
TOOLS_PATH        ?= $(MODULES_PATH)/livetex-tools
ENV_EXTERNS_PATH  ?= $(TOOLS_PATH)/externs


# TOOLS ########################################################################


# ENVIRONMENT ##################################################################


################################################################################
# AUX RULES
################################################################################


%.node:
	cp $(GIP_BUILD_PATH)/Release/$@ $(CPP_BUILD_PATH)


################################################################################
# MAIN RULES
################################################################################


################################################################################
# GENERAL RULES
################################################################################


cpp: cpp-clean cpp-build
	@echo $@: DONE


cpp-build:
	@mkdir -p $(CPP_BUILD_PATH)
	@$(foreach FILE, \
	$(shell find $(CPP_NODES_PATH) -maxdepth 1 -iname '*.node'), \
	make -s $(shell echo $(FILE) | rev | cut -d '/' -f 1 | rev))
	@rm -rf $(GIP_BUILD_PATH)
	@echo $@: DONE


cpp-clean:
	@rm -f $(wildcard $(CPP_BUILD_PATH)/*.node)
	@echo $@: DONE
