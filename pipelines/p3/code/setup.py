from setuptools import setup, find_packages
setup(
    name = 'p3',
    version = '1.0',
    packages = find_packages(include = ('p3*', )) + ['prophecy_config_instances.p3'],
    package_dir = {'prophecy_config_instances.p3' : 'configs/resources/p3'},
    package_data = {'prophecy_config_instances.p3' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-libs==2.1.16'],
    entry_points = {
'console_scripts' : [
'main = p3.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html', 'pytest-cov'], }
)
