# Architecture

## Offline/indexing path
`dataset manifest -> TextLoader -> metadata -> RecursiveCharacterTextSplitter -> OllamaEmbeddings -> Chroma`

## Online/question path
`incident question + service scope -> hybrid BM25 + Chroma retrieval -> retrieved evidence -> structured prompt -> local Ollama LLM -> Pydantic response`

## Final class workflow
`START -> retrieve -> generate -> END`

The LLM is not given unrestricted operational authority. Recommended steps are generated from retrieved evidence and require human execution/approval.
