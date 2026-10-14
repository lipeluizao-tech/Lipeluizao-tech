# Documentar projetos desde o primeiro dia

Documentação útil permite que outra pessoa entenda o problema, execute o código e confira o resultado.

## Primeiro registro

Use o [modelo](../templates/projeto.md). Descreva problema, público, uma entrega pequena e critérios de conclusão. Informe ferramentas realmente usadas; identifique decisões pendentes.

No repositório do aplicativo, mantenha:

- `README.md`: objetivo, requisitos, instalação, execução e testes.
- Exemplo de configuração, como `.env.example`, com nomes e valores fictícios.
- Testes relevantes, arquivos de dependências e lockfiles apropriados.
- Licença escolhida pelo autor, quando aplicável.

## A cada sessão

Preencha o [diário](../templates/diario.md) com objetivo, mudanças, comandos executados e resultados. Inclua o erro observado quando um teste falhar. Se não houver teste, registre “não executado”.

Antes de publicar, confira `git diff` e `git diff --cached`. Revise configurações e capturas de tela para evitar exposição de chaves, senhas ou dados pessoais.

## A cada entrega

Registre commit ou release da versão demonstrada, instruções reproduzíveis e uma captura ou exemplo de entrada e saída. Explique uma decisão técnica e uma limitação relevante.

Atualize o [catálogo](../projetos/README.md), mantendo ideias separadas de projetos executáveis. Ao usar tutorial ou código externo, cite a origem e explique sua contribuição.

## Rotina de Git

```bash
git status
git diff
# Substitua pelo caminho do arquivo que deseja incluir.
git add caminho/do/arquivo
git diff --cached
git commit -m "docs: registrar entrega do projeto"
```

O commit registra trabalho localmente. O envio ao GitHub é separado, usando o remoto e a branch corretos.
