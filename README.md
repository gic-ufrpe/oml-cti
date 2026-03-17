## Ontologia de CT&I com OML

Este repositório contém a ontologia de **Ciência, Tecnologia e Inovação (CT&I)** do GIC/UFRPE (Disciplina de Gestão da Informação e do Conhecimento, UFRPE), modelada em **OML (Ontological Modeling Language)** e processada com as ferramentas do projeto **openCAESAR**.

A ontologia descreve, entre outros elementos:

- programas de pós-graduação (conceito `PPG`)
- instituições de ciência e tecnologia (`ICT`)
- conceitos de avaliação da CAPES (`Conceito_PPG`)
- pessoas envolvidas (`Pessoa`, `Discente`, `Docente`, `Autor`)
- produções científicas (`Producao_Cientifica`) e seus veículos de publicação (`Veiculo_Publicacao`)
- métricas de impacto e citação (`Citacao`)

Esses conceitos estão definidos principalmente em `src/oml/gic.ufrpe.br/vocabulary/cti.oml` e serão usados para consultas e análises sobre CT&I.

Para editar e validar esta ontologia usaremos **OML Rosetta**, mas boa parte das instruções também vale para outros projetos OML baseados em Gradle.

A figura abaixo apresenta uma visão geral do modelo conceitual de CT&I usado neste projeto:

![Visão geral do modelo CTI](docs/images/0-modelo-cti.png)

---

## Índice

- [Como funciona este projeto OML](#como-funciona-este-projeto-oml)
- [Preparação do ambiente (Rosetta e workspace)](docs/preparacao.md)
- [Tutorial 1 – OML Basics (CTI)](docs/tutorial1-cti.md)
 - [Tutorial 2 – Modelagem gráfica com Sirius (CTI)](docs/tutorial2-sirius-cti.md)

---

## Como funciona este projeto OML

Projetos OML criados pelo openCAESAR são projetos **Gradle**. Neste caso, o artefato principal é a ontologia de CT&I (`cti`), descrita em OML e convertida para OWL durante o *build*.

As ferramentas de análise e transformação (conversão OML→OWL, raciocínio, carga em Fuseki, execução de consultas SPARQL etc.) são executadas como *tasks* Gradle definidas em `build.gradle`.

Essas tarefas podem ser executadas de duas formas:

1. **Pela interface gráfica do editor**  
	Exemplo: pelo painel **Gradle Tasks** no Eclipse/Rosetta.
2. **Pelo terminal**, usando o Gradle Wrapper:

	```bash
	./gradlew <task>
	```

No caso deste projeto, as tarefas Gradle mais importantes (que são usadas no Tutorial 1) incluem:

- `omlToOwl` – converte os modelos OML em OWL
- `owlReason` – roda o raciocinador DL e gera [build/reports/reasoning.xml](build/reports/reasoning.xml)
- `owlLoad` e `owlQuery` – carregam a ontologia em um dataset Fuseki e executam consultas SPARQL
- tarefas do grupo `oml` como `startFuseki` e `stopFuseki`, usadas para iniciar/parar o servidor Fuseki local

Os detalhes passo a passo de preparação do ambiente e do Tutorial 1 estão separados nos arquivos da pasta `docs/`, conforme o índice acima.