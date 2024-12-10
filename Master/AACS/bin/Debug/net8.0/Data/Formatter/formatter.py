
def format_python(code):
  code = re.sub(r'(\s+)\n', r'\1', code)
  code = re.sub(r'\s+', ' ', code)
  code = re.sub(r'(\w+)\s*=\s*(.*?)\s*;', r'\1 = \2', code)
  return code

def format_javascript(code):
  code = re.sub(r'(\s+)\n', r'\1', code)
  code = re.sub(r'\s+', ' ', code)
  code = re.sub(r'(\w+)\s*=\s*(.*?)\s*,\s*', r'\1 = \2,', code)
  return code

def format_code(code, language):
  if language == 'python':
    return format_python(code)
  elif language == 'javascript':
    return format_javascript(code)
  else:
    return code

# Example usage
code = """
def my_function(x):
  y = x * 2
  return y

console.log('Hello world!');
"""

formatted_code = format_code(code, 'python')
print(formatted_code)