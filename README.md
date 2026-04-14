# NOC Knowledge Base — RAG Ingestion Pipeline

## What this is
A Python pipeline that loads 21 DAS NOC runbook files into Supabase (pgvector)
for use as a RAG knowledge base for the NOC triage agent.

## Folder structure
```
noc_rag_kb/
├── noc_kb/
│   ├── internal_alarms/      # INT-001 through INT-012
│   ├── external_alarms/      # EXT-001 through EXT-005
│   ├── ops_guides/           # OPS-001 through OPS-003
│   └── metadata/             # META-001 (severity matrix)
├── ingest_kb.py              # Main ingestion script
├── supabase_setup.sql        # Run once in Supabase SQL editor
├── .env.template             # Copy to .env and fill in keys
└── README.md
```

## Setup — Step by Step

### 1. Install dependencies
```bash
pip install anthropic supabase python-frontmatter tiktoken python-dotenv
```

### 2. Configure credentials
```bash
cp .env.template .env
# Edit .env with your actual keys
```

You need:
- **ANTHROPIC_API_KEY** — from console.anthropic.com
- **SUPABASE_URL** — from your Supabase project Settings > API
- **SUPABASE_SERVICE_KEY** — the service_role key (not anon key) from same page

### 3. Set up the Supabase database
1. Open your Supabase project
2. Go to SQL Editor
3. Paste the contents of `supabase_setup.sql` and run it

This creates the `noc_kb_chunks` table, the vector index, metadata indexes,
and the `match_noc_chunks` retrieval function.

### 4. Dry run — verify chunking without writing to DB
```bash
python ingest_kb.py --dry-run
```
This shows chunk counts and token distributions per file. No API calls, no DB writes.

### 5. Run the full ingestion
```bash
python ingest_kb.py
```
Output:
- Parses all 21 markdown files
- Chunks by section (300–450 tokens each)
- Embeds all chunks using Anthropic voyage-3
- Writes to Supabase
- Prints a verification summary

### 6. Test retrieval
```bash
# Test a query against the loaded KB
python ingest_kb.py --query "DL output power low on multiple remotes"

# Filter by category
python ingest_kb.py --query "fan fault overtemp" --category internal

# External alarm query
python ingest_kb.py --query "carrier not transmitting POI no signal" --category external
```

## How the chunking works

Each markdown file has YAML frontmatter (alarm_id, category, severity, tags).
The script:
1. Parses the frontmatter as metadata — stored as columns for filtering
2. Splits the body into sections by `##` heading
3. Keeps sections under 450 tokens as single chunks
4. Splits larger sections into overlapping paragraph chunks (50-token overlap)
5. Prefixes every chunk with a document anchor line so the LLM always knows context

Example chunk for INT-006:
```
Document: Downlink output power low / DL gain alarm (ID: INT-006, Category: internal, Severity: major)

Section: CRITICAL — Most common misdiagnosis in DAS NOC operations

This alarm is frequently caused by an external issue (no or low DL input at
the POI from the carrier BTS), NOT a DAS hardware fault.

Always check EXT-001 (DL input low at POI) before assuming the DAS is at fault...
```

## How to use in your LangGraph agent

```python
from supabase import create_client
import anthropic

def retrieve_kb(query: str, category: str = None, top_k: int = 5) -> list[dict]:
    ac = anthropic.Anthropic()
    sb = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Embed the query
    response = ac.embeddings.create(
        model="voyage-3",
        input=[query],
        input_type="query",   # <-- use "query" for retrieval, "document" for ingestion
    )
    q_vec = response.data[0].embedding

    # Retrieve from Supabase
    result = sb.rpc("match_noc_chunks", {
        "query_embedding": q_vec,
        "match_count": top_k,
        "filter_category": category,
        "filter_severity": None,
    }).execute()

    return result.data
```

Wire `retrieve_kb` as a tool in your LangGraph RCA agent node.

## Re-ingesting after KB updates

Just run `python ingest_kb.py` again — the script clears the table and reloads.
Safe to re-run as many times as needed.

## What's still needed in the KB (fill-in items)

These are marked `[FILL IN]` throughout the runbooks:
- Carrier NOC contact numbers (EXT-001, OPS-001)
- SLA response time targets per severity (META-001, OPS-002)
- Site criticality classifications (which sites have public safety or SLA obligations)
- Operations on-call contact number (OPS-002)
- Ticketing system name (OPS-002, OPS-003)
ENDOFFILE
