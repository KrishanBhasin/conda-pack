import os

test_dir = os.path.dirname(os.path.abspath(__file__))
croot = os.environ.get('CONDA_ROOT')
if croot is None:
    croot = os.path.join(test_dir, '..', '..', 'testing', 'conda')
env_dir = os.path.join(os.path.abspath(croot), 'envs')

py38_path = os.path.join(env_dir, 'py38')
py38_editable_path = os.path.join(env_dir, 'py38_editable')
py38_broken_path = os.path.join(env_dir, 'py38_broken')
py38_missing_files_path = os.path.join(env_dir, 'py38_missing_files')
py310_path = os.path.join(env_dir, 'py310')
nopython_path = os.path.join(env_dir, 'nopython')
has_conda_path = os.path.join(env_dir, 'has_conda')
activate_scripts_path = os.path.join(env_dir, 'activate_scripts')
