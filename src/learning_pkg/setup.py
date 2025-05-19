from setuptools import find_packages, setup

package_name = 'learning_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='frostin006',
    maintainer_email='austinmcglashan1@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "ping_node = learning_pkg.ping_node:main",
            "pong_node = learning_pkg.pong_node:main",
            "plant_node = learning_pkg.plant_node:main",
            "controller_node = learning_pkg.controller_node:main"
        ],
    },
)
