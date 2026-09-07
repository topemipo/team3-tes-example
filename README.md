# GA4GH TES Federated Microbiome Workflow Example

**Team 3: Rosetta \| HDR UK Black Internship Programme 2026**

## Portfolio summary

**GA4GH TES Federated Microbiome Workflow Validation**
Built a standards-aligned federated health-data workflow example using **JSON, Python, R, jsonschema/jsonvalidate and QIIME 2/DADA2**, defining a synthetic **3-step 16S rRNA microbiome denoising task** as a GA4GH Task Execution Service (TES) document, declaring inputs, outputs, containerised executors, compute resources, shared volumes and provenance tags, then validating it against the official `tesTask` schema and documenting reproducibility limits, interoperability risks and plain-language explanations for public and health-data audiences.

## The short version

Health research often depends on data that cannot easily move. It may be too large to transfer, governed by local data-sharing rules, held inside a secure research environment, or difficult to anonymise fully.

The safer pattern is often to move the analysis to the data instead of moving the data to the analysis. That only works if different compute systems can understand the same description of the job.

The Global Alliance for Genomics and Health (GA4GH) Task Execution Service (TES) provides a standard way to describe a computational task: what data it needs, what software should run, what resources are required, and where outputs should go.

This repository demonstrates that idea with a synthetic 16S rRNA microbiome analysis written as a TES task document and checked against the official TES schema.

## What this repository contains

| File                                         | Purpose                                                                                               |
|----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| `tes_task_16s_denoising.json`                | Example TES task document for a synthetic paired-end 16S rRNA denoising workflow                      |
| `tesTask.schema.json`                        | `tesTask` JSON schema extracted from the GA4GH TES v1.1 OpenAPI specification                         |
| `validate.py`                                | Python validator that checks the task document against the schema using `jsonschema`                  |
| `validate.R`                                 | R validator that checks the same task document using `jsonvalidate`                                   |
| `Team3_GA4GH_Report.html`                    | Full report explaining GA4GH, TES, ELIXIR Cloud and AAI, the example task, validation and limitations |
| `Team3_Slides.pdf`                           | Presentation deck for the Team 3 Rosetta interoperability project                                     |
| `Team3s_Interoperability_Poster_Rosetta.pdf` | Poster summarising the project for a wider audience                                                   |
| `LICENSE`                                    | Repository licence                                                                                    |

## What the TES task describes

The task document models a paired-end 16S rRNA amplicon pipeline:

1.  Import raw FASTQ reads into QIIME 2 format.
2.  Trim primer sequences using the QIIME 2 cutadapt plugin.
3.  Denoise reads with DADA2 through QIIME 2.

The task declares:

- one input directory for paired-end FASTQ files;
- three outputs: a feature table, representative sequences and denoising statistics;
- three sequential executors using the same QIIME 2 container image;
- compute resources: 4 CPU cores, 16 GB RAM and 20 GB disk;
- a shared work volume so the executors can pass intermediate files between steps;
- task tags for project, workflow and data-domain provenance.

## Why this matters

This is a small structural example of a larger federated-computing pattern:

- Data can remain with the organisation responsible for it.
- Analysis instructions can be described in a standard format.
- TES-compatible systems can read the same task description.
- Only the result needs to return to the requester.

The repository also makes an important distinction: schema validation proves that the document has the expected structure, but it does not prove that the scientific workflow is correct or that a live TES service will execute it successfully.

## Validation

Validate with Python:

``` bash
pip install jsonschema
python validate.py
```

Expected output:

``` text
tes_task_16s_denoising.json is VALID against tesTask.schema.json
```

Validate with R:

``` r
install.packages("jsonvalidate")
source("validate.R")
```

The R validator may emit schema-format warnings from the validation engine, but the task document validates successfully against the included schema.

## Reproducibility notes

- The task document and schema are stored in the repository.
- The validators read both files from disk, so the validation result is tied to the checked-in artefacts.
- The report includes the full task document as an appendix.
- The example uses placeholder object-store paths and synthetic scenario details.
- No patient or real sequencing data is included.

## Limitations

- The task has not been submitted to a live TES service.
- The storage paths are illustrative placeholders, not real buckets.
- The container image is referenced but not executed here.
- Schema validation checks structure and types, not scientific correctness.
- A syntactically valid TES document can still fail at runtime if paths, tools, permissions or execution environments are wrong.

## References

- GA4GH, [Task Execution Service](https://www.ga4gh.org/product/task-execution-service-tes/)
- GA4GH, [task-execution-schemas](https://github.com/ga4gh/task-execution-schemas)
- GA4GH, [About us](https://www.ga4gh.org/about-us/)
- GA4GH Driver Projects, [ELIXIR Cloud and AAI](https://www.ga4gh.org/driver_project/elixir-cloud-and-aai-for-human-data/)
- GA4GH, [Workflow Execution Service](https://www.ga4gh.org/product/workflow-execution-service-wes/)
- QIIME 2, [Documentation](https://docs.qiime2.org/)
- DADA2, [DADA2 pipeline](https://benjjneb.github.io/dada2/)

Sources were accessed for the original team report on 19 August 2026.

## Team

Temitope Adeyelu, Emmanuel Oparaku, Victor Daniel, Aisosa Elizabeth Erhunmwunsee and Aseel Fadl.
