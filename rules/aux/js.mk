

%.js-deps-headers:
	@echo $(foreach DIR, $(MODULES), \
	$(wildcard $(DIR)/externs/*.js)) > $@

%.js-vendor-headers:
	@echo $(wildcard $(VENDOR_EXTERNS_PATH)/*.js) > $@

%.js-node-headers:
	echo $(foreach FILE, $(wildcard $(NODE_EXTERNS_PATH)/*), $(FILE)) > $@


%.jsh-node: %.js-node-headers %.js-deps-headers %.js-vendor-headers
	@cat $(shell cat $^ < /dev/null) > $@


################################################################################


%.js-compile-advanced: %.jsd %.jsh-node
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


%.chmod:
	@$(foreach FILE, $(wildcard $(JS_BUILD_PATH)/*), \
	if grep -Rq "#\!/" $(FILE) ; then \
		chmod +x $(FILE) ; \
	fi)
