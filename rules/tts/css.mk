

%.css-compile: %.cssd
	$(CSS_COMPILER) $(foreach FILE, $(shell cat $<), $(CSS_SOURCES_PATH)/$(FILE))

