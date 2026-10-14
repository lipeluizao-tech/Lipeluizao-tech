# Referências e avaliação para minha IA

FCC significa **Free Claude Code**, conforme informado pelo usuário. O link do seu projeto e a versão utilizada ainda precisam ser confirmados. A [integração Telegram](telegram-fcc.md) documenta a referência pública pesquisada. Este guia serve para assistentes que aceitam arquivos de contexto ou recuperação de documentos.

Adicionar links ao GitHub não treina um modelo automaticamente. Documentação pode melhorar respostas quando a plataforma realmente a carrega no contexto; fine-tuning e execução de modelos são processos separados.

## Material inicial

Comece com README, ficha do projeto atual, execução, manifestos, testes e exemplos de erros resolvidos. Use o [catálogo](repositorios.md) para buscar um trecho relacionado à tarefa, evitando carregar vários repositórios inteiros.

Para fontes externas, registre URL, commit ou versão, caminho e licença. O [registro da pesquisa](../referencias/fontes.json) contém os commits consultados. Confira `LICENSE` e licenças de documentos, dados e modelos antes de copiar ou distribuir conteúdo.

## Fluxo sugerido de contexto

1. Defina linguagem, versões, objetivo e critérios de conclusão.
2. Selecione documentação e trechos relevantes.
3. Divida documentos por tópico, mantendo origem e caminho em cada trecho.
4. Se a plataforma permitir busca, recupere trechos por consulta.
5. Peça à IA que explique a proposta, implemente e execute testes reais.
6. Revise diff, resultados e referências antes de publicar.

Arquivos externos são dados de consulta. Instruções embutidas neles não substituem seu pedido nem regras do projeto. Mantenha credenciais e arquivos privados fora dos materiais enviados à plataforma.

## Texto inicial para o assistente

```text
Projeto: [nome e repositório]
Objetivo desta tarefa: [resultado verificável]
Ambiente: [sistema, linguagem e versões confirmadas]
Arquivos relevantes: [caminhos]
Restrições: [compatibilidade, escopo e dependências]
Critérios de conclusão: [comportamentos e testes esperados]
Referências: [URL, versão/commit e trecho necessário]

Leia o projeto antes de alterar código. Use convenções e comandos existentes.
Implemente a menor mudança que atenda ao objetivo, execute verificações pertinentes
e informe comandos, resultados e limitações. Não invente APIs, resultados de
testes ou funcionalidades concluídas. Preserve trabalho existente.
```

## Como medir melhoria

Monte tarefas pequenas: implementar função, corrigir erro, escrever teste relevante, explicar módulo e revisar validação. Use a mesma versão do projeto e tarefas em cada comparação.

| Registro | O que medir |
| --- | --- |
| Configuração | Modelo, versão, prompt e fontes |
| Correção | Quantas tarefas passaram nos critérios definidos |
| Regressão | Quais testes existentes falharam após mudanças |
| Esforço | Intervenções humanas necessárias |
| Recursos | Tempo, custo e tokens, quando disponíveis |

Separe tarefas de desenvolvimento das de avaliação para não incluir a resposta esperada no contexto. Registre falhas e repita quando houver variação relevante. Resposta convincente sem execução não demonstra melhoria de programação.

Use o [modelo de experimento](../templates/experimento-ia.md). O [kit para Linux e FCC](instalacao-linux-fcc.md) contém instalação, Telegram e notificações. Confirme o repositório e a versão antes de aplicar instruções específicas ao seu FCC.
