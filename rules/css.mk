

include $(TOOLS_PATH)/rules/var/css.mk
include $(TOOLS_PATH)/rules/tts/css.mk
include $(TOOLS_PATH)/rules/aux/css.mk


css-clean:
	@#rm -rf $(wildcard $(CSS_BUILD_PATH)/*.css)
	@rm -rf $(shell find $(CSS_BUILD_PATH) -maxdepth 1 \
	-not -name mobile-invite.css -not -name css)
	@echo $@: DONE


css-build: css-clean
	@mkdir -p $(CSS_BUILD_PATH)
	@$(foreach TARGET_NAME, $(CSS_TEMPLATES), \
	$(MAKE) -s $(TARGET_NAME).css-assemble;)
	@echo $@: DONE


css: | css-clean css-build
	@echo $@: DONE
