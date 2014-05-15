

include $(TOOLS_PATH)/rules/var/all.mk


versions:
	@$(REVERSIONER)
	@echo $@: DONE


set-version:
	@$(REVERSIONER) -I True
	@echo $@: DONE


commit-version:
	@$(REVERSIONER) -C True
	@echo $@: DONE


npm-publish:
	@npm login --loglevel=silent
	@npm ls 1> /dev/null
	@npm publish --loglevel=silent
	@echo $@: DONE


npm-modules:
  @npm --loglevel=silent update > /dev/null
  @echo $@: DONE


git-modules:
	@git submodule update --init > /dev/null
	@$(foreach SUBMODULE, $(SUBMODULES), \
	cd $(SUBMODULE); $(MAKE) -s js; cd -;)
	@echo $@: DONE


publish: | js-check js set-version npm-publish commit-version
	@echo $@: DONE

