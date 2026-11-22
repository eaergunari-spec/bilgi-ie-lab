# BİLGİ IE Lab

Interactive Industrial Engineering taster labs for Istanbul Bilgi University.

## From Forecast to Decision

A 50-minute preparatory-program decision lab built around one integrated operations problem:

**forecast → resource allocation → optimization → trade-offs → uncertainty → simulation → adaptation**

The student-facing lab is a fully static HTML/CSS/JavaScript site, so it can run on GitHub Pages without a backend.

### Student lab

Once GitHub Pages is enabled for this repository:

https://eaergunari-spec.github.io/bilgi-ie-lab/

### Repository structure

- `index.html` — the complete interactive student lab
- `code/code_moment_1.py` — exhaustive search / optimization reveal
- `code/code_moment_2.py` — Monte Carlo simulation reveal
- `data/forecast_case.csv` — synthetic forecast case
- `data/actual_evening_example.csv` — synthetic realized demand
- `data/policy_comparison_sample.csv` — illustrative policy comparison

### Classroom flow

The lab supports:
- allocating 20 couriers across four Istanbul zones,
- live throughput and service-level feedback,
- a throughput-maximizing optimization reveal,
- an efficiency-versus-service-floor comparison,
- forecast-versus-actual demand,
- a 1,000-evening uncertainty simulation,
- a disruption and re-optimization scenario,
- two short Python code moments students can copy into a notebook.

### Enable GitHub Pages

In **Settings → Pages**:
1. Under **Build and deployment**, select **Deploy from a branch**.
2. Choose **main** and **/(root)**.
3. Click **Save**.

---
Istanbul Bilgi University · Department of Industrial Engineering
