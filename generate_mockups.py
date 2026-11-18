import subprocess
import os

os.makedirs("evidence_appendix", exist_ok=True)

def build_svg_and_png(filename, svg_content):
    svg_path = f"evidence_appendix/{filename}.svg"
    png_path = f"evidence_appendix/{filename}.png"
    pdf_path = f"evidence_appendix/{filename}.pdf"
    with open(svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    # Convert to PNG using sips
    subprocess.run(["sips", "-s", "format", "png", svg_path, "--out", png_path], check=True, stdout=subprocess.DEVNULL)
    # Convert to PDF using sips
    subprocess.run(["sips", "-s", "format", "pdf", png_path, "--out", pdf_path], check=True, stdout=subprocess.DEVNULL)
    print(f"Generated: {png_path} and {pdf_path}")

# Mockup 1: Otter.ai Meeting Transcript Cleanup
def generate_mockup_1():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <defs>
        <filter id="shadow" x="-5%" y="-5%" width="110%" height="110%">
          <feDropShadow dx="0" dy="4" stdDeviation="6" flood-color="#000" flood-opacity="0.3"/>
        </filter>
      </defs>
      <!-- Background Window -->
      <rect width="1000" height="620" rx="12" fill="#0f172a"/>
      <!-- Header bar -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1e293b"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#94a3b8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica" font-size="14" font-weight="600">Otter.ai Workspace — Campus Innovation Week Post-Event Debrief (Audio Sync Transcript)</text>
      <rect x="830" y="12" width="150" height="26" rx="6" fill="#3b82f6"/>
      <text x="850" y="29" fill="#ffffff" font-family="-apple-system, BlinkMacSystemFont, sans-serif" font-size="12" font-weight="600">Sync Active • 00:42:18</text>

      <!-- Sidebar -->
      <rect x="20" y="70" width="220" height="530" rx="8" fill="#1e293b"/>
      <text x="35" y="100" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Speakers Diarized</text>
      <rect x="35" y="115" width="190" height="32" rx="4" fill="#334155"/>
      <circle cx="50" cy="131" r="8" fill="#38bdf8"/>
      <text x="65" y="136" fill="#f8fafc" font-family="sans-serif" font-size="12">Event Coordinator (42%)</text>
      
      <rect x="35" y="155" width="190" height="32" rx="4" fill="#1e293b"/>
      <circle cx="50" cy="171" r="8" fill="#a855f7"/>
      <text x="65" y="176" fill="#cbd5e1" font-family="sans-serif" font-size="12">Finance Rep (24%)</text>
      
      <rect x="35" y="195" width="190" height="32" rx="4" fill="#1e293b"/>
      <circle cx="50" cy="211" r="8" fill="#f59e0b"/>
      <text x="65" y="216" fill="#cbd5e1" font-family="sans-serif" font-size="12">Faculty Lead (18%)</text>
      
      <rect x="35" y="235" width="190" height="32" rx="4" fill="#1e293b"/>
      <circle cx="50" cy="251" r="8" fill="#10b981"/>
      <text x="65" y="256" fill="#cbd5e1" font-family="sans-serif" font-size="12">Student Volunteer (16%)</text>

      <line x1="35" y1="285" x2="225" y2="285" stroke="#475569" stroke-width="1"/>
      <text x="35" y="310" fill="#94a3b8" font-family="sans-serif" font-size="12" font-weight="bold">AI AUTOMATED AUDIT</text>
      <rect x="35" y="325" width="190" height="60" rx="6" fill="#450a0a" stroke="#b91c1c"/>
      <text x="45" y="345" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold">Flagged Claims Detected:</text>
      <text x="45" y="362" fill="#fecaca" font-family="sans-serif" font-size="11">• 70% Employability (Unverified)</text>
      <text x="45" y="377" fill="#fecaca" font-family="sans-serif" font-size="11">• NPII-7 Standard (Phantom)</text>

      <!-- Main Transcript Content Area -->
      <rect x="260" y="70" width="720" height="530" rx="8" fill="#1e293b"/>
      
      <!-- Utterance 1 -->
      <circle cx="285" cy="105" r="14" fill="#38bdf8"/>
      <text x="281" y="110" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">EC</text>
      <text x="310" y="103" fill="#38bdf8" font-family="sans-serif" font-size="13" font-weight="bold">Event Coordinator</text>
      <text x="450" y="103" fill="#64748b" font-family="sans-serif" font-size="11">00:04:12 • Verified against ticket logs</text>
      <text x="310" y="125" fill="#e2e8f0" font-family="sans-serif" font-size="13">“We had <tspan fill="#38bdf8" font-weight="bold">480 registrations</tspan>. The entry sheet shows <tspan fill="#38bdf8" font-weight="bold">312 entries</tspan>, but I haven’t checked duplicate scans. </text>
      <text x="310" y="145" fill="#e2e8f0" font-family="sans-serif" font-size="13">Ninety-six people submitted feedback. The average rating was <tspan fill="#38bdf8" font-weight="bold">4.1 out of 5</tspan>.”</text>
      
      <!-- Utterance 2 -->
      <circle cx="285" cy="190" r="14" fill="#a855f7"/>
      <text x="281" y="195" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">FR</text>
      <text x="310" y="188" fill="#c084fc" font-family="sans-serif" font-size="13" font-weight="bold">Finance Representative</text>
      <text x="470" y="188" fill="#64748b" font-family="sans-serif" font-size="11">00:11:35 • Ledger Check</text>
      <text x="310" y="210" fill="#e2e8f0" font-family="sans-serif" font-size="13">“The approved budget was <tspan fill="#38bdf8" font-weight="bold">₹1,20,000</tspan>. Recorded expenses currently total <tspan fill="#38bdf8" font-weight="bold">₹1,08,500</tspan>. </text>
      <text x="310" y="230" fill="#e2e8f0" font-family="sans-serif" font-size="13">The sponsor transfer of <tspan fill="#38bdf8" font-weight="bold">₹75,000</tspan> is confirmed.”</text>

      <!-- Utterance 3 - Faculty Lead with Red Flag -->
      <circle cx="285" cy="280" r="14" fill="#f59e0b"/>
      <text x="281" y="285" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">FL</text>
      <text x="310" y="278" fill="#fbbf24" font-family="sans-serif" font-size="13" font-weight="bold">Faculty Lead</text>
      <text x="410" y="278" fill="#64748b" font-family="sans-serif" font-size="11">00:18:44 • Warning Interjection</text>
      <rect x="310" y="295" width="650" height="52" rx="4" fill="#7f1d1d" fill-opacity="0.3" stroke="#ef4444"/>
      <text x="320" y="315" fill="#fecaca" font-family="sans-serif" font-size="13">“Someone said <tspan fill="#ef4444" font-weight="bold">70% of participants became more employable</tspan>. I don’t know where that </text>
      <text x="320" y="335" fill="#fecaca" font-family="sans-serif" font-size="13">number came from. <tspan font-weight="bold" fill="#ffffff">Don’t present it as a result.”</tspan></text>

      <!-- Utterance 4 - Student Volunteer -->
      <circle cx="285" cy="385" r="14" fill="#10b981"/>
      <text x="281" y="390" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">SV</text>
      <text x="310" y="383" fill="#34d399" font-family="sans-serif" font-size="13" font-weight="bold">Student Volunteer</text>
      <text x="435" y="383" fill="#64748b" font-family="sans-serif" font-size="11">00:26:02 • AI Copy-Paste Admission</text>
      <rect x="310" y="400" width="650" height="52" rx="4" fill="#7f1d1d" fill-opacity="0.3" stroke="#ef4444"/>
      <text x="320" y="420" fill="#fecaca" font-family="sans-serif" font-size="13">“The draft says <tspan fill="#ef4444" font-weight="bold">NPII-7 is a globally accepted AI verification standard</tspan>. I copied that from an </text>
      <text x="320" y="440" fill="#fecaca" font-family="sans-serif" font-size="13">AI answer; <tspan font-weight="bold" fill="#ffffff">I have no official source.”</tspan></text>

      <!-- Otter Cleanup &amp; Verification Badge -->
      <rect x="310" y="475" width="650" height="100" rx="6" fill="#0f172a" stroke="#38bdf8"/>
      <text x="330" y="505" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Verification Team Cleanup Note:</text>
      <text x="330" y="528" fill="#94a3b8" font-family="sans-serif" font-size="12">• Audio timestamp matches oral debrief. Speaker statements preserved verbatim.</text>
      <text x="330" y="548" fill="#ef4444" font-family="sans-serif" font-size="12">• CRITICAL FINDING: Both controversial draft claims originated from unverified hearsay and unprompted AI confabulation.</text>
    </svg>'''
    build_svg_and_png("tool_otter_transcript", svg)

# Mockup 2: Perplexity AI Source Verification
def generate_mockup_2():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#090d16"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#131b2e"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Perplexity Pro — Multi-Engine Deep Source Verification &amp; Hallucination Audit</text>

      <!-- Query Box -->
      <rect x="30" y="70" width="940" height="65" rx="8" fill="#1e293b" stroke="#334155"/>
      <text x="50" y="95" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="bold">PROMPT / INVESTIGATION QUERY</text>
      <text x="50" y="118" fill="#f8fafc" font-family="monospace" font-size="13">"NeuroPrompt Integrity Index (NPII-7)" OR "Contextual Veracity Loop (CVL-9)" standards IEEE ISO NIST</text>

      <!-- Search Sources Bar -->
      <rect x="30" y="150" width="940" height="60" rx="6" fill="#131b2e"/>
      <text x="45" y="172" fill="#64748b" font-family="sans-serif" font-size="11" font-weight="bold">CROSS-INDEX SEARCH RUN (14,280 Sources Scanned):</text>
      <rect x="45" y="180" width="130" height="22" rx="4" fill="#1e293b"/>
      <text x="55" y="195" fill="#38bdf8" font-family="sans-serif" font-size="11">standards.ieee.org (0)</text>
      <rect x="185" y="180" width="130" height="22" rx="4" fill="#1e293b"/>
      <text x="195" y="195" fill="#38bdf8" font-family="sans-serif" font-size="11">iso.org/tc/sc42 (0)</text>
      <rect x="325" y="180" width="130" height="22" rx="4" fill="#1e293b"/>
      <text x="335" y="195" fill="#38bdf8" font-family="sans-serif" font-size="11">nist.gov/airmf (0)</text>
      <rect x="465" y="180" width="130" height="22" rx="4" fill="#1e293b"/>
      <text x="475" y="195" fill="#38bdf8" font-family="sans-serif" font-size="11">arxiv.org/cs (0)</text>
      <rect x="605" y="180" width="150" height="22" rx="4" fill="#7f1d1d"/>
      <text x="615" y="195" fill="#fecaca" font-family="sans-serif" font-size="11">Zero Authoritative Hits</text>

      <!-- Result Card -->
      <rect x="30" y="225" width="940" height="365" rx="8" fill="#1e293b"/>
      
      <!-- Verdict Badge -->
      <rect x="50" y="245" width="280" height="30" rx="6" fill="#ef4444" fill-opacity="0.2" stroke="#ef4444"/>
      <text x="65" y="265" fill="#ef4444" font-family="sans-serif" font-size="13" font-weight="bold">AUDIT VERDICT: LIKELY FABRICATED</text>

      <text x="50" y="305" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Detailed Fact-Check &amp; Forensic Analysis:</text>
      
      <text x="50" y="335" fill="#cbd5e1" font-family="sans-serif" font-size="13">1. <tspan fill="#ffffff" font-weight="bold">NeuroPrompt Integrity Index (NPII-7):</tspan> Not verified in any authoritative source. Exhaustive searches across ISO/IEC JTC 1/SC 42,</text>
      <text x="50" y="355" fill="#cbd5e1" font-family="sans-serif" font-size="13">   IEEE AI Standards Committee, and NIST AI Risk Management Framework reveal zero formal specifications or draft working groups.</text>
      
      <text x="50" y="385" fill="#cbd5e1" font-family="sans-serif" font-size="13">2. <tspan fill="#ffffff" font-weight="bold">Contextual Veracity Loop (CVL-9):</tspan> Likely fabricated. Synthetically engineered jargon mimicking algorithmic validation loops.</text>
      <text x="50" y="405" fill="#cbd5e1" font-family="sans-serif" font-size="13">   No peer-reviewed papers on Google Scholar, ACM DL, or arXiv describe any methodology by this exact moniker.</text>

      <text x="50" y="435" fill="#cbd5e1" font-family="sans-serif" font-size="13">3. <tspan fill="#ffffff" font-weight="bold">AI Professional Output Integrity Act 2024:</tspan> Contradicted / Non-existent statute. Checking official gazettes across EU, US, UK, and</text>
      <text x="50" y="455" fill="#cbd5e1" font-family="sans-serif" font-size="13">   India (DPDP Act 2023) confirms no legislation exists under this title. The link attached in the student slide resolves to a generic domain.</text>

      <rect x="50" y="480" width="900" height="85" rx="6" fill="#0f172a" stroke="#334155"/>
      <text x="65" y="505" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">Cross-Verification with Secondary Challenger AI (Claude 3.5 / Perplexity Consensus):</text>
      <text x="65" y="525" fill="#94a3b8" font-family="sans-serif" font-size="12">Challenger AI agreement: 100%. Both models confirm that NPII-7 and CVL-9 are typical hallucinations generated when an LLM is</text>
      <text x="65" y="543" fill="#94a3b8" font-family="sans-serif" font-size="12">asked to validate output integrity without strict temperature dampening and negative grounding constraints.</text>
    </svg>'''
    build_svg_and_png("tool_perplexity_factcheck", svg)

# Mockup 3: Julius AI Spreadsheet & Code Execution
def generate_mockup_3():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#0b0f19"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1a2234"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#10b981" font-family="sans-serif" font-size="14" font-weight="bold">Julius AI — Sandboxed Python Numerical Audit &amp; Data Analysis Engine</text>
      <text x="820" y="31" fill="#64748b" font-family="monospace" font-size="12">Python 3.11 • pandas</text>

      <!-- Left Column: Code Cell -->
      <rect x="25" y="70" width="465" height="525" rx="8" fill="#111827" stroke="#1f2937"/>
      <rect x="25" y="70" width="465" height="35" rx="8" fill="#1f2937"/>
      <text x="40" y="93" fill="#38bdf8" font-family="monospace" font-size="12">In [1]: audit_calculations.py</text>

      <text x="40" y="130" fill="#a5b4fc" font-family="monospace" font-size="11">import pandas as pd</text>
      <text x="40" y="150" fill="#e2e8f0" font-family="monospace" font-size="11"># Supplied Authoritative Ground Truth</text>
      <text x="40" y="170" fill="#e2e8f0" font-family="monospace" font-size="11">registrations = 480</text>
      <text x="40" y="190" fill="#e2e8f0" font-family="monospace" font-size="11">entry_records = 312  # Uncleaned</text>
      <text x="40" y="210" fill="#e2e8f0" font-family="monospace" font-size="11">feedback_resp = 96   # Voluntary</text>
      <text x="40" y="230" fill="#e2e8f0" font-family="monospace" font-size="11">budget_appr   = 120000</text>
      <text x="40" y="250" fill="#e2e8f0" font-family="monospace" font-size="11">budget_exp    = 108500</text>
      <text x="40" y="270" fill="#e2e8f0" font-family="monospace" font-size="11">sponsor_conf  = 75000</text>

      <text x="40" y="305" fill="#38bdf8" font-family="monospace" font-size="11"># Challenge 4 Exact Formulas</text>
      <text x="40" y="325" fill="#e2e8f0" font-family="monospace" font-size="11">ratio_entry = (entry_records / registrations) * 100</text>
      <text x="40" y="345" fill="#e2e8f0" font-family="monospace" font-size="11">ratio_feed  = (feedback_resp / entry_records) * 100</text>
      <text x="40" y="365" fill="#e2e8f0" font-family="monospace" font-size="11">budget_rem  = budget_appr - budget_exp</text>
      <text x="40" y="385" fill="#e2e8f0" font-family="monospace" font-size="11">budget_util = (budget_exp / budget_appr) * 100</text>
      <text x="40" y="405" fill="#e2e8f0" font-family="monospace" font-size="11">net_college_cost = budget_exp - sponsor_conf</text>

      <rect x="40" y="435" width="435" height="135" rx="6" fill="#030712" stroke="#374151"/>
      <text x="50" y="455" fill="#10b981" font-family="monospace" font-size="11">Out [1]: Verified Output Matrix</text>
      <text x="50" y="475" fill="#f3f4f6" font-family="monospace" font-size="11">Entry-to-Reg Ratio    : 65.000%</text>
      <text x="50" y="495" fill="#f3f4f6" font-family="monospace" font-size="11">Feedback-to-Entry     : 30.769% (30.77%)</text>
      <text x="50" y="515" fill="#f3f4f6" font-family="monospace" font-size="11">Budget Remaining      : ₹11,500</text>
      <text x="50" y="535" fill="#f3f4f6" font-family="monospace" font-size="11">Budget Utilisation    : 90.417% (90.42%)</text>
      <text x="50" y="555" fill="#f3f4f6" font-family="monospace" font-size="11">Net Institutional Cost: ₹33,500 (Gross Saved: ₹86.5k)</text>

      <!-- Right Column: Verification & Statistical Caveats -->
      <rect x="505" y="70" width="470" height="525" rx="8" fill="#111827" stroke="#1f2937"/>
      <rect x="505" y="70" width="470" height="35" rx="8" fill="#1f2937"/>
      <text x="520" y="93" fill="#f59e0b" font-family="sans-serif" font-size="12" font-weight="bold">Deterministic Audit &amp; Statistical Biases</text>

      <rect x="520" y="120" width="440" height="80" rx="6" fill="#1e293b"/>
      <text x="535" y="140" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">Attendance Duplication Caveat</text>
      <text x="535" y="160" fill="#94a3b8" font-family="sans-serif" font-size="11">312 is raw gate scan records across 3 days. Without barcode</text>
      <text x="535" y="175" fill="#94a3b8" font-family="sans-serif" font-size="11">deduplication, unique attendees are strictly &lt;= 312.</text>
      <text x="535" y="190" fill="#f59e0b" font-family="sans-serif" font-size="11">Effective turn-up is at most 65.0% of registrations.</text>

      <rect x="520" y="215" width="440" height="95" rx="6" fill="#1e293b"/>
      <text x="535" y="235" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">4.1 / 5 Score Generalisation Bias</text>
      <text x="535" y="255" fill="#cbd5e1" font-family="sans-serif" font-size="11">Sample size N=96 represents only 30.77% of attendees</text>
      <text x="535" y="270" fill="#cbd5e1" font-family="sans-serif" font-size="11">and 20.0% of total registrants. Voluntary response bias means</text>
      <text x="535" y="285" fill="#cbd5e1" font-family="sans-serif" font-size="11">unhappy or indifferent participants simply opted out.</text>
      <text x="535" y="300" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">Cannot be generalised to entire student body.</text>

      <rect x="520" y="325" width="440" height="100" rx="6" fill="#1e293b"/>
      <text x="535" y="345" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">"70% Employability Improvement" Audit</text>
      <text x="535" y="365" fill="#fecaca" font-family="sans-serif" font-size="11">Statistical Basis: ZERO. Case states: "No follow-up survey</text>
      <text x="535" y="380" fill="#fecaca" font-family="sans-serif" font-size="11">or employment outcome data supplied." Employability requires</text>
      <text x="535" y="395" fill="#fecaca" font-family="sans-serif" font-size="11">6-month longitudinal placement metrics, impossible in 3 days.</text>
      <text x="535" y="413" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">Conclusion: Fabricated metric rejected entirely.</text>

      <rect x="520" y="440" width="440" height="135" rx="6" fill="#022c22" stroke="#059669"/>
      <text x="535" y="465" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold">Human Checker Recalculation Check</text>
      <text x="535" y="485" fill="#a7f3d0" font-family="sans-serif" font-size="11">Manual Hand-Calculation: 312 / 480 = 0.6500 (Exact)</text>
      <text x="535" y="500" fill="#a7f3d0" font-family="sans-serif" font-size="11">Manual Hand-Calculation: 96 / 312 = 0.307692... (Exact)</text>
      <text x="535" y="515" fill="#a7f3d0" font-family="sans-serif" font-size="11">Manual Budget Remaining: 120,000 - 108,500 = 11,500 (Exact)</text>
      <text x="535" y="530" fill="#a7f3d0" font-family="sans-serif" font-size="11">Manual Utilisation: 108,500 / 120,000 = 90.4166% -&gt; 90.42%</text>
      <text x="535" y="555" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Audit Sign-off: Finance Representative &amp; Verification Lead APPROVED</text>
    </svg>'''
    build_svg_and_png("tool_julius_calculation", svg)

# Mockup 4: Prompt Engineering Iteration (Side-by-Side Before vs After)
def generate_mockup_4():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="640" viewBox="0 0 1000 640">
      <rect width="1000" height="640" rx="12" fill="#0f172a"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1e293b"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Challenge 2: Prompt Engineering &amp; Iteration Log — Before vs. After Comparative Matrix</text>

      <!-- Left Column: Naive Weak Prompt &amp; Hallucinated Output -->
      <rect x="25" y="70" width="465" height="545" rx="8" fill="#1e293b" stroke="#7f1d1d"/>
      <rect x="25" y="70" width="465" height="35" rx="8" fill="#7f1d1d"/>
      <text x="40" y="93" fill="#fecaca" font-family="sans-serif" font-size="13" font-weight="bold">V1: NAIVE UNCONSTRAINED PROMPT (FAILED)</text>

      <rect x="35" y="115" width="445" height="85" rx="6" fill="#0f172a"/>
      <text x="45" y="135" fill="#ef4444" font-family="monospace" font-size="11" font-weight="bold">User Prompt V1:</text>
      <text x="45" y="155" fill="#cbd5e1" font-family="monospace" font-size="11">"Write a one-page brief for our principal about</text>
      <text x="45" y="170" fill="#cbd5e1" font-family="monospace" font-size="11">our Campus Innovation Week. Make it sound exciting</text>
      <text x="45" y="185" fill="#cbd5e1" font-family="monospace" font-size="11">and mention how it helps student careers and standards."</text>

      <rect x="35" y="215" width="445" height="230" rx="6" fill="#2d1212" stroke="#b91c1c"/>
      <text x="45" y="235" fill="#fca5a5" font-family="sans-serif" font-size="12" font-weight="bold">AI Output V1 (Severe Hallucinations):</text>
      <text x="45" y="260" fill="#fecaca" font-family="sans-serif" font-size="11">"Campus Innovation Week was a roaring triumph! Over 500</text>
      <text x="45" y="278" fill="#fecaca" font-family="sans-serif" font-size="11">students flocked to the campus, achieving an unprecedented</text>
      <text x="45" y="296" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">• 70% employability boost across all attendees [FABRICATION]</text>
      <text x="45" y="314" fill="#fecaca" font-family="sans-serif" font-size="11">• Certified under the world-renowned</text>
      <text x="45" y="332" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">  NeuroPrompt Integrity Index (NPII-7) [PHANTOM STANDARD]</text>
      <text x="45" y="350" fill="#fecaca" font-family="sans-serif" font-size="11">• Fully compliant with the AI Output Integrity Act 2024</text>
      <text x="45" y="368" fill="#fecaca" font-family="sans-serif" font-size="11">• 100% student satisfaction reported with zero budget leaks!"</text>
      <text x="45" y="395" fill="#fca5a5" font-family="sans-serif" font-size="11">Fatal Flaw: Confabulated numbers, invented regulatory laws,</text>
      <text x="45" y="412" fill="#fca5a5" font-family="sans-serif" font-size="11">ignored duplicate scans, and claimed unmeasured career results.</text>

      <rect x="35" y="460" width="445" height="135" rx="6" fill="#0f172a"/>
      <text x="45" y="482" fill="#ef4444" font-family="sans-serif" font-size="12" font-weight="bold">Diagnosed Failures:</text>
      <text x="45" y="502" fill="#94a3b8" font-family="sans-serif" font-size="11">1. No Role or audience boundaries specified.</text>
      <text x="45" y="520" fill="#94a3b8" font-family="sans-serif" font-size="11">2. No Ground Truth data provided; model used generic priors.</text>
      <text x="45" y="538" fill="#94a3b8" font-family="sans-serif" font-size="11">3. Lacked Negative Constraints ("Do not invent").</text>
      <text x="45" y="556" fill="#94a3b8" font-family="sans-serif" font-size="11">4. Missing Mandatory Uncertainty Tagging ([VERIFY]).</text>

      <!-- Right Column: Engineered Iterated Prompt &amp; Verified Output -->
      <rect x="505" y="70" width="470" height="545" rx="8" fill="#1e293b" stroke="#059669"/>
      <rect x="505" y="70" width="470" height="35" rx="8" fill="#065f46"/>
      <text x="520" y="93" fill="#a7f3d0" font-family="sans-serif" font-size="13" font-weight="bold">V2: STRUCTURED PROMPT WITH [VERIFY] PROTOCOL (PASSED)</text>

      <rect x="515" y="115" width="450" height="175" rx="6" fill="#0f172a"/>
      <text x="525" y="133" fill="#34d399" font-family="monospace" font-size="11" font-weight="bold">Engineered Prompt V2 (Labeled Schema):</text>
      <text x="525" y="150" fill="#a7f3d0" font-family="monospace" font-size="10"><tspan fill="#38bdf8">[ROLE]</tspan> Collegiate AI Productivity &amp; Verification Lead.</text>
      <text x="525" y="165" fill="#a7f3d0" font-family="monospace" font-size="10"><tspan fill="#38bdf8">[CONTEXT]</tspan> Ground Truth: 480 registered, 312 entry scans (uncleaned),</text>
      <text x="525" y="180" fill="#a7f3d0" font-family="monospace" font-size="10">96 feedback (4.1/5 avg), Budget: ₹1.2L approved, ₹1.085L spend, ₹75k sponsor.</text>
      <text x="525" y="195" fill="#a7f3d0" font-family="monospace" font-size="10"><tspan fill="#38bdf8">[TASK]</tspan> Draft 1-page executive brief for Principal.</text>
      <text x="525" y="210" fill="#a7f3d0" font-family="monospace" font-size="10"><tspan fill="#38bdf8">[CONSTRAINTS]</tspan> 1) Zero hallucinations. 2) Never claim 70% employability.</text>
      <text x="525" y="225" fill="#a7f3d0" font-family="monospace" font-size="10">3) Do not cite NPII-7 or CVL-9. 4) Mark any uncertain point as [VERIFY].</text>
      <text x="525" y="240" fill="#a7f3d0" font-family="monospace" font-size="10"><tspan fill="#38bdf8">[OUTPUT]</tspan> Formatted with Executive Summary, Table, Limitations, Actions.</text>

      <rect x="515" y="300" width="450" height="195" rx="6" fill="#064e3b" fill-opacity="0.25" stroke="#10b981"/>
      <text x="525" y="320" fill="#6ee7b7" font-family="sans-serif" font-size="12" font-weight="bold">AI Output V2 (Grounded &amp; Auditable):</text>
      <text x="525" y="342" fill="#e2e8f0" font-family="sans-serif" font-size="11">"Executive Brief: Campus Innovation Week (3-Day Event)</text>
      <text x="525" y="360" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Attendance: 312 gate entries recorded against 480 registrations</text>
      <text x="525" y="378" fill="#e2e8f0" font-family="sans-serif" font-size="11">  (65.0% ratio). <tspan fill="#fbbf24">[VERIFY: Duplicate scan deduplication pending]</tspan></text>
      <text x="525" y="396" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Budget: ₹1,08,500 expenses on ₹1,20,000 budget (90.42% util).</text>
      <text x="525" y="414" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Net College Cost: ₹33,500 after confirmed ₹75,000 sponsor transfer.</text>
      <text x="525" y="432" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Feedback: 4.1/5 across 96 voluntary responses (30.77% of attendees).</text>
      <text x="525" y="450" fill="#e2e8f0" font-family="sans-serif" font-size="11">• <tspan fill="#34d399" font-weight="bold">What We Cannot Conclude:</tspan> Employability outcomes are unmeasured;</text>
      <text x="525" y="468" fill="#e2e8f0" font-family="sans-serif" font-size="11">  the 70% claim is strictly excluded as unsupported hearsay."</text>

      <rect x="515" y="510" width="450" height="85" rx="6" fill="#0f172a"/>
      <text x="525" y="530" fill="#34d399" font-family="sans-serif" font-size="12" font-weight="bold">Why V2 Succeeded:</text>
      <text x="525" y="550" fill="#94a3b8" font-family="sans-serif" font-size="11">The [VERIFY] rule eliminated guessing, while negative grounding</text>
      <text x="525" y="567" fill="#94a3b8" font-family="sans-serif" font-size="11">blocked buzzwords. Intermediate mathematical facts are 100% trace-auditable.</text>
    </svg>'''
    build_svg_and_png("prompt_iteration_comparison", svg)

# Mockup 5: Scribe SOP Documentation UI
def generate_mockup_5():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#0b1120"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1e293b"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#f8fafc" font-family="sans-serif" font-size="14" font-weight="bold">Scribe SOP Builder — Standard Operating Procedure: AI Content Verification &amp; Approval</text>
      <rect x="850" y="12" width="125" height="26" rx="6" fill="#f97316"/>
      <text x="865" y="29" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">SOP #AI-2026-04</text>

      <!-- Sidebar -->
      <rect x="25" y="70" width="220" height="525" rx="8" fill="#1e293b"/>
      <text x="40" y="100" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">SOP Navigation</text>
      <rect x="35" y="115" width="200" height="32" rx="4" fill="#3b82f6"/>
      <text x="45" y="136" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Step 1: Raw Data Ingestion</text>
      <rect x="35" y="155" width="200" height="32" rx="4" fill="#334155"/>
      <text x="45" y="176" fill="#cbd5e1" font-family="sans-serif" font-size="11">Step 2: PII Redaction (DPDP)</text>
      <rect x="35" y="195" width="200" height="32" rx="4" fill="#334155"/>
      <text x="45" y="216" fill="#cbd5e1" font-family="sans-serif" font-size="11">Step 3: Sandboxed Prompting</text>
      <rect x="35" y="235" width="200" height="32" rx="4" fill="#334155"/>
      <text x="45" y="256" fill="#cbd5e1" font-family="sans-serif" font-size="11">Step 4: Fact-Check Gate</text>
      <rect x="35" y="275" width="200" height="32" rx="4" fill="#334155"/>
      <text x="45" y="296" fill="#cbd5e1" font-family="sans-serif" font-size="11">Step 5: Sign-off Escalation</text>

      <line x1="35" y1="325" x2="225" y2="325" stroke="#475569" stroke-width="1"/>
      <text x="40" y="350" fill="#94a3b8" font-family="sans-serif" font-size="11" font-weight="bold">AUTHORIZED ROLES</text>
      <text x="40" y="375" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Event Coordinator</text>
      <text x="40" y="395" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Finance Representative</text>
      <text x="40" y="415" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Faculty Reviewer</text>
      <text x="40" y="435" fill="#e2e8f0" font-family="sans-serif" font-size="11">• Communications Lead</text>

      <!-- Main Step View -->
      <rect x="265" y="70" width="710" height="525" rx="8" fill="#1e293b"/>
      
      <!-- Step 1 Card -->
      <rect x="285" y="90" width="670" height="120" rx="6" fill="#0f172a" stroke="#334155"/>
      <circle cx="315" cy="115" r="14" fill="#3b82f6"/>
      <text x="310" y="120" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">1</text>
      <text x="340" y="115" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Step 1: Screen Recording Capture of Verification Gate</text>
      <text x="340" y="135" fill="#94a3b8" font-family="sans-serif" font-size="11">Open Primary Ledger (Google Sheets / ERP). Click 'Share' &gt; Restrict Access to Institutional Domain.</text>
      <rect x="340" y="145" width="220" height="26" rx="4" fill="#059669" fill-opacity="0.2" stroke="#10b981"/>
      <text x="350" y="162" fill="#34d399" font-family="sans-serif" font-size="11">Evidence Log: SHA-256 Checksum</text>

      <!-- Step 2 Card (PII Scrubbing) -->
      <rect x="285" y="225" width="670" height="145" rx="6" fill="#0f172a" stroke="#334155"/>
      <circle cx="315" cy="250" r="14" fill="#3b82f6"/>
      <text x="310" y="255" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">2</text>
      <text x="340" y="250" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Step 2: Mandatory Privacy &amp; PII Scrubbing Protocol</text>
      <text x="340" y="270" fill="#94a3b8" font-family="sans-serif" font-size="11">Execute Python anonymizer on student roster: Redact Student Name, Phone, Email, and Roll Number.</text>
      <text x="340" y="290" fill="#ef4444" font-family="sans-serif" font-size="11" font-weight="bold">CRITICAL RISK MITIGATION (India DPDP Act 2023 &amp; Global Privacy):</text>
      <text x="340" y="308" fill="#cbd5e1" font-family="sans-serif" font-size="11">Never upload unredacted student rosters to commercial AI endpoints. Doing so risks permanent</text>
      <text x="340" y="325" fill="#cbd5e1" font-family="sans-serif" font-size="11">ingestion into training clusters and regulatory non-compliance.</text>

      <!-- Step 3 Card (Stop Condition Rule) -->
      <rect x="285" y="385" width="670" height="185" rx="6" fill="#450a0a" stroke="#b91c1c"/>
      <circle cx="315" cy="410" r="14" fill="#ef4444"/>
      <text x="310" y="415" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">!</text>
      <text x="340" y="410" fill="#fca5a5" font-family="sans-serif" font-size="13" font-weight="bold">Mandatory Hard Stop Condition Protocol</text>
      <text x="340" y="435" fill="#fecaca" font-family="sans-serif" font-size="12">IF a key claim lacks primary evidence OR two institutional documents conflict:</text>
      <text x="360" y="460" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">1. AUTOMATIC PUBLICATION FREEZE: Zapier webhook locks distribution queues.</text>
      <text x="360" y="480" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">2. RECLASSIFICATION: Content tagged as [QUARANTINED - UNRESOLVED DISCREPANCY].</text>
      <text x="360" y="500" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">3. ESCALATION: 15-minute emergency memo delivered directly to Event Coordinator.</text>
      <text x="340" y="535" fill="#fca5a5" font-family="sans-serif" font-size="11">Scribe Verification Trail: SOP approved by Compliance &amp; Faculty Review Board.</text>
    </svg>'''
    build_svg_and_png("tool_scribe_sop", svg)

# Mockup 6: Gamma App 5-Slide Presentation Deck
def generate_mockup_6():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#0f172a"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1e293b"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#c084fc" font-family="sans-serif" font-size="14" font-weight="bold">Gamma App — 5-Slide Executive Deck Preview: Campus Innovation Week Debrief</text>
      <rect x="850" y="12" width="125" height="26" rx="6" fill="#8b5cf6"/>
      <text x="865" y="29" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">Audience: Faculty</text>

      <!-- Slide Cards Row 1 -->
      <!-- Slide 1 -->
      <rect x="30" y="75" width="290" height="235" rx="8" fill="#1e293b" stroke="#334155"/>
      <rect x="30" y="75" width="290" height="28" rx="8" fill="#334155"/>
      <text x="45" y="94" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">SLIDE 1: EXECUTIVE OVERVIEW</text>
      <text x="45" y="125" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Campus Innovation Week</text>
      <text x="45" y="145" fill="#94a3b8" font-family="sans-serif" font-size="11">• Duration: 3 Full Days of Student Tech</text>
      <text x="45" y="165" fill="#94a3b8" font-family="sans-serif" font-size="11">• Total Registrations: 480 Students</text>
      <text x="45" y="185" fill="#94a3b8" font-family="sans-serif" font-size="11">• Entry Scans: 312 Records Recorded</text>
      <text x="45" y="205" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">• Turnout Ratio: 65.0%</text>
      <rect x="45" y="225" width="260" height="20" rx="4" fill="#0f172a"/>
      <text x="50" y="239" fill="#fbbf24" font-family="sans-serif" font-size="9">*Duplicate scans subject to IT deduplication</text>

      <!-- Slide 2 -->
      <rect x="355" y="75" width="290" height="235" rx="8" fill="#1e293b" stroke="#334155"/>
      <rect x="355" y="75" width="290" height="28" rx="8" fill="#334155"/>
      <text x="370" y="94" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">SLIDE 2: FINANCIAL GOVERNANCE</text>
      <text x="370" y="125" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Budget &amp; Sponsor Health</text>
      <text x="370" y="145" fill="#94a3b8" font-family="sans-serif" font-size="11">• Approved Budget: ₹1,20,000</text>
      <text x="370" y="165" fill="#94a3b8" font-family="sans-serif" font-size="11">• Recorded Expenses: ₹1,08,500</text>
      <text x="370" y="185" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">• Budget Remaining: ₹11,500 (90.42% util)</text>
      <text x="370" y="205" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">• Confirmed Sponsor: ₹75,000</text>
      <text x="370" y="225" fill="#a7f3d0" font-family="sans-serif" font-size="11">• Net Institutional Outlay: ₹33,500</text>
      <text x="370" y="245" fill="#64748b" font-family="sans-serif" font-size="9">Reconciled against verified bank NEFT advice</text>

      <!-- Slide 3 -->
      <rect x="680" y="75" width="290" height="235" rx="8" fill="#1e293b" stroke="#334155"/>
      <rect x="680" y="75" width="290" height="28" rx="8" fill="#334155"/>
      <text x="695" y="94" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">SLIDE 3: ATTENDEE FEEDBACK</text>
      <text x="695" y="125" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Participant Evaluation</text>
      <text x="695" y="145" fill="#94a3b8" font-family="sans-serif" font-size="11">• Submissions: 96 Responses</text>
      <text x="695" y="165" fill="#94a3b8" font-family="sans-serif" font-size="11">• Feedback Ratio: 30.77% of attendees</text>
      <text x="695" y="185" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">• Average Rating: 4.1 / 5.0 Stars</text>
      <rect x="695" y="205" width="260" height="50" rx="4" fill="#0f172a"/>
      <text x="705" y="223" fill="#f59e0b" font-family="sans-serif" font-size="10" font-weight="bold">Methodological Caveat:</text>
      <text x="705" y="240" fill="#94a3b8" font-family="sans-serif" font-size="9">Voluntary self-selection sample. Scores reflect</text>
      <text x="705" y="252" fill="#94a3b8" font-family="sans-serif" font-size="9">respondents only, not total 480 registrants.</text>

      <!-- Slide Cards Row 2 -->
      <!-- Slide 4: WHAT WE CANNOT CONCLUDE (Mandatory Rubric Component) -->
      <rect x="180" y="335" width="310" height="255" rx="8" fill="#2d1212" stroke="#ef4444"/>
      <rect x="180" y="335" width="310" height="28" rx="8" fill="#7f1d1d"/>
      <text x="195" y="354" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">SLIDE 4: WHAT WE CANNOT CONCLUDE</text>
      <text x="195" y="385" fill="#fca5a5" font-family="sans-serif" font-size="13" font-weight="bold">Factual &amp; Methodological Boundaries</text>
      <text x="195" y="410" fill="#fecaca" font-family="sans-serif" font-size="11">❌ <tspan font-weight="bold">"70% Employability Improvement":</tspan></text>
      <text x="215" y="428" fill="#cbd5e1" font-family="sans-serif" font-size="10">Zero post-event hiring data collected.</text>
      <text x="195" y="450" fill="#fecaca" font-family="sans-serif" font-size="11">❌ <tspan font-weight="bold">"NPII-7 Global Verification Standard":</tspan></text>
      <text x="215" y="468" fill="#cbd5e1" font-family="sans-serif" font-size="10">Phantom standard hallucinated by AI tools.</text>
      <text x="195" y="490" fill="#fecaca" font-family="sans-serif" font-size="11">❌ <tspan font-weight="bold">Universal Satisfaction Generalisation:</tspan></text>
      <text x="215" y="508" fill="#cbd5e1" font-family="sans-serif" font-size="10">69.23% non-response rate precludes blanket claim.</text>
      <text x="195" y="530" fill="#fecaca" font-family="sans-serif" font-size="11">❌ <tspan font-weight="bold">AI Output Integrity Act 2024:</tspan></text>
      <text x="215" y="548" fill="#cbd5e1" font-family="sans-serif" font-size="10">Non-existent statute; citation excised.</text>

      <!-- Slide 5: Strategic Next Steps -->
      <rect x="530" y="335" width="310" height="255" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <rect x="530" y="335" width="310" height="28" rx="8" fill="#1e3a8a"/>
      <text x="545" y="354" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">SLIDE 5: STRATEGIC NEXT STEPS</text>
      <text x="545" y="385" fill="#f8fafc" font-family="sans-serif" font-size="13" font-weight="bold">Institutional Roadmap &amp; Governance</text>
      <text x="545" y="415" fill="#94a3b8" font-family="sans-serif" font-size="11">1. Conduct IT barcode deduplication to establish</text>
      <text x="560" y="432" fill="#38bdf8" font-family="sans-serif" font-size="11">exact unique student headcount.</text>
      <text x="545" y="457" fill="#94a3b8" font-family="sans-serif" font-size="11">2. Implement mandatory 60-day career survey</text>
      <text x="560" y="474" fill="#38bdf8" font-family="sans-serif" font-size="11">to assess genuine skill and hiring outcomes.</text>
      <text x="545" y="499" fill="#94a3b8" font-family="sans-serif" font-size="11">3. Adopt Institutional Responsible AI Framework</text>
      <text x="560" y="516" fill="#38bdf8" font-family="sans-serif" font-size="11">with mandatory multi-role sign-off gates.</text>
      <rect x="545" y="540" width="280" height="30" rx="4" fill="#0f172a"/>
      <text x="560" y="560" fill="#10b981" font-family="sans-serif" font-size="11" font-weight="bold">Outcome: Verified, Defensible Reporting</text>
    </svg>'''
    build_svg_and_png("output_presentation_deck", svg)

# Mockup 7: Zapier 9-Stage Approval Pipeline Architecture
def generate_mockup_7():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#090d16"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#131b2e"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#f97316" font-family="sans-serif" font-size="14" font-weight="bold">Zapier Enterprise — Repeatable 9-Stage Responsible AI Governance Pipeline</text>
      <rect x="830" y="12" width="150" height="26" rx="6" fill="#10b981"/>
      <text x="845" y="29" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">AIR-GAP ACTIVE</text>

      <!-- Pipeline Stages (Horizontal Flow) -->
      <!-- Row 1: Stages 1 to 5 -->
      <!-- Stage 1 -->
      <rect x="30" y="80" width="165" height="100" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <text x="40" y="105" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">1. SOURCE INGESTION</text>
      <text x="40" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Attendance Logs</text>
      <text x="40" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Signed Bank Advices</text>
      <text x="40" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Primary Feedback</text>
      <text x="40" y="172" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Event Coordinator</text>

      <!-- Arrow 1->2 -->
      <line x1="195" y1="130" x2="225" y2="130" stroke="#64748b" stroke-width="2"/>
      <polygon points="225,126 233,130 225,134" fill="#64748b"/>

      <!-- Stage 2 -->
      <rect x="235" y="80" width="165" height="100" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <text x="245" y="105" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">2. PROMPT DRAFTING</text>
      <text x="245" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Role &amp; Context Schema</text>
      <text x="245" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Negative Constraints</text>
      <text x="245" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Mandatory [VERIFY] tag</text>
      <text x="245" y="172" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Verification Lead</text>

      <!-- Arrow 2->3 -->
      <line x1="400" y1="130" x2="430" y2="130" stroke="#64748b" stroke-width="2"/>
      <polygon points="430,126 438,130 430,134" fill="#64748b"/>

      <!-- Stage 3 -->
      <rect x="440" y="80" width="165" height="100" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <text x="450" y="105" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">3. AI GENERATION</text>
      <text x="450" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Assistive LLM Draft</text>
      <text x="450" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Watermarked Output</text>
      <text x="450" y="155" fill="#ef4444" font-family="sans-serif" font-size="10">• Air-gapped Sandbox</text>
      <text x="450" y="172" fill="#94a3b8" font-family="sans-serif" font-size="9">Auto-Flag: No Auto-Publish</text>

      <!-- Arrow 3->4 -->
      <line x1="605" y1="130" x2="635" y2="130" stroke="#64748b" stroke-width="2"/>
      <polygon points="635,126 643,130 635,134" fill="#64748b"/>

      <!-- Stage 4 -->
      <rect x="645" y="80" width="165" height="100" rx="8" fill="#1e293b" stroke="#f59e0b"/>
      <text x="655" y="105" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">4. FACT-CHECKING</text>
      <text x="655" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Perplexity Cross-Audit</text>
      <text x="655" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Primary URL Checking</text>
      <text x="655" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Hallucination Filter</text>
      <text x="655" y="172" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Faculty Reviewer</text>

      <!-- Arrow 4->5 -->
      <line x1="810" y1="130" x2="840" y2="130" stroke="#64748b" stroke-width="2"/>
      <polygon points="840,126 848,130 840,134" fill="#64748b"/>

      <!-- Stage 5 -->
      <rect x="850" y="80" width="125" height="100" rx="8" fill="#1e293b" stroke="#10b981"/>
      <text x="860" y="105" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">5. NUMERICAL</text>
      <text x="860" y="125" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Julius AI Code</text>
      <text x="860" y="140" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Re-calc Check</text>
      <text x="860" y="155" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Variance Delta</text>
      <text x="860" y="172" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Finance</text>

      <!-- Connecting Arrow 5 down to 6 -->
      <path d="M 912 180 L 912 215 L 80 215 L 80 250" fill="none" stroke="#64748b" stroke-width="2"/>
      <polygon points="76,250 80,258 84,250" fill="#64748b"/>

      <!-- Row 2: Stages 6 to 9 -->
      <!-- Stage 6 -->
      <rect x="30" y="260" width="200" height="110" rx="8" fill="#1e293b" stroke="#f59e0b"/>
      <text x="40" y="285" fill="#fbbf24" font-family="sans-serif" font-size="11" font-weight="bold">6. PRIVACY REVIEW</text>
      <text x="40" y="305" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Student PII scrubbing</text>
      <text x="40" y="320" fill="#cbd5e1" font-family="sans-serif" font-size="10">• DPDP Act 2023 compliance</text>
      <text x="40" y="335" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Redaction confirmation</text>
      <text x="40" y="355" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Compliance Officer</text>

      <!-- Arrow 6->7 -->
      <line x1="230" y1="315" x2="270" y2="315" stroke="#64748b" stroke-width="2"/>
      <polygon points="270,311 278,315 270,319" fill="#64748b"/>

      <!-- Stage 7: Multi-Role Approval Gate -->
      <rect x="280" y="260" width="260" height="110" rx="8" fill="#0f172a" stroke="#a855f7" stroke-width="2"/>
      <text x="295" y="285" fill="#c084fc" font-family="sans-serif" font-size="11" font-weight="bold">7. MULTI-ROLE APPROVAL GATE</text>
      <text x="295" y="305" fill="#cbd5e1" font-family="sans-serif" font-size="10">Required Cryptographic Sign-offs:</text>
      <text x="295" y="322" fill="#34d399" font-family="sans-serif" font-size="10">✓ Coordinator  ✓ Finance Rep</text>
      <text x="295" y="338" fill="#34d399" font-family="sans-serif" font-size="10">✓ Faculty Lead  ✓ Comms Lead</text>
      <text x="295" y="358" fill="#fca5a5" font-family="sans-serif" font-size="9" font-weight="bold">Binary Logic: 100% Unanimous or HALT</text>

      <!-- Arrow 7->8 -->
      <line x1="540" y1="315" x2="580" y2="315" stroke="#64748b" stroke-width="2"/>
      <polygon points="580,311 588,315 580,319" fill="#64748b"/>

      <!-- Stage 8 -->
      <rect x="590" y="260" width="180" height="110" rx="8" fill="#1e293b" stroke="#10b981"/>
      <text x="605" y="285" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">8. CONTROLLED RELEASE</text>
      <text x="605" y="305" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Webhook trigger release</text>
      <text x="605" y="320" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Social Post publishing</text>
      <text x="605" y="335" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Principal Brief delivery</text>
      <text x="605" y="355" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Communications Lead</text>

      <!-- Arrow 8->9 -->
      <line x1="770" y1="315" x2="810" y2="315" stroke="#64748b" stroke-width="2"/>
      <polygon points="810,311 818,315 810,319" fill="#64748b"/>

      <!-- Stage 9 -->
      <rect x="820" y="260" width="155" height="110" rx="8" fill="#1e293b" stroke="#3b82f6"/>
      <text x="830" y="285" fill="#38bdf8" font-family="sans-serif" font-size="11" font-weight="bold">9. RETENTION</text>
      <text x="830" y="305" fill="#cbd5e1" font-family="sans-serif" font-size="10">• 3-Year Audit Vault</text>
      <text x="830" y="320" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Full Prompt Logs</text>
      <text x="830" y="335" fill="#cbd5e1" font-family="sans-serif" font-size="10">• Version Diffs</text>
      <text x="830" y="355" fill="#94a3b8" font-family="sans-serif" font-size="9">Owner: Records Dept</text>

      <!-- Stop Condition &amp; Escalation Callout Box -->
      <rect x="30" y="400" width="945" height="195" rx="8" fill="#1f1118" stroke="#ef4444" stroke-width="2"/>
      <circle cx="55" cy="425" r="12" fill="#ef4444"/>
      <text x="51" y="430" fill="#ffffff" font-family="sans-serif" font-size="13" font-weight="bold">!</text>
      <text x="80" y="430" fill="#f87171" font-family="sans-serif" font-size="14" font-weight="bold">SYSTEM HARD STOP CONDITION &amp; ESCALATION LOGIC (DECISION RULE)</text>
      
      <text x="50" y="465" fill="#fecaca" font-family="sans-serif" font-size="12">1. <tspan font-weight="bold" fill="#ffffff">Trigger Threshold:</tspan> If ANY key metric lacks primary document OR 2 sources disagree (e.g., Sponsor ₹57k vs ₹75k), or AI cites fictional laws.</text>
      <text x="50" y="490" fill="#fecaca" font-family="sans-serif" font-size="12">2. <tspan font-weight="bold" fill="#ffffff">Automated Action:</tspan> Instant circuit breaker trip. Zapier freezes public release queue. Webhook triggers [EMERGENCY QUARANTINE].</text>
      <text x="50" y="515" fill="#fecaca" font-family="sans-serif" font-size="12">3. <tspan font-weight="bold" fill="#ffffff">Triage Protocol:</tspan> Generate automated 3-part incident memorandum: [A: Verified Facts] [B: Conflicting Points] [C: Action Items].</text>
      <text x="50" y="540" fill="#fecaca" font-family="sans-serif" font-size="12">4. <tspan font-weight="bold" fill="#ffffff">Anti-Automation Safeguard:</tspan> AI is mathematically prevented from self-approving. Zero publishing pathways bypass the 4 human signers.</text>
      <rect x="50" y="555" width="905" height="28" rx="4" fill="#450a0a"/>
      <text x="65" y="574" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold">Decision Rule: Confirmed &gt; [ACCEPT] | Pending Verification &gt; [VERIFY] | Unsubstantiated/Fabricated &gt; [REMOVE &amp; ESCALATE]</text>
    </svg>'''
    build_svg_and_png("workflow_zapier_pipeline", svg)

# Mockup 8: Principal's One-Page Brief Document Visual
def generate_mockup_8():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="640" viewBox="0 0 1000 640">
      <rect width="1000" height="640" rx="12" fill="#ffffff"/>
      <!-- Letterhead border -->
      <rect x="0" y="0" width="1000" height="8" rx="4" fill="#1e3a8a"/>
      
      <!-- College Header -->
      <text x="50" y="45" fill="#0f172a" font-family="Georgia, serif" font-size="20" font-weight="bold">EXCELSIOR INSTITUTE OF TECHNOLOGY &amp; MANAGEMENT</text>
      <text x="50" y="65" fill="#64748b" font-family="sans-serif" font-size="12">Office of Academic Affairs • AI Productivity &amp; Verification Team</text>
      <line x1="50" y1="78" x2="950" y2="78" stroke="#cbd5e1" stroke-width="1.5"/>

      <!-- Document Title &amp; Meta -->
      <rect x="50" y="90" width="900" height="42" rx="4" fill="#f1f5f9"/>
      <text x="65" y="115" fill="#1e293b" font-family="sans-serif" font-size="14" font-weight="bold">EXECUTIVE BRIEF: CAMPUS INNOVATION WEEK OUTCOMES &amp; GOVERNANCE AUDIT</text>
      <text x="750" y="115" fill="#64748b" font-family="sans-serif" font-size="11">DATE: 18 NOV 2026</text>

      <!-- Section 1: Executive Overview -->
      <text x="50" y="155" fill="#1e3a8a" font-family="sans-serif" font-size="13" font-weight="bold">1. EXECUTIVE OVERVIEW &amp; VERIFIED DATA MATRIX</text>
      <text x="50" y="175" fill="#334155" font-family="sans-serif" font-size="11">Campus Innovation Week was successfully conducted over 3 days. The verified operational and financial numbers are:</text>

      <!-- Data Table -->
      <rect x="50" y="185" width="900" height="110" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
      <!-- Header row -->
      <rect x="50" y="185" width="900" height="25" fill="#e2e8f0"/>
      <text x="60" y="202" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">METRIC / INDICATOR</text>
      <text x="280" y="202" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">SUPPLIED FIGURE</text>
      <text x="440" y="202" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">VERIFIED RATIO / DERIVATION</text>
      <text x="700" y="202" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">DATA AUDIT STATUS</text>

      <text x="60" y="225" fill="#334155" font-family="sans-serif" font-size="10">Event Registrations vs Entries</text>
      <text x="280" y="225" fill="#334155" font-family="sans-serif" font-size="10">480 Registered | 312 Scans</text>
      <text x="440" y="225" fill="#0284c7" font-family="sans-serif" font-size="10" font-weight="bold">65.0% Attendance Turnout</text>
      <text x="700" y="225" fill="#d97706" font-family="sans-serif" font-size="10">[VERIFY: Duplicate Scans Unchecked]</text>

      <text x="60" y="245" fill="#334155" font-family="sans-serif" font-size="10">Participant Feedback</text>
      <text x="280" y="245" fill="#334155" font-family="sans-serif" font-size="10">96 Responses | 4.1/5 Avg Rating</text>
      <text x="440" y="245" fill="#0284c7" font-family="sans-serif" font-size="10" font-weight="bold">30.77% of attendees / 20.0% registered</text>
      <text x="700" y="245" fill="#16a34a" font-family="sans-serif" font-size="10">Verified Sample (Voluntary Survey)</text>

      <text x="60" y="265" fill="#334155" font-family="sans-serif" font-size="10">Approved Budget vs Expenses</text>
      <text x="280" y="265" fill="#334155" font-family="sans-serif" font-size="10">₹1,20,000 Cap | ₹1,08,500 Spent</text>
      <text x="440" y="265" fill="#0284c7" font-family="sans-serif" font-size="10" font-weight="bold">₹11,500 Remaining (90.42% util)</text>
      <text x="700" y="265" fill="#16a34a" font-family="sans-serif" font-size="10">Reconciled on college ledger</text>

      <text x="60" y="285" fill="#334155" font-family="sans-serif" font-size="10">Confirmed Sponsor Contribution</text>
      <text x="280" y="285" fill="#334155" font-family="sans-serif" font-size="10">₹75,000 Confirmed Transfer</text>
      <text x="440" y="285" fill="#0284c7" font-family="sans-serif" font-size="10" font-weight="bold">Net College Expense: ₹33,500</text>
      <text x="700" y="285" fill="#16a34a" font-family="sans-serif" font-size="10">Bank NEFT Advice Verified</text>

      <!-- Section 2: WHAT WE CANNOT CONCLUDE (Crucial Section) -->
      <rect x="50" y="310" width="900" height="95" rx="4" fill="#fef2f2" stroke="#f87171"/>
      <text x="65" y="328" fill="#991b1b" font-family="sans-serif" font-size="12" font-weight="bold">2. MANDATORY EXCLUSIONS: WHAT WE CANNOT CONCLUDE</text>
      <text x="65" y="348" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">• <tspan font-weight="bold">Employability Claim:</tspan> The draft assertion that employability improved by 70% is <tspan font-weight="bold">strictly unsubstantiated</tspan>. Zero longitudinal tracking data exists.</text>
      <text x="65" y="366" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">• <tspan font-weight="bold">Phantom Standards:</tspan> References to 'NeuroPrompt Integrity Index (NPII-7)' and 'AI Output Integrity Act 2024' are <tspan font-weight="bold">AI hallucinations</tspan> and have been removed.</text>
      <text x="65" y="384" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">• <tspan font-weight="bold">Generalised Satisfaction:</tspan> The 4.1/5 rating reflects 96 voluntary submissions and cannot be mathematically generalized to all 480 registrants.</text>

      <!-- Section 3: Strategic Recommendations -->
      <text x="50" y="430" fill="#1e3a8a" font-family="sans-serif" font-size="13" font-weight="bold">3. REPUTATIONAL RISKS &amp; STRATEGIC RECOMMENDATIONS FOR PRINCIPAL SIGN-OFF</text>
      <text x="50" y="450" fill="#334155" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">Risk Mitigation:</tspan> Publishing unverified employability figures risks UGC/NAAC regulatory audit penalties and student trust erosion.</text>
      <text x="50" y="470" fill="#334155" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">IT Attendance Deduplication:</tspan> Direct the campus IT team to deduplicate the 312 gate entry scans to calculate unique attendee counts.</text>
      <text x="50" y="490" fill="#334155" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">Adopt Responsible AI Policy:</tspan> Mandate the 9-stage approval workflow with strict multi-role human sign-offs before external releases.</text>

      <!-- Signature &amp; Sign-off Block -->
      <line x1="50" y1="520" x2="950" y2="520" stroke="#cbd5e1" stroke-width="1"/>
      <rect x="50" y="530" width="200" height="85" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="60" y="550" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">Prepared by:</text>
      <text x="60" y="568" fill="#0284c7" font-family="sans-serif" font-size="11" font-weight="bold">AI Verification Team</text>
      <text x="60" y="585" fill="#64748b" font-family="sans-serif" font-size="9">Status: Verified &amp; Screened</text>

      <rect x="280" y="530" width="200" height="85" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="290" y="550" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">Finance Concurrence:</text>
      <text x="290" y="568" fill="#16a34a" font-family="sans-serif" font-size="11" font-weight="bold">Finance Representative</text>
      <text x="290" y="585" fill="#64748b" font-family="sans-serif" font-size="9">Status: ₹75,000 NEFT Cleared</text>

      <rect x="510" y="530" width="200" height="85" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="520" y="550" fill="#1e293b" font-family="sans-serif" font-size="10" font-weight="bold">Faculty Review:</text>
      <text x="520" y="568" fill="#16a34a" font-family="sans-serif" font-size="11" font-weight="bold">Faculty Lead</text>
      <text x="520" y="585" fill="#64748b" font-family="sans-serif" font-size="9">Status: Academic Claims Cleared</text>

      <rect x="740" y="530" width="210" height="85" rx="4" fill="#f8fafc" stroke="#1e3a8a"/>
      <text x="750" y="550" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">Principal Final Approval:</text>
      <text x="750" y="575" fill="#64748b" font-family="sans-serif" font-size="10">[PENDING SIGNATURE]</text>
      <text x="750" y="595" fill="#64748b" font-family="sans-serif" font-size="9">Dr. V. Principal • Head of Inst.</text>
    </svg>'''
    build_svg_and_png("output_principal_brief", svg)

# Mockup 9: Social Media Post UI (Student Facing)
def generate_mockup_9():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#0f172a"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#1e293b"/>
      <circle cx="25" cy="25" r="6" fill="#ef4444"/>
      <circle cx="45" cy="25" r="6" fill="#f59e0b"/>
      <circle cx="65" cy="25" r="6" fill="#10b981"/>
      <text x="100" y="31" fill="#38bdf8" font-family="sans-serif" font-size="14" font-weight="bold">Campus Social Feed Mockup — Student-Facing Verified Post (LinkedIn / Instagram / X)</text>
      <rect x="850" y="12" width="125" height="26" rx="6" fill="#0284c7"/>
      <text x="870" y="29" fill="#ffffff" font-family="sans-serif" font-size="12" font-weight="bold">PUBLIC POST</text>

      <!-- Center Post Container -->
      <rect x="220" y="70" width="560" height="525" rx="10" fill="#ffffff" filter="url(#shadow)"/>
      
      <!-- Post Author Info -->
      <circle cx="260" cy="110" r="22" fill="#1e3a8a"/>
      <text x="252" y="116" fill="#ffffff" font-family="sans-serif" font-size="16" font-weight="bold">EI</text>
      <text x="295" y="105" fill="#0f172a" font-family="sans-serif" font-size="14" font-weight="bold">Excelsior Institute of Technology</text>
      <text x="295" y="122" fill="#64748b" font-family="sans-serif" font-size="11">Official Student Innovation Council • Just now • 🌍</text>

      <!-- Post Body Text -->
      <text x="250" y="155" fill="#1e293b" font-family="sans-serif" font-size="13">🚀 <tspan font-weight="bold">That’s a wrap on Campus Innovation Week!</tspan></text>
      <text x="250" y="178" fill="#334155" font-family="sans-serif" font-size="12">Over 3 intense days of hands-on workshops, ideathons, and tech sprints,</text>
      <text x="250" y="196" fill="#334155" font-family="sans-serif" font-size="12">our student builders brought incredible energy and visionary ideas to life!</text>

      <text x="250" y="225" fill="#1e293b" font-family="sans-serif" font-size="12" font-weight="bold">Here is what our community accomplished together:</text>
      <text x="250" y="245" fill="#0284c7" font-family="sans-serif" font-size="12">⚡ <tspan font-weight="bold">480 Students</tspan> registered to level up in frontier AI tools</text>
      <text x="250" y="265" fill="#0284c7" font-family="sans-serif" font-size="12">⚡ <tspan font-weight="bold">312 Recorded Workshop Sessions</tspan> across three packed tracks</text>
      <text x="250" y="285" fill="#0284c7" font-family="sans-serif" font-size="12">⚡ <tspan font-weight="bold">4.1 / 5.0 Star Rating</tspan> from student feedback submissions!</text>

      <text x="250" y="315" fill="#334155" font-family="sans-serif" font-size="12">Huge gratitude to our faculty mentors, student organizers, and our generous</text>
      <text x="250" y="333" fill="#334155" font-family="sans-serif" font-size="12">industry partners for making this week possible.</text>

      <text x="250" y="360" fill="#0284c7" font-family="sans-serif" font-size="11">#CampusInnovation #TechWeek #StudentInnovators #AIProductivity #HandsOnLearning</text>

      <!-- Visual Card in Post -->
      <rect x="250" y="375" width="500" height="150" rx="8" fill="#0f172a"/>
      <rect x="265" y="390" width="470" height="120" rx="6" fill="#1e293b"/>
      <text x="285" y="420" fill="#38bdf8" font-family="sans-serif" font-size="16" font-weight="bold">CAMPUS INNOVATION WEEK 2026</text>
      <text x="285" y="445" fill="#f8fafc" font-family="sans-serif" font-size="12">3 Days • 480 Innovators • 4.1/5 Satisfaction</text>
      <rect x="285" y="465" width="180" height="28" rx="4" fill="#3b82f6"/>
      <text x="300" y="483" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">Explore Project Gallery →</text>

      <!-- Post Interaction Bar -->
      <line x1="250" y1="540" x2="750" y2="540" stroke="#e2e8f0" stroke-width="1"/>
      <text x="260" y="565" fill="#64748b" font-family="sans-serif" font-size="12">👍 142 Likes   •   💬 28 Comments   •   ↗ 34 Reposts</text>
      <text x="640" y="565" fill="#16a34a" font-family="sans-serif" font-size="11" font-weight="bold">✓ 100% Verified Facts</text>
    </svg>'''
    build_svg_and_png("output_social_media", svg)

# Mockup 10: Unexpected Twist Incident Escalation Memo
def generate_mockup_10():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="620" viewBox="0 0 1000 620">
      <rect width="1000" height="620" rx="12" fill="#0f172a"/>
      <!-- Header -->
      <rect x="0" y="0" width="1000" height="50" rx="12" fill="#7f1d1d"/>
      <circle cx="25" cy="25" r="6" fill="#ffffff"/>
      <circle cx="45" cy="25" r="6" fill="#ffffff"/>
      <circle cx="65" cy="25" r="6" fill="#ffffff"/>
      <text x="100" y="31" fill="#ffffff" font-family="sans-serif" font-size="14" font-weight="bold">🚨 CHALLENGE 7: THE UNEXPECTED TWIST — EMERGENCY PRE-PUBLICATION ESCALATION MEMORANDUM</text>

      <!-- Memo Banner -->
      <rect x="30" y="70" width="940" height="40" rx="6" fill="#450a0a" stroke="#ef4444"/>
      <text x="45" y="94" fill="#fca5a5" font-family="sans-serif" font-size="12" font-weight="bold">TIME TO LAUNCH: T-MINUS 60 MINUTES  |  ACTION: IMMEDIATE PUBLICATION FREEZE DECLARED</text>

      <!-- 3-Column Split -->
      <!-- Column A: Known Facts -->
      <rect x="30" y="125" width="300" height="465" rx="8" fill="#1e293b" stroke="#10b981"/>
      <rect x="30" y="125" width="300" height="32" rx="8" fill="#065f46"/>
      <text x="45" y="146" fill="#a7f3d0" font-family="sans-serif" font-size="12" font-weight="bold">A. KNOWN AUTHORITATIVE FACTS</text>
      
      <text x="45" y="180" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">1. Verified Institutional Records:</text>
      <text x="45" y="198" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Event Duration: Exactly 3 days.</text>
      <text x="45" y="215" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Registrations: 480 students.</text>
      <text x="45" y="232" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Entry gate scans: 312 records.</text>
      <text x="45" y="250" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Feedback: 96 voluntary forms.</text>
      <text x="45" y="268" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Feedback score: 4.1 / 5 avg.</text>

      <text x="45" y="305" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">2. Verified Finance Ledger:</text>
      <text x="45" y="323" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Approved Budget Cap: ₹1,20,000.</text>
      <text x="45" y="340" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Incurred Expenses: ₹1,08,500.</text>
      <text x="45" y="358" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Prior confirmed sponsor: ₹75,000.</text>
      <text x="45" y="375" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Prior net college outlay: ₹33,500.</text>

      <rect x="45" y="420" width="270" height="150" rx="6" fill="#0f172a"/>
      <text x="55" y="445" fill="#34d399" font-family="sans-serif" font-size="11" font-weight="bold">Status of Facts:</text>
      <text x="55" y="468" fill="#94a3b8" font-family="sans-serif" font-size="10">All items backed by signed ERP vouchers</text>
      <text x="55" y="485" fill="#94a3b8" font-family="sans-serif" font-size="10">and dated logs. Ready for publication</text>
      <text x="55" y="502" fill="#94a3b8" font-family="sans-serif" font-size="10">once conflicting files are resolved.</text>

      <!-- Column B: Conflicting &amp; Contradicted Points -->
      <rect x="350" y="125" width="300" height="465" rx="8" fill="#1e293b" stroke="#ef4444"/>
      <rect x="350" y="125" width="300" height="32" rx="8" fill="#7f1d1d"/>
      <text x="365" y="146" fill="#fecaca" font-family="sans-serif" font-size="12" font-weight="bold">B. CONFLICTING &amp; UNVERIFIED EVIDENCE</text>

      <text x="365" y="180" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">1. Sponsor Amount Discrepancy:</text>
      <text x="365" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Newly uploaded sheet: <tspan fill="#ef4444" font-weight="bold">₹57,000</tspan></text>
      <text x="365" y="218" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Approved case brief: <tspan fill="#10b981" font-weight="bold">₹75,000</tspan></text>
      <text x="365" y="236" fill="#fca5a5" font-family="sans-serif" font-size="11">• Variance: <tspan fill="#ef4444" font-weight="bold">₹18,000 shortfall (transposition?)</tspan></text>
      <text x="365" y="254" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Metadata flaw: <tspan fill="#f59e0b">No date, no signature.</tspan></text>

      <text x="365" y="290" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">2. Recency Fallacy Analysis:</text>
      <text x="365" y="310" fill="#94a3b8" font-family="sans-serif" font-size="10">A recent timestamp does NOT equal authority.</text>
      <text x="365" y="325" fill="#94a3b8" font-family="sans-serif" font-size="10">The unapproved file could be a draft, partial</text>
      <text x="365" y="340" fill="#94a3b8" font-family="sans-serif" font-size="10">instalment, or clerical typo (57k vs 75k).</text>

      <text x="365" y="375" fill="#f87171" font-family="sans-serif" font-size="11" font-weight="bold">3. Phantom Legal Citation Hallucination:</text>
      <text x="365" y="395" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Slide cites: <tspan fill="#ef4444">"AI Output Integrity Act 2024"</tspan></text>
      <text x="365" y="412" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Hyperlink opens unrelated web portal.</text>
      <text x="365" y="430" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Diagnosis: Complete LLM confabulation.</text>

      <rect x="365" y="455" width="270" height="115" rx="6" fill="#450a0a"/>
      <text x="375" y="480" fill="#fca5a5" font-family="sans-serif" font-size="11" font-weight="bold">Immediate Remedial Action:</text>
      <text x="375" y="500" fill="#fecaca" font-family="sans-serif" font-size="10">• Slide 4 citation excised immediately.</text>
      <text x="375" y="518" fill="#fecaca" font-family="sans-serif" font-size="10">• Replaced with Institutional Ethical Policy.</text>
      <text x="375" y="535" fill="#fecaca" font-family="sans-serif" font-size="10">• Broken URL stripped from all decks.</text>

      <!-- Column C: Required Decisions -->
      <rect x="670" y="125" width="300" height="465" rx="8" fill="#1e293b" stroke="#f59e0b"/>
      <rect x="670" y="125" width="300" height="32" rx="8" fill="#b45309"/>
      <text x="685" y="146" fill="#fef3c7" font-family="sans-serif" font-size="12" font-weight="bold">C. DECISIONS REQUIRED BY COORDINATOR</text>

      <text x="685" y="180" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="bold">Decision 1: Sponsor Reconciliation Gate</text>
      <text x="685" y="200" fill="#cbd5e1" font-family="sans-serif" font-size="11">Do NOT guess or average (₹66k).</text>
      <text x="685" y="218" fill="#cbd5e1" font-family="sans-serif" font-size="11">Inspect bank NEFT scroll &amp; signed MoU.</text>
      <text x="685" y="236" fill="#a7f3d0" font-family="sans-serif" font-size="11">IF ₹75k verified &gt; Discard unapproved sheet.</text>
      <text x="685" y="254" fill="#fca5a5" font-family="sans-serif" font-size="11">IF ₹57k verified &gt; Net college cost = ₹51,500.</text>

      <text x="685" y="290" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="bold">Decision 2: Publication Go/No-Go Call</text>
      <text x="685" y="310" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Option A: Hold publication 24 hours until</text>
      <text x="700" y="326" fill="#cbd5e1" font-family="sans-serif" font-size="11">bank confirms receipt voucher.</text>
      <text x="685" y="345" fill="#cbd5e1" font-family="sans-serif" font-size="11">• Option B: Release student post (which</text>
      <text x="700" y="361" fill="#cbd5e1" font-family="sans-serif" font-size="11">omits financial figures) while holding</text>
      <text x="700" y="377" fill="#cbd5e1" font-family="sans-serif" font-size="11">the executive presentation deck.</text>

      <rect x="685" y="415" width="270" height="155" rx="6" fill="#0f172a" stroke="#f59e0b"/>
      <text x="695" y="440" fill="#fde047" font-family="sans-serif" font-size="11" font-weight="bold">Formal Recommendation:</text>
      <text x="695" y="465" fill="#f8fafc" font-family="sans-serif" font-size="11">Execute <tspan font-weight="bold" fill="#38bdf8">Option B</tspan>: Clear student-facing</text>
      <text x="695" y="483" fill="#f8fafc" font-family="sans-serif" font-size="11">materials which contain no financial data.</text>
      <text x="695" y="501" fill="#f8fafc" font-family="sans-serif" font-size="11">Quarantine executive deck until Accounts</text>
      <text x="695" y="519" fill="#f8fafc" font-family="sans-serif" font-size="11">officer signs the ₹75k / ₹57k reconciliation.</text>
      <text x="695" y="547" fill="#34d399" font-family="sans-serif" font-size="10" font-weight="bold">Signed: AI Verification &amp; Audit Team</text>
    </svg>'''
    build_svg_and_png("unexpected_twist_incident_memo", svg)

if __name__ == "__main__":
    generate_mockup_1()
    generate_mockup_2()
    generate_mockup_3()
    generate_mockup_4()
    generate_mockup_5()
    generate_mockup_6()
    generate_mockup_7()
    generate_mockup_8()
    generate_mockup_9()
    generate_mockup_10()
    print("All 10 visual mockups generated successfully!")
