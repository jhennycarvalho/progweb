Pesquisa — Controle de versões com Git/GitHub
 ===== Atividade do AVA =====
1. O que são branches e como trocar de branch

Uma branch (ramo) é uma linha independente de desenvolvimento. Na prática, é apenas um ponteiro leve para um commit.  
Ela permite trabalhar numa funcionalidade ou correção sem afetar a branch principal (main/master).

git branch                  # lista as branches locais
git branch nova-feature     # cria uma branch
git switch nova-feature     # troca de branch (forma moderna)
git checkout nova-feature   # troca de branch (forma antiga)
git switch -c nova-feature  # cria e já troca
git branch -d nova-feature  # apaga (só se já foi mergeada)


2. Como fazer share push ? 

O push envia seus commits locais para o repositório remoto.

git push origin main                  # envia a branch main
git push -u origin nova-feature       # primeiro push; -u vincula a branch local à remota
git push                              # depois do -u, basta isso


3. Como reescrever commit?

Alterar a mensagem do último commit	--- > git commit --amend -m "nova mensagem"
Adicionar arquivo esquecido ao último commit	------> git add arquivo e depois git commit --amend --no-edit
Reescrever vários commits	------> git rebase -i HEAD~3

No rebase -i, escolhe-se uma ação por commit: 
reword (muda mensagem), edit (altera conteúdo), squash/fixup (junta), drop (remove) e pode reordenar as linhas.

4. As diferenças entre revert e merge.

Os dois têm objetivos diferentes, não são alternativas um do outro.

git merge <branch>: integra o histórico de outra branch na atual, juntando o trabalho de ambas. Pode gerar um merge commit e conflitos.
git revert <commit>: cria um novo commit que desfaz as mudanças de um commit anterior, sem apagar o histórico. É a forma segura de desfazer algo já publicado.


git merge feature        # traz a feature para a branch atual
git revert a1b2c3d       # desfaz o commit a1b2c3d com um novo commit

5.O que é stage (staging área) ? 

É uma área intermediária entre o diretório de trabalho e o commit. O usuário escolhe exatamente o que entrará no próximo commit.

Ex: Working directory  --git add-->  Staging area  --git commit-->  Repositório


git add arquivo.txt        # coloca no stage
git add -p                 # escolhe trechos específicos
git restore --staged arquivo.txt   # tira do stage
git status                 # mostra o que está em cada área

OBS: Isso permite dividir várias alterações em commits pequenos e organizados.



6• Para que serve squash de commit? 

O squash combina vários commits em um só. É útil para limpar o histórico, por exemplo transformar "wip", "corrige typo" e "ajuste" em um único commit coerente antes de abrir um pull request.
git rebase -i HEAD~4     # marque os commits seguintes como "squash" (ou "s")
git merge --squash feature   # traz as mudanças da branch como um único commit

7• Para que serve reflog? 
O reflog registra todos os movimentos do HEAD localmente (commits, resets, rebases, trocas de branch), mesmo os que não aparecem no git log. 
Ele é a sua "rede de segurança" para recuperar trabalho aparentemente perdido.

git reflog                       # lista o histórico de movimentos
git reset --hard HEAD@{2}        # volta ao estado de 2 movimentos atrás
git branch recuperada a1b2c3d    # recria uma branch num commit "perdido"


8• Diferenças entre reset e clean.


8. Diferenças entre reset e clean

Atuam em coisas diferentes:

git reset mexe em arquivos rastreados (que o Git já conhece) e no histórico/stage.
git clean remove arquivos não rastreados (novos, que nunca foram adicionados).

git reset --soft HEAD~1	Desfaz o commit, mantém as mudanças no stage
git reset --mixed HEAD~1 (padrão)	Desfaz o commit, mantém as mudanças fora do stage
git reset --hard HEAD~1	Desfaz o commit e descarta as mudanças
git clean -n	Simula (mostra o que seria apagado)
git clean -f	Apaga arquivos não rastreados
git clean -fd	Apaga também diretórios não rastreados

Ambos podem causar perda de dados sem volta. Tem   que executar sempre git clean -n antes e usar reset --hard com cuidado.



