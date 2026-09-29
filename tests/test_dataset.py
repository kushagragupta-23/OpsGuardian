from pathlib import Path
import pandas as pd
ROOT=Path(__file__).resolve().parents[1]
def test_dataset_manifest_and_files_exist():
    df=pd.read_csv(ROOT/'dataset/source_manifest.csv')
    assert len(df) >= 30
    for rel in df.source_path:
        assert (ROOT/'dataset/knowledge_base'/rel).exists()
def test_eval_cases():
    df=pd.read_csv(ROOT/'evaluation/evaluation_questions.csv')
    assert len(df) >= 20
    assert {'question_id','service','question','expected_source','expected_category'}.issubset(df.columns)
