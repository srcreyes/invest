"""setup.py module for natcap.invest

InVEST - Integrated Valuation of Ecosystem Services and Tradeoffs

Common functionality provided by setup.py:
    build_sphinx

For other commands, try `python setup.py --help-commands`
"""
from setuptools.extension import Extension
from setuptools import setup
import Cython.Build
import numpy


# Read in requirements.txt and populate the python readme with the
# non-comment, non-environment-specifier contents.
_REQUIREMENTS = [req.split(';')[0].split('#')[0].strip() for req in
                 open('requirements.txt').readlines()
                 if not req.startswith(('#', 'hg+', 'git+')) and len(req.strip()) > 0]
_GUI_REQUIREMENTS = [req.split(';')[0].split('#')[0].strip() for req in
                     open('requirements-gui.txt').readlines()
                     if not req.startswith(('#', 'hg+')) and len(req.strip()) > 0]
README = open('README_PYTHON.rst').read().format(
    requirements='\n'.join(['    ' + r for r in _REQUIREMENTS]))


setup(
    name='natcap.invest',
    description="InVEST Ecosystem Service models",
    long_description=README,
    maintainer='James Douglass',
    maintainer_email='jdouglass@stanford.edu',
    url='http://bitbucket.org/natcap/invest',
    namespace_packages=['natcap'],
    packages=[
        'natcap',
        'natcap.invest',
        'natcap.invest.coastal_blue_carbon',
        'natcap.invest.finfish_aquaculture',
        'natcap.invest.fisheries',
        'natcap.invest.hydropower',
        'natcap.invest.ui',
        'natcap.invest.ndr',
        'natcap.invest.sdr',
        'natcap.invest.recreation',
        'natcap.invest.reporting',
        'natcap.invest.scenic_quality',
        'natcap.invest.seasonal_water_yield',
    ],
    package_dir={
        'natcap': 'src/natcap'
    },
    use_scm_version={'version_scheme': 'post-release',
                     'local_scheme': 'node-and-date'},
    include_package_data=True,
    install_requires=_REQUIREMENTS,
    setup_requires=['setuptools_scm', 'numpy', 'cython'],
    license='BSD',
    zip_safe=False,
    keywords='gis invest',
    classifiers=[
        'Intended Audience :: Developers',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Cython',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: GIS'
    ],
    ext_modules=[
        Extension(
            name="natcap.invest.recreation.out_of_core_quadtree",
            sources=[
                'src/natcap/invest/recreation/out_of_core_quadtree.pyx'],
            include_dirs=[numpy.get_include()],
            language="c++"),
        Extension(
            name="natcap.invest.scenic_quality.viewshed",
            sources=[
                'src/natcap/invest/scenic_quality/viewshed.pyx'],
            include_dirs=[numpy.get_include(),
                          'src/natcap/invest/scenic_quality'],
            language="c++"),
        Extension(
            name="natcap.invest.ndr.ndr_core",
            sources=['src/natcap/invest/ndr/ndr_core.pyx'],
            include_dirs=[numpy.get_include()],
            language="c++"),
        Extension(
            name="natcap.invest.sdr.sdr_core",
            sources=['src/natcap/invest/sdr/sdr_core.pyx'],
            include_dirs=[numpy.get_include()],
            language="c++"),
        Extension(
            name="natcap.invest.seasonal_water_yield.seasonal_water_yield_core",
            sources=['src/natcap/invest/seasonal_water_yield/seasonal_water_yield_core.pyx'],
            include_dirs=[numpy.get_include()],
            language="c++"),
    ],
    cmdclass={'build_ext': Cython.Build.build_ext},
    entry_points={
        'console_scripts': [
            'invest = natcap.invest.cli:main'
        ],
    },
    extras_require={
        'ui': _GUI_REQUIREMENTS,
    },
    package_data={
        'natcap.invest.reporting': [
            'reporting_data/*.js',
            'reporting_data/*.css',
        ],
    }
)
