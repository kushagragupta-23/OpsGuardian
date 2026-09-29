import shutil, subprocess, sys
print('Python:',sys.version.split()[0])
print('Ollama executable:', shutil.which('ollama') or 'NOT FOUND')
if shutil.which('ollama'):
    try: print(subprocess.check_output(['ollama','list'], text=True, timeout=10))
    except Exception as e: print('Could not query Ollama:',e)
