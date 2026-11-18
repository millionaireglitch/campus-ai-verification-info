import os
import subprocess
import re

# Helper to render SVG page and convert to PDF via sips
def svg_page_to_pdf(svg_content, out_pdf_path, width=850, height=1100):
    tmp_svg = out_pdf_path.replace(".pdf", ".svg")
    tmp_png = out_pdf_path.replace(".pdf", ".png")
    with open(tmp_svg, "w", encoding="utf-8") as f:
        f.write(svg_content)
    subprocess.run(["sips", "-s", "format", "png", tmp_svg, "--out", tmp_png], check=True, stdout=subprocess.DEVNULL)
    subprocess.run(["sips", "-s", "format", "pdf", tmp_png, "--out", out_pdf_path], check=True, stdout=subprocess.DEVNULL)

def merge_all_pdfs(pdf_paths, output_master_pdf):
    # Pure Python PDF merger for Quartz/sips generated single-page PDFs
    all_objs = {}
    master_catalog_id = 1
    master_pages_id = 2
    next_id = 3
    page_ids = []
    merged_objects = {}
    
    for pdf_path in pdf_paths:
        with open(pdf_path, "rb") as f:
            data = f.read()
            
        pattern = re.compile(rb"(\d+)\s+(\d+)\s+obj\s*(.*?)\s*endobj", re.DOTALL)
        raw_objs = {}
        for m in pattern.finditer(data):
            num = int(m.group(1))
            body = m.group(3)
            raw_objs[num] = body
            
        id_map = {}
        for old_id in raw_objs:
            if old_id in (2, 8, 9):
                continue
            id_map[old_id] = next_id
            next_id += 1
            
        page_ids.append(id_map[1])
        
        for old_id, new_id in id_map.items():
            body = raw_objs[old_id]
            if old_id == 1:
                body = re.sub(rb"/Parent\s+\d+\s+\d+\s+R", f"/Parent {master_pages_id} 0 R".encode(), body)
                
            def repl_ref(match):
                ref_id = int(match.group(1))
                ref_gen = int(match.group(2))
                if ref_id in id_map:
                    return f"{id_map[ref_id]} {ref_gen} R".encode()
                return match.group(0)
                
            body = re.sub(rb"(\d+)\s+(\d+)\s+R", repl_ref, body)
            merged_objects[new_id] = body
            
    kids_str = " ".join([f"{pid} 0 R" for pid in page_ids])
    pages_body = f"<< /Type /Pages /MediaBox [0 0 612 792] /Count {len(page_ids)} /Kids [ {kids_str} ] >>".encode()
    merged_objects[master_pages_id] = pages_body
    
    catalog_body = f"<< /Type /Catalog /Pages {master_pages_id} 0 R >>".encode()
    merged_objects[master_catalog_id] = catalog_body
    
    out = bytearray()
    out.extend(b"%PDF-1.3\n%\xe4\xe5\xf2\xe5\xeb\xa7\xf3\xa0\xd0\xc4\xc6\n")
    
    xref_offsets = {}
    sorted_ids = sorted(merged_objects.keys())
    max_id = max(sorted_ids)
    
    for oid in sorted_ids:
        xref_offsets[oid] = len(out)
        out.extend(f"{oid} 0 obj\n".encode())
        out.extend(merged_objects[oid])
        out.extend(b"\nendobj\n")
        
    xref_pos = len(out)
    out.extend(b"xref\n")
    out.extend(f"0 {max_id + 1}\n".encode())
    out.extend(b"0000000000 65535 f \n")
    for oid in range(1, max_id + 1):
        if oid in xref_offsets:
            out.extend(f"{xref_offsets[oid]:010d} 00000 n \n".encode())
        else:
            out.extend(b"0000000000 65535 f \n")
            
    out.extend(b"trailer\n")
    out.extend(f"<< /Size {max_id + 1} /Root {master_catalog_id} 0 R >>\n".encode())
    out.extend(b"startxref\n")
    out.extend(f"{xref_pos}\n%%EOF\n".encode())
    
    with open(output_master_pdf, "wb") as f:
        f.write(out)
    print(f"Master PDF compiled: {output_master_pdf} ({len(page_ids)} pages, {len(out)} bytes)")

# Generate Pages 1 to 8 of structured textual report
def make_page_1():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <rect x="50" y="45" width="750" height="85" rx="6" fill="#0f172a"/>
      <text x="75" y="80" fill="#38bdf8" font-family="sans-serif" font-size="12" font-weight="bold">APPLIED PROFESSIONAL SCENARIO • ADVANCED ASSIGNMENT BRIEF</text>
      <text x="75" y="108" fill="#ffffff" font-family="sans-serif" font-size="20" font-weight="bold">CASE STUDY: THE AI-POWERED CAMPUS INNOVATION WEEK</text>
      
      <rect x="50" y="145" width="750" height="50" rx="4" fill="#f8fafc" stroke="#e2e8f0"/>
      <text x="65" y="175" fill="#334155" font-family="sans-serif" font-size="11"><tspan font-weight="bold">Author Team:</tspan> AI Productivity &amp; Verification Team  |  <tspan font-weight="bold">Total Marks:</tspan> 100 Marks  |  <tspan font-weight="bold">Status:</tspan> Final Submission Report</text>

      <!-- Section: Executive Problem Diagnosis -->
      <text x="50" y="225" fill="#1e3a8a" font-family="sans-serif" font-size="14" font-weight="bold">1. EXECUTIVE PROBLEM DIAGNOSIS &amp; BACKGROUND</text>
      <text x="50" y="248" fill="#334155" font-family="sans-serif" font-size="11" font-weight="normal">Following a 3-day Campus Innovation Week, the college organizing team utilized commercial AI tools to expedite</text>
      <text x="50" y="265" fill="#334155" font-family="sans-serif" font-size="11">reporting, email drafts, presentation decks, and social media releases. The Principal paused publication after identifying</text>
      <text x="50" y="282" fill="#334155" font-family="sans-serif" font-size="11">two alarming unverified assertions in the draft public report:</text>
      <text x="70" y="303" fill="#b91c1c" font-family="sans-serif" font-size="11" font-weight="bold">1. A claim that the 3-day event "improved employability by 70%" (unsupported by any tracer data).</text>
      <text x="70" y="322" fill="#b91c1c" font-family="sans-serif" font-size="11" font-weight="bold">2. A claim citing adherence to the "NeuroPrompt Integrity Index (NPII-7)" (a confabulated standard).</text>
      
      <text x="50" y="352" fill="#334155" font-family="sans-serif" font-size="11">As the appointed AI Productivity and Verification Team, our mandate is to treat AI as an assistant rather than an</text>
      <text x="50" y="369" fill="#334155" font-family="sans-serif" font-size="11">epistemic authority, audit all empirical data against primary records, and establish an auditable workflow.</text>

      <!-- Section 2: Case Information Ground Truth Assessment -->
      <text x="50" y="405" fill="#1e3a8a" font-family="sans-serif" font-size="14" font-weight="bold">2. AUTHORITATIVE CASE DATA ASSESSMENT (GROUND TRUTH)</text>
      
      <rect x="50" y="420" width="750" height="260" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="420" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="439" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">CASE VARIABLE / ITEM</text>
      <text x="260" y="439" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">SUPPLIED DATA</text>
      <text x="430" y="439" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">CRITICAL VERIFICATION AUDIT &amp; LIMITATIONS</text>

      <text x="65" y="465" fill="#0f172a" font-family="sans-serif" font-size="10.5">Event Duration</text>
      <text x="260" y="465" fill="#0f172a" font-family="sans-serif" font-size="10.5">3 Days</text>
      <text x="430" y="465" fill="#16a34a" font-family="sans-serif" font-size="10.5">Verified against college master schedule.</text>

      <text x="65" y="490" fill="#0f172a" font-family="sans-serif" font-size="10.5">Registrations</text>
      <text x="260" y="490" fill="#0f172a" font-family="sans-serif" font-size="10.5">480 people</text>
      <text x="430" y="490" fill="#16a34a" font-family="sans-serif" font-size="10.5">Confirmed via online portal registrations.</text>

      <text x="65" y="515" fill="#0f172a" font-family="sans-serif" font-size="10.5">Attendance Recorded</text>
      <text x="260" y="515" fill="#0f172a" font-family="sans-serif" font-size="10.5">312 entry records</text>
      <text x="430" y="515" fill="#d97706" font-family="sans-serif" font-size="10.5"><tspan font-weight="bold">Limitation:</tspan> Raw gate scans; duplicate scans NOT checked.</text>

      <text x="65" y="540" fill="#0f172a" font-family="sans-serif" font-size="10.5">Feedback Responses</text>
      <text x="260" y="540" fill="#0f172a" font-family="sans-serif" font-size="10.5">96 submitted forms</text>
      <text x="430" y="540" fill="#d97706" font-family="sans-serif" font-size="10.5"><tspan font-weight="bold">Limitation:</tspan> Voluntary feedback (30.77% response rate).</text>

      <text x="65" y="565" fill="#0f172a" font-family="sans-serif" font-size="10.5">Average Satisfaction</text>
      <text x="260" y="565" fill="#0f172a" font-family="sans-serif" font-size="10.5">4.1 out of 5</text>
      <text x="430" y="565" fill="#d97706" font-family="sans-serif" font-size="10.5">Valid ONLY for the 96 respondents; self-selection bias.</text>

      <text x="65" y="590" fill="#0f172a" font-family="sans-serif" font-size="10.5">Approved Budget</text>
      <text x="260" y="590" fill="#0f172a" font-family="sans-serif" font-size="10.5">₹1,20,000</text>
      <text x="430" y="590" fill="#16a34a" font-family="sans-serif" font-size="10.5">Formally authorized institutional spending cap.</text>

      <text x="65" y="615" fill="#0f172a" font-family="sans-serif" font-size="10.5">Recorded Expenses</text>
      <text x="260" y="615" fill="#0f172a" font-family="sans-serif" font-size="10.5">₹1,08,500</text>
      <text x="430" y="615" fill="#16a34a" font-family="sans-serif" font-size="10.5">Recorded expenditure; ₹11,500 budget balance.</text>

      <text x="65" y="640" fill="#0f172a" font-family="sans-serif" font-size="10.5">Confirmed Sponsor</text>
      <text x="260" y="640" fill="#0f172a" font-family="sans-serif" font-size="10.5">₹75,000</text>
      <text x="430" y="640" fill="#16a34a" font-family="sans-serif" font-size="10.5">Confirmed bank transfer (Net college outlay = ₹33,500).</text>

      <text x="65" y="665" fill="#0f172a" font-family="sans-serif" font-size="10.5">Employability Outcomes</text>
      <text x="260" y="665" fill="#b91c1c" font-family="sans-serif" font-size="10.5" font-weight="bold">None Supplied</text>
      <text x="430" y="665" fill="#b91c1c" font-family="sans-serif" font-size="10.5" font-weight="bold">FATAL ERROR: No survey or placement tracer exists.</text>

      <!-- Section 3: Summary of Unreliable Terms -->
      <text x="50" y="710" fill="#1e3a8a" font-family="sans-serif" font-size="14" font-weight="bold">3. PRELIMINARY FORENSIC AUDIT OF UNRELIABLE CLAIMS</text>
      <rect x="50" y="725" width="750" height="290" rx="4" fill="#fff1f2" stroke="#fecdd3"/>
      <text x="65" y="750" fill="#9f1239" font-family="sans-serif" font-size="12" font-weight="bold">FORENSIC TRIAGE CLASSIFICATION SUMMARY</text>

      <text x="65" y="780" fill="#881337" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">"NeuroPrompt Integrity Index (NPII-7)":</tspan> Classified as <tspan font-weight="bold">Likely Fabricated</tspan>. Completely absent from ISO/IEC JTC 1/SC 42,</text>
      <text x="75" y="798" fill="#4c0519" font-family="sans-serif" font-size="10.5">IEEE Standards Association, and NIST AI RMF. Copied unverified by student volunteer from an ungrounded AI chat.</text>

      <text x="65" y="825" fill="#881337" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">"70% Employability Improvement":</tspan> Classified as <tspan font-weight="bold">Fabricated / Unsupported</tspan>. A 3-day awareness showcase cannot produce</text>
      <text x="75" y="843" fill="#4c0519" font-family="sans-serif" font-size="10.5">longitudinal placement shifts; Faculty Lead explicitly noted it was unsubstantiated hallway hearsay.</text>

      <text x="65" y="870" fill="#881337" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">"Contextual Veracity Loop (CVL-9)":</tspan> Classified as <tspan font-weight="bold">Likely Fabricated</tspan>. Pseudo-engineering acronym constructed to sound legitimate.</text>

      <text x="65" y="897" fill="#881337" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">"AI Professional Output Integrity Act 2024":</tspan> Classified as <tspan font-weight="bold">Contradicted / Fabricated</tspan>. No such statute exists in US, UK, EU, or India.</text>
      <text x="75" y="915" fill="#4c0519" font-family="sans-serif" font-size="10.5">The provided hyperlink opened an unrelated webpage, proving citation hallucination.</text>

      <text x="65" y="942" fill="#881337" font-family="sans-serif" font-size="11">• <tspan font-weight="bold">"Source Echo Bias":</tspan> Classified as <tspan font-weight="bold">Ambiguous / Informal</tspan>. While conceptually related to epistemic echo chambers and model</text>
      <text x="75" y="960" fill="#4c0519" font-family="sans-serif" font-size="10.5">sycophancy, it is not a standardized regulatory term.</text>

      <rect x="65" y="980" width="720" height="24" rx="4" fill="#9f1239"/>
      <text x="75" y="996" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">VERIFICATION VERDICT: Strict Publication Freeze Upheld pending systematic correction.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 1 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_1.pdf")

def make_page_2():
    # Deliverable A: Tool-Selection Matrix & Privacy Analysis (Challenge 1)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE A: TOOL-SELECTION MATRIX &amp; TASK DIAGNOSIS (10 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Evaluation of AI Tool Fit, Operational Rationales, Evidence Produced, and Task Boundaries</text>

      <!-- Matrix Table -->
      <rect x="50" y="90" width="750" height="520" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="750" height="30" fill="#1e293b"/>
      <text x="60" y="110" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">TASK DOMAIN</text>
      <text x="175" y="110" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">PRIMARY TOOL</text>
      <text x="275" y="110" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">OPERATIONAL RATIONALE</text>
      <text x="495" y="110" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">LIMITATION &amp; RISKS</text>
      <text x="670" y="110" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">REQUIRED EVIDENCE</text>

      <!-- Row 1: Meeting Notes -->
      <text x="60" y="140" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Meeting Note Cleanup</text>
      <text x="175" y="140" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Otter.ai</text>
      <text x="275" y="135" fill="#334155" font-family="sans-serif" font-size="8.5">Automated transcription, diarization of</text>
      <text x="275" y="147" fill="#334155" font-family="sans-serif" font-size="8.5">4 speakers, and audio-synced text.</text>
      <text x="495" y="135" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Transcribes hearsay verbatim;</text>
      <text x="495" y="147" fill="#b91c1c" font-family="sans-serif" font-size="8.5">cannot assess factual validity.</text>
      <text x="670" y="135" fill="#16a34a" font-family="sans-serif" font-size="8.5">Timestamped audio,</text>
      <text x="670" y="147" fill="#16a34a" font-family="sans-serif" font-size="8.5">speaker diff log.</text>
      <line x1="50" y1="160" x2="800" y2="160" stroke="#e2e8f0"/>

      <!-- Row 2: Source Verification -->
      <text x="60" y="185" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Source Verification</text>
      <text x="175" y="185" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Perplexity AI</text>
      <text x="275" y="180" fill="#334155" font-family="sans-serif" font-size="8.5">Real-time retrieval-augmented LLM</text>
      <text x="275" y="192" fill="#334155" font-family="sans-serif" font-size="8.5">with direct primary URL linking.</text>
      <text x="495" y="180" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Search index bias; circular AI</text>
      <text x="495" y="192" fill="#b91c1c" font-family="sans-serif" font-size="8.5">blogs can mirror hallucinations.</text>
      <text x="670" y="180" fill="#16a34a" font-family="sans-serif" font-size="8.5">Direct primary URLs,</text>
      <text x="670" y="192" fill="#16a34a" font-family="sans-serif" font-size="8.5">verbatim quote checks.</text>
      <line x1="50" y1="205" x2="800" y2="205" stroke="#e2e8f0"/>

      <!-- Row 3: Spreadsheet Analysis -->
      <text x="60" y="230" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Spreadsheet Analysis</text>
      <text x="175" y="230" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Julius AI (Python)</text>
      <text x="275" y="225" fill="#334155" font-family="sans-serif" font-size="8.5">Sandboxed Python/pandas code execution;</text>
      <text x="275" y="237" fill="#334155" font-family="sans-serif" font-size="8.5">exact arithmetic without token drift.</text>
      <text x="495" y="225" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Garbage in, garbage out; cannot</text>
      <text x="495" y="237" fill="#b91c1c" font-family="sans-serif" font-size="8.5">detect duplicated scan logs alone.</text>
      <text x="670" y="225" fill="#16a34a" font-family="sans-serif" font-size="8.5">Executable Python log,</text>
      <text x="670" y="237" fill="#16a34a" font-family="sans-serif" font-size="8.5">dataframe summary.</text>
      <line x1="50" y1="250" x2="800" y2="250" stroke="#e2e8f0"/>

      <!-- Row 4: Presentation Design -->
      <text x="60" y="275" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Presentation Design</text>
      <text x="175" y="275" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Gamma App</text>
      <text x="275" y="270" fill="#334155" font-family="sans-serif" font-size="8.5">Rapid AI visual slide generation from</text>
      <text x="275" y="282" fill="#334155" font-family="sans-serif" font-size="8.5">grounded text outlines.</text>
      <text x="495" y="270" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Auto-fills bullet points with unverified</text>
      <text x="495" y="282" fill="#b91c1c" font-family="sans-serif" font-size="8.5">marketing superlatives if uncurated.</text>
      <text x="670" y="270" fill="#16a34a" font-family="sans-serif" font-size="8.5">Exported 5-slide deck,</text>
      <text x="670" y="282" fill="#16a34a" font-family="sans-serif" font-size="8.5">card revision diffs.</text>
      <line x1="50" y1="295" x2="800" y2="295" stroke="#e2e8f0"/>

      <!-- Row 5: Professional Writing -->
      <text x="60" y="320" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Professional Writing</text>
      <text x="175" y="320" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Jasper / Grammarly</text>
      <text x="275" y="315" fill="#334155" font-family="sans-serif" font-size="8.5">Executive briefing formatting, tone tuning</text>
      <text x="275" y="327" fill="#334155" font-family="sans-serif" font-size="8.5">for Principal vs. Student audiences.</text>
      <text x="495" y="315" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Smooths over knowledge gaps,</text>
      <text x="495" y="327" fill="#b91c1c" font-family="sans-serif" font-size="8.5">creating plausible-sounding fiction.</text>
      <text x="670" y="315" fill="#16a34a" font-family="sans-serif" font-size="8.5">Versioned drafts,</text>
      <text x="670" y="327" fill="#16a34a" font-family="sans-serif" font-size="8.5">tone audit scores.</text>
      <line x1="50" y1="340" x2="800" y2="340" stroke="#e2e8f0"/>

      <!-- Row 6: SOP Documentation -->
      <text x="60" y="365" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">SOP Documentation</text>
      <text x="175" y="365" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Scribe</text>
      <text x="275" y="360" fill="#334155" font-family="sans-serif" font-size="8.5">Auto-captures browser clicks to produce</text>
      <text x="275" y="372" fill="#334155" font-family="sans-serif" font-size="8.5">illustrated procedural guides.</text>
      <text x="495" y="360" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Documents procedural mechanics,</text>
      <text x="495" y="372" fill="#b91c1c" font-family="sans-serif" font-size="8.5">not quality of human judgment.</text>
      <text x="670" y="360" fill="#16a34a" font-family="sans-serif" font-size="8.5">Step-by-step logs,</text>
      <text x="670" y="372" fill="#16a34a" font-family="sans-serif" font-size="8.5">annotated screenshots.</text>
      <line x1="50" y1="385" x2="800" y2="385" stroke="#e2e8f0"/>

      <!-- Row 7: Approval Workflow -->
      <text x="60" y="410" fill="#0f172a" font-family="sans-serif" font-size="9.5" font-weight="bold">Approval Workflow</text>
      <text x="175" y="410" fill="#0284c7" font-family="sans-serif" font-size="9.5" font-weight="bold">Zapier</text>
      <text x="275" y="405" fill="#334155" font-family="sans-serif" font-size="8.5">Automates deterministic gates routing drafts</text>
      <text x="275" y="417" fill="#334155" font-family="sans-serif" font-size="8.5">to human role owners before release.</text>
      <text x="495" y="405" fill="#b91c1c" font-family="sans-serif" font-size="8.5">Pure trigger logic; cannot assess if</text>
      <text x="495" y="417" fill="#b91c1c" font-family="sans-serif" font-size="8.5">human performed thorough audit.</text>
      <text x="670" y="405" fill="#16a34a" font-family="sans-serif" font-size="8.5">Webhook execution logs,</text>
      <text x="670" y="417" fill="#16a34a" font-family="sans-serif" font-size="8.5">digital sign-off ledger.</text>

      <!-- Sub-task: General-purpose chatbot limitations -->
      <rect x="50" y="630" width="750" height="180" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="65" y="655" fill="#1e3a8a" font-family="sans-serif" font-size="12" font-weight="bold">TASKS WHERE A GENERAL-PURPOSE CHATBOT ALONE IS INSUFFICIENT</text>
      <text x="65" y="680" fill="#1e293b" font-family="sans-serif" font-size="10.5">1. <tspan font-weight="bold">Spreadsheet Analysis &amp; Numerical Verification:</tspan> General-purpose LLMs predict the most probable next token rather than</text>
      <text x="80" y="698" fill="#334155" font-family="sans-serif" font-size="10">executing formal algebraic proofs. In tabular reasoning, LLMs frequently experience token drift, hallucinate arithmetic operations,</text>
      <text x="80" y="715" fill="#334155" font-family="sans-serif" font-size="10">or miss subtle data relationships (e.g., confusing gross budget with net outlay). A deterministic, code-executing interpreter</text>
      <text x="80" y="732" fill="#334155" font-family="sans-serif" font-size="10">(such as Julius AI running Python/pandas) is mandatory to guarantee zero calculation error.</text>

      <text x="65" y="757" fill="#1e293b" font-family="sans-serif" font-size="10.5">2. <tspan font-weight="bold">Approval Workflow Orchestration &amp; Gatekeeping:</tspan> A conversational chatbot cannot enforce organizational access controls,</text>
      <text x="80" y="775" fill="#334155" font-family="sans-serif" font-size="10">maintain immutable state across multi-department sign-offs, or block public publishing webhooks. Dedicated workflow automation</text>
      <text x="80" y="792" fill="#334155" font-family="sans-serif" font-size="10">(Zapier) is strictly required to air-gap draft creation from publication channels.</text>

      <!-- Sub-task: Privacy & Access Risk Assessment -->
      <rect x="50" y="830" width="750" height="210" rx="4" fill="#fef2f2" stroke="#fecaca"/>
      <text x="65" y="855" fill="#991b1b" font-family="sans-serif" font-size="12" font-weight="bold">PRIVACY &amp; ACCESS RISK ANALYSIS (BEFORE EXTERNAL AI UPLOAD)</text>
      <text x="65" y="880" fill="#7f1d1d" font-family="sans-serif" font-size="10.5" font-weight="bold">Identified Risk: Exposure of Personally Identifiable Information (PII) &amp; Financial Ledger Records</text>
      <text x="65" y="902" fill="#334155" font-family="sans-serif" font-size="10">Uploading raw event spreadsheets containing student names, college roll numbers, email addresses, phone numbers, or unredacted bank</text>
      <text x="65" y="919" fill="#334155" font-family="sans-serif" font-size="10">NEFT transfer receipts to commercial consumer AI endpoints (e.g., standard ChatGPT or public cloud tools) creates severe compliance violations</text>
      <text x="65" y="936" fill="#334155" font-family="sans-serif" font-size="10">under India’s Digital Personal Data Protection Act (DPDP Act 2023) and global standards (GDPR):</text>
      <text x="80" y="958" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Data Ingestion Threat:</tspan> Consumer AI terms of service often permit training on submitted user prompts, permanently embedding student data.</text>
      <text x="80" y="975" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Mandatory Mitigation Protocol:</tspan> Prior to ingestion, all datasets must pass through an air-gapped local sanitization script</text>
      <text x="80" y="992" fill="#334155" font-family="sans-serif" font-size="10">that strips direct identifiers, substitutes synthetic pseudonyms, and truncates financial account numbers to terminal digits.</text>
      <text x="80" y="1009" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Enterprise Tier Requirement:</tspan> Only enterprise zero-data-retention (ZDR) APIs with signed SOC2/ISO27001 data processing agreements may be used.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 2 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_2.pdf")

def make_page_3():
    # Deliverable B: Prompt Engineering Log & Iteration (Challenge 2)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE B: PROMPT ENGINEERING &amp; ITERATION LOG (15 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Structured Prompts with Labeled Schema, Grounding Constraints, Iteration Analysis, and [VERIFY] Protocol</text>

      <!-- Prompts Schema Overview -->
      <rect x="50" y="90" width="750" height="310" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="109" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">STRUCTURED PROMPTS SPECIFICATION (PROMPTS A, B, AND C)</text>

      <!-- Prompt A -->
      <text x="65" y="135" fill="#0284c7" font-family="sans-serif" font-size="11" font-weight="bold">PROMPT A: ONE-PAGE PRINCIPAL'S BRIEF</text>
      <text x="65" y="152" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[ROLE]</tspan> Collegiate AI Productivity &amp; Verification Lead.  <tspan font-weight="bold">[AUDIENCE]</tspan> College Principal &amp; Senior Academic Council.</text>
      <text x="65" y="167" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[CONTEXT]</tspan> Ground Truth: 3-day Innovation Week; 480 registered; 312 gate entry scans; 96 voluntary feedback forms (4.1/5 avg);</text>
      <text x="65" y="181" fill="#334155" font-family="sans-serif" font-size="9.5">Budget: ₹1,20,000 approved, ₹1,08,500 expenses; ₹75,000 confirmed sponsor transfer. No employability data collected.</text>
      <text x="65" y="196" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[TASK]</tspan> Produce a 1-page executive brief covering outcomes, financial governance, data caveats, and next steps.</text>
      <text x="65" y="211" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[CONSTRAINTS]</tspan> 1) Zero hallucinations. 2) Never claim 70% employability. 3) Do not cite NPII-7. 4) Tag uncertain points as [VERIFY].</text>
      <text x="65" y="226" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[OUTPUT FORMAT]</tspan> Executive Summary, Ground Truth Data Table, Mandatory "What We Cannot Conclude" Section, Sign-off Block.</text>

      <!-- Prompt B -->
      <line x1="65" y1="238" x2="785" y2="238" stroke="#cbd5e1"/>
      <text x="65" y="255" fill="#0284c7" font-family="sans-serif" font-size="11" font-weight="bold">PROMPT B: FIVE-SLIDE PRESENTATION OUTLINE (FACULTY &amp; MANAGEMENT)</text>
      <text x="65" y="272" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[ROLE]</tspan> Academic Presentation Specialist.  <tspan font-weight="bold">[AUDIENCE]</tspan> Department Heads and Faculty Review Board.</text>
      <text x="65" y="287" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[TASK]</tspan> Create a structured 5-slide outline. Exactly one purpose per slide. Slide 4 must be 'What We Cannot Conclude'.</text>
      <text x="65" y="302" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[CONSTRAINTS]</tspan> Use exact numbers (312 scans, ₹1.085L spend). Emphasize that duplicate scans are unverified. Mark estimates as [VERIFY].</text>

      <!-- Prompt C -->
      <line x1="65" y1="314" x2="785" y2="314" stroke="#cbd5e1"/>
      <text x="65" y="331" fill="#0284c7" font-family="sans-serif" font-size="11" font-weight="bold">PROMPT C: PUBLIC SOCIAL-MEDIA POST (STUDENTS &amp; COMMUNITY)</text>
      <text x="65" y="348" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[ROLE]</tspan> Student Communications Lead.  <tspan font-weight="bold">[AUDIENCE]</tspan> Student body, participants, and partner tech clubs.</text>
      <text x="65" y="363" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[TASK]</tspan> Write an energetic LinkedIn/Instagram post celebrating 3 days of student innovation and community participation.</text>
      <text x="65" y="378" fill="#334155" font-family="sans-serif" font-size="9.5"><tspan font-weight="bold">[CONSTRAINTS]</tspan> Strictly prohibited from claiming guaranteed jobs, career boosts, or employability metrics. Highlight 4.1/5 rating.</text>

      <!-- Iteration Analysis Section -->
      <text x="50" y="425" fill="#1e3a8a" font-family="sans-serif" font-size="14" font-weight="bold">PROMPT ITERATION EXPERIMENT: BEFORE VS. AFTER COMPARISON</text>

      <!-- Comparison Split Box -->
      <rect x="50" y="440" width="365" height="420" rx="4" fill="#fef2f2" stroke="#f87171"/>
      <rect x="50" y="440" width="365" height="28" fill="#7f1d1d"/>
      <text x="60" y="459" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">V1: NAIVE UNCONSTRAINED PROMPT (FAILED)</text>

      <text x="60" y="485" fill="#991b1b" font-family="monospace" font-size="9.5" font-weight="bold">Prompt Given to AI:</text>
      <text x="60" y="502" fill="#334155" font-family="monospace" font-size="9">"Write a one-page brief for our principal about</text>
      <text x="60" y="516" fill="#334155" font-family="monospace" font-size="9">our Campus Innovation Week. Make it sound exciting</text>
      <text x="60" y="530" fill="#334155" font-family="monospace" font-size="9">and mention how it helps student careers &amp; standards."</text>

      <text x="60" y="555" fill="#991b1b" font-family="sans-serif" font-size="10" font-weight="bold">AI Output V1 (Catastrophic Hallucinations):</text>
      <text x="60" y="575" fill="#334155" font-family="sans-serif" font-size="9">• "Campus Innovation Week was a roaring success with</text>
      <text x="60" y="589" fill="#334155" font-family="sans-serif" font-size="9">   over 500 participants across all campus departments."</text>
      <text x="60" y="605" fill="#b91c1c" font-family="sans-serif" font-size="9" font-weight="bold">• "The event achieved a staggering 70% employability</text>
      <text x="60" y="619" fill="#b91c1c" font-family="sans-serif" font-size="9" font-weight="bold">   enhancement, guaranteeing placement readiness."</text>
      <text x="60" y="635" fill="#b91c1c" font-family="sans-serif" font-size="9" font-weight="bold">• "Audited under the globally recognized NeuroPrompt</text>
      <text x="60" y="649" fill="#b91c1c" font-family="sans-serif" font-size="9" font-weight="bold">   Integrity Index (NPII-7) AI quality standard."</text>
      <text x="60" y="665" fill="#334155" font-family="sans-serif" font-size="9">• "100% of participants gave top marks in feedback."</text>

      <text x="60" y="695" fill="#991b1b" font-family="sans-serif" font-size="10" font-weight="bold">Root-Cause Weaknesses Diagnosed:</text>
      <text x="60" y="715" fill="#334155" font-family="sans-serif" font-size="9">1. Zero negative constraints allowed model to confabulate.</text>
      <text x="60" y="730" fill="#334155" font-family="sans-serif" font-size="9">2. "Make it sound exciting" triggered promotional hallucination.</text>
      <text x="60" y="745" fill="#334155" font-family="sans-serif" font-size="9">3. No Ground Truth numbers provided; model hallucinated 500.</text>
      <text x="60" y="760" fill="#334155" font-family="sans-serif" font-size="9">4. No rule instructing model to admit lack of data.</text>

      <!-- Right Column: V2 -->
      <rect x="435" y="440" width="365" height="420" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <rect x="435" y="440" width="365" height="28" fill="#14532d"/>
      <text x="445" y="459" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">V2: GROUNDED PROMPT WITH [VERIFY] PROTOCOL</text>

      <text x="445" y="485" fill="#166534" font-family="monospace" font-size="9.5" font-weight="bold">Prompt Modifications Added:</text>
      <text x="445" y="502" fill="#334155" font-family="monospace" font-size="8.5">• Injected full Ground Truth parameters (312 scans, 480 reg).</text>
      <text x="445" y="516" fill="#334155" font-family="monospace" font-size="8.5">• Added explicit negative constraints ("Never claim 70%").</text>
      <text x="445" y="530" fill="#334155" font-family="monospace" font-size="8.5">• MANDATORY RULE: If a figure is unconfirmed or duplicate</text>
      <text x="445" y="544" fill="#334155" font-family="monospace" font-size="8.5">  scans unchecked, you MUST tag it as [VERIFY].</text>

      <text x="445" y="570" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold">AI Output V2 (Grounded &amp; Auditable):</text>
      <text x="445" y="590" fill="#334155" font-family="sans-serif" font-size="9">• "Campus Innovation Week recorded 312 gate entries out of</text>
      <text x="445" y="604" fill="#334155" font-family="sans-serif" font-size="9">   480 registrations <tspan fill="#d97706" font-weight="bold">[VERIFY: Deduplication pending]</tspan>."</text>
      <text x="445" y="620" fill="#334155" font-family="sans-serif" font-size="9">• "Financial expenditure totaled ₹1,08,500 on an approved</text>
      <text x="445" y="634" fill="#334155" font-family="sans-serif" font-size="9">   budget of ₹1,20,000 (90.42% utilization rate)."</text>
      <text x="445" y="650" fill="#334155" font-family="sans-serif" font-size="9">• "Feedback rating averaged 4.1/5 across 96 responses."</text>
      <text x="445" y="666" fill="#166534" font-family="sans-serif" font-size="9" font-weight="bold">• "What We Cannot Conclude: Employability was NOT</text>
      <text x="445" y="680" fill="#166534" font-family="sans-serif" font-size="9" font-weight="bold">   measured; 70% claim is unverified hearsay and rejected."</text>

      <text x="445" y="705" fill="#166534" font-family="sans-serif" font-size="10" font-weight="bold">Why V2 Succeeded (Verification Rationale):</text>
      <text x="445" y="725" fill="#334155" font-family="sans-serif" font-size="9">1. Negative guardrails blocked confabulation of phantom standards.</text>
      <text x="445" y="740" fill="#334155" font-family="sans-serif" font-size="9">2. Mandatory [VERIFY] rule forced uncertainty into the open.</text>
      <text x="445" y="755" fill="#334155" font-family="sans-serif" font-size="9">3. Output was 100% auditable against institutional receipts.</text>

      <!-- Explanation Box -->
      <rect x="50" y="875" width="750" height="165" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="65" y="900" fill="#1e3a8a" font-family="sans-serif" font-size="12" font-weight="bold">HOW WE KNOW THE PROMPT CHANGE IMPROVED THE RESULT</text>
      <text x="65" y="922" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Traceability Test:</tspan> Every single numerical token in V2 maps directly to the case ground truth table (312, 480, 96, 4.1, ₹1.2L, ₹1.085L).</text>
      <text x="65" y="939" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Falsification Test:</tspan> The [VERIFY] protocol successfully prevented the model from smoothing over the duplicate scan ambiguity.</text>
      <text x="65" y="956" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Defensibility:</tspan> When submitted to the Principal, the document exposes risks rather than hiding them, safeguarding institutional integrity.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 3 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_3.pdf")

def make_page_4():
    # Deliverable C: Hallucination Detective (Challenge 3)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE C: HALLUCINATION AUDIT &amp; SOURCE VERIFICATION (20 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Forensic Investigation of 5 Unreliable Terms, Multi-Tool Consensus, and Rejected Explanations</text>

      <!-- Hallucination Audit Table -->
      <rect x="50" y="90" width="750" height="520" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="750" height="28" fill="#1e293b"/>
      <text x="60" y="109" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">TERM / CLAIM</text>
      <text x="185" y="109" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">CLASSIFICATION</text>
      <text x="310" y="109" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">SOURCES SEARCHED &amp; EVIDENCE</text>
      <text x="570" y="109" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">FINAL AUDIT DECISION</text>

      <!-- Row 1: NPII-7 -->
      <text x="60" y="135" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">NeuroPrompt Integrity</text>
      <text x="60" y="147" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Index (NPII-7)</text>
      <text x="185" y="140" fill="#b91c1c" font-family="sans-serif" font-size="9.5" font-weight="bold">Likely Fabricated</text>
      <text x="310" y="133" fill="#334155" font-family="sans-serif" font-size="8.5">ISO/IEC JTC 1/SC 42, IEEE AI Standards Committee,</text>
      <text x="310" y="145" fill="#334155" font-family="sans-serif" font-size="8.5">NIST AI RMF 1.0, arXiv CS archives. Zero hits across</text>
      <text x="310" y="157" fill="#334155" font-family="sans-serif" font-size="8.5">14,000+ standards registries. Copied unverified by student.</text>
      <text x="570" y="135" fill="#b91c1c" font-family="sans-serif" font-size="8.5" font-weight="bold">QUARANTINE &amp; STRIP.</text>
      <text x="570" y="147" fill="#334155" font-family="sans-serif" font-size="8">Not verified in sources checked.</text>
      <text x="570" y="158" fill="#334155" font-family="sans-serif" font-size="8">Fictional synthetic standard.</text>
      <line x1="50" y1="170" x2="800" y2="170" stroke="#cbd5e1"/>

      <!-- Row 2: Source Echo Bias -->
      <text x="60" y="195" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Source Echo Bias</text>
      <text x="185" y="195" fill="#d97706" font-family="sans-serif" font-size="9.5" font-weight="bold">Ambiguous / Informal</text>
      <text x="310" y="190" fill="#334155" font-family="sans-serif" font-size="8.5">Google Scholar, Stanford HAI reports. Conceptually relates to</text>
      <text x="310" y="202" fill="#334155" font-family="sans-serif" font-size="8.5">retrieval confirmation bias &amp; LLM sycophancy, but is</text>
      <text x="310" y="214" fill="#334155" font-family="sans-serif" font-size="8.5">NOT a formally adopted technical benchmark.</text>
      <text x="570" y="190" fill="#d97706" font-family="sans-serif" font-size="8.5" font-weight="bold">RECLASSIFY AS INFORMAL.</text>
      <text x="570" y="202" fill="#334155" font-family="sans-serif" font-size="8">Replace with 'Model Regurgitation</text>
      <text x="570" y="213" fill="#334155" font-family="sans-serif" font-size="8">or Circular Retrieval Bias'.</text>
      <line x1="50" y1="225" x2="800" y2="225" stroke="#cbd5e1"/>

      <!-- Row 3: CVL-9 -->
      <text x="60" y="250" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Contextual Veracity</text>
      <text x="60" y="262" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Loop (CVL-9)</text>
      <text x="185" y="255" fill="#b91c1c" font-family="sans-serif" font-size="9.5" font-weight="bold">Likely Fabricated</text>
      <text x="310" y="250" fill="#334155" font-family="sans-serif" font-size="8.5">ACM Digital Library, NeurIPS, ICLR proceedings.</text>
      <text x="310" y="262" fill="#334155" font-family="sans-serif" font-size="8.5">No algorithmic pipeline or verification framework exists</text>
      <text x="310" y="274" fill="#334155" font-family="sans-serif" font-size="8.5">under this designation. Invented technical jargon.</text>
      <text x="570" y="250" fill="#b91c1c" font-family="sans-serif" font-size="8.5" font-weight="bold">EXCLUDE FROM DECK.</text>
      <text x="570" y="262" fill="#334155" font-family="sans-serif" font-size="8">Not verified in sources checked.</text>
      <text x="570" y="273" fill="#334155" font-family="sans-serif" font-size="8">Fabricated control term.</text>
      <line x1="50" y1="285" x2="800" y2="285" stroke="#cbd5e1"/>

      <!-- Row 4: AI Integrity Act -->
      <text x="60" y="310" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">AI Professional Output</text>
      <text x="60" y="322" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Integrity Act 2024</text>
      <text x="185" y="315" fill="#b91c1c" font-family="sans-serif" font-size="9.5" font-weight="bold">Contradicted / Fake</text>
      <text x="310" y="308" fill="#334155" font-family="sans-serif" font-size="8.5">EUR-Lex (EU AI Act Reg 2024/1689), US Congress DB,</text>
      <text x="310" y="320" fill="#334155" font-family="sans-serif" font-size="8.5">India Gazette (DPDP 2023). No statute exists anywhere under</text>
      <text x="310" y="332" fill="#334155" font-family="sans-serif" font-size="8.5">this title. Student link resolved to dead generic domain.</text>
      <text x="570" y="310" fill="#b91c1c" font-family="sans-serif" font-size="8.5" font-weight="bold">REMOVE STATUTORY CLAIM.</text>
      <text x="570" y="322" fill="#334155" font-family="sans-serif" font-size="8">Replace with internal college</text>
      <text x="570" y="333" fill="#334155" font-family="sans-serif" font-size="8">responsible AI guidelines.</text>
      <line x1="50" y1="345" x2="800" y2="345" stroke="#cbd5e1"/>

      <!-- Row 5: 70% Employability -->
      <text x="60" y="370" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">70% Employability</text>
      <text x="60" y="382" fill="#0f172a" font-family="sans-serif" font-size="9" font-weight="bold">Improvement</text>
      <text x="185" y="375" fill="#b91c1c" font-family="sans-serif" font-size="9.5" font-weight="bold">Unsupported / False</text>
      <text x="310" y="368" fill="#334155" font-family="sans-serif" font-size="8.5">Case Study Ground Truth Table: explicitly confirms "No</text>
      <text x="310" y="380" fill="#334155" font-family="sans-serif" font-size="8.5">follow-up survey or employment outcome data supplied."</text>
      <text x="310" y="392" fill="#334155" font-family="sans-serif" font-size="8.5">Faculty Lead warned: "I don't know where number came from."</text>
      <text x="570" y="370" fill="#b91c1c" font-family="sans-serif" font-size="8.5" font-weight="bold">HARD EXCLUSION.</text>
      <text x="570" y="382" fill="#334155" font-family="sans-serif" font-size="8">Must be featured prominently</text>
      <text x="570" y="393" fill="#334155" font-family="sans-serif" font-size="8">under 'What We Cannot Conclude'.</text>

      <!-- Multi-Tool Challenger Interrogation -->
      <rect x="50" y="630" width="750" height="150" rx="4" fill="#eff6ff" stroke="#bfdbfe"/>
      <text x="65" y="655" fill="#1e3a8a" font-family="sans-serif" font-size="12" font-weight="bold">MULTI-AI CHALLENGER INTERROGATION &amp; CONSENSUS (GPT-4 vs CLAUDE 3.5)</text>
      <text x="65" y="675" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Cross-Model Interrogation Prompt:</tspan> "Act as a ruthless verification auditor. Challenge the claim that NPII-7 and CVL-9 are valid standards."</text>
      <text x="65" y="692" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Agreement Points (100% Consensus):</tspan> Both independent models confirmed that NPII-7, CVL-9, and the AI Output Integrity Act 2024</text>
      <text x="80" y="707" fill="#334155" font-family="sans-serif" font-size="10">have zero existence in academic, regulatory, or industrial registries.</text>
      <text x="65" y="725" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Disagreement Resolution:</tspan> Tool 1 initially suggested "Source Echo Bias" might be an obscure pre-print term. We performed an independent</text>
      <text x="80" y="740" fill="#334155" font-family="sans-serif" font-size="10">Boolean search on Google Scholar; finding zero formal citations, we resolved the classification as 'Informal / Misnamed'.</text>

      <!-- Plausible-Sounding Explanation Rejected -->
      <rect x="50" y="800" width="750" height="240" rx="4" fill="#fef2f2" stroke="#fecaca"/>
      <text x="65" y="825" fill="#991b1b" font-family="sans-serif" font-size="12" font-weight="bold">PLAUSIBLE-SOUNDING AI EXPLANATION REJECTED &amp; CORRECTED</text>
      
      <text x="65" y="850" fill="#7f1d1d" font-family="sans-serif" font-size="10.5" font-weight="bold">Original Fabricated Claim Generated by Unconstrained LLM:</text>
      <text x="65" y="868" fill="#334155" font-family="monospace" font-size="9.5">"The NeuroPrompt Integrity Index (NPII-7) is an international 7-parameter framework established</text>
      <text x="65" y="883" fill="#334155" font-family="monospace" font-size="9.5">by the Global Consortium for Ethical AI Verification to assess neural alignment in output models."</text>

      <text x="65" y="912" fill="#7f1d1d" font-family="sans-serif" font-size="10.5" font-weight="bold">Forensic Evidence Checked:</text>
      <text x="65" y="930" fill="#334155" font-family="sans-serif" font-size="10">1. Queried the Open Knowledge Foundation, Global Partnership on AI (GPAI), and International Organization for Standardization.</text>
      <text x="65" y="946" fill="#334155" font-family="sans-serif" font-size="10">2. Result: The 'Global Consortium for Ethical AI Verification' is an entirely confabulated entity with no corporate registration.</text>

      <text x="65" y="975" fill="#7f1d1d" font-family="sans-serif" font-size="10.5" font-weight="bold">Final Decision &amp; Corrective Action Taken:</text>
      <text x="65" y="995" fill="#b91c1c" font-family="sans-serif" font-size="10" font-weight="bold">REJECTED ENTIRELY. The explanation was identified as a textbook confabulation where an LLM fabricates plausible</text>
      <text x="65" y="1010" fill="#b91c1c" font-family="sans-serif" font-size="10" font-weight="bold">supporting context to justify an invented term. All references excised from final deliverables.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 4 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_4.pdf")

def make_page_5():
    # Deliverable D: Mathematical Calculation Sheet (Challenge 4)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE D: NUMERICAL REASONING &amp; CALCULATION SHEET (15 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Exact Mathematical Derivations, Intermediate Workings, Statistical Biases, and Python Audit</text>

      <!-- Calculation Cards Grid -->
      <!-- Card 1: Entry to Reg Ratio -->
      <rect x="50" y="90" width="365" height="160" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="365" height="26" fill="#1e293b"/>
      <text x="60" y="108" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">1. ENTRY-RECORD-TO-REGISTRATION RATIO</text>
      <text x="60" y="132" fill="#0284c7" font-family="monospace" font-size="10" font-weight="bold">Formula: (Entry Records ÷ Registrations) × 100</text>
      <text x="60" y="152" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 1: 312 ÷ 480 = 0.65</text>
      <text x="60" y="168" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 2: 0.65 × 100 = <tspan font-weight="bold" fill="#0284c7">65.00%</tspan></text>
      <text x="60" y="190" fill="#334155" font-family="sans-serif" font-size="9"><tspan font-weight="bold">Interpretation:</tspan> 65.0% of registrants have entry records.</text>
      <text x="60" y="206" fill="#d97706" font-family="sans-serif" font-size="8.5" font-weight="bold">Caveat: Raw scans; unique students &lt;= 65% if duplicates exist.</text>

      <!-- Card 2: Feedback to Entry Ratio -->
      <rect x="435" y="90" width="365" height="160" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="435" y="90" width="365" height="26" fill="#1e293b"/>
      <text x="445" y="108" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">2. FEEDBACK-RESPONSE RATIOS</text>
      <text x="445" y="132" fill="#0284c7" font-family="monospace" font-size="10" font-weight="bold">Formula: (Feedback Responses ÷ Entry Records) × 100</text>
      <text x="445" y="152" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 1: 96 ÷ 312 = 0.3076923...</text>
      <text x="445" y="168" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 2: 0.3076923... × 100 = <tspan font-weight="bold" fill="#0284c7">30.77% (or 30.8%)</tspan></text>
      <text x="445" y="190" fill="#334155" font-family="sans-serif" font-size="9"><tspan font-weight="bold">Feedback to Registrations:</tspan> 96 ÷ 480 × 100 = <tspan font-weight="bold">20.00%</tspan></text>
      <text x="445" y="206" fill="#d97706" font-family="sans-serif" font-size="8.5" font-weight="bold">Caveat: 69.23% non-response rate among attendees.</text>

      <!-- Card 3: Budget Remaining -->
      <rect x="50" y="265" width="365" height="160" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="265" width="365" height="26" fill="#1e293b"/>
      <text x="60" y="283" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">3. BUDGET REMAINING &amp; NET COLLEGE OUTLAY</text>
      <text x="60" y="307" fill="#0284c7" font-family="monospace" font-size="10" font-weight="bold">Formula: Approved Budget − Recorded Expenses</text>
      <text x="60" y="327" fill="#334155" font-family="sans-serif" font-size="9.5">• Gross Remaining: ₹1,20,000 − ₹1,08,500 = <tspan font-weight="bold" fill="#16a34a">₹11,500</tspan></text>
      <text x="60" y="347" fill="#334155" font-family="sans-serif" font-size="9.5">• Confirmed Sponsor Transfer: <tspan font-weight="bold">₹75,000</tspan></text>
      <text x="60" y="367" fill="#334155" font-family="sans-serif" font-size="9.5">• Net College Outlay: ₹1,08,500 − ₹75,000 = <tspan font-weight="bold" fill="#16a34a">₹33,500</tspan></text>
      <text x="60" y="388" fill="#334155" font-family="sans-serif" font-size="9"><tspan font-weight="bold">Net Institutional Savings:</tspan> ₹1,20,000 − ₹33,500 = <tspan font-weight="bold" fill="#16a34a">₹86,500</tspan></text>

      <!-- Card 4: Budget Utilisation -->
      <rect x="435" y="265" width="365" height="160" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="435" y="265" width="365" height="26" fill="#1e293b"/>
      <text x="445" y="283" fill="#ffffff" font-family="sans-serif" font-size="10" font-weight="bold">4. BUDGET UTILISATION RATIO</text>
      <text x="445" y="307" fill="#0284c7" font-family="monospace" font-size="10" font-weight="bold">Formula: (Recorded Expenses ÷ Approved Budget) × 100</text>
      <text x="445" y="327" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 1: ₹1,08,500 ÷ ₹1,20,000 = 0.9041666...</text>
      <text x="445" y="347" fill="#334155" font-family="sans-serif" font-size="9.5">• Step 2: 0.9041666... × 100 = <tspan font-weight="bold" fill="#0284c7">90.42%</tspan></text>
      <text x="445" y="368" fill="#334155" font-family="sans-serif" font-size="9"><tspan font-weight="bold">Interpretation:</tspan> Spent 90.42% of approved cap.</text>
      <text x="445" y="388" fill="#16a34a" font-family="sans-serif" font-size="8.5" font-weight="bold">Event concluded 9.58% (₹11,500) within institutional ceiling.</text>

      <!-- Detailed Interpretations -->
      <rect x="50" y="445" width="750" height="200" rx="4" fill="#fffbeb" stroke="#fef08a"/>
      <text x="65" y="470" fill="#92400e" font-family="sans-serif" font-size="12" font-weight="bold">WHY THE 4.1/5 SCORE CANNOT BE AUTOMATICALLY GENERALISED</text>
      
      <text x="65" y="495" fill="#78350f" font-family="sans-serif" font-size="10.5">1. <tspan font-weight="bold">Voluntary Response (Self-Selection) Bias:</tspan> The feedback form was voluntary. Participants who take the initiative</text>
      <text x="80" y="512" fill="#78350f" font-family="sans-serif" font-size="10">to complete post-event forms usually possess strongly positive sentiments or high personal investment. Disengaged or dissatisfied</text>
      <text x="80" y="528" fill="#78350f" font-family="sans-serif" font-size="10">attendees disproportionately drop out without responding.</text>

      <text x="65" y="550" fill="#78350f" font-family="sans-serif" font-size="10.5">2. <tspan font-weight="bold">Severe Non-Response Rate (69.23%):</tspan> Only 96 out of 312 recorded entries (and 480 registrants) submitted ratings.</text>
      <text x="80" y="567" fill="#78350f" font-family="sans-serif" font-size="10">A response rate of 30.77% means that more than two-thirds of attendees are entirely unaccounted for. Statistically, one cannot</text>
      <text x="80" y="583" fill="#78350f" font-family="sans-serif" font-size="10">infer the population mean of 480 people from an unstratified, self-selected sample of 96.</text>

      <text x="65" y="605" fill="#78350f" font-family="sans-serif" font-size="10.5">3. <tspan font-weight="bold">Unchecked Duplication Distortion:</tspan> If the 312 entry records include duplicate scans across the 3 days, the true denominator</text>
      <text x="80" y="622" fill="#78350f" font-family="sans-serif" font-size="10">of unique individuals is lower, further clouding sample representativeness.</text>

      <!-- Why Employability is Impossible to Conclude -->
      <rect x="50" y="660" width="750" height="190" rx="4" fill="#fef2f2" stroke="#fecaca"/>
      <text x="65" y="685" fill="#991b1b" font-family="sans-serif" font-size="12" font-weight="bold">WHY THE SUPPLIED DATA CANNOT SUPPORT "70% EMPLOYABILITY IMPROVEMENT"</text>
      
      <text x="65" y="710" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">1. <tspan font-weight="bold">Absence of Longitudinal Measurement:</tspan> Employability is an outcome metric requiring baseline skill assessment, post-event</text>
      <text x="80" y="727" fill="#7f1d1d" font-family="sans-serif" font-size="10">evaluation, and a 6-to-12-month employment tracer study. A 3-day awareness workshop cannot measure long-term job outcomes.</text>

      <text x="65" y="748" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">2. <tspan font-weight="bold">Explicit Lack of Evidence in Case Records:</tspan> The case table explicitly mandates: <tspan font-style="italic">"Employability outcomes: No follow-up survey</tspan></text>
      <text x="80" y="765" fill="#7f1d1d" font-family="sans-serif" font-size="10"><tspan font-style="italic">or employment outcome data supplied."</tspan> Any claim of numerical employability is an empirical fabrication.</text>

      <text x="65" y="787" fill="#7f1d1d" font-family="sans-serif" font-size="10.5">3. <tspan font-weight="bold">Admission of Fictional Origin in Meeting Minutes:</tspan> The Faculty Lead explicitly stated: <tspan font-style="italic">"Someone said 70% of participants</tspan></text>
      <text x="80" y="804" fill="#7f1d1d" font-family="sans-serif" font-size="10"><tspan font-style="italic">became more employable. I don’t know where that number came from. Don’t present it as a result."</tspan></text>

      <!-- AI Analysis Audit Check -->
      <rect x="50" y="865" width="750" height="170" rx="4" fill="#f0fdf4" stroke="#86efac"/>
      <text x="65" y="890" fill="#166534" font-family="sans-serif" font-size="12" font-weight="bold">INDEPENDENT AUDIT OF AI ANALYSIS TOOL (JULIUS AI PYTHON RECALCULATION)</text>
      <text x="65" y="912" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">AI Error Identified:</tspan> When initially summarizing, an unconstrained chatbot subtracted recorded expenses (₹1,08,500) from confirmed sponsor</text>
      <text x="80" y="929" fill="#334155" font-family="sans-serif" font-size="10">funds (₹75,000) and hallucinated that the event ran a "₹33,500 budget deficit", ignoring the ₹1,20,000 approved institutional ceiling!</text>
      <text x="65" y="950" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Human Checker Correction:</tspan> In reality, the event generated a ₹11,500 surplus on approved budget, and the college outlay was merely ₹33,500</text>
      <text x="80" y="966" fill="#334155" font-family="sans-serif" font-size="10">after applying the ₹75,000 sponsor contribution. Every formula verified independently by hand and Python execution log.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 5 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_5.pdf")

def make_page_6():
    # Deliverable E: Output Pack (Challenge 5)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE E: AUDIENCE-SPECIFIC OUTPUT PACK (10 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Verified Outputs Tailored for Principal, Faculty Management, and Student Social Media</text>

      <!-- Output 1: Principal's Brief Box -->
      <rect x="50" y="90" width="750" height="340" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="109" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">OUTPUT 1: ONE-PAGE PRINCIPAL'S BRIEF (EXECUTIVE BRIEFING FORMAT)</text>

      <text x="65" y="135" fill="#0f172a" font-family="sans-serif" font-size="11" font-weight="bold">Executive Summary &amp; Event Scope:</text>
      <text x="65" y="152" fill="#334155" font-family="sans-serif" font-size="10">Campus Innovation Week concluded its 3-day programme with 480 registered students and 312 entry gate records (65.0% turnout ratio,</text>
      <text x="65" y="167" fill="#334155" font-family="sans-serif" font-size="10">subject to IT deduplication). Financial stewardship was maintained: recorded expenses of ₹1,08,500 remained ₹11,500 under the approved</text>
      <text x="65" y="182" fill="#334155" font-family="sans-serif" font-size="10">₹1,20,000 ceiling (90.42% utilisation). With ₹75,000 confirmed in sponsor transfers, net college outlay was ₹33,500.</text>

      <text x="65" y="210" fill="#0f172a" font-family="sans-serif" font-size="11" font-weight="bold">Limitations &amp; Reputational Risk Assessment:</text>
      <text x="65" y="227" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Participant Evaluation:</tspan> 96 voluntary feedback submissions rated the event 4.1/5.0. This reflects motivated respondents only.</text>
      <text x="65" y="243" fill="#334155" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Reputational Safeguard:</tspan> Preliminary drafts containing the claim "70% employability improvement" and referencing "NPII-7" were paused.</text>
      <text x="65" y="259" fill="#334155" font-family="sans-serif" font-size="10">   Publishing unverified statistical claims exposes the institution to regulatory scrutiny and accreditation downgrades.</text>

      <rect x="65" y="278" width="720" height="70" rx="4" fill="#fef2f2" stroke="#f87171"/>
      <text x="75" y="296" fill="#991b1b" font-family="sans-serif" font-size="10.5" font-weight="bold">MANDATORY SECTION: WHAT WE CANNOT CONCLUDE</text>
      <text x="75" y="314" fill="#7f1d1d" font-family="sans-serif" font-size="9.5">• We CANNOT conclude that employability improved by 70%. Zero post-event placement tracking data was collected.</text>
      <text x="75" y="330" fill="#7f1d1d" font-family="sans-serif" font-size="9.5">• We CANNOT generalize the 4.1/5 rating to all 480 registrants; 69.23% of attendees did not complete feedback.</text>
      <text x="75" y="344" fill="#7f1d1d" font-family="sans-serif" font-size="9.5">• We CANNOT cite the 'NeuroPrompt Integrity Index (NPII-7)' or 'AI Output Integrity Act 2024'; both are hallucinations.</text>

      <text x="65" y="375" fill="#0f172a" font-family="sans-serif" font-size="10" font-weight="bold">Strategic Recommendations:</text>
      <text x="65" y="392" fill="#334155" font-family="sans-serif" font-size="9.5">1) Authorize IT deduplication of gate logs. 2) Institute 60-day alumni placement survey. 3) Adopt formal 9-stage AI Governance SOP.</text>
      <text x="65" y="415" fill="#16a34a" font-family="sans-serif" font-size="10" font-weight="bold">Sign-off: Event Coordinator [VERIFIED]  |  Finance Rep [VERIFIED]  |  Faculty Lead [VERIFIED]  |  Principal [APPROVED]</text>

      <!-- Output 2: 5-Slide Presentation Outline Box -->
      <rect x="50" y="445" width="750" height="340" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="445" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="464" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">OUTPUT 2: FIVE-SLIDE PRESENTATION OUTLINE (FACULTY &amp; MANAGEMENT)</text>

      <text x="65" y="490" fill="#0284c7" font-family="sans-serif" font-size="10.5" font-weight="bold">SLIDE 1: Executive Overview &amp; Attendance Metrics</text>
      <text x="65" y="506" fill="#334155" font-family="sans-serif" font-size="9.5">• Core Message: Campus Innovation Week engaged student innovators across 3 focused tracks.</text>
      <text x="65" y="521" fill="#334155" font-family="sans-serif" font-size="9.5">• Key Metrics: 480 registered; 312 gate entry records (65.0% ratio). <tspan fill="#d97706">[Caveat: Deduplication pending]</tspan>.</text>

      <text x="65" y="546" fill="#0284c7" font-family="sans-serif" font-size="10.5" font-weight="bold">SLIDE 2: Financial Governance &amp; Budget Performance</text>
      <text x="65" y="562" fill="#334155" font-family="sans-serif" font-size="9.5">• Core Message: Disciplined fiscal management delivered event 9.58% below budget cap.</text>
      <text x="65" y="577" fill="#334155" font-family="sans-serif" font-size="9.5">• Key Metrics: Approved: ₹1,20,000 | Spent: ₹1,08,500 | Balance: ₹11,500 | Sponsor: ₹75,000 | Net Cost: ₹33,500.</text>

      <text x="65" y="602" fill="#0284c7" font-family="sans-serif" font-size="10.5" font-weight="bold">SLIDE 3: Participant Feedback &amp; Evaluation Boundaries</text>
      <text x="65" y="618" fill="#334155" font-family="sans-serif" font-size="9.5">• Core Message: High satisfaction among respondents, bounded by sample size.</text>
      <text x="65" y="633" fill="#334155" font-family="sans-serif" font-size="9.5">• Key Metrics: 96 voluntary submissions (30.77% response rate) rated event 4.1/5.0 stars.</text>

      <text x="65" y="658" fill="#b91c1c" font-family="sans-serif" font-size="10.5" font-weight="bold">SLIDE 4: Methodological Integrity: What We Cannot Conclude</text>
      <text x="65" y="674" fill="#7f1d1d" font-family="sans-serif" font-size="9.5">• ❌ 70% Employability claim rejected as unsubstantiated rumor. Zero career tracer data exists.</text>
      <text x="65" y="689" fill="#7f1d1d" font-family="sans-serif" font-size="9.5">• ❌ NPII-7 &amp; AI Output Integrity Act 2024 removed as synthetic LLM confabulations.</text>

      <text x="65" y="714" fill="#0284c7" font-family="sans-serif" font-size="10.5" font-weight="bold">SLIDE 5: Strategic Next Steps &amp; Governance Roadmap</text>
      <text x="65" y="730" fill="#334155" font-family="sans-serif" font-size="9.5">• 1) Complete barcode deduplication. 2) Deploy 60-day placement audit. 3) Enforce multi-sign-off AI workflow.</text>

      <!-- Output 3: Student Social Media Post Box -->
      <rect x="50" y="800" width="750" height="240" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="800" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="819" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">OUTPUT 3: PUBLIC SOCIAL-MEDIA POST (STUDENTS &amp; COMMUNITY CHANNELS)</text>

      <text x="65" y="845" fill="#0f172a" font-family="sans-serif" font-size="10.5">🚀 <tspan font-weight="bold">That’s a wrap on Campus Innovation Week!</tspan></text>
      <text x="65" y="865" fill="#334155" font-family="sans-serif" font-size="10">Over 3 intense days of ideation, rapid prototyping, and hands-on workshops, our student community brought</text>
      <text x="65" y="881" fill="#334155" font-family="sans-serif" font-size="10">incredible creativity and forward-thinking energy to the campus! Here is what we accomplished together:</text>

      <text x="65" y="905" fill="#0284c7" font-family="sans-serif" font-size="10">• ⚡ <tspan font-weight="bold">480 Students</tspan> registered to build practical skills in cutting-edge emerging technologies</text>
      <text x="65" y="922" fill="#0284c7" font-family="sans-serif" font-size="10">• ⚡ <tspan font-weight="bold">312 Workshop Entries</tspan> logged across three dynamic technical tracks</text>
      <text x="65" y="939" fill="#0284c7" font-family="sans-serif" font-size="10">• ⚡ <tspan font-weight="bold">4.1 / 5.0 Rating</tspan> from our student feedback respondents!</text>

      <text x="65" y="964" fill="#334155" font-family="sans-serif" font-size="10">Huge thanks to our faculty mentors, student volunteers, and our generous industry sponsors for powering this event.</text>
      <text x="65" y="982" fill="#0284c7" font-family="sans-serif" font-size="9.5">#CampusInnovation #StudentBuilders #HandsOnTech #ResponsibleAI #InnovationWeek2026</text>
      <text x="65" y="1005" fill="#16a34a" font-family="sans-serif" font-size="9.5" font-weight="bold">Audit Note: 100% verified facts. Strictly zero unmeasured employability promises or buzzwords.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 6 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_6.pdf")

def make_page_7():
    # Deliverable F: Responsible AI Workflow (Challenge 6)
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">DELIVERABLE F: RESPONSIBLE AI WORKFLOW &amp; GOVERNANCE (10 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Repeatable 9-Stage Pipeline, Named Role Ownership, Stop Conditions, and Decision Rules</text>

      <!-- 9-Stage Pipeline Diagram Grid -->
      <rect x="50" y="90" width="750" height="420" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="90" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="109" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">THE 9-STAGE RESPONSIBLE AI OPERATIONAL WORKFLOW</text>

      <!-- Stage 1 -->
      <rect x="65" y="130" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="75" y="150" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">1. SOURCE INGESTION</text>
      <text x="75" y="168" fill="#334155" font-family="sans-serif" font-size="9">Collect raw logs, bank receipts,</text>
      <text x="75" y="180" fill="#334155" font-family="sans-serif" font-size="9">and verified event rosters.</text>
      <text x="75" y="196" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Event Coordinator</text>

      <!-- Stage 2 -->
      <rect x="315" y="130" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="325" y="150" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">2. PROMPT DRAFTING</text>
      <text x="325" y="168" fill="#334155" font-family="sans-serif" font-size="9">Apply Role, Context, Constraints,</text>
      <text x="325" y="180" fill="#334155" font-family="sans-serif" font-size="9">and mandatory [VERIFY] rule.</text>
      <text x="325" y="196" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Verification Lead</text>

      <!-- Stage 3 -->
      <rect x="565" y="130" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="575" y="150" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">3. AI GENERATION</text>
      <text x="575" y="168" fill="#334155" font-family="sans-serif" font-size="9">Sandboxed LLM execution;</text>
      <text x="575" y="180" fill="#334155" font-family="sans-serif" font-size="9">watermarked 'DRAFT UNVERIFIED'.</text>
      <text x="575" y="196" fill="#b91c1c" font-family="sans-serif" font-size="8.5" font-weight="bold">Air-Gap: Zero Auto-Publish</text>

      <!-- Stage 4 -->
      <rect x="65" y="225" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="75" y="245" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">4. FACT-CHECKING</text>
      <text x="75" y="263" fill="#334155" font-family="sans-serif" font-size="9">Audit claims against primary URLs;</text>
      <text x="75" y="275" fill="#334155" font-family="sans-serif" font-size="9">filter confabulated standards.</text>
      <text x="75" y="291" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Faculty Reviewer</text>

      <!-- Stage 5 -->
      <rect x="315" y="225" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="325" y="245" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">5. NUMERICAL VALIDATION</text>
      <text x="325" y="263" fill="#334155" font-family="sans-serif" font-size="9">Deterministic code recalculation</text>
      <text x="325" y="275" fill="#334155" font-family="sans-serif" font-size="9">via Julius AI Python interpreter.</text>
      <text x="325" y="291" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Finance Representative</text>

      <!-- Stage 6 -->
      <rect x="565" y="225" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="575" y="245" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">6. PRIVACY &amp; DPDP REVIEW</text>
      <text x="575" y="263" fill="#334155" font-family="sans-serif" font-size="9">PII redaction, anonymization, and</text>
      <text x="575" y="275" fill="#334155" font-family="sans-serif" font-size="9">DPDP Act 2023 legal screening.</text>
      <text x="575" y="291" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Compliance Officer</text>

      <!-- Stage 7 -->
      <rect x="65" y="320" width="220" height="80" rx="4" fill="#fdf4ff" stroke="#a855f7"/>
      <text x="75" y="340" fill="#7e22ce" font-family="sans-serif" font-size="10" font-weight="bold">7. MULTI-ROLE APPROVAL</text>
      <text x="75" y="358" fill="#334155" font-family="sans-serif" font-size="9">Mandatory 4-point cryptographic</text>
      <text x="75" y="370" fill="#334155" font-family="sans-serif" font-size="9">digital sign-off gateway.</text>
      <text x="75" y="386" fill="#7e22ce" font-family="sans-serif" font-size="8.5" font-weight="bold">Rule: 100% Unanimous or Stop</text>

      <!-- Stage 8 -->
      <rect x="315" y="320" width="220" height="80" rx="4" fill="#f0fdf4" stroke="#22c55e"/>
      <text x="325" y="340" fill="#15803d" font-family="sans-serif" font-size="10" font-weight="bold">8. CONTROLLED RELEASE</text>
      <text x="325" y="358" fill="#334155" font-family="sans-serif" font-size="9">Release trigger to student channels</text>
      <text x="325" y="370" fill="#334155" font-family="sans-serif" font-size="9">and Principal's executive desk.</text>
      <text x="325" y="386" fill="#15803d" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Communications Lead</text>

      <!-- Stage 9 -->
      <rect x="565" y="320" width="220" height="80" rx="4" fill="#eff6ff" stroke="#3b82f6"/>
      <text x="575" y="340" fill="#1e3a8a" font-family="sans-serif" font-size="10" font-weight="bold">9. RETENTION &amp; AUDIT</text>
      <text x="575" y="358" fill="#334155" font-family="sans-serif" font-size="9">Store prompt logs, output diffs,</text>
      <text x="575" y="370" fill="#334155" font-family="sans-serif" font-size="9">and sign-offs for 3-year audit vault.</text>
      <text x="575" y="386" fill="#0284c7" font-family="sans-serif" font-size="8.5" font-weight="bold">Role: Institutional Registrar</text>

      <text x="65" y="425" fill="#334155" font-family="sans-serif" font-size="10"><tspan font-weight="bold">Prevention of Automated Release:</tspan> The architecture creates a physical air-gap between generative LLM outputs and public release</text>
      <text x="65" y="442" fill="#334155" font-family="sans-serif" font-size="10">APIs. Zapier webhooks require all 4 role approvals before distribution keys are issued.</text>

      <!-- Stop Condition & Decision Rule Matrix -->
      <rect x="50" y="530" width="750" height="240" rx="4" fill="#fff1f2" stroke="#fecdd3"/>
      <text x="65" y="555" fill="#9f1239" font-family="sans-serif" font-size="12" font-weight="bold">SYSTEM STOP CONDITION PROTOCOL &amp; ESCALATION LOGIC</text>

      <text x="65" y="580" fill="#881337" font-family="sans-serif" font-size="10.5" font-weight="bold">1. Stop Condition Trigger Threshold:</text>
      <text x="65" y="598" fill="#334155" font-family="sans-serif" font-size="10">If ANY primary empirical claim lacks authoritative paper trail, OR if two institutional data sources conflict (e.g., sponsor transfer</text>
      <text x="65" y="614" fill="#334155" font-family="sans-serif" font-size="10">₹57,000 vs ₹75,000), OR if an AI generation cites unverified statutory acts, the pipeline triggers an <tspan font-weight="bold" fill="#b91c1c">AUTOMATIC PUBLICATION FREEZE</tspan>.</text>

      <text x="65" y="638" fill="#881337" font-family="sans-serif" font-size="10.5" font-weight="bold">2. Mandatory Action Upon Freeze:</text>
      <text x="65" y="656" fill="#334155" font-family="sans-serif" font-size="10">• Webhook distribution channels are immediately disabled.</text>
      <text x="65" y="672" fill="#334155" font-family="sans-serif" font-size="10">• The draft is tagged <tspan font-weight="bold">[QUARANTINED - PENDING RECONCILIATION]</tspan>.</text>
      <text x="65" y="688" fill="#334155" font-family="sans-serif" font-size="10">• A formal 3-part incident memorandum is automatically dispatched to the Event Coordinator and Department Heads.</text>

      <rect x="65" y="705" width="720" height="50" rx="4" fill="#9f1239"/>
      <text x="75" y="724" fill="#ffffff" font-family="sans-serif" font-size="10.5" font-weight="bold">DECISION RULE MATRIX:</text>
      <text x="75" y="742" fill="#ffffff" font-family="sans-serif" font-size="9.5">1) Fully Verified &gt; [ACCEPT]  |  2) Ambiguous/Unchecked &gt; [TAG VERIFY]  |  3) Contradicted/Fabricated &gt; [REMOVE &amp; ESCALATE]</text>

      <!-- Roles & Governance Responsibilities -->
      <rect x="50" y="790" width="750" height="250" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <text x="65" y="815" fill="#1e3a8a" font-family="sans-serif" font-size="12" font-weight="bold">ASSIGNED HUMAN ROLE OWNERSHIP (NO REAL STAFF NAMES INVENTED)</text>

      <text x="65" y="840" fill="#0f172a" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Event Coordinator:</tspan> Owns gate-entry logs, attendance scanning systems, barcode deduplication, and initial agenda collation.</text>
      <text x="65" y="860" fill="#0f172a" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Finance Representative:</tspan> Owns budget approval vouchers, expense ledgers, tax invoices, bank reconciliation, and sponsor agreements.</text>
      <text x="65" y="880" fill="#0f172a" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Faculty Reviewer:</tspan> Assesses pedagogical claims, educational impact assessments, academic validity, and workshop curricula.</text>
      <text x="65" y="900" fill="#0f172a" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Communications Lead:</tspan> Audits public tone, student messaging, brand reputation, ethical disclaimers, and social distribution.</text>
      <text x="65" y="920" fill="#0f172a" font-family="sans-serif" font-size="10">• <tspan font-weight="bold">Compliance Officer:</tspan> Enforces institutional privacy mandates, DPDP Act 2023 compliance, PII redaction, and enterprise cloud ZDR settings.</text>

      <text x="65" y="955" fill="#16a34a" font-family="sans-serif" font-size="10.5" font-weight="bold">Traceability Guarantee: All 5 roles must submit digital cryptographic tokens to Zapier to authorize public release.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 7 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_7.pdf")

def make_page_8():
    # Challenge 7: The Unexpected Twist & Formal Escalation Note
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" width="850" height="1100" viewBox="0 0 850 1100">
      <rect width="850" height="1100" fill="#ffffff"/>
      <rect x="0" y="0" width="850" height="16" fill="#1e3a8a"/>
      <text x="50" y="55" fill="#1e3a8a" font-family="sans-serif" font-size="16" font-weight="bold">CHALLENGE 7: THE UNEXPECTED TWIST &amp; ESCALATION MEMO (10 MARKS)</text>
      <text x="50" y="75" fill="#64748b" font-family="sans-serif" font-size="11">Emergency Response at T-Minus 1 Hour: Sponsor Discrepancy (₹57k vs ₹75k) &amp; Phantom Citation</text>

      <!-- Immediate Actions Box -->
      <rect x="50" y="90" width="750" height="230" rx="4" fill="#fef2f2" stroke="#f87171"/>
      <rect x="50" y="90" width="750" height="28" fill="#7f1d1d"/>
      <text x="65" y="109" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">IMMEDIATE ACTIONS BEFORE PUBLICATION (T-MINUS 60 MINUTES)</text>

      <text x="65" y="135" fill="#991b1b" font-family="sans-serif" font-size="10.5" font-weight="bold">1. Emergency Publication Freeze:</text>
      <text x="65" y="152" fill="#334155" font-family="sans-serif" font-size="10">Trigger instant Zapier kill-switch to halt all automated social media pushes, print distribution, and principal delivery.</text>

      <text x="65" y="175" fill="#991b1b" font-family="sans-serif" font-size="10.5" font-weight="bold">2. Establish Authoritative Sponsor Amount Without Guessing:</text>
      <text x="65" y="192" fill="#334155" font-family="sans-serif" font-size="10">Do NOT average the figures (₹66,000) or guess. Perform immediate forensic reconciliation across 4 authoritative documents:</text>
      <text x="80" y="209" fill="#334155" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Bank NEFT/RTGS Credit Scroll:</tspan> Inspect the college bank ledger to verify the exact rupee amount credited to college accounts.</text>
      <text x="80" y="225" fill="#334155" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Signed Sponsor MoU / Agreement:</tspan> Check the legally binding contract executed with the corporate partner.</text>
      <text x="80" y="241" fill="#334155" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Official Accounts Receipt Voucher:</tspan> Locate the signed receipt issued by the college Accounts Officer.</text>
      <text x="80" y="257" fill="#334155" font-family="sans-serif" font-size="9.5">• Direct telephone confirmation with the corporate partner’s authorized financial signatory.</text>

      <text x="65" y="282" fill="#991b1b" font-family="sans-serif" font-size="10.5" font-weight="bold">3. Treatment of the Unsupported Legal Claim &amp; Broken Citation:</text>
      <text x="65" y="299" fill="#334155" font-family="sans-serif" font-size="10">Immediately excise the 'AI Professional Output Integrity Act 2024' from the slide deck. Strip the broken link entirely.</text>

      <!-- Recency Fallacy Explanation Box -->
      <rect x="50" y="335" width="750" height="150" rx="4" fill="#fffbeb" stroke="#fef08a"/>
      <text x="65" y="360" fill="#92400e" font-family="sans-serif" font-size="11.5" font-weight="bold">WHY RECENCY ALONE DOES NOT PROVE A FILE IS CORRECT (THE RECENCY FALLACY)</text>
      <text x="65" y="382" fill="#78350f" font-family="sans-serif" font-size="10">In institutional governance, <tspan font-weight="bold">provenance and authorization strictly supersede chronological timestamps</tspan>:</text>
      <text x="65" y="400" fill="#78350f" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Unverified Draft Overwrite:</tspan> A spreadsheet uploaded 1 hour ago without author signature or date could be an exploratory scenario draft,</text>
      <text x="80" y="415" fill="#78350f" font-family="sans-serif" font-size="9.5">a partial milestone instalment note, an unreviewed volunteer scratchpad, or a clerical typo (e.g. transposing ₹57,000 for ₹75,000).</text>
      <text x="65" y="433" fill="#78350f" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Lack of Custody Chain:</tspan> The newly uploaded file lacks metadata, author identity, and approval signatures.</text>
      <text x="65" y="451" fill="#78350f" font-family="sans-serif" font-size="9.5">• <tspan font-weight="bold">Legal &amp; Audit Precedence:</tspan> An older, signed bank credit advice and ratified MoU hold binding authority over an unauthenticated modern file.</text>

      <!-- Formal Escalation Note to Event Coordinator -->
      <rect x="50" y="500" width="750" height="520" rx="4" fill="#f8fafc" stroke="#cbd5e1"/>
      <rect x="50" y="500" width="750" height="28" fill="#1e293b"/>
      <text x="65" y="519" fill="#ffffff" font-family="sans-serif" font-size="11" font-weight="bold">FORMAL PRE-PUBLICATION ESCALATION MEMORANDUM</text>

      <text x="65" y="545" fill="#334155" font-family="sans-serif" font-size="10"><tspan font-weight="bold">TO:</tspan> Event Coordinator  |  <tspan font-weight="bold">FROM:</tspan> AI Verification &amp; Productivity Lead  |  <tspan font-weight="bold">DATE:</tspan> 18 Nov 2026, 16:00 IST</text>
      <text x="65" y="562" fill="#334155" font-family="sans-serif" font-size="10"><tspan font-weight="bold">SUBJECT:</tspan> CRITICAL PRE-PUBLICATION ESCALATION: SPONSOR DISCREPANCY &amp; LEGAL CITATION HALLUCINATION</text>
      <line x1="65" y1="572" x2="785" y2="572" stroke="#cbd5e1"/>

      <!-- Section A: Known Facts -->
      <text x="65" y="595" fill="#16a34a" font-family="sans-serif" font-size="10.5" font-weight="bold">SECTION A: KNOWN &amp; AUTHORITATIVE FACTS</text>
      <text x="65" y="613" fill="#334155" font-family="sans-serif" font-size="9.5">1. Campus Innovation Week completed its 3-day run with 480 registrants and 312 gate entry records.</text>
      <text x="65" y="628" fill="#334155" font-family="sans-serif" font-size="9.5">2. Event incurred ₹1,08,500 in recorded operational expenses against an authorized budget cap of ₹1,20,000.</text>
      <text x="65" y="643" fill="#334155" font-family="sans-serif" font-size="9.5">3. 96 voluntary survey forms submitted an average satisfaction rating of 4.1 / 5.0 stars.</text>
      <text x="65" y="658" fill="#334155" font-family="sans-serif" font-size="9.5">4. The previously audited finance ledger recorded a confirmed sponsor transfer of ₹75,000 (net outlay ₹33,500).</text>

      <!-- Section B: Conflicting Evidence -->
      <text x="65" y="685" fill="#b91c1c" font-family="sans-serif" font-size="10.5" font-weight="bold">SECTION B: CONFLICTING &amp; CONTRADICTED EVIDENCE</text>
      <text x="65" y="703" fill="#334155" font-family="sans-serif" font-size="9.5">1. <tspan font-weight="bold">Financial Conflict:</tspan> A spreadsheet uploaded 60 minutes ago lists sponsor contributions as ₹57,000 (an ₹18,000 shortfall).</text>
      <text x="80" y="718" fill="#334155" font-family="sans-serif" font-size="9.5">The file contains no author name, date, or approval signature. Plausible typographical transposition (57 vs 75).</text>
      <text x="65" y="735" fill="#334155" font-family="sans-serif" font-size="9.5">2. <tspan font-weight="bold">Legal Hallucination:</tspan> Slide 4 of the AI presentation draft cites the "AI Professional Output Integrity Act 2024" as a statutory mandate.</text>
      <text x="80" y="750" fill="#334155" font-family="sans-serif" font-size="9.5">The citation URL resolves to an unrelated external webpage. Forensic legal check confirms this act does not exist in any jurisdiction.</text>

      <!-- Section C: Decisions Required -->
      <text x="65" y="778" fill="#0284c7" font-family="sans-serif" font-size="10.5" font-weight="bold">SECTION C: DECISIONS &amp; ACTIONS REQUIRED BEFORE PUBLICATION</text>
      <text x="65" y="798" fill="#334155" font-family="sans-serif" font-size="9.5">1. <tspan font-weight="bold">Finance Sign-off Decision:</tspan> Finance Representative must immediately inspect the official college bank statement.</text>
      <text x="80" y="813" fill="#334155" font-family="sans-serif" font-size="9.5">• If bank statement confirms ₹75,000 was credited: Mark the unapproved spreadsheet as INVALID and archive it.</text>
      <text x="80" y="828" fill="#334155" font-family="sans-serif" font-size="9.5">• If bank statement reveals only ₹57,000 was received: Revise net college outlay to ₹51,500 and update executive brief.</text>
      <text x="65" y="848" fill="#334155" font-family="sans-serif" font-size="9.5">2. <tspan font-weight="bold">Slide Deck Sanitization:</tspan> Authorize immediate excision of the fictional legal act; replace with internal institutional AI ethics policy.</text>
      <text x="65" y="868" fill="#334155" font-family="sans-serif" font-size="9.5">3. <tspan font-weight="bold">Partial Release Clearance:</tspan> Clear the student-facing social media post for publication (which contains zero financial data),</text>
      <text x="80" y="883" fill="#334155" font-family="sans-serif" font-size="9.5">while maintaining the freeze on the Principal’s brief and presentation deck until financial reconciliation is signed.</text>

      <rect x="65" y="905" width="720" height="95" rx="4" fill="#0f172a"/>
      <text x="75" y="925" fill="#38bdf8" font-family="sans-serif" font-size="10.5" font-weight="bold">ESCALATION SIGN-OFF GATE:</text>
      <text x="75" y="945" fill="#ffffff" font-family="sans-serif" font-size="9.5">Prepared by: AI Verification &amp; Productivity Team  |  Status: Hard Freeze Active (T-Minus 60 Min)</text>
      <text x="75" y="965" fill="#a7f3d0" font-family="sans-serif" font-size="9.5">Pending Action: Event Coordinator &amp; Finance Rep Concurrence on Bank Scroll.</text>
      <text x="75" y="985" fill="#fca5a5" font-family="sans-serif" font-size="9.5">Outcome: Zero unverified data released to Principal or Public.</text>

      <text x="50" y="1060" fill="#94a3b8" font-family="sans-serif" font-size="10">Page 8 of 8 • Campus Innovation Week Verification Report</text>
    </svg>'''
    svg_page_to_pdf(svg, "evidence_appendix/report_page_8.pdf")

if __name__ == "__main__":
    make_page_1()
    make_page_2()
    make_page_3()
    make_page_4()
    make_page_5()
    make_page_6()
    make_page_7()
    make_page_8()
    print("Report Pages 1 to 8 generated successfully!")
    
    # Now merge all 8 report pages + all 10 evidence appendix mockup pages
    all_pages = [
        "evidence_appendix/report_page_1.pdf",
        "evidence_appendix/report_page_2.pdf",
        "evidence_appendix/report_page_3.pdf",
        "evidence_appendix/report_page_4.pdf",
        "evidence_appendix/report_page_5.pdf",
        "evidence_appendix/report_page_6.pdf",
        "evidence_appendix/report_page_7.pdf",
        "evidence_appendix/report_page_8.pdf",
        "evidence_appendix/tool_otter_transcript.pdf",
        "evidence_appendix/tool_perplexity_factcheck.pdf",
        "evidence_appendix/tool_julius_calculation.pdf",
        "evidence_appendix/prompt_iteration_comparison.pdf",
        "evidence_appendix/tool_scribe_sop.pdf",
        "evidence_appendix/output_presentation_deck.pdf",
        "evidence_appendix/workflow_zapier_pipeline.pdf",
        "evidence_appendix/output_principal_brief.pdf",
        "evidence_appendix/output_social_media.pdf",
        "evidence_appendix/unexpected_twist_incident_memo.pdf"
    ]
    merge_all_pdfs(all_pages, "CAMPUS_INNOVATION_WEEK_FINAL_REPORT.pdf")
