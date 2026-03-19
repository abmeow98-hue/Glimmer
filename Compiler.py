import sys

def compile_glimmer(source_code):
    lines = source_code.split('\n')
    python_output = []
    
    for line in lines:
        line = line.strip()
        if not line: continue
        
        # Simple translation rules
        if line.startswith('let '):
            python_output.append(line.replace('let ', ''))
        elif line.startswith('print '):
            python_output.append(line.replace('print ', 'print(') + ')')
            
    return "\n".join(python_output)

# Simulate reading a .glm file
source = """
let x = 10
let y = 20
print x + y
"""

compiled_code = compile_glimmer(source)
exec(compiled_code) # Runs the translated code
