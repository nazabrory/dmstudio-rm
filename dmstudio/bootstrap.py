'''
dmstudio.bootstrap
------------------

Bootstrapping utility to download tutorials and sample datasets.
'''
import os
import shutil
import tempfile
import urllib.request
import zipfile


def download_tutorials(target_dir):
    '''
    download_tutorials
    ------------------

    Download the latest tutorials and sample datasets from the GitHub repository
    and extract them into the specified target directory.

    Parameters:
    -----------
    target_dir: str
        Absolute or relative path to the folder where the "tutorials" directory
        should be created.
    '''
    # 1. Validate target directory
    target_dir = os.path.abspath(target_dir)
    os.makedirs(target_dir, exist_ok=True)
    
    url = 'https://github.com/nazabrory/dmstudio-rm/archive/refs/heads/master.zip'
    fallback_url = 'https://github.com/nazabrory/dmstudio-rm/archive/refs/heads/main.zip'
    
    # 2. Create temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix='.zip') as tmp_file:
        tmp_path = tmp_file.name
        
    try:
        # Download the zip
        try:
            print('Downloading tutorials from {}...'.format(url))
            urllib.request.urlretrieve(url, tmp_path)
        except Exception:
            print('Failed to download from default branch. Trying fallback: {}...'.format(fallback_url))
            urllib.request.urlretrieve(fallback_url, tmp_path)
        
        # 3. Extract the tutorials folder
        print('Extracting tutorials...')
        with zipfile.ZipFile(tmp_path, 'r') as zip_ref:
            # Find the top level directory name inside the zip (typically 'dmstudio-main')
            top_dir = None
            for name in zip_ref.namelist():
                if name.endswith('/tutorials/'):
                    top_dir = name.split('/')[0]
                    break
            
            if not top_dir:
                # Try fallback: look for any 'tutorials/' entry
                for name in zip_ref.namelist():
                    if 'tutorials/' in name:
                        top_dir = name.split('/')[0]
                        break
            
            if not top_dir:
                raise RuntimeError('Could not find \'tutorials\' folder in the downloaded zip archive.')
            
            # Extract only files in the tutorials folder
            tutorials_prefix = '{}/tutorials/'.format(top_dir)
            extracted_count = 0
            for member in zip_ref.infolist():
                if member.filename.startswith(tutorials_prefix) and not member.is_dir():
                    # Compute relative path under 'tutorials/'
                    rel_path = member.filename[len(tutorials_prefix):]
                    out_path = os.path.join(target_dir, 'tutorials', rel_path)
                    
                    # Ensure parent dir exists
                    os.makedirs(os.path.dirname(out_path), exist_ok=True)
                    
                    # Write file
                    with zip_ref.open(member) as source, open(out_path, 'wb') as target:
                        shutil.copyfileobj(source, target)
                    extracted_count += 1
                    
        print('Successfully extracted {} tutorial files to: {}'.format(
            extracted_count, os.path.join(target_dir, 'tutorials')
        ))
        
    finally:
        # Clean up temporary file
        if os.path.exists(tmp_path):
            os.remove(tmp_path)


def install_agent_skills(target_dir=None):
    '''
    install_agent_skills
    --------------------

    Install the AI agent skills and guidelines into the specified project
    directory (specifically under `.agents/skills/dmstudio-rules/SKILL.md`).
    This allows local agent harnesses (like Antigravity) to automatically
    discover and adhere to Datamine Studio RM rules.

    Parameters:
    -----------
    target_dir: str, optional
        Absolute or relative path to the project directory. If omitted,
        the current working directory is used.
    '''
    if target_dir is None:
        target_dir = os.getcwd()
    
    target_dir = os.path.abspath(target_dir)
    
    # 1. Locate source rules file
    package_dir = os.path.dirname(os.path.abspath(__file__))
    rules_src = os.path.join(package_dir, 'agent_rules.md')
    
    if not os.path.exists(rules_src):
        # Try fallback if not packaged properly
        raise FileNotFoundError(
            'Agent rules source file not found at: {}. Please make sure the package was installed correctly.'.format(rules_src)
        )
        
    # 2. Determine target path
    # Target directory structure: .agents/skills/dmstudio-rules/SKILL.md
    skills_dir = os.path.join(target_dir, '.agents', 'skills', 'dmstudio-rules')
    target_path = os.path.join(skills_dir, 'SKILL.md')
    
    # 3. Create target directory and copy
    os.makedirs(skills_dir, exist_ok=True)
    
    try:
        shutil.copy2(rules_src, target_path)
        print('Successfully installed AI agent skill to: {}'.format(target_path))
        return target_path
    except Exception as e:
        raise RuntimeError('Failed to install AI agent skill: {}'.format(e))

