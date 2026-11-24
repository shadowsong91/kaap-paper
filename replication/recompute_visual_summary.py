from pathlib import Path
import csv
import json
root=Path(__file__).parent
rows=list(csv.DictReader((root/'anonymous-ratings.csv').open(encoding='utf-8')))
assert len(rows)==96
assert len({(r['rater_id'],r['task'],r['system']) for r in rows})==96
means={}
for system in ['successor','incumbent']:
    selected=[r for r in rows if r['system']==system]
    means[system]={'scores':len(selected),'sum':sum(int(r['quality']) for r in selected),'mean':sum(int(r['quality']) for r in selected)/len(selected),'severe_marked':sum(r['severe_defect_marked']=='True' for r in selected)}
assert means['successor']['sum']==233 and means['incumbent']['sum']==235
direct={s:[int(r['quality']) for r in rows if r['system']==s and r['task']!='task07'] for s in means}
assert sum(direct['successor'])==213 and sum(direct['incumbent'])==215
print(json.dumps({'four_rater_panel':means,'eleven_original_delivery_visual_means':{s:sum(v)/len(v) for s,v in direct.items()},'scope':'Scalar visual judgments only; no equivalence, full functional acceptance or raw evidence validation.'},indent=2))
