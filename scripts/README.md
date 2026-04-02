# 📖 Script: Gerador de OML a partir de Dados CAPES

Um **pipeline didático e modular** para transformar dados tabulares (CSV) da CAPES em ontologias **OML (Ontological Modeling Language)**, demonstrando as melhores práticas em engenharia de conhecimento.

## 📚 Objetivo

Este script é ferramental didático para ensinar:

- ✅ Engenharia de dados: leitura, filtragem, normalização
- ✅ Qualidade de dados: validação, deduplicação
- ✅ Estruturas semânticas: instâncias, relações, propriedades
- ✅ Ontologias: mapeamento de dados para modelos conceituais
- ✅ Arquitetura de software: classes, responsabilidades, separação de concerns

**Dados de entrada:** 18.597 linhas (CSV de 4 anos)  
**Resultado:** 867 instâncias OML (15 ICT + 178 PPG + 674 Conceito_PPG)

---

## 🎯 Fluxo de Processamento (4 Etapas)

```
┌──────────────────────────────────────────────────────────────┐
│ ETAPA 1: Leitura de CSV Files                               │
│ • Busca dinâmica com glob() em data/raw/capes/              │
│ • Concatenação automática de múltiplos anos (2021-2024)     │
│ • Suporte a encoding ISO-8859-1 (padrão CAPES)             │
│ Resultado: 18.597 linhas
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ ETAPA 2: Filtragem e Normalização                           │
│ • Filtra apenas SG_UF_PROGRAMA == "PE" (Pernambuco)         │
│ • Remove espaços em branco (strip) de strings               │
│ • Converte tipos de dados (str → int)                       │
│ • Valida valores críticos (não-nulos)                       │
│ Resultado: 674 linhas limpas
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ ETAPA 3: Extração de Instâncias                             │
│ • Deduplicação de ICT (15 únicas por CD_ENTIDADE_CAPES)     │
│ • Deduplicação de PPG (178 únicas por CD_PROGRAMA_IES)      │
│ • Conceito_PPG: 674 (1 por ano × programa)                  │
│ • Mapeamento de relações (sediado, avaliado)                │
│ Resultado: 867 instâncias
└──────────────────────────────────────────────────────────────┘
                            ↓
┌──────────────────────────────────────────────────────────────┐
│ ETAPA 4: Geração OML                                        │
│ • Arquivo único cti-pe.oml (descrição unificada)            │
│ • Instâncias com propriedades atômicas                       │
│ • Relações semânticas estruturadas                          │
│ • Conformidade OML com URIs e namespaces                    │
│ Resultado: cti-pe.oml (50KB)
└──────────────────────────────────────────────────────────────┘
```

---

## 📂 Estrutura de Diretórios

```
oml-cti/
├── data/
│   ├── raw/
│   │   └── capes/                    ← CSV files de entrada
│   │       ├── br-capes-...-2021-*.csv
│   │       ├── br-capes-...-2022-*.csv
│   │       ├── br-capes-...-2023-*.csv
│   │       └── br-capes-...-2024-*.csv
│   │
│   └── processed/                    ← Dados processados (saída)
│       └── capes_programas_pernambuco.csv
│
├── src/oml/gic.ufrpe.br/cti/
│   └── description/                  ← Arquivo OML (saída)
│       └── cti-pe.oml
│
└── scripts/
    ├── generate_oml_from_capes.py   ← Script principal
    ├── generate_oml_from_capes.py.bkp
    └── README.md                     ← Este arquivo
```

---

## 🚀 Como Usar

### Pré-requisitos

```bash
# 1. Python 3.8+
python3 --version

# 2. Ativar ambiente virtual (se ainda não feito)
cd /Users/renatomendes/workspace-ufrpe/ciclo-km/rosetta-workspace/oml-cti
source venv/bin/activate

# 3. Instalar pandas (se ainda não feito)
pip install --only-binary :all: pandas
```

### Executar o Script

```bash
# Opção A: Com Python do venv
./venv/bin/python scripts/generate_oml_from_capes.py

# Opção B: Com ambiente ativado
python3 scripts/generate_oml_from_capes.py
```

### Saídas Esperadas

#### 📄 Console Output
```
======================================================================
 CAPES to OML Converter - Didactic Pipeline
======================================================================

[STEP 1] Reading CAPES CSV files...
2026-04-02 13:19:46,007 - INFO - Found 4 CSV files
2026-04-02 13:19:46,031 - INFO -   ✓ Loaded 4709 rows (2021)
2026-04-02 13:19:46,047 - INFO -   ✓ Loaded 4594 rows (2022)
2026-04-02 13:19:46,062 - INFO -   ✓ Loaded 4659 rows (2023)
2026-04-02 13:19:46,075 - INFO -   ✓ Loaded 4635 rows (2024)
2026-04-02 13:19:46,077 - INFO - Total rows after concatenation: 18597

[STEP 2] Filtering and normalizing data...
2026-04-02 13:19:46,080 - INFO - Filtered data for state 'PE': 18597 → 674 rows

[STEP 3] Extracting ontology instances...
2026-04-02 13:19:46,084 - INFO -   Extracted 15 unique ICT instances
2026-04-02 13:19:46,087 - INFO -   Extracted 178 unique PPG instances
2026-04-02 13:19:46,095 - INFO -   Extracted 674 Conceito_PPG instances

======================================================================
 EXTRACTION SUMMARY
======================================================================
  ICT Instances (Unique Institutions):        15
  PPG Instances (Unique Programs):             178
  Conceito Instances (Evaluations):            674
  Total Rows Processed:                        674
======================================================================

[STEP 4] Generating OML description file...
2026-04-02 13:19:46,096 - INFO - Saved: .../cti-pe.oml

PIPELINE COMPLETED SUCCESSFULLY!
Generated file in: src/oml/gic.ufrpe.br/cti/description
  - cti-pe.oml (Complete CT&I description)

Generated data file in: data/processed
  - capes_programas_pernambuco.csv
```

#### 📁 Arquivos Gerados

1. **`cti-pe.oml`** (50 KB)
   - Descrição unificada com todas as instâncias
   - Relações semânticas (sediado, avaliado)
   - Pronto para usar em triplestore

2. **`capes_programas_pernambuco.csv`** (674 linhas, 32 colunas)
   - Dados capturados durante processamento
   - Útil para verificação e análise posterior

---

## 🏗️ Arquitetura do Código

O script organiza o processamento em **4 classes principais** com responsabilidades bem definidas:

### 1️⃣ Classe `CAPESProcessor`
**O quê faz:** Lê, filtra e limpa dados  
**Responsabilidades:**
- Lê múltiplos CSVs com glob()
- Concatena DataFrames
- Filtra por estado (UF)
- Normaliza tipos e espaços
- Valida qualidade

```python
# Exemplo de uso
processor = CAPESProcessor()
processor.read_csv_files()         # 18.597 linhas
processor.filter_by_state("PE")    # 674 linhas (apenas PE)
processor.normalize_data()         # Remove espaços, converte tipos
processor.validate_data()          # Verifica valores críticos
processor.save_processed_data()    # Salva CSV processado
```

**Métodos principais:**
```python
read_csv_files()           # Concatena CSVs dinamicamente
filter_by_state(state)     # Filtra por UF
normalize_data()           # Limpa espaços, converte tipos
validate_data()            # Verifica faltantes
save_processed_data()      # Exporta CSV para data/processed/
```

---

### 2️⃣ Classe `InstanceExtractor`
**O quê faz:** Extrai e deduplicainstâncias  
**Responsabilidades:**
- Identifica entidades únicas
- Remove duplicatas
- Cria mapeamentos de relações

```python
# Exemplo de uso
extractor = InstanceExtractor(dataframe)
icts = extractor.extract_icts()            # 15 instituições
ppgs = extractor.extract_ppgs()            # 178 programas
conceitos = extractor.extract_conceitos()  # 674 avaliações
summary = extractor.get_summary()
```

**Deduplicação:**
```
ICT:         1 por CD_ENTIDADE_CAPES
PPG:         1 por CD_PROGRAMA_IES
Conceito_PPG: N por (CD_PROGRAMA_IES, AN_BASE)
              → Múltiplas avaliações por ano
```

**Métodos principais:**
```python
extract_icts()                      # Extrai 15 instituições
extract_ppgs()                      # Extrai 178 programas
extract_conceitos()                 # Extrai 674 avaliações
get_ppg_conceito_mapping()          # Mapa: PPG → [Conceitos]
```

---

### 3️⃣ Dataclasses: `@dataclass`
**O quê são:** Estruturas de dados tipadas para instâncias

```python
@dataclass
class ICTInstance:
    """Instituição de Ciência e Tecnologia"""
    id: str                     # Ex: "ict_25001"
    cd_entidade_capes: str      # Código único CAPES
    sg_entidade_ensino: str     # Sigla (ex: "UFPE")
    nm_entidade_ensino: str     # Nome completo
    sg_uf: str                  # Estado (ex: "PE")

@dataclass
class PPGInstance:
    """Programa de Pós-Graduação"""
    id: str                      # Ex: "ppg_25001019001P7"
    cd_programa_ies: str         # Código do programa
    nm_programa_ies: str         # Nome (ex: "EDUCAÇÃO")
    nm_modalidade_programa: str  # ACADÊMICO ou PROFISSIONAL
    nm_area_conhecimento: str    # Área de pesquisa
    ict_id: str                  # Referência a ICT (relação!)

@dataclass
class ConceituPPGInstance:
    """Avaliação de um PPG em um ano"""
    id: str                  # Ex: "conceito_25001019_2021"
    cd_programa_ies: str     # Qual programa?
    cd_conceito_programa: str # Conceito 1-7
    an_base_conceito: int    # Ano da avaliação
```

---

### 4️⃣ Classe `OMLGenerator`
**O quê faz:** Cria arquivo OML estruturado  
**Responsabilidades:**
- Monta arquivo OML
- Define relações (sediado, avaliado)
- Exporta para arquivo

```python
# Exemplo de uso
generator = OMLGenerator(output_dir)
content = generator.generate_cti_pe_description(
    icts, ppgs, conceitos
)
generator.save_file("cti-pe.oml", content)
```

**Relações no OML:**
```
PPG --(sediado)--> ICT
PPG --(avaliado)--> Conceito_PPG
```

---

## 📊 Exemplo de Saída - Arquivo OML

```oml
@dc:description "Descrição de elementos de Ciência..."
description <http://gic.ufrpe.br/cti/description/cti-pe#> as cti-pe {

    uses <http://purl.org/dc/elements/1.1/> as dc
    uses <http://gic.ufrpe.br/cti/vocabulary/cti#> as cti

    // ========== INSTITUIÇÕES ==========
    instance ict_25001 : cti:ICT [
        cti:cd_entidade_capes "25001"
        cti:sg_entidade_ensino "UFPE"
        cti:nm_entidade_ensino "Universidade Federal de Pernambuco"
        cti:sg_uf "PE"
    ]

    // ========== PROGRAMAS ==========
    instance ppg_25001019001P7 : cti:PPG [
        cti:cd_programa_ies "25001019001P7"
        cti:nm_programa_ies "EDUCAÇÃO"
        cti:nm_modalidade_programa "ACADÊMICO"
        cti:nm_area_conhecimento "Educação"
        cti:sediado ict_25001            ← Relação: em qual ICT?
        cti:avaliado conceito_25001019001P7_2021
        cti:avaliado conceito_25001019001P7_2022
        cti:avaliado conceito_25001019001P7_2023
    ]

    // ========== AVALIAÇÕES ==========
    instance conceito_25001019001P7_2021 : cti:Conceito_PPG [
        cti:cd_conceito_programa "5"     ← Conceito 5/7
        cti:an_base_conceito 2021        ← Ano da avaliação
    ]

    instance conceito_25001019001P7_2022 : cti:Conceito_PPG [
        cti:cd_conceito_programa "5"
        cti:an_base_conceito 2022
    ]

    instance conceito_25001019001P7_2023 : cti:Conceito_PPG [
        cti:cd_conceito_programa "5"
        cti:an_base_conceito 2023
    ]
}
```

---

## 🎓 Conceitos-chave para Alunos

### 1. **Deduplicação**
**Por quê?** Evitar duplicatas quando mesma entidade aparece múltiplas vezes

```
❌ SEM deduplicação:
18.597 registros → 18.597 instâncias ICT (muitas repetidas!)

✅ COM deduplicação por CD_ENTIDADE_CAPES:
18.597 registros → 15 instâncias ICT (cada uma única)
```

### 2. **Relações Semânticas**
**Por quê?** Capturar significado e conectar entidades

```
Relação: "sediado"
PPG-X é sediado em UFPE
→ A Universidade Y hospeda o Programa X

Relação: "avaliado"
PPG-X foi avaliado em 2021 com conceito 5
→ Naquele ano, tinha qualidade 5/7
```

### 3. **Normalização**
**Por quê?** Garantir consistência e qualidade

```
Antes (sujo)       |  Depois (limpo)
"  EDUCAÇÃO  "     →  "EDUCAÇÃO"           # sem espaços
"5" (string)       →  5 (integer)          # tipo certo
"NA"               →  (null/missing)       # faltante marcado
```

### 4. **Instâncias vs Conceitos**
**Instância:** Uma coisa específica (ex: EDUCAÇÃO em UFPE)  
**Conceito:** Categoria geral (ex: PPG)

```
Conceito:    PPG
Instância:   ppg_25001019001P7
             (nome=EDUCAÇÃO, ict=UFPE, modalidade=ACADÊMICO)
```

---

## 📋 Checklist de Execução

Antes de rodar, garanta:

- [ ] Ambiente Python 3.8+ disponível
- [ ] Venv criado: `python3 -m venv venv`
- [ ] Venv ativado: `source venv/bin/activate`
- [ ] Pandas instalado: `pip install --only-binary :all: pandas`
- [ ] CSV files em `data/raw/capes/` (4 arquivos)
- [ ] Pasta `src/oml/gic.ufrpe.br/cti/description/` existe
- [ ] Pasta `data/processed/` será criada automaticamente

---

## 🐛 Troubleshooting

| Problema | Solução |
|----------|---------|
| `ModuleNotFoundError: pandas` | `pip install --only-binary :all: pandas` |
| `FileNotFoundError: No CSV files` | Verificar `data/raw/capes/` tem 4 CSVs |
| `UnicodeDecodeError` | Script já usa `iso-8859-1`; se falhar, converter CSV |
| `PermissionError` ao salvar | Verificar permissões de diretórios |
| Arquivo OML vazio | Verificar se dataframe não ficou vazio (STEP 2) |

---

## 💡 Extensões Possíveis

Ideias para aprender mais:

1. **Filtrar por conceito** - Gerar OML apenas com conceito ≥ 5
2. **Filtrar por ano** - Apenas avaliações de 2024
3. **Múltiplas regiões** - Estender de PE para Brasil inteiro
4. **Validação** - Alertar conceitos inválidos (< 1 ou > 7)
5. **RDF Export** - Converter OML para Turtle/RDF
6. **Gráficos** - Matplotlib com distribuição de conceitos
7. **API GraphQL** - Expor dados via GraphQL endpoint

---

## 📚 Referências

- [OML at OpenCaesar](https://www.opencaesar.io/)
- [CAPES - Coordenação de Aperfeiçoamento de Pessoal de Nível Superior](https://www.gov.br/capes)
- [Pandas User Guide](https://pandas.pydata.org/docs/)
- [Python Dataclasses](https://docs.python.org/3/library/dataclasses.html)
- [Engenharia de Conhecimento - UFRPE/GIC](https://www.ufrpe.br)

---

## 👨‍💻 Autor e Contexto

**Script didático** para disciplina de Engenharia de Conhecimento  
Grupo de Engenharia do Conhecimento (GIC)  
UFRPE - Universidade Federal Rural de Pernambuco  
2025

**Contribuidores:** GitHub Copilot + Alunos GIC
ls -lh src/oml/gic.ufrpe.br/cti/description/*.oml
```

## 📊 Saída Esperada

```
======================================================================
 EXTRACTION SUMMARY
======================================================================
  ICT Instances (Unique Institutions):        15
  PPG Instances (Unique Programs):             178
  Conceito Instances (Evaluations):            674
  ─────────────────────────────────────────────────────────────────
  Total Rows Processed:                        674
======================================================================
```

## 🔍 Estrutura do Código

### Classes Principais

**`CAPESProcessor`**
- Leitura dinâmica de CSVs com glob
- Filtragem por estado (PE)
- Normalização de dados
- Validação de qualidade

**`InstanceExtractor`**
- Extrai instâncias dedupllichadas (ICT, PPG)
- Extrai instâncias multi-ano (Conceito_PPG)
- Gerencia mapeamento de relações

**`OMLGenerator`**
- Gera arquivos OML estruturados
- Cria relações semânticas (sediado, avaliado)
- Salva bundle de agregação

### Dataclasses

```python
@dataclass
class ICTInstance
    # id: "ict_25003011"
    # cd_entidade_capes, sg_entidade_ensino, nm_entidade_ensino, sg_uf

@dataclass
class PPGInstance
    # id: "ppg_25003011041P5"
    # cd_programa_ies, nm_programa_ies, nm_modalidade_programa, 
    # nm_area_conhecimento, ict_id (para relação sediado)

@dataclass
class ConceituPPGInstance
    # id: "conceito_25003011041P5_2024"
    # cd_programa_ies, cd_conceito_programa, an_base_conceito
```

## 📖 Exemplos de Output

### ICT (Instituição)
```oml
instance ict_25003011 : cti:ICT [
    cti:cd_entidade_capes "25003011"
    cti:sg_entidade_ensino "UFRPE"
    cti:nm_entidade_ensino "UNIVERSIDADE FEDERAL RURAL DE PERNAMBUCO"
    cti:sg_uf "PE"
]
```

### PPG (com relação sediado)
```oml
instance ppg_25003011041P5 : cti:PPG [
    cti:cd_programa_ies "25003011041P5"
    cti:nm_programa_ies "CIÊNCIA, TECNOLOGIA E INOVAÇÃO"
    cti:nm_modalidade_programa "ACADÊMICO"
    cti:nm_area_conhecimento "INTERDISCIPLINAR"
    cti:sediado ict:ict_25003011
]
```

### Conceito_PPG (Avaliação)
```oml
instance conceito_25003011041P5_2024 : cti:Conceito_PPG [
    cti:an_base_conceito 2024
    cti:cd_conceito_programa "6"
]
```

## 🧩 Padrões de Engenharia de Conhecimento

### 1. Deduplicação por Tipo

**ICT** (Unique CDEntidade CAPES):
```python
unique_icts = self.dataframe.drop_duplicates(
    subset=['CD_ENTIDADE_CAPES'],
    keep='first'
)
```

**PPG** (Unique CD Programa):
```python
unique_ppgs = self.dataframe.drop_duplicates(
    subset=['CD_PROGRAMA_IES'],
    keep='first'
)
```

**Conceito** (NO deduplication - multi-year):
```python
for _, row in self.dataframe.iterrows():
    # Cria instância para CADA (programa, ano)
```

### 2. Relações Semânticas

**Relação sediado (PPG hosted by ICT)**:
```python
ict_id = f"ict_{row['CD_ENTIDADE_CAPES']}"
# ... later in OML:
cti:sediado ict:{ict_id}
```

### 3. IDs Estruturados

```python
ict_id = f"ict_{CD_ENTIDADE_CAPES}"
ppg_id = f"ppg_{CD_PROGRAMA_IES}"
conceito_id = f"conceito_{CD_PROGRAMA_IES}_{AN_BASE}"
```

## ⚙️ Configuração

Editar em `generate_oml_from_capes.py`:

```python
# Paths
DATA_INPUT_DIR = PROJECT_ROOT / "data" / "raw" / "capes"
OML_OUTPUT_DIR = PROJECT_ROOT / "src" / "oml" / "gic.ufrpe.br" / "cti" / "description"

# Namespaces
VOCABULARY_URI = "http://gic.ufrpe.br/cti/vocabulary/cti"
ICT_DESCRIPTION_URI = "http://gic.ufrpe.br/cti/description/ict"
PPG_DESCRIPTION_URI = "http://gic.ufrpe.br/cti/description/ppg"
CONCEITO_DESCRIPTION_URI = "http://gic.ufrpe.br/cti/description/conceito"

# Filtro padrão
state_code = "PE"  # Alterar para UF diferente
```

## 🔧 Troubleshooting

### Erro: `ModuleNotFoundError: No module named 'pandas'`
```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### Erro: `FileNotFoundError: No CSV files found`
- Verificar se arquivos CAPES estão em `data/raw/capes/`
- Confirmar encoding (ISO-8859-1)

### Aviso: Pandas deprecation warning
- Ignorar, ou atualizar `select_dtypes()` conforme instruído

## 📝 Logging

O script registra todas as etapas:
- Arquivos lidos e quantidade de registros
- Filtragem e normalização
- Instâncias extraídas
- Arquivo gerado e localização

```bash
2026-04-02 09:18:57,508 - INFO - Found 4 CSV files
2026-04-02 09:18:57,528 - INFO -   ✓ Loaded 4709 rows
2026-04-02 09:18:57,578 - INFO - Filtered data for state 'PE': 18597 → 674 rows
```

## 🎓 Conceitos Didáticos Demonstrados

1. **Modularidade**: Separação de preocupações (Processor, Extractor, Generator)
2. **Type Safety**: Uso de dataclasses para estruturas
3. **Logging**: Rastreabilidade de processos
4. **Error Handling**: Validação e tratamento de exceções
5. **Documentation**: Docstrings e comentários explicativos
6. **OML Patterns**: Bundles, extends, uses, relações
7. **Data Engineering**: Glob, filtering, normalization, deduplication

## 📚 Referências

- [OML Specification](https://github.com/opencaesar/oml)
- [OpenCAESAR Documentation](https://opencaesar.github.io/)
- [CAPES Data Schema](https://dadosabertos.capes.gov.br/)
- [Pandas Documentation](https://pandas.pydata.org/)
