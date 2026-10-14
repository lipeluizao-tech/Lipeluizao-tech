# Repositórios para aprender e construir

Foram consultados os READMEs oficiais dos 15 repositórios abaixo. Os commits e URLs consultados estão em [fontes.json](../referencias/fontes.json). A seleção considera finalidade e aplicação nos estudos; não é ranking por estrelas nem auditoria de segurança. Os programas não foram instalados ou testados nesta pesquisa.

## Programação e fundamentos

| Repositório | Por que estudar | Atividade sugerida |
| --- | --- | --- |
| [freeCodeCamp/freeCodeCamp](https://github.com/freeCodeCamp/freeCodeCamp) | Plataforma e currículo aberto de desenvolvimento web e outros temas | Concluir uma unidade e criar uma aplicação própria com o aprendizado |
| [TheAlgorithms/Python](https://github.com/TheAlgorithms/Python) | Implementações de algoritmos em Python | Estudar busca ou ordenação, implementar sem copiar e testar entradas vazias e repetidas |
| [ossu/computer-science](https://github.com/ossu/computer-science) | Currículo organizado de ciência da computação | Escolher um curso introdutório e registrar exercícios e conceitos |
| [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning) | Tutoriais organizados por linguagem para construir aplicações | Escolher um projeto pequeno, adaptar o problema e explicar sua contribuição |

Comece pelo currículo ou por uma aplicação pequena. Clonar a plataforma inteira do freeCodeCamp não é necessário para estudar seus cursos. Verifique requisitos e custo dos cursos externos indicados pelo OSSU.

## Cibersegurança e desenvolvimento seguro

| Repositório | Por que estudar | Atividade sugerida |
| --- | --- | --- |
| [OWASP/CheatSheetSeries](https://github.com/OWASP/CheatSheetSeries) | Recomendações para proteger aplicações | Usar o [site oficial das cheat sheets](https://cheatsheetseries.owasp.org/) para revisar validação, autenticação e controle de acesso em um projeto próprio |
| [juice-shop/juice-shop](https://github.com/juice-shop/juice-shop) | Aplicação intencionalmente vulnerável para aprendizagem | Fazer um exercício local e documentar causa, impacto e correção proposta |
| [WebGoat/WebGoat](https://github.com/WebGoat/WebGoat) | Lições práticas sobre falhas em aplicações web | Estudar uma lição e explicar como testar a proteção equivalente em código próprio |
| [mitmproxy/mitmproxy](https://github.com/mitmproxy/mitmproxy) | Proxy interativo para observar tráfego HTTP/HTTPS | Inspecionar requisições da sua aplicação com dados fictícios |
| [semgrep/semgrep](https://github.com/semgrep/semgrep) | Análise estática baseada em padrões | Criar uma regra simples para código próprio, conferir achados e falsos positivos |

Juice Shop e WebGoat são vulneráveis de propósito: use um laboratório local isolado, sem expor portas à rede pública. Ao mapear portas de containers, prefira vínculo explícito a `127.0.0.1`. Pratique apenas em sistemas próprios ou autorizados. Requisitos de Java, Node e imagens variam por release; siga as instruções da versão escolhida.

Semgrep ajuda na revisão, mas achados precisam de análise e uma execução sem alertas não prova ausência de vulnerabilidades. Para mitmproxy, entenda o escopo da CA de laboratório e remova a confiança temporária ao terminar.

## IA e assistência à programação

| Repositório | Papel | Atividade sugerida |
| --- | --- | --- |
| [huggingface/transformers](https://github.com/huggingface/transformers) | Biblioteca para trabalhar com modelos, incluindo inferência e treinamento | Executar um exemplo pequeno compatível com o hardware e registrar modelo e resultado |
| [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | Inferência de modelos em C/C++ com opções para diferentes hardwares | Estudar quantização e medir tempo e memória em uma tarefa pequena |
| [ollama/ollama](https://github.com/ollama/ollama) | Ferramentas para utilizar modelos e integrar aplicações | Experimentar um modelo adequado à RAM e avaliar respostas nas mesmas tarefas |
| [Aider-AI/aider](https://github.com/Aider-AI/aider) | Assistente de programação pelo terminal | Aplicar uma alteração pequena em projeto próprio e revisar diff e testes |

O código do motor e os pesos dos modelos podem ter licenças distintas. Confira memória, armazenamento, privacidade e custos de APIs antes de escolher. A instalação de uma ferramenta ou o cadastro de links não treina sua IA; o [guia de contexto e avaliação](ia-contexto.md) explica como verificar melhoria.

## Ferramentas do ambiente

| Repositório | Finalidade | Uso sugerido |
| --- | --- | --- |
| [microsoft/vscode](https://github.com/microsoft/vscode) | Código-fonte do Code - OSS, base do VS Code | Consultar documentação do editor e preparar execução e depuração; a distribuição VS Code tem licença própria |
| [nvm-sh/nvm](https://github.com/nvm-sh/nvm) | Gerenciamento de versões do Node.js | Usar a versão exigida por cada projeto e registrar o requisito |

## Como aproveitar as referências

1. Escolha uma habilidade e uma tarefa concreta.
2. Leia o README e requisitos da versão selecionada.
3. Consulte `LICENSE` e orientações de contribuição antes de reutilizar conteúdo.
4. Execute exemplos em ambiente separado, sem dados privados.
5. Registre seu resultado na [ficha de projeto](../templates/projeto.md) ou no [diário](../templates/diario.md).

Links mantêm referências acessíveis. Um fork é útil quando você pretende estudar alterações ou contribuir; mantenha a autoria e licença originais. Registre seu trabalho próprio separadamente para que o portfólio mostre o que você construiu.

## Atualização da biblioteca

Ao adicionar uma fonte, informe finalidade, exercício sugerido, URL e versão consultada. Reavalie os requisitos quando atualizar versões. Links externos citados pelos READMEs e guias de instalação podem mudar; a pesquisa verificou os READMEs registrados, sem conferir todas as páginas externas.
