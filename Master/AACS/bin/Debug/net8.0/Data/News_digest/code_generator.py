def generate_python_function():
  function_name = input("Enter function name: ")
  parameters = input("Enter parameters (comma-separated): ")
  body = input("Enter function body: ")
  return f"def {function_name}({parameters}): \n  {body}"

def generate_html_element():
  element_type = input("Enter HTML element type: ")
  attributes = input("Enter attributes (key=value pairs, comma-separated): ")
  content = input("Enter element content: ")
  return f"<{element_type} {attributes}>{content}</{element_type}>"

if __name__ == "__main__":
  choice = input("Generate Python function or HTML element? (python/html): ")
  if choice.lower() == "python":
    code = generate_python_function()
    print(code)
  elif choice.lower() == "html":
    code = generate_html_element()
    print(code)
  else:
    print("Invalid choice.")