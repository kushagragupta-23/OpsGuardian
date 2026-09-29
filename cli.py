import argparse
from rag_pipeline import OpsGuardianRAG
p=argparse.ArgumentParser(); p.add_argument('question'); p.add_argument('--service', default='all'); p.add_argument('--method', default='hybrid', choices=['similarity','mmr','hybrid']); a=p.parse_args()
rag=OpsGuardianRAG(); answer,docs=rag.ask(a.service,a.question,a.method)
print(answer.model_dump_json(indent=2))
print('\nRetrieved sources:')
for d in docs: print('-',d.metadata.get('source'))
