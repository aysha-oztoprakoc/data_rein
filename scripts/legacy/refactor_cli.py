import os
import shutil
from pathlib import Path

def refactor():
    base = Path('/home/amdy/data_rein')
    scripts_dir = base / 'scripts'
    tools_dir = base / 'tools'
    cli_file = base / 'src' / 'data_harness' / 'cli.py'
    
    # Create CLI entrypoint
    cli_code = """import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Sovereign AI Data Harness CLI')
    subparsers = parser.add_subparsers(dest='command')
    
    migrate_parser = subparsers.add_parser('migrate', help='Run database migration')
    build_wiki_parser = subparsers.add_parser('build_wiki', help='Build the wiki')
    ingest_parser = subparsers.add_parser('ingest', help='Ingest training data')
    
    args = parser.parse_args()
    
    if args.command == 'migrate':
        print('Running migration...')
        # import migration logic here
    elif args.command == 'build_wiki':
        print('Building wiki...')
    elif args.command == 'ingest':
        print('Ingesting data...')
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
"""
    cli_file.write_text(cli_code)
    
    # Move shell scripts to tools
    if scripts_dir.exists():
        for item in scripts_dir.iterdir():
            if item.suffix == '.sh':
                shutil.move(str(item), str(tools_dir / item.name))
                
    # Update pyproject.toml
    pyproject_file = base / 'pyproject.toml'
    if pyproject_file.exists():
        content = pyproject_file.read_text()
        if '[project.scripts]' not in content:
            content += "\n[project.scripts]\nharness = \"data_harness.cli:main\"\n"
            pyproject_file.write_text(content)
            
    print("CLI refactor complete.")

if __name__ == '__main__':
    refactor()
