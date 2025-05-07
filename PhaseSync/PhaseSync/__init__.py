import os
import click
from typing import Dict, List, Tuple
import logging
from .symbol_compressor import (
    analyze_file_complexity, 
    compress, 
    compress_word,
    extract_phase_tags
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def analyze_project_structure(project_path: str) -> Dict[str, List[str]]:
    """Analyze the project structure and categorize files."""
    structure = {
        'core': [],
        'utils': [],
        'tests': [],
        'other': []
    }
    
    for root, dirs, files in os.walk(project_path):
        for file in files:
            if file.endswith('.py'):
                rel_path = os.path.relpath(os.path.join(root, file), project_path)
                full_path = os.path.join(project_path, rel_path)
                
                # Read file content to check for phase tags
                try:
                    with open(full_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        tags = extract_phase_tags(content)
                        
                        if 'phase' in tags:
                            phase = tags['phase'].lower()
                            if phase in structure:
                                structure[phase].append(rel_path)
                            else:
                                structure['other'].append(rel_path)
                        else:
                            # Fallback to directory-based categorization
                            if 'core' in rel_path:
                                structure['core'].append(rel_path)
                            elif 'utils' in rel_path:
                                structure['utils'].append(rel_path)
                            elif 'tests' in rel_path:
                                structure['tests'].append(rel_path)
                            else:
                                structure['other'].append(rel_path)
                except Exception as e:
                    logger.error(f"Error reading file {rel_path}: {e}")
                    structure['other'].append(rel_path)
    
    return structure

def calculate_phase_weights(structure: Dict[str, List[str]], project_path: str) -> Dict[str, Tuple[int, int, Dict[str, str]]]:
    """Calculate weights for each phase using Symbolic Weight Protocol."""
    weights = {
        'core': (0, 0, {}),
        'utils': (0, 0, {}),
        'tests': (0, 0, {}),
        'other': (0, 0, {})
    }
    
    for phase, files in structure.items():
        phase_mass = 0
        phase_tags = {}
        
        for file in files:
            full_path = os.path.join(project_path, file)
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    mass, _ = compress(content)
                    phase_mass += mass
                    
                    # Extract tags
                    tags = extract_phase_tags(content)
                    if tags:
                        phase_tags[file] = tags
            except Exception as e:
                logger.error(f"Error processing file {file}: {e}")
        
        # Calculate reduced digit for the phase
        reduced = sum(int(digit) for digit in str(phase_mass))
        while reduced >= 10:
            reduced = sum(int(digit) for digit in str(reduced))
        
        weights[phase] = (phase_mass, reduced, phase_tags)
    
    return weights

@click.command()
@click.argument('project_path', type=click.Path(exists=True))
@click.option('--scan-tags', is_flag=True, help='Scan and validate phase tags')
@click.option('--generate-prompt', is_flag=True, help='Generate phase prompt context')
def main(project_path: str, scan_tags: bool, generate_prompt: bool):
    """Analyze a project's structure and calculate phase weights using SWP."""
    logger.info(f"Analyzing project at: {project_path}")
    
    # Analyze project structure
    structure = analyze_project_structure(project_path)
    
    # Calculate weights using SWP
    weights = calculate_phase_weights(structure, project_path)
    
    # Display results
    click.echo("\nProject Analysis Results (Using Symbolic Weight Protocol):")
    click.echo("=" * 70)
    
    for phase, files in structure.items():
        mass, reduced, tags = weights[phase]
        click.echo(f"\n{phase.upper()} Phase:")
        click.echo("-" * 30)
        click.echo(f"Symbolic Mass: {mass}")
        click.echo(f"Reduced Digit: {reduced}")
        
        if scan_tags and tags:
            click.echo("\nPhase Tags:")
            for file, file_tags in tags.items():
                click.echo(f"  {file}:")
                for tag_name, tag_value in file_tags.items():
                    click.echo(f"    @{tag_name}: {tag_value}")
        
        click.echo("\nFiles:")
        for file in files:
            full_path = os.path.join(project_path, file)
            file_mass, file_reduced = analyze_file_complexity(full_path)
            click.echo(f"  - {file} (Mass: {file_mass}, Reduced: {file_reduced})")
    
    click.echo("\nPhase Weights Summary:")
    click.echo("-" * 30)
    for phase, (mass, reduced, _) in weights.items():
        click.echo(f"{phase}: Mass={mass}, Reduced={reduced}")
    
    if generate_prompt:
        click.echo("\nPhase Prompt Context:")
        click.echo("-" * 30)
        for phase, (_, reduced, tags) in weights.items():
            if tags:
                click.echo(f"\n{phase.upper()} Phase (Reduced: {reduced}):")
                for file, file_tags in tags.items():
                    if 'task' in file_tags:
                        click.echo(f"  - {file_tags['task']}")

if __name__ == '__main__':
    main() 