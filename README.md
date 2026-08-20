# A GA4GH TES task document, built and validated

**Team 3: Rosetta · HDR UK Black Internship Programme 2026**

This repository holds one example **task document** written to the
[GA4GH Task Execution Service (TES)](https://www.ga4gh.org/product/task-execution-service-tes/)
specification, together with the schema it was checked against and the code that
checked it.

## The short version

Health research often needs to analyse data that cannot move. It may be too large to
transfer, governed by different data-sharing laws in the country where it sits, or
stored in a format the other institution does not use.

The way round this is to move the analysis instead of the data. But that only works if
every compute system can read the same description of the job. TES is the international
standard that provides that shared description.

This repository is one such description: a synthetic 16S rRNA microbiome analysis,
written so that any TES-compatible system could read it.

## Files

| File | What it is |
|---|---|
| `tes_task_16s_denoising.json` | The task document. Three sequential steps: import reads, trim primers, denoise with DADA2 via QIIME2 |
| `tesTask.schema.json` | The `tesTask` schema, extracted from the official GA4GH TES v1.1 OpenAPI specification |
| `validate.py` | Checks the task document against the schema |
| `validate.R` | The same check in R |

## What the task document does

It describes a paired-end 16S rRNA amplicon pipeline:

1. **Import** the raw sequencing files into QIIME2's internal format
2. **Trim** the primer sequences off every read
3. **Denoise** with DADA2, separating real biological signal from sequencing error and
   removing chimeras

It produces a feature table, the representative sequence for each amplicon sequence
variant, and per-sample denoising statistics.

## How it was validated

```bash
pip install jsonschema
python validate.py
```

```
tes_task_16s_denoising.json is VALID against tesTask.schema.json
```

The schema was taken from the `main` branch of
[ga4gh/task-execution-schemas](https://github.com/ga4gh/task-execution-schemas),
`openapi/task_execution_service.openapi.yaml` (OpenAPI v3.0.1).

## Important limits

Please read these before drawing conclusions from this repository.

- **This is a structural example.** It has not been submitted to a live TES service.
- **No real data.** The scenario is synthetic and the storage locations are placeholders,
  not real buckets.
- **Validation checks shape, not science.** The schema confirms that the required fields
  are present and of the right type. It cannot tell whether the commands are
  scientifically appropriate, whether the file paths line up between steps, or whether
  the container image is available. A typo in a filename would pass every check here and
  fail only when the task actually ran.
- **A standard does not guarantee interoperability.** Adopting one removes avoidable
  differences. Implementation quality, version compatibility and testing still decide
  whether two systems really work together.

## Sources

- GA4GH, [About us](https://www.ga4gh.org/about-us/)
- GA4GH, [Task Execution Service](https://www.ga4gh.org/product/task-execution-service-tes/)
- GA4GH, [task-execution-schemas](https://github.com/ga4gh/task-execution-schemas)
- GA4GH Driver Projects, [ELIXIR Cloud and AAI](https://www.ga4gh.org/driver_project/elixir-cloud-and-aai-for-human-data/)
- GA4GH, [ELIXIR and GA4GH expand collaboration](https://www.ga4gh.org/news/elixir-and-ga4gh-expand-collaboration/), 2 May 2019

All accessed 19 August 2026.

## Team

Temitope Adeyelu (Lead), Victor Daniel, Aisosa Elizabeth Erhunmwunsee, Aseel Fadl,
Charles Bruce, Emmanuel Oparaku, Kayode Olaseni.
