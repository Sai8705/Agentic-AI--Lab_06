async function load(){
 const r=await fetch('/api/policies'); const ps=await r.json();
 policy.innerHTML=ps.map(p=>`<option value="${p.policy_id}">${p.policy_id} — ${p.name}</option>`).join('');
}
async function audit(){
 result.innerHTML='<p>Evaluating...</p>';
 const r=await fetch('/api/compliance/audit',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({policy_id:policy.value,scenario:scenario.value})});
 const d=await r.json();
 if(!r.ok){result.innerHTML=`<p>${d.detail}</p>`;return}
 const cls=d.status==='COMPLIANT'?'ok':d.status==='WARNING'?'warn':'bad';
 result.innerHTML=`<div class="score ${cls}">${d.score}% — ${d.status}</div>
 <div class="grid"><div class="metric">Passed<br><b>${d.passed}</b></div><div class="metric">Failed<br><b>${d.failed}</b></div><div class="metric">Warnings<br><b>${d.warnings}</b></div><div class="metric">Critical<br><b>${d.critical_violations}</b></div></div>
 <h2>Rule Evaluation</h2>${d.evaluations.map(e=>`<div class="rule ${e.status.toLowerCase()}"><b>${e.rule_id} — ${e.name}</b><br>${e.status} • ${e.severity}<br><small>${e.reason}</small></div>`).join('')}
 <div class="rem"><h2>Remediation Plan</h2>${d.remediations.length?d.remediations.map(x=>`<p>→ ${x}</p>`).join(''):'<p>No remediation required.</p>'}</div>`;
}
load();
