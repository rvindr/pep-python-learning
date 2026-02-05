from pathlib import Path

dir = Path.cwd()
print(dir)

p = 'fullstack/java'
obj = Path(p)
print(obj.exists())

print(obj.is_dir())
print(obj.is_file())