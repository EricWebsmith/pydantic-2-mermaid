from setuptools import setup  # type: ignore

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='pydantic-2-mermaid',
    version='0.3.0',
    description='Convert pydantic 2 classes to markdown mermaid class charts',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Eric Websmith',
    author_email='eric.websmith@gmail.com',
    url='https://github.com/EricWebsmith/pydantic_2_mermaid',
    packages=['pydantic_2_mermaid'],
    package_data={'pydantic_2_mermaid': ['py.typed']},
    install_requires=[
        'pydantic>=2.0.0'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
    entry_points={
        'console_scripts': [
            'pydantic-2-mermaid = pydantic_2_mermaid.__main__:main'
        ]
    }
)
