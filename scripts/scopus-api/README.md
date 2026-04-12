## Integração com API Scopus

Além dos dados tabulares da CAPES, este repositório contém scripts para extração automatizada de metadados de artigos científicos diretamente da base **Scopus (Elsevier)**.

### Componentes

- **`/scopus-api/gic_scopus_client.py`**: Um cliente de baixo nível que encapsula as chamadas HTTP para a Scopus Search API. Ele gerencia:
    - Autenticação via API Key.
    - Paginação automática baseada em cursores (permitindo baixar grandes volumes de dados).
    - Cabeçalhos de requisição e tratamento de erros de rede.

- **`scripts/scopus-api/gic_main.py`**: O orquestrador da extração. Ele:
    - Define os critérios de busca (ex: Instituição, Área de Conhecimento, Ano).
    - Consome o cliente Scopus para obter os dados brutos.
    - Realiza o *parsing* do JSON complexo da Elsevier para um formato simplificado e estruturado (Título, Autores, Afiliações, DOI, etc.).
    - Exporta o resultado final para um arquivo JSON pronto para ser processado ou convertido em instâncias OML.

### Como usar

1. **API Key**: Obtenha uma chave de acesso no Elsevier Developer Portal.
2. **Ambiente**: Crie um arquivo `.env` na pasta do script com sua chave:
   ```env
   ELSEVIER_API_KEY=sua_chave_aqui
   ```
3. **Dependências**:
   ```bash
   pip install requests python-dotenv
   ```
4. **Execução**:
   ```bash
   python scripts/scopus-api/gic_main.py
   ```

---

