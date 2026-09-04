# Enhancing Digital Forensics Evidence Analysis with Large Language Models

<img src="https://upload.wikimedia.org/wikipedia/commons/3/3c/BJA_Logo.png" width="150">

## Overview

As the scale and complexity of digital evidence grow in the modern world, the integration of Large Language Models (LLMs) into digital forensics offers a transformative path forward. This three-hour tutorial at KDD 2025 explores how LLMs can be effectively leveraged to automate the analysis of forensic artifacts, extract meaningful patterns from raw data, and support timely, intelligent decision-making in investigations.

Participants will engage in an interactive, hands-on environment that combines practical labs, real-world datasets, and guided exploration of LLM tools. The tutorial covers key applications such as evidence entity recognition, knowledge graph construction from forensic records, and insight extraction from browser activity and sensitive communication datasets.

Designed for researchers, practitioners, and students alike, this session emphasizes both technical rigor and ethical responsibility. By the end of the tutorial, attendees will have a deep understanding of how to deploy LLMs responsibly in forensic workflows, ultimately enhancing justice, transparency, and investigative efficiency in an increasingly data-driven world.

---

## Date and Location

**August 3–7, 2025**  
31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining (KDD)  
Toronto, Canada

---

## Speakers

**Eric Xu**  
University of Maryland, College Park  
Email: [exu17288@terpmail.umd.edu](mailto:exu17288@terpmail.umd.edu)

**Dr. Lin Deng**  
Associate Professor, Towson University  
Email: [ldeng@towson.edu](mailto:ldeng@towson.edu)

**Damodar Dhital**  
Towson University  
Email: [ddhital1@students.towson.edu](mailto:ddhital1@students.towson.edu)

---

## Table of Contents


- Introduction [KDD2025(PPTX)](https://github.com/damodar344/digital-forensics-lab/blob/main/KDD2025/Slides/KDD2025.pdf)
- Forensic evidence entity recognition (hands-on lab)
  - [Evidence entity recognition](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/PhishingAttack/PhishingAttackScenarioDemo/01_evidence_entity_recognition.ipynb)
  - [Visualize evidence and their relations](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/PhishingAttack/PhishingAttackScenarioDemo/02_evidence_knowledge_dot_generator.ipynb)

- Evidence knowledge graphs reconstruction (hands-on lab)
  - [Construct a knowledge graph in STIX (zero-shot)](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/PhishingAttack/PhishingAttackScenarioDemo/03_evidence_stix_zeroshot.ipynb)
  - [Construct a knowledge graph in STIX (one-shot)](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/PhishingAttack/PhishingAttackScenarioDemo/04_evidence_stix_oneshot.ipynb)
  - [Compare one-shot vs. zero-shot](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/PhishingAttack/PhishingAttackScenarioDemo/05_evidence_stix_dot_generator.ipynb)
- Profiling suspect based on browser history (hands-on lab)
  - [Intro](/AI4Forensics/CKIM2024/BrowserHistory/Eric/HistoryProfilingLLMsIntro.pptx)
  - [Profiling lab](https://colab.research.google.com/github/frankwxu/digital-forensics-lab/blob/main/AI4Forensics/CKIM2024/BrowserHistory/Eric/profile_browser_history_Eric.ipynb) and [video](https://youtu.be/flfKG2Cbmu4)
  - [Data Preprocessing](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/BrowserHistory/profile_browser_history_Eric_dataprocess.ipynb)
  - [Student Practice](/AI4Forensics/CKIM2024/BrowserHistory/Eric/HistoryProfilingLLMsLab.docx)
- [Insight on LLM Forensic Ransomware](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/BrowserHistory/LLMForensicRansomwareDemo.ipynb)
- [Ireland’s Health Service Executive Ransomware](https://colab.research.google.com/github/damodar344/digital-forensics-lab/blob/main/KDD2025/BrowserHistory/HSERANSOMEWARE.ipynb)
- Challenges and Limitations of Leveraging LLM in Digital Forensics
- Conclusion


---

## Tutorial Environment Setup

Participants will engage in hands-on exercises using **Google Colab**, **LangChain**, and **Gemini LLM APIs**.  
All code, datasets, and resources are provided via a public GitHub repository.

---

## Societal Impact

By leveraging LLMs in digital investigations, this tutorial empowers professionals to improve justice outcomes, uncover hidden patterns in large datasets, and enhance cybersecurity efforts. It also addresses ethical considerations to ensure responsible AI deployment.

---

## Citation

Xu, Eric, and Deng, Lin. "Enhancing Digital Forensics Evidence Analysis with Large Language Models." In _Proceedings of the 31st ACM SIGKDD Conference on Knowledge Discovery and Data Mining V. 2_, pp. 6251-6252. 2025. (https://dl.acm.org/doi/abs/10.1145/3711896.3737600)

## Acknowledgments

This tutorial is partially supported by the **Bureau of Justice Assistance (2019-DF-BX-K001)**.
