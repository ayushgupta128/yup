from setuptools import setup, find_packages
setup(
    name = 'HashiCorpVault',
    version = '1.0',
    packages = (
      find_packages(include = ('hashicorpvault*', ))
      + ['prophecy_config_instances', 'prophecy_config_instances.hashicorpvault']
    ),
    package_dir = {'prophecy_config_instances' : 'configs/resources'},
    package_data = {'prophecy_config_instances.hashicorpvault' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.17'],
    entry_points = {
'console_scripts' : [
'main = hashicorpvault.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
