from transformers import CodeGenerationPipeline

model_name = "facebook/bart-large-cnn"
pipe = CodeGenerationPipeline.from_pretrained(model_name)

def refactor_code(code):
  inputs = {"code": code}
  output = pipe(inputs, max_length=200, num_return_sequences=3)[0]
  return output["generated_text"]