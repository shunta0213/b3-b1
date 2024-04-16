.PHONY:
set-env:
	@tlmgr conf texmf $(KEY) $(VALUE)
	@echo '\CatchFileEdef{\\var$(KEY)}{|"kpsewhich -var-value=$(KEY)"}{\\endlinechar=-1 }' >> ./src/styles/env.sty

.PHONY:
clean:
	@rm -rf ./**/dist/
