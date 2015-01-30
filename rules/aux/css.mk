

%.css-assemble: %.csst
	@mkdir -p $(CSS_BUILD_PATH)
	$(TEMPLATER) $< > \
	$(shell echo $(CSS_BUILD_PATH)/$(shell basename $<) | cut -d '.' -f 1).css

