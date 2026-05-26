Início de um Repositório

    git init: -----Transforma a pasta atual em um repositório Git.

    git branch -M main: -----Renomeia a ramificação principal para main.

    git remote add origin URL_DO_REPOSITORIO: -----Conecta a sua pasta local ao repositório vazio que você criou lá no site do GitHub.

Ciclo Diário de Trabalho

    git status: -----Mostra quais arquivos foram modificados, criados ou deletados. Use sempre para saber o que está acontecendo.

    git add .: -----Prepara todas as alterações da pasta para serem salvas. Se quiser adicionar apenas um arquivo específico, use git add nome-do-arquivo.py.

    git commit -m "Mensagem explicativa": -----Salva oficialmente as alterações no histórico do seu computador, criando um ponto de restauração com uma mensagem descritiva.

Sincronização com o GitHub (Nuvem)

    git push -u origin main: -----Envia seus commits locais para o GitHub pela primeira vez (o -u configura o destino padrão). Nas próximas vezes, basta usar apenas git push.

    git pull origin main: -----Traz todas as novidades do GitHub para o seu computador (fundamental rodar antes de começar a programar se você mexe no projeto de outro lugar).

    git clone URL_DO_REPOSITORIO: -----Baixa um projeto inteirinho do GitHub para o seu PC do zero (cria a pasta e baixa todos os arquivos automaticamente).

Desfazendo Besteiras (Para emergências)

    git log --oneline: -----Mostra a lista dos seus últimos commits de forma resumida (útil para ver o histórico).

    git checkout nome-do-arquivo.py: -----Descarta as alterações feitas em um arquivo desde o seu último commit (limpa as bobagens que você testou e deram errado).