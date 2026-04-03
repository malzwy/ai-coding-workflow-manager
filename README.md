# AI Coding Workflow Manager

[![Python Version](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Claude API](https://img.shields.io/badge/Claude-API-green.svg)](https://www.anthropic.com/claude)
[![OpenAI API](https://img.shields.io/badge/OpenAI-API-blue.svg)](https://openai.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub Stars](https://img.shields.io/github/stars/malzwy/ai-coding-workflow-manager?style=social)](https://github.com/malzwy/ai-coding-workflow-manager/stargazers)
[![GitHub Issues](https://img.shields.io/github/issues/malzwy/ai-coding-workflow-manager)](https://github.com/malzwy/ai-coding-workflow-manager/issues)

> 🚀 一个强大的AI编码助手工作流管理工具，支持多AI模型协作，提供丰富的模板和最佳实践

## 📊 项目背景

基于2026年GitHub趋势分析，AI编码工具正在爆发式增长：
- **Claude Code**: +10,749 stars today (100,845 total)
- **OpenAI Codex**: +2,390 stars today (71,730 total)
- **Claude Howto**: +3,301 stars today (15,606 total)

本项目旨在整合这些强大的AI编码工具，提供统一的工作流管理平台。

## ✨ 核心功能

### 🤖 多AI模型协作
- 支持 Claude API 和 OpenAI API
- 智能模型选择和切换
- 并行任务处理
- 结果聚合和优化

### 📋 工作流模板
- 代码审查工作流
- 重构优化工作流
- 测试生成工作流
- 文档生成工作流
- Bug修复工作流

### 🎯 最佳实践
- 提示词工程模板
- 代码质量检查
- 安全审计流程
- 性能优化建议

### 🔧 集成工具
- Git版本控制集成
- CI/CD流水线支持
- IDE插件接口
- 命令行工具

## 🚀 快速开始

### 安装

```bash
# 克隆项目
git clone https://github.com/malzwy/ai-coding-workflow-manager.git
cd ai-coding-workflow-manager

# 安装依赖
pip install -r requirements.txt

# 配置API密钥
cp .env.example .env
# 编辑 .env 文件，添加你的API密钥
```

### 基本使用

```python
from ai_coding_workflow import WorkflowManager

# 初始化工作流管理器
manager = WorkflowManager(
    claude_api_key="your-claude-api-key",
    openai_api_key="your-openai-api-key"
)

# 创建代码审查工作流
workflow = manager.create_workflow("code_review")

# 添加任务
workflow.add_task(
    model="claude",
    task="review_code",
    file_path="src/main.py"
)

# 执行工作流
results = workflow.execute()
print(results)
```

### CLI工具

```bash
# 使用代码审查模板
python scripts/run_workflow.py --template code_review --file src/main.py

# 使用重构优化模板
python scripts/run_workflow.py --template refactor --file src/utils.py

# 使用测试生成模板
python scripts/run_workflow.py --template test_generation --file src/api.py
```

## 📚 文档

- [快速开始指南](docs/quickstart.md)
- [工作流模板](docs/templates.md)
- [API文档](docs/api.md)
- [最佳实践](docs/best_practices.md)
- [贡献指南](docs/contributing.md)

## 🎯 使用案例

### 案例1: 代码审查

```python
from ai_coding_workflow import WorkflowManager

# 初始化
manager = WorkflowManager(
    claude_api_key="your-claude-api-key"
)

# 创建代码审查工作流
workflow = manager.create_workflow("code_review")

# 添加多个代码审查任务
workflow.add_task(
    model="claude",
    task="review_code",
    file_path="src/api.py",
    context="Focus on security vulnerabilities and performance issues"
)
workflow.add_task(
    model="openai",
    task="review_code",
    file_path="src/models.py",
    context="Check for code quality and best practices"
)

# 执行并获取报告
report = workflow.execute()
print(f"Review Summary: {report['summary']}")
print(f"Issues Found: {len(report['issues'])}")
for issue in report['issues']:
    print(f"- {issue['severity']}: {issue['message']}")
```

### 案例2: 代码重构

```python
from ai_coding_workflow import WorkflowManager

# 初始化
manager = WorkflowManager(
    openai_api_key="your-openai-api-key"
)

# 创建重构工作流
workflow = manager.create_workflow("refactor")

# 添加重构任务
workflow.add_task(
    model="openai",
    task="refactor_code",
    file_path="src/legacy_code.py",
    requirements="Improve readability, reduce complexity, add type hints"
)

# 执行重构
results = workflow.execute()
if results['success']:
    print("Refactoring completed successfully!")
    print(f"Code complexity reduced from {results['original_complexity']} to {results['new_complexity']}")
else:
    print("Refactoring failed:", results['error'])
```

### 案例3: 测试生成

```python
from ai_coding_workflow import WorkflowManager

# 初始化
manager = WorkflowManager(
    claude_api_key="your-claude-api-key"
)

# 创建测试生成工作流
workflow = manager.create_workflow("test_generation")

# 添加测试生成任务
workflow.add_task(
    model="claude",
    task="generate_tests",
    file_path="src/calculator.py",
    test_framework="pytest",
    coverage_target=90
)

# 执行测试生成
results = workflow.execute()
print(f"Generated {len(results['test_cases'])} test cases")
print(f"Coverage: {results['coverage']}%")
```

### 案例4: 混合模型协作

```python
from ai_coding_workflow import WorkflowManager

# 初始化（使用两个模型）
manager = WorkflowManager(
    claude_api_key="your-claude-api-key",
    openai_api_key="your-openai-api-key"
)

# 创建复杂工作流
workflow = manager.create_workflow("code_review")

# 使用Claude进行初步审查
workflow.add_task(
    model="claude",
    task="review_code",
    file_path="src/complex_module.py",
    priority="high"
)

# 使用OpenAI进行深度分析
workflow.add_task(
    model="openai",
    task="analyze_code",
    file_path="src/complex_module.py",
    focus="performance and security"
)

# 执行并聚合结果
results = workflow.execute()
print(f"Analysis completed with {len(results['tasks'])} sub-tasks")
```

### 案例5: CI/CD集成

```python
# .github/workflows/test.yml
name: Test Workflow

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
      
      - name: Run code review
        run: |
          python scripts/run_workflow.py --template code_review --file src/
      
      - name: Generate tests
        run: |
          python scripts/run_workflow.py --template test_generation --file src/
      
      - name: Run tests
        run: |
          pytest tests/
```

## 🛠️ 技术栈

- **语言**: Python 3.10+
- **AI模型**: Claude API, OpenAI API
- **版本控制**: Git
- **文档**: Markdown
- **测试**: pytest

## 📦 项目结构

```
ai-coding-workflow-manager/
├── ai_coding_workflow/       # 核心模块
│   ├── __init__.py
│   ├── manager.py            # 核心管理器
│   ├── workflow.py           # 工作流定义
│   ├── task.py               # 任务管理
│   └── models.py             # AI模型配置
├── templates/                # 工作流模板
│   ├── code_review.yaml
│   ├── refactor.yaml
│   └── test_generation.yaml
├── examples/                 # 使用示例
│   ├── basic_usage.py
│   ├── advanced_usage.py
│   └── ci_cd_integration.py
├── scripts/                  # CLI工具
│   └── run_workflow.py
├── docs/                     # 文档
│   ├── quickstart.md
│   ├── templates.md
│   ├── api.md
│   ├── best_practices.md
│   └── contributing.md
├── tests/                    # 测试目录
├── .github/workflows/        # CI/CD配置
├── LICENSE                   # MIT许可证
├── README.md                 # 项目说明
├── requirements.txt          # 依赖列表
└── .env.example              # 环境变量示例
```

## 🤝 贡献指南

欢迎贡献！请查看 [贡献指南](docs/contributing.md) 了解详情。

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [Claude Code](https://github.com/anthropics/claude-code) - 强大的AI编码助手
- [OpenAI Codex](https://github.com/openai/codex) - 轻量级编码代理
- [Claude Howto](https://github.com/luongnv89/claude-howto) - 优秀的Claude Code指南

本项目基于2026年4月2日的GitHub趋势分析开发，重点关注：
- AI编码工具的爆发式增长
- 多模型协作的需求
- 工作流自动化的趋势

## 🌟 Star History

如果这个项目对你有帮助，请给个Star！⭐

[![Star History Chart](https://api.star-history.com/svg?repos=malzwy/ai-coding-workflow-manager&type=Date)](https://star-history.com/#malzwy/ai-coding-workflow-manager&Date)

---

**Made with ❤️ by the AI Coding Workflow Manager Community**
