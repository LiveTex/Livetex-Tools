

publish:
	@npm version patch
	@npm login
	@npm publish

	@#TMP
	@#git push

	@echo $@: DONE