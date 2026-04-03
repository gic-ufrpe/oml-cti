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
- [Data Acquisition – Exemplo prático (gerador OML a partir de CAPES CSV)](#exemplo-data-acquisition-capes)

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

Principais tarefas utilizadas:

- `omlToOwl` – converte OML para OWL  
- `owlReason` – executa raciocínio DL  
- `owlLoad` / `owlQuery` – carga e consulta SPARQL  
- `startFuseki` / `stopFuseki` – controle do servidor  

---

## Exemplo: Data Acquisition (CAPES)

Uma das etapas do ciclo KM trabalhadas neste projeto é a **aquisição de dados** (*data acquisition*). Para isso, foi implementado um exemplo prático utilizando dados abertos da CAPES.

Além da ontologia em si, o repositório inclui scripts que mostram como sair de dados tabulares (CSV) e chegar em instâncias OML aderentes ao modelo.

O script principal está em:
👉 `scripts/generate_oml_from_capes.py`

Ele realiza um fluxo completo:

1. leitura dos dados da CAPES (CSV)  
2. filtragem e limpeza (ex.: programas de PE)  
3. extração das entidades do modelo (ICT, PPG, Conceito_PPG)  
4. geração do arquivo OML com instâncias (`cti-pe.oml`)  

A pasta `scripts/` concentra esse material, incluindo instruções de execução e explicação do pipeline.

Consulte:
👉 [scripts/README.md](scripts/README.md)

A ideia é deixar claro o caminho entre:

- dados brutos  
- processamento  
- instâncias da ontologia  
