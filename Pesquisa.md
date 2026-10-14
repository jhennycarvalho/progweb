# Pesquisa Teórica — Git e GitHub

* **Branches e Troca de Branches**: Branches são ramificações isoladas do código. Para trocar, usa-se `git checkout <nome-branch>` ou `git switch <nome-branch>`.
* **Share Push**: O comando `git push origin <branch>` envia os commits locais para o servidor remoto.
* **Reescrever Commit**: Utiliza-se `git commit --amend` para ajustar a mensagem ou arquivos do último commit local.
* **Revert vs Merge**: O `git revert` cria um novo commit que anula alterações passadas sem apagar o histórico. O `git merge` une duas branches em uma só.
* **Stage (Staging Area)**: Área intermediária onde os arquivos alterados são preparados (`git add`) antes do commit.
* **Squash**: Combina múltiplos commits em um único commit mais limpo.
* **Reflog**: Registro de movimentações no Git que permite recuperar commits perdidos (`git reflog`).
* **Reset vs Clean**: O `git reset` restaura o estado de arquivos rastreados; o `git clean` apaga arquivos não rastreados do diretório.