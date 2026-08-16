---
name: utfpr-tcc-abnt
description: Strict guidelines for creating technical documents, monographs, and papers following UTFPR (Universidade Tecnológica Federal do Paraná) and ABNT (Associação Brasileira de Normas Técnicas) standards in English.
tags: "academic, abnt, utfpr, tcc, monograph, formatting, citations, nbr-14724"
---

# UTFPR & ABNT Formatting Guidelines for Technical Papers

This skill defines the structure, formatting, and aesthetic required to produce technical documentation, monographs (TCCs), and papers that comply with the academic standards of UTFPR and ABNT, specifically adapted for English-language documents.

## Document Structure (ABNT NBR 14724)
A technical monograph or paper must be divided into three main parts:

### 1. Pre-textual Elements (Elementos Pré-textuais)
- **Title Page (Capa & Folha de Rosto):** Institution name, author, title, subtitle, city, year.
- **Abstract (Resumo/Abstract):** A single paragraph (150-500 words) summarizing the context, objective, methodology, results, and conclusion. Followed by Keywords.
- **Table of Contents (Sumário):** Exact alignment of sections and page numbers (or logical links in Markdown).
- **List of Figures / Tables / Abbreviations:** Optional but highly recommended for technical works.

### 2. Textual Elements (Elementos Textuais)
Sections must be numbered sequentially using Arabic numerals (e.g., 1, 1.1, 1.1.1).
- **1. Introduction:**
  - Contextualization and Theme (Theme definition).
  - Problem Statement (Problematização).
  - Objectives (General and Specific).
  - Justification (Why this work is relevant).
- **2. Theoretical Foundation (Referencial Teórico):**
  - Literature review and explanation of every core technology used.
  - Subsections for each major concept (e.g., 2.1 Large Language Models, 2.2 Notification-Oriented Paradigm, etc.).
- **3. Methodology (Metodologia):**
  - Detailed explanation of the architecture, implementation steps, and engineering decisions.
  - Clear separation of hardware, software, and protocols.
- **4. Results and Discussion (Resultados e Discussões):**
  - Performance metrics, architectural achievements, optimizations, and validations.
- **5. Conclusion (Conclusão / Considerações Finais):**
  - Summary of the achievements regarding the objectives.
  - Future works (Trabalhos futuros).

### 3. Post-textual Elements (Elementos Pós-textuais)
- **References (Referências):** Must follow ABNT NBR 6023 (Author. Title. Edition. City: Publisher, Year).
- **Appendices / Annexes:** Extra code, configurations, or raw data.

## Writing Style and Aesthetics
- **Tone:** Formal, academic, objective, third-person passive voice (e.g., "It was observed that..." instead of "I saw that...").
- **Formatting in Markdown:**
  - Use `# 1 INTRODUCTION` for main chapters (all caps is common in ABNT main titles, but standard Title Case is acceptable if adapted for web).
  - Use `## 1.1 Specific Objectives` for secondary sections.
  - Use blockquotes (`>`) for long direct citations.
  - Figures and tables must be numbered (e.g., **Figure 1 – System Architecture**) and sourced at the bottom (e.g., *Source: The Author (2026)*).
- **Citations (ABNT NBR 10520):**
  - Indirect citation: Author (Year) states that...
  - End of sentence: (AUTHOR, Year).

## Execution
When invoked, agents must organize their output strictly following this hierarchical structure, ensuring deep technical depth in the Theoretical Foundation and Methodology sections to serve as a proper study guide.
