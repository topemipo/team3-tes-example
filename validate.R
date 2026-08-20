# Validate the example TES task document against the official tesTask schema.
# install.packages(c("jsonlite", "jsonvalidate"))

library(jsonvalidate)

task   <- paste(readLines("tes_task_16s_denoising.json", warn = FALSE), collapse = "\n")
schema <- paste(readLines("tesTask.schema.json",         warn = FALSE), collapse = "\n")

validator <- json_validator(schema, engine = "ajv")
result    <- validator(task, verbose = TRUE, greedy = TRUE)

if (isTRUE(result)) {
  message("tes_task_16s_denoising.json is VALID against tesTask.schema.json")
} else {
  message("tes_task_16s_denoising.json is INVALID against tesTask.schema.json")
  print(attr(result, "errors"))
}
