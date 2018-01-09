from setuptools import setup

setup(name='gopher_version',
      version='0.12',
      description='Create a file containing the name and version of various ROS and system packages',
      author='Thomas Kostas',
      url='https://github.com/yotabits/gopher_version',
      author_email='tkostas75@gmail.com',
      license='MIT',
      packages=['gopher_version'],
      scripts=['bin/gopher_version'],
      install_requires=[],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        ],
      zip_safe=False)
