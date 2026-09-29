from pathlib import Path
import pandas as pd
from rag_pipeline import OpsGuardianRAG
ROOT=Path(__file__).resolve().parent
cases=pd.read_csv(ROOT/'evaluation/evaluation_questions.csv').fillna('')
rag=OpsGuardianRAG()
def rr(sources, expected):
    if not expected: return 0.0
    for i,s in enumerate(sources,1):
        if expected == s: return 1.0/i
    return 0.0
rows=[]
for method in ['similarity','mmr','hybrid']:
    for _,r in cases[cases.expected_source!=''].iterrows():
        retr = rag.similarity_retriever(r.service) if method=='similarity' else rag.mmr_retriever(r.service) if method=='mmr' else rag.hybrid_retriever(r.service)
        docs=retr.invoke(r.question); sources=[d.metadata.get('source','') for d in docs]
        cats=[d.metadata.get('category','') for d in docs]
        rows.append({'question_id':r.question_id,'method':method,'source_hit':int(r.expected_source in sources),'category_hit':int(r.expected_category in cats),'reciprocal_rank':rr(sources,r.expected_source),'sources':' | '.join(sources)})
out=pd.DataFrame(rows)
summary=out.groupby('method')[['source_hit','category_hit','reciprocal_rank']].mean().round(3)

out.to_csv(ROOT/'evaluation/retrieval_results.csv',index=False)
summary.to_csv(ROOT/'evaluation/retrieval_summary.csv')

print()
print('SUMMARY')
print(summary)
print()
print('Saved evaluation/retrieval_results.csv and retrieval_summary.csv')
