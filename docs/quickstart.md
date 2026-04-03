# 快速开始指南

本文档将帮助您快速上手 AI Coding Workflow Manager。

## 1. 安装

### 1.1 从源码安装

```bash
# 克隆项目
git clone https://github.com/yourusername/ai-coding-workflow-manager.git
cd ai-coding-workflow-manager

# 安装依赖
pip install -r requirements.txt

# 安装项目
pip install -e .
```

### 1.2 从PyPI安装

```bash
pip install ai-coding-workflow-manager
```

## 2. 配置API密钥

### 2.1 创建环境变量文件

```bash
cp .env.example .env
```

### 2.2 编辑环境变量文件

打开 `.env` 文件，添加您的API密钥：

```env
# Claude API Configuration
CLAUDE_API_KEY=your-claude-api-key-here

# OpenAI API Configuration
OPENAI_API_KEY=your-openai-api-key-here
```

## 3. 快速开始示例

### 3.1 创建第一个工作流

```python
import os
from ai_coding_workflow import WorkflowManager

# 初始化工作流管理器
manager = WorkflowManager()

# 创建工作流
workflow = manager.create_workflow(
    name="my_first_workflow",
    description="My first AI coding workflow"
)

# 添加任务
workflow.add_task(
    model="claude",
    task_type="code_review",
    file_path="src/main.py",
    check_style=True
)

# 执行工作流
results = workflow.execute()
print(results)
```

### 3.2 使用模板

```python
from ai_coding_workflow import WorkflowManager

manager = WorkflowManager()

# 使用预定义模板
workflow = manager.create_workflow(
    name="code_review",
    template="code_review"
)

# 执行工作流
results = workflow.execute()
```

## 4. 命令行工具

### 4.1 初始化

```bash
python scripts/run_workflow.py init \
  --claude-key YOUR_CLAUDE_KEY \
  --openai-key YOUR_OPENAI_KEY
```

### 4.2 创建工作流

```bash
# 创建简单工作流
python scripts/run_workflow.py create \
  --name "my_code_review" \
  --description "Review my code"

# 使用模板创建工作流
python scripts/run_workflow.py create \
  --name "refactor_workflow" \
  --template "refactor"
```

### 4.3 列出工作流

```bash
python scripts/run_workflow.py list
```

### 4.4 执行工作流

```bash
python scripts/run_workflow.py execute --name "my_code_review"
```

### 4.5 查看可用模板

```bash
python scripts/run_workflow.py templates
```

## 5. 常见任务示例

### 5.1 代码审查

```python
workflow = manager.create_workflow(
    name="code_review",
    description="Automated code review"
)

workflow.add_task(
    model="claude",
    task_type="code_review",
    file_path="src/main.py",
    check_style=True,
    check_security=True,
    check_performance=True
)

workflow.add_task(
    model="openai",
    task_type="security_audit",
    file_path="src/main.py",
    deep_scan=True
)
```

### 5.2 代码重构

```python
workflow = manager.create_workflow(
    name="refactor",
    description="Code refactoring"
)

workflow.add_task(
    model="claude",
    task_type="analyze_code",
    file_path="src/utils.py",
    identify_smells=True,
    suggest_improvements=True
)

workflow.add_task(
    model="openai",
    task_type="refactor",
    file_path="src/utils.py",
    preserve_behavior=True,
    improve_readability=True
)
```

### 5.3 测试生成

```python
workflow = manager.create_workflow(
    name="test_generation",
    description="Generate tests"
)

workflow.add_task(
    model="claude",
    task_type="analyze_code",
    file_path="src/api.py",
    identify_testable_functions=True
)

workflow.add_task(
    model="openai",
    task_type="generate_unit_tests",
    file_path="src/api.py",
    framework="pytest",
    coverage_target=80
)
```

## 6. 保存和加载工作流

### 6.1 保存工作流

```python
# 保存到默认位置
output_path = manager.save_workflow("my_workflow")

# 保存到指定位置
output_path = manager.save_workflow(
    "my_workflow",
    output_path="workflows/my_workflow.json"
)
```

### 6.2 加载工作流

```python
# 加载工作流
workflow = manager.load_workflow("workflows/my_workflow.json")

# 继续使用
workflow.add_task(
    model="claude",
    task_type="additional_task",
    file_path="src/new_file.py"
)

results = workflow.execute()
```

## 7. 故障排除

### 7.1 API密钥错误

**问题**: `AuthenticationError: Invalid API key`

**解决方案**:
1. 检查 `.env` 文件中的API密钥是否正确
2. 确保API密钥有足够的权限
3. 检查API密钥是否过期

### 7.2 导入错误

**问题**: `ModuleNotFoundError: No module named 'ai_coding_workflow'`

**解决方案**:
1. 确保已经安装了项目: `pip install -e .`
2. 检查当前工作目录是否正确

### 7.3 文件路径错误

**问题**: `FileNotFoundError: No such file or directory`

**解决方案**:
1. 检查文件路径是否正确
2. 使用绝对路径而不是相对路径

## 8. 下一步

- 查看 [API文档](api.md) 了解更多细节
- 探索 [最佳实践](best_practices.md) 提高效率
- 查看 [模板指南](templates.md) 了解可用模板
- 阅读 [贡献指南](contributing.md) 参与开发