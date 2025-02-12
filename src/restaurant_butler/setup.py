from setuptools import setup

package_name = 'restaurant_butler'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='your_name',
    maintainer_email='your_email@example.com',
    description='Restaurant Butler Robot in ROS 2 Humble',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
           'butler_node = restaurant_butler.butler_node:main',
        'order_manager = restaurant_butler.order_manager:main',
        ],
    },
)
