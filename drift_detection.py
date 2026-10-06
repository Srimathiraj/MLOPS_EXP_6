import json
from pathlib import Path
import pandas as pd
from evidently import Report
from evidently.presets import DataDriftPreset
PROJECT_DIR=Path(__file__).resolve().parent; DATA_DIR=PROJECT_DIR/'data'
reference=pd.read_csv(DATA_DIR/'reference_data.csv'); current=pd.read_csv(DATA_DIR/'current_data.csv')
def run_detection():
    report=Report(metrics=[DataDriftPreset()]); snapshot=report.run(current_data=current,reference_data=reference); snapshot.save_html(str(PROJECT_DIR/'drift_report.html'))
    result=snapshot.dict(); drift_detected=False; drifted_columns=0
    for metric in result.get('metrics',[]):
        value=metric.get('value',{})
        if isinstance(value,dict):
            if 'dataset_drift' in value: drift_detected=value['dataset_drift']
            if 'count' in value: drifted_columns=value['count']
    summary={'reference_rows':len(reference),'current_rows':len(current),'drift_detected':bool(drift_detected),'drifted_columns':int(drifted_columns),'total_columns':4}
    with open(PROJECT_DIR/'drift_summary.json','w') as f: json.dump(summary,f,indent=4)
    print('Reference rows:',len(reference)); print('Current rows:',len(current)); print('Drift detected:','YES' if drift_detected else 'NO'); print('Drifted columns:',drifted_columns); print('Total columns:',4); return summary
if __name__=='__main__': run_detection()
