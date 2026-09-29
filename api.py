from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import OpsGuardianRAG
app=FastAPI(title='OpsGuardian API',version='1.0.0'); rag=OpsGuardianRAG()
class AskRequest(BaseModel): service:str='all'; question:str; method:str='hybrid'
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/ask')
def ask(req: AskRequest):
    ans,docs=rag.ask(req.service,req.question,req.method)
    return {'answer':ans.model_dump(),'sources':[d.metadata for d in docs]}
