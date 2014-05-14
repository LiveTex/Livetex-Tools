

%.js-lint: %.jsd
	@$(JS_LINTER) \
	$(foreach FILE, $(shell cat $^), $(JS_SOURCES_PATH)/$(FILE)) 1> /dev/null


%.js-check: %.jst
	@$(TEMPLATER) -a True $< > /dev/null


%.js-assemble: %.jst
	@mkdir -p $(JS_BUILD_PATH)
	@$(TEMPLATER) $< > \
	$(JS_BUILD_PATH)/$(shell echo $(shell basename $<) | cut -d '.' -f 1).js


%.js-extract-externs: %.js
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(JS_EXTERNS_XTRACTOR) $< > \
	$(JS_EXTERNS_PATH)/$(shell basename $<)


%.js-test: %.js
	@node --eval "require('$^').test.run('$(names)')"

