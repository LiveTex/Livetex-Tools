

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


modules:
	@rm -rf $(MODULES_PATH)
	@npm --loglevel=silent i > /dev/null
	@if [ $(wildcard $(PROJECT_PATH)/.gitmodules) ] ; \
	then \
		git submodule update --init ; \
	fi;
	@echo $@: DONE


publish: | js-check js set-version npm-publish commit-version
	@echo $@: DONE

