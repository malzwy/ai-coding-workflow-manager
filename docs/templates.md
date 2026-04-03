# 工作流模板指南

本文档介绍了 AI Coding Workflow Manager 中可用的所有工作流模板。

## 可用模板

### 1. code_review - 代码审查

**描述**: 自动化代码审查工作流，检查代码质量、安全性和最佳实践

**任务**:
1. **Claude - 代码审查**
   - 检查代码风格
   - 检查安全性
   - 检查性能

2. **OpenAI - 安全审计**
   - 深度安全扫描
   - 依赖项检查

3. **Claude - 最佳实践**
   - 语言特定最佳实践
   - 框架特定建议

**使用方法**:
```python
workflow = manager.create_workflow(
    name="code_review",
    template="code_review"
)
```

**参数**:
- `file_path`: 要审查的文件路径
- `check_style`: 是否检查代码风格 (默认: true)
- `check_security`: 是否检查安全性 (默认: true)
- `check_performance`: 是否检查性能 (默认: true)
- `language`: 编程语言 (默认: python)
- `framework`: 框架名称 (可选)

---

### 2. refactor - 代码重构

**描述**: 代码重构和优化工作流

**任务**:
1. **Claude - 代码分析**
   - 识别代码异味
   - 建议改进

2. **OpenAI - 重构**
   - 保持行为不变
   - 提高可读性
   - 优化性能

3. **Claude - 验证重构**
   - 运行测试
   - 检查破坏性变更

**使用方法**:
```python
workflow = manager.create_workflow(
    name="refactor",
    template="refactor"
)
```

**参数**:
- `file_path`: 要重构的文件路径
- `identify_smells`: 是否识别代码异味 (默认: true)
- `suggest_improvements`: 是否建议改进 (默认: true)
- `preserve_behavior`: 是否保持行为不变 (默认: true)
- `improve_readability`: 是否提高可读性 (默认: true)
- `optimize_performance`: 是否优化性能 (默认: true)
- `run_tests`: 是否运行测试 (默认: true)
- `check_breaking_changes`: 是否检查破坏性变更 (默认: true)

---

### 3. test_generation - 测试生成

**描述**: 自动化测试生成工作流

**任务**:
1. **Claude - 代码分析**
   - 识别可测试函数
   - 分析依赖关系

2. **OpenAI - 单元测试生成**
   - 生成单元测试
   - 目标覆盖率

3. **Claude - 集成测试生成**
   - 测试端点
   - 测试数据库

4. **OpenAI - 端到端测试生成**
   - 测试场景
   - 使用Playwright

**使用方法**:
```python
workflow = manager.create_workflow(
    name="test_generation",
    template="test_generation"
)
```

**参数**:
- `file_path`: 要测试的文件路径
- `identify_testable_functions`: 是否识别可测试函数 (默认: true)
- `analyze_dependencies`: 是否分析依赖关系 (默认: true)
- `framework`: 测试框架 (默认: pytest)
- `coverage_target`: 目标覆盖率 (默认: 80)
- `test_endpoints`: 是否测试端点 (默认: true)
- `test_database`: 是否测试数据库 (默认: true)
- `test_scenarios`: 测试场景列表

---

## 自定义模板

### 创建自定义模板

1. 在 `templates/` 目录下创建新的 YAML 文件

2. 定义模板结构:

```yaml
# templates/my_custom_template.yaml

description: "My custom workflow description"

tasks:
  - model: claude
    task_type: my_task_type
    file_path: "src/my_file.py"
    parameters:
      param1: value1
      param2: value2

  - model: openai
    task_type: another_task_type
    file_path: "src/another_file.py"
    parameters:
      param1: value1
```

3. 使用自定义模板:

```python
workflow = manager.create_workflow(
    name="my_workflow",
    template="my_custom_template"
)
```

### 模板最佳实践

1. **命名规范**: 使用小写字母和下划线
2. **描述清晰**: 提供详细的模板描述
3. **参数合理**: 设置合理的默认参数值
4. **任务顺序**: 按逻辑顺序排列任务
5. **文档完善**: 为每个参数添加注释

---

## 模板参数说明

### 通用参数

- `file_path`: 文件路径 (必需)
- `model`: 使用的AI模型 (claude 或 openai)
- `task_type`: 任务类型

### Claude 特定参数

- `check_style`: 检查代码风格
- `check_security`: 检查安全性
- `check_performance`: 检查性能
- `language`: 编程语言
- `framework`: 框架名称

### OpenAI 特定参数

- `deep_scan`: 深度扫描
- `check_dependencies`: 检查依赖项
- `preserve_behavior`: 保持行为不变
- `improve_readability`: 提高可读性
- `optimize_performance`: 优化性能

---

## 模板示例

### 完整示例

```python
from ai_coding_workflow import WorkflowManager

# 初始化管理器
manager = WorkflowManager()

# 使用代码审查模板
workflow = manager.create_workflow(
    name="my_code_review",
    template="code_review"
)

# 修改任务参数
for task in workflow.tasks:
    if task.task_type == "code_review":
        task.parameters["file_path"] = "src/my_app.py"
        task.parameters["language"] = "python"
        task.parameters["framework"] = "fastapi"

# 执行工作流
results = workflow.execute()

# 保存结果
manager.save_workflow("my_code_review")
```

### 命令行示例

```bash
# 使用模板创建工作流
python scripts/run_workflow.py create \
  --name "my_review" \
  --template "code_review"

# 执行工作流
python scripts/run_workflow.py execute --name "my_review"
```

---

## 模板维护

### 更新模板

1. 编辑 `templates/` 目录下的 YAML 文件
2. 测试更新后的模板
3. 更新文档

### 删除模板

```bash
rm templates/old_template.yaml
```

### 查看所有模板

```bash
python scripts/run_workflow.py templates
```

---

## 常见问题

### Q: 如何修改模板中的参数？

A: 创建工作流后，可以修改任务的参数:

```python
workflow = manager.create_workflow(name="my_workflow", template="code_review")

# 修改第一个任务的参数
workflow.tasks[0].parameters["file_path"] = "new/path.py"
```

### Q: 可以组合多个模板吗？

A: 可以，创建多个工作流然后合并任务:

```python
workflow1 = manager.create_workflow(name="review", template="code_review")
workflow2 = manager.create_workflow(name="refactor", template="refactor")

# 合并任务
combined_workflow = manager.create_workflow(name="combined")
combined_workflow.tasks = workflow1.tasks + workflow2.tasks
```

### Q: 如何创建自己的模板？

A: 在 `templates/` 目录下创建新的 YAML 文件，参考现有模板的结构。

---

## 下一步

- 查看 [API文档](api.md) 了解更多细节
- 探索 [最佳实践](best_practices.md) 提高效率
- 阅读 [快速开始](quickstart.md) 快速上手
