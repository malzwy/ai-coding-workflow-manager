"""
CI/CD集成案例 - CI/CD Integration Examples

本文件展示了如何将AI编码工作流管理器集成到CI/CD管道中。
"""

import os
import json
import subprocess
from typing import Dict, List, Any
from pathlib import Path


# ============================================================================
# GitHub Actions 集成
# ============================================================================

def github_actions_integration() -> Dict[str, Any]:
    """GitHub Actions CI/CD 集成配置"""
    
    github_workflow_config = {
        "name": "AI Coding Workflow Manager CI/CD",
        "description": "Continuous Integration and Deployment with AI-powered workflows",
        "workflows": {
            "test_and_lint": {
                "name": "Test and Lint",
                "trigger": ["push", "pull_request"],
                "jobs": {
                    "test": {
                        "runs-on": "ubuntu-latest",
                        "python-versions": ["3.10", "3.11", "3.12"],
                        "steps": [
                            {"name": "Checkout", "uses": "actions/checkout@v4"},
                            {"name": "Setup Python", "uses": "actions/setup-python@v5"},
                            {"name": "Install Dependencies", "run": "pip install -r requirements.txt"},
                            {"name": "Run Tests", "run": "pytest tests/ -v"},
                            {"name": "Run Code Review Workflow", "run": "python scripts/run_workflow.py --template code_review --file ."},
                            {"name": "Run Test Generation Workflow", "run": "python scripts/run_workflow.py --template test_generation --file src/"},
                        ]
                    },
                    "lint": {
                        "runs-on": "ubuntu-latest",
                        "steps": [
                            {"name": "Checkout", "uses": "actions/checkout@v4"},
                            {"name": "Setup Python", "uses": "actions/setup-python@v5"},
                            {"name": "Install Linting Tools", "run": "pip install flake8 black isort pylint mypy"},
                            {"name": "Run flake8", "run": "flake8 ai_coding_workflow/"},
                            {"name": "Run black", "run": "black --check ai_coding_workflow/"},
                            {"name": "Run isort", "run": "isort --check-only ai_coding_workflow/"},
                            {"name": "Run pylint", "run": "pylint ai_coding_workflow/ --exit-zero"},
                            {"name": "Run mypy", "run": "mypy ai_coding_workflow/ --ignore-missing-imports"},
                        ]
                    },
                    "build": {
                        "runs-on": "ubuntu-latest",
                        "needs": ["test", "lint"],
                        "steps": [
                            {"name": "Checkout", "uses": "actions/checkout@v4"},
                            {"name": "Setup Python", "uses": "actions/setup-python@v5"},
                            {"name": "Install Build Tools", "run": "pip install build twine"},
                            {"name": "Build Package", "run": "python -m build"},
                            {"name": "Check Package", "run": "twine check dist/*"},
                            {"name": "Upload Artifacts", "uses": "actions/upload-artifact@v4"},
                        ]
                    }
                }
            },
            "ai_code_review": {
                "name": "AI Code Review",
                "trigger": ["pull_request"],
                "jobs": {
                    "review": {
                        "runs-on": "ubuntu-latest",
                        "env": {
                            "CLAUDE_API_KEY": "${{ secrets.CLAUDE_API_KEY }}",
                            "OPENAI_API_KEY": "${{ secrets.OPENAI_API_KEY }}"
                        },
                        "steps": [
                            {"name": "Checkout", "uses": "actions/checkout@v4"},
                            {"name": "Setup Python", "uses": "actions/setup-python@v5"},
                            {"name": "Install Dependencies", "run": "pip install -r requirements.txt"},
                            {"name": "Run AI Code Review", "run": "python scripts/run_workflow.py --template code_review --file . --output review-report.json"},
                            {"name": "Upload Review Report", "uses": "actions/upload-artifact@v4", "with": {"name": "ai-code-review-report", "path": "review-report.json"}},
                        ]
                    }
                }
            }
        }
    }
    
    return github_workflow_config


# ============================================================================
# Jenkins Pipeline 集成
# ============================================================================

def jenkins_pipeline_integration() -> Dict[str, Any]:
    """Jenkins Pipeline 集成配置"""
    
    jenkins_pipeline_config = {
        "pipeline": {
            "agent": {
                "docker": {
                    "image": "python:3.11-slim",
                    "args": "-u root"
                }
            },
            "stages": [
                {
                    "stage": "Checkout",
                    "steps": [
                        {"sh": "git checkout ${GIT_BRANCH}"},
                        {"sh": "git config --global user.name 'Jenkins'"},
                        {"sh": "git config --global user.email 'jenkins@localhost'"}
                    ]
                },
                {
                    "stage": "Setup",
                    "steps": [
                        {"sh": "pip install --upgrade pip"},
                        {"sh": "pip install -r requirements.txt"},
                        {"sh": "pip install pytest pytest-cov flake8 black isort pylint mypy"}
                    ]
                },
                {
                    "stage": "Code Review",
                    "steps": [
                        {"sh": "python scripts/run_workflow.py --template code_review --file . --output jenkins-review-report.json"},
                        {"archiveArtifacts": "jenkins-review-report.json"}
                    ]
                },
                {
                    "stage": "Testing",
                    "steps": [
                        {"sh": "pytest tests/ -v --junitxml=test-results.xml --cov=ai_coding_workflow --cov-report=xml"},
                        {"junit": "test-results.xml"},
                        {"cobertura": "coverage.xml"}
                    ]
                },
                {
                    "stage": "Linting",
                    "steps": [
                        {"sh": "flake8 ai_coding_workflow/ --count --exit-zero"},
                        {"sh": "black --check ai_coding_workflow/"},
                        {"sh": "isort --check-only ai_coding_workflow/"},
                        {"sh": "pylint ai_coding_workflow/ --exit-zero"},
                        {"sh": "mypy ai_coding_workflow/ --ignore-missing-imports"}
                    ]
                },
                {
                    "stage": "Build",
                    "steps": [
                        {"sh": "pip install build twine"},
                        {"sh": "python -m build"},
                        {"sh": "twine check dist/*"},
                        {"archiveArtifacts": "dist/*"}
                    ]
                }
            ],
            "post": {
                "always": {
                    "steps": [
                        {"sh": "echo 'Pipeline completed'"}
                    ]
                },
                "success": {
                    "steps": [
                        {"sh": "echo 'Pipeline succeeded!'"}
                    ]
                },
                "failure": {
                    "steps": [
                        {"sh": "echo 'Pipeline failed!'"}
                    ]
                }
            }
        }
    }
    
    return jenkins_pipeline_config


# ============================================================================
# GitLab CI/CD 集成
# ============================================================================

def gitlab_ci_integration() -> Dict[str, Any]:
    """GitLab CI/CD 集成配置"""
    
    gitlab_ci_config = {
        "image": "python:3.11-slim",
        "variables": {
            "PIP_CACHE_DIR": "$CI_PROJECT_DIR/.cache/pip",
            "PYTHON_VERSION": "3.11"
        },
        "cache": {
            "paths": [
                ".cache/pip",
                "venv/"
            ]
        },
        "stages": ["test", "review", "build", "deploy"],
        "before_script": [
            "python --version",
            "pip install --upgrade pip",
            "pip install virtualenv",
            "virtualenv venv",
            "source venv/bin/activate"
        ],
        "test": {
            "stage": "test",
            "script": [
                "pip install -r requirements.txt",
                "pytest tests/ -v --cov=ai_coding_workflow --cov-report=xml --cov-report=html",
                "coverage report"
            ],
            "artifacts": {
                "paths": ["coverage.xml", "htmlcov/"],
                "reports": {"cobertura": "coverage.xml"}
            }
        },
        "ai_review": {
            "stage": "review",
            "script": [
                "pip install -r requirements.txt",
                "python scripts/run_workflow.py --template code_review --file . --output gitlab-review-report.json"
            ],
            "artifacts": {
                "paths": ["gitlab-review-report.json"],
                "when": "always"
            },
            "only": ["merge_requests"]
        },
        "lint": {
            "stage": "test",
            "script": [
                "pip install flake8 black isort pylint mypy",
                "flake8 ai_coding_workflow/",
                "black --check ai_coding_workflow/",
                "isort --check-only ai_coding_workflow/",
                "pylint ai_coding_workflow/ --exit-zero",
                "mypy ai_coding_workflow/ --ignore-missing-imports"
            ]
        },
        "build": {
            "stage": "build",
            "script": [
                "pip install build twine",
                "python -m build",
                "twine check dist/*"
            ],
            "artifacts": {
                "paths": ["dist/*"]
            }
        },
        "pages": {
            "stage": "deploy",
            "script": [
                "mv htmlcov/ public/",
                "echo 'Deploying to GitLab Pages...'"
            ],
            "artifacts": {
                "paths": ["public"]
            },
            "only": ["main"]
        }
    }
    
    return gitlab_ci_config


# ============================================================================
# 本地 CI/CD 脚本
# ============================================================================

def local_cicd_script() -> str:
    """本地 CI/CD 脚本（不依赖云平台）"""
    
    script = """#!/bin/bash
# 本地 CI/CD 脚本 - 适用于任何环境

set -e  # 出现错误时立即退出

echo "🚀 开始本地 CI/CD 流程"
echo "="*50

# 检查 Python 环境
echo "🔍 检查 Python 环境..."
python --version

# 安装依赖
echo "📦 安装依赖..."
pip install --upgrade pip
pip install -r requirements.txt
pip install pytest pytest-cov flake8 black isort pylint mypy

# 运行代码审查工作流
echo "🔍 运行 AI 代码审查..."
python scripts/run_workflow.py --template code_review --file . --output local-review-report.json

# 运行测试生成工作流
echo "🧪 运行测试生成..."
python scripts/run_workflow.py --template test_generation --file src/ --output local-tests-generated.json

# 运行测试
echo "🧪 运行测试..."
pytest tests/ -v --junitxml=test-results.xml --cov=ai_coding_workflow --cov-report=xml --cov-report=html

# 代码检查
echo "🔍 运行代码检查..."
flake8 ai_coding_workflow/ --count --exit-zero || true
black --check ai_coding_workflow/ || true
isort --check-only ai_coding_workflow/ || true
pylint ai_coding_workflow/ --exit-zero || true
mypy ai_coding_workflow/ --ignore-missing-imports || true

# 构建包
echo "📦 构建包..."
pip install build twine
python -m build
twine check dist/*

echo ""
echo "✅ 本地 CI/CD 流程完成！"
echo ""
echo "📊 生成的文件:"
echo "  - 代码审查报告: local-review-report.json"
echo "  - 测试生成结果: local-tests-generated.json"
echo "  - 测试结果: test-results.xml"
echo "  - 覆盖率报告: coverage.xml, htmlcov/"
echo "  - 构建包: dist/*"
echo ""
echo "🎉 所有检查通过！"
"""
    
    return script


# ============================================================================
# 实用函数
# ============================================================================

def save_ci_config(config_type: str, config: Dict[str, Any]) -> str:
    """保存 CI/CD 配置文件"""
    
    config_files = {
        "github": ".github/workflows/ci-cd.yml",
        "jenkins": "Jenkinsfile",
        "gitlab": ".gitlab-ci.yml",
        "local": "local-cicd.sh"
    }
    
    if config_type not in config_files:
        raise ValueError(f"Unsupported config type: {config_type}")
    
    file_path = config_files[config_type]
    
    if config_type == "github":
        content = yaml_dump(config)
    elif config_type == "jenkins":
        content = groovy_dump(config)
    elif config_type == "gitlab":
        content = yaml_dump(config)
    else:  # local
        content = config  # 字符串
    
    try:
        Path(file_path).parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, 'w') as f:
            if isinstance(content, str):
                f.write(content)
            else:
                json.dump(content, f, indent=2, ensure_ascii=False)
        return f"✅ 保存配置文件: {file_path}"
    except Exception as e:
        return f"❌ 保存失败: {str(e)}"


def yaml_dump(data: Dict[str, Any]) -> str:
    """简单 YAML 转换（实际使用中应该用 pyyaml）"""
    
    # 这是一个简化的 YAML 生成函数
    # 实际使用中应该安装 pyyaml
    
    def _to_yaml(obj, indent=0):
        lines = []
        if isinstance(obj, dict):
            for key, value in obj.items():
                if isinstance(value, (dict, list)):
                    lines.append(f"{' ' * indent}{key}:")
                    lines.append(_to_yaml(value, indent + 2))
                else:
                    if isinstance(value, str):
                        lines.append(f"{' ' * indent}{key}: '{value}'")
                    else:
                        lines.append(f"{' ' * indent}{key}: {value}")
        elif isinstance(obj, list):
            for item in obj:
                if isinstance(item, (dict, list)):
                    lines.append(f"{' ' * indent}- ")
                    lines.append(_to_yaml(item, indent + 4))
                else:
                    lines.append(f"{' ' * indent}- {item}")
        else:
            lines.append(f"{' ' * indent}{obj}")
        
        return "\n".join(filter(None, lines))
    
    return _to_yaml(data)


def groovy_dump(data: Dict[str, Any]) -> str:
    """简单 Groovy 转换"""
    
    pipeline = data.get("pipeline", {})
    
    lines = [
        "pipeline {",
        f"    agent {{ docker {{ image '{pipeline.get('agent', {}).get('docker', {}).get('image', 'python:3.11-slim')}' }} }}",
        "    stages {"
    ]
    
    for stage in pipeline.get("stages", []):
        stage_name = stage.get("stage", "")
        lines.append(f"        stage('{stage_name}') {{")
        lines.append("            steps {")
        
        for step in stage.get("steps", []):
            for key, value in step.items():
                if key == "sh":
                    lines.append(f'                sh "{value}"')
                elif key == "archiveArtifacts":
                    lines.append(f'                archiveArtifacts "{value}"')
                elif key == "junit":
                    lines.append(f'                junit "{value}"')
                elif key == "cobertura":
                    lines.append(f'                cobertura "{value}"')
        
        lines.append("            }")
        lines.append("        }")
    
    lines.append("    }")
    lines.append("    post {")
    lines.append("        always {")
    lines.append("            steps {")
    lines.append('                sh "echo \'Pipeline completed\'"')
    lines.append("            }")
    lines.append("        }")
    lines.append("        success {")
    lines.append("            steps {")
    lines.append('                sh "echo \'Pipeline succeeded!\'"')
    lines.append("            }")
    lines.append("        }")
    lines.append("        failure {")
    lines.append("            steps {")
    lines.append('                sh "echo \'Pipeline failed!\'"')
    lines.append("            }")
    lines.append("        }")
    lines.append("    }")
    lines.append("}")
    
    return "\n".join(lines)


# ============================================================================
# 使用示例
# ============================================================================

if __name__ == "__main__":
    print("CI/CD 集成案例示例")
    print("=" * 50)
    
    print("\n1. GitHub Actions 集成配置")
    print("-" * 50)
    github_config = github_actions_integration()
    print(json.dumps(github_config, indent=2, ensure_ascii=False)[:500] + "...")
    
    print("\n2. Jenkins Pipeline 集成配置")
    print("-" * 50)
    jenkins_config = jenkins_pipeline_integration()
    print(json.dumps(jenkins_config, indent=2, ensure_ascii=False)[:500] + "...")
    
    print("\n3. GitLab CI/CD 集成配置")
    print("-" * 50)
    gitlab_config = gitlab_ci_integration()
    print(json.dumps(gitlab_config, indent=2, ensure_ascii=False)[:500] + "...")
    
    print("\n4. 本地 CI/CD 脚本")
    print("-" * 50)
    local_script = local_cicd_script()
    print(local_script[:500] + "...")
    
    print("\n使用方法:")
    print("1. 将配置文件保存到相应位置")
    print("2. 配置必要的环境变量")
    print("3. 集成到你的 CI/CD 管道")
    print("\n🎉 CI/CD 集成准备就绪！")