# BİLGİ IE Lab

Interactive Industrial Engineering taster labs for Istanbul Bilgi University.

## From Forecast to Decision

A 50-minute preparatory-program decision lab built around one integrated operations problem:

**forecast → resource allocation → optimization → trade-offs → uncertainty → simulation → adaptation**

### Student lab

https://eaergunari-spec.github.io/bilgi-ie-lab/

The main page includes two **Open Python Lab** links that launch browser-based JupyterLite notebooks:

- Code Moment 1 — Optimization
- Code Moment 2 — Simulation

JupyterLite runs entirely in the browser with the Pyodide Python kernel. Students do **not** need a Google account, a Jupyter server, Visual Studio, or a local Python installation.

### Repository structure

- `index.html` — interactive student decision lab
- `jupyterlite/content/01_Optimization.ipynb` — exhaustive-search optimization notebook
- `jupyterlite/content/02_Simulation.ipynb` — Monte Carlo simulation notebook
- `requirements-jupyterlite.txt` — JupyterLite/Pyodide build dependencies
- `.github/workflows/deploy-jupyterlite.yml` — builds the complete site and deploys it to GitHub Pages
- `code/` — standalone Python versions of the two code moments
- `data/` — synthetic classroom data

### Classroom flow

The lab supports:
- allocating 20 couriers across four Istanbul zones,
- live throughput and service-level feedback,
- a throughput-maximizing optimization reveal,
- an efficiency-versus-service-floor comparison,
- forecast-versus-actual demand,
- a 1,000-evening uncertainty simulation,
- a disruption and re-optimization scenario,
- two short Python notebooks that run without login or installation.

### Deployment

The GitHub Actions workflow builds JupyterLite, combines it with the main student lab, and deploys the complete site to GitHub Pages.

---
Istanbul Bilgi University · Department of Industrial Engineering
