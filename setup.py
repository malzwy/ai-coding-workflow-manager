"""
AI Coding Workflow Manager - Setup Configuration
"""

from setuptools import setup, find_packages
from pathlib import Path

# 读取README文件
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

# 读取requirements.txt
requirements = []
with open('requirements.txt') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name="ai-coding-workflow-manager",
    version="1.0.0",
    author="AI Coding Workflow Manager Contributors",
    author_email="openclaw@localhost",
    description="A powerful AI coding assistant workflow manager supporting multi-AI model collaboration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/malzwy/ai-coding-workflow-manager",
    project_urls={
        "Bug Tracker": "https://github.com/malzwy/ai-coding-workflow-manager/issues",
        "Source Code": "https://github.com/malzwy/ai-coding-workflow-manager",
        "Documentation": "https://github.com/malzwy/ai-coding-workflow-manager/blob/main/docs/README.md",
    },
    packages=find_packages(exclude=["tests", "tests.*", "examples", "examples.*", "docs", "docs.*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Code Generators",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Environment :: Console",
        "Framework :: AsyncIO",
    ],
    python_requires=">=3.10",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "pytest-asyncio>=0.21.0",
            "black>=23.0.0",
            "isort>=5.12.0",
            "flake8>=6.0.0",
            "pylint>=2.17.0",
            "mypy>=1.0.0",
            "bandit>=1.7.0",
        ],
        "docs": [
            "sphinx>=6.0.0",
            "sphinx-rtd-theme>=1.2.0",
            "myst-parser>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "ai-workflow=ai_coding_workflow.cli:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    keywords="ai coding workflow automation claude openai code-review refactoring test-generation",
)
