# AI Coding Workflow Manager

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Claude API](https://img.shields.io/badge/Claude-API-green.svg)](https://www.anthropic.com/claude)
[![OpenAI API](https://img.shields.io/badge/OpenAI-API-blue.svg)](https://openai.com/)

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

## 🛠️ 技术栈

- **语言**: Python 3.10+
- **AI模型**: Claude API, OpenAI API
- **版本控制**: Git
- **文档**: Markdown
- **测试**: pytest

## 📦 安装

```bash
# 克隆项目
git clone https://github.com/yourusername/ai-coding-workflow-manager.git
cd ai-coding-workflow-manager

# 安装依赖
pip install -r requirements.txt

# 配置API密钥
cp .env.example .env
# 编辑 .env 文件，添加你的API密钥
```

## 🚀 快速开始

### 基础使用

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

### 使用模板

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

## 🎯 使用场景

### 1. 代码审查
自动化的代码审查流程，检查代码质量、安全性和最佳实践。

### 2. 重构优化
智能识别代码改进点，提供重构建议和自动化重构。

### 3. 测试生成
根据代码自动生成单元测试、集成测试和端到端测试。

### 4. 文档生成
自动生成代码文档、API文档和用户手册。

### 5. Bug修复
智能分析bug，提供修复建议和自动化修复。

## 🤝 贡献

欢迎贡献！请查看[贡献指南](docs/contributing.md)了解详情。

## 📄 许可证

本项目采用 MIT 许可证 - 详见 [LICENSE](LICENSE) 文件

## 🙏 致谢

- [Claude Code](https://github.com/anthropics/claude-code) - 强大的AI编码助手
- [OpenAI Codex](https://github.com/openai/codex) - 轻量级编码代理
- [Claude Howto](https://github.com/luongnv89/claude-howto) - 优秀的Claude Code指南

## 📈 趋势分析

本项目基于2026年4月2日的GitHub趋势分析开发，重点关注：
- AI编码工具的爆发式增长
- 多模型协作的需求
- 工作流自动化的趋势

## 🔗 相关链接

- [GitHub Trending](https://github.com/trending)
- [Claude API Documentation](https://docs.anthropic.com/claude/reference)
- [OpenAI API Documentation](https://platform.openai.com/docs)

---

**⭐ 如果这个项目对你有帮助，请给个Star！**
