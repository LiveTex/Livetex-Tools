

################################################################################
# PATHS
################################################################################


# PROJECT PATHS ################################################################


CSS_BUILD_PATH      ?= $(PROJECT_PATH)/public/css
CSS_SOURCES_PATH    ?= $(PROJECT_PATH)/css


# PREREQUISITES PATHS ##########################################################


vpath %.csst        $(TEMPLATES_PATH)/css
vpath %.cssd        $(SOURCES_LISTS_PATH)/css
vpath %.css         $(CSS_BUILD_PATH)


################################################################################
# VARS
################################################################################


# TOOLS ########################################################################


CSS_COMPILER        ?= java -jar $(TOOLS_PATH)/tools/closure-stylesheets.jar


# NAMES ########################################################################


CSS_TEMPLATES       ?= $(foreach FILE, \
                       $(shell find $(TEMPLATES_PATH)/css -maxdepth 1 \
                       -iname '*.csst'), \
                       $(shell basename $(FILE) | cut -d '.' -f 1))
