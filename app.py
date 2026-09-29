import streamlit as st
from rag_pipeline import OpsGuardianRAG
st.set_page_config(page_title='OpsGuardian', page_icon='🛠️', layout='wide')
st.title('OpsGuardian - DevOps Incident Resolution RAG')
st.caption("Sir's Labs 1-6 flow: split -> embed -> Chroma -> hybrid retrieval -> structured answer -> LangGraph")
@st.cache_resource
def get_rag(): return OpsGuardianRAG()
rag=get_rag()
service=st.selectbox('Service scope',['all','checkout-api','payments-api','inventory-service','auth-service','orders-worker','platform'])
method=st.selectbox('Retrieval',['hybrid','similarity','mmr'])
q=st.text_area('Incident question','Why did checkout latency spike after v2.18.0?')
if st.button('Investigate'):
    try:
        ans,docs=rag.ask(service,q,method)
        st.subheader('Evidence-grounded response'); st.json(ans.model_dump())
        st.subheader('Retrieved evidence')
        for d in docs:
            with st.expander(d.metadata.get('source','source')):
                st.write(d.page_content); st.caption(str(d.metadata))
    except Exception as e: st.error(str(e))
