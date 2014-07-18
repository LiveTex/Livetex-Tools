

%.js-deps-headers:
	@echo $(foreach DIR, $(wildcard $(MODULES_PATH)/*), \
	$(wildcard $(DIR)/externs/*.js)) > $@


%.js-node-headers:
	@echo $(foreach FILE, $(wildcard $(ENV_EXTERNS_PATH)/node/*), $(FILE)) > $@


%.jsh-node: %.js-node-headers %.js-deps-headers
	@cat $(shell cat $^ < /dev/null) > $@


%.jsh-web:
	@echo $(foreach FILE, $(wildcard $(ENV_EXTERNS_PATH)/browser/*), cat $(FILE)) > $@


################################################################################


%.js-compile-advanced: %.jsd %.jsh-node
	@$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


%.js-web-compile-advanced: %.jsd %.jsh-web
	@$(JS_COMPILER) \
	--compilation_level ADVANCED_OPTIMIZATIONS \
	--js        $(foreach FILE, $(shell cat $<), $(JS_SOURCES_PATH)/$(FILE)) \
	--externs   $(shell echo "$^" | cut -d " " -f 2)


################################################################################


%.js-lint: %.jsd
	@$(JS_LINTER) \
	$(foreach FILE, $(shell cat $^), $(JS_SOURCES_PATH)/$(FILE)) 1> /dev/null


%.js-check: %.jst
	@$(TEMPLATER) -a True $< > /dev/null
	@echo CHECKED: $(shell echo $@ | cut -d '.' -f 1).js


%.js-assemble: %.jst
	@mkdir -p $(JS_BUILD_PATH)
	$(TEMPLATER) $< > \
	$(JS_BUILD_PATH)/$(shell echo $(shell basename $<) | cut -d '.' -f 1).js


%.js-extract-externs: %.js
	@mkdir -p $(JS_EXTERNS_PATH)
	@$(JS_EXTERNS_XTRACTOR) $< > \
	$(JS_EXTERNS_PATH)/$(shell basename $<)


%.js-test: %.js
	@node --eval "require('$^').test.run('$(names)')"

