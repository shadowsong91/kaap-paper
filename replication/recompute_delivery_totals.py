"""Recompute declared worker totals from the accompanying anonymous CSV."""
from pathlib import Path
import csv
import json

rows=list(csv.DictReader((Path(__file__).parent/'tables/delivery-consumption.csv').open(encoding='utf-8-sig')))
assert len(rows)==12
direct=[r for r in rows if r['visual_from_same_successor_worker']=='True']
assert len(direct)==11
def totals(data):
    new=sum(int(r['successor_original_worker_tokens']) for r in data)
    old=sum(int(r['incumbent_worker_tokens']) for r in data)
    return {'successor_tokens':new,'incumbent_tokens':old,'observed_delta_percent':(new/old-1)*100}
result={'original_twelve_sessions':totals(rows),'eleven_original_recordings':totals(direct),
        'separate_task07_rerun_tokens':3112916,
        'eleven_visual_means':{arm:sum(float(r[arm+'_visual_mean_assessed']) for r in direct)/11 for arm in ['successor','incumbent']},
        'scope':'Descriptive observations. Each task has four complete ratings; task means are equally weighted. The task07 assessed visual belongs to a different execution. No equivalence or functional pass claim.'}
assert result['original_twelve_sessions']['successor_tokens']==56219271
assert result['eleven_original_recordings']['successor_tokens']==49969436
assert result['eleven_original_recordings']['incumbent_tokens']==63756348
print(json.dumps(result,indent=2))
