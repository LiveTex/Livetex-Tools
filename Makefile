

publish:
	@npm version patch
	@npm login
	@npm publish
	@git push
	@echo $@: DONE
