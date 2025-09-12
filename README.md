# GAIDeT Declaration Generator

[![w3id.org permanent identifier](https://img.shields.io/badge/w3id.org-gaidet-blue)](https://w3id.org/gaidet/)

This is a **beta version** of the <a href="https://panbibliotekar.github.io/gaidet-declaration/">GAIDeT Declaration Generator</a> — an interactive HTML tool that helps researchers transparently disclose the use of Generative AI (GAI) tools in scientific writing and research.
The declaration is based on the **GAIDeT taxonomy** (Generative AI Delegation Taxonomy), developed to promote transparency and accountability in academic publishing. 
We recommend presenting the generated statement as a separate section immediately following the CRediT authorship contributions, in line with the model proposed in our manuscript. This ensures clear delineation between human and AI contributions in the research workflow.

---

## Resources

- **Permanent identifier (PURL):** https://w3id.org/gaidet/  
- **Ontology (OWL):** [gaidet.owl](https://w3id.org/gaidet/gaidet.owl)  
- **Source taxonomy (YAML):** [terms.yml](https://w3id.org/gaidet/terms.yml)  
- **Interactive generator (HTML):** [index.html](https://panbibliotekar.github.io/gaidet-declaration/)

All GAIDeT terms are resolvable as URIs, e.g.  
- Text generation → https://w3id.org/gaidet/0000030  
- Data analysis → https://w3id.org/gaidet/0000026  

---

## 🧪 How it works

The GAIDeT Declaration Generator is an interactive HTML tool that helps researchers declare the use of generative AI in scientific writing and publishing. Here's how to use it:

1. Fill in the name of the responsible author  
   *(or enter “Collective responsibility” if all authors share responsibility)*

2. Specify which version of the LLM was used
   *(e.g., ChatGPT-4.5, Claude 3, Gemini 1.5)*

3. Select the relevant research and writing tasks  
   *(based on the GAIDeT taxonomy of delegable tasks)*

4. Optionally, add a short comment for clarification

5. Click **“Generate”** to create a declaration that can be copied into the Methods, Acknowledgments, or CRediT section of a manuscript, or it could be supplied as a new and separate GAI use statement.

---

## 🔗 Crossref Assertion Helper

We have also developed the **GAIDeT Crossref Assertion Helper** — an interactive tool to simplify adding GAIDeT disclosures into Crossref metadata via Crossmark assertions.  

👉 English version: [gaidet-crossref-helper.html](https://panbibliotekar.github.io/gaidet-declaration/gaidet-crossref-helper.html)  
👉 Ukrainian version: [gaidet-crossref-helper-ua.html](https://panbibliotekar.github.io/gaidet-declaration/gaidet-crossref-helper-ua.html)  

📖 Full instruction with XML and Web Deposit Form examples is available here:  
[Instruction for Editors and Depositors: How to Integrate GAIDeT into Crossref Metadata via Crossmark (PDF)](https://doi.org/10.5281/zenodo.17101228)  

---

## 📄 Citation

If you use this tool or taxonomy in your research, please cite the following manuscript:

> Suchikova, Y., Tsybuliak, N., & Teixeira da Silva, J. A. & Nazarovets, S. (2025). GAIDeT (Generative AI Delegation Taxonomy): A taxonomy for humans to delegate tasks to generative artificial intelligence in scientific research and publishing. <i>Accountability in Research</i>, in press. <a href="https://doi.org/10.1080/08989621.2025.2544331">https://doi.org/10.1080/08989621.2025.2544331</a>

📬 Full text available on  <a href="https://www.researchgate.net/publication/394419819_GAIDeT_Generative_AI_Delegation_Taxonomy_A_taxonomy_for_humans_to_delegate_tasks_to_generative_artificial_intelligence_in_scientific_research_and_publishing">request via ResearchGate</a>.

---

## 📩 Feedback

We welcome your suggestions and comments to improve the tool before public release.  
Contact us at: **serhii.nazarovets@gmail.com**; **yanasuchikova@gmail.com**

---

## ⚖️ License

© 2025 Yana Suchikova, Natalia Tsybuliak, Jaime A. Teixeira da Silva, Serhii Nazarovets – MIT License
