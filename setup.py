from setuptools import setup, find_packages

setup(
    name='ScuttleSelfBalancingRobot',
    version='1.0.0',
    author='SMDHuman',
    author_email='halidyildirim64@gmail.com',
    description='Self Balancing robot based on Scuttle robot',
    url='https://github.com/SMDHuman/ScuttleBalancingRobot',
    packages=find_packages(),
    install_requires=[
        'RPi.GPIO>=0.7.1',
        'evdev>=1.6.1',
        'mpu6050-raspberrypi>=1.2'
    ],
    python_requires='>=3.11.1',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Rasbian OS',
        'Programming Language :: Python>=3.11.1',
    ],
)