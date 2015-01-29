

include $(TOOLS_PATH)/rules/var/all.mk


all: js


set-version:
	@$(REVERSIONER)
	@echo $@: DONE


npm-publish:
	@npm login --loglevel=silent
	@npm ls 1> /dev/null
	@npm publish --loglevel=silent
	@echo $@: DONE


publish: | js-check js set-version npm-publish
  @echo $@: DONE


web-publish: | js-lint js set-version npm-publish
  @echo $@: DONE
