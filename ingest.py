import argparse, shutil
from pathlib import Path
from rag_pipeline import OpsGuardianRAG, PERSIST_DIR

p=argparse.ArgumentParser(); p.add_argument('--reset', action='store_true'); args=p.parse_args()
if args.reset and Path(PERSIST_DIR).exists(): shutil.rmtree(PERSIST_DIR)
rag=OpsGuardianRAG(); print(f"Indexed {rag.index(reset=False)} chunks into Chroma at {PERSIST_DIR}")
