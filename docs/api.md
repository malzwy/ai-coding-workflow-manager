# API 文档

本文档提供了 AI Coding Workflow Manager 的完整 API 参考。

## WorkflowManager

工作流管理器的主要类，用于创建和管理工作流。

### 初始化

```python
WorkflowManager(
    claude_api_key: Optional[str] = None,
    openai_api_key: Optional[str] = None,
    config_file: Optional[str] = None
)
```

**参数**:
- `claude_api_key`: Claude API 密钥（可选，可通过环境变量设置）
- `openai_api_key`: OpenAI API 密钥（可选，可通过环境变量设置）
- `config_file`: 配置文件路径（可选）

**示例**:
```python
from ai_coding_workflow import WorkflowManager

# 使用环境变量
manager = WorkflowManager()

# 直接指定API密钥
manager = WorkflowManager(
    claude_api_key="your-claude-key",
    openai_api_key="your-openai-key"
)
```

### 方法

#### create_workflow

创建新的工作流。

```python
create_workflow(
    name: str,
    description: str = "",
    template: Optional[str] = None
) -> Workflow
```

**参数**:
- `name`: 工作流名称
- `description`: 工作流描述
- `template`: 模板名称（可选）

**返回**: Workflow 实例

**示例**:
```python
workflow = manager.create_workflow(
    name="my_workflow",
    description="My first workflow"
)
```

#### get_workflow

获取工作流。

```python
get_workflow(name: str) -> Optional[Workflow]
```

**参数**:
- `name`: 工作流名称

**返回**: Workflow 实例或 None

**示例**:
```python
workflow = manager.get_workflow("my_workflow")
```

#### list_workflows

列出所有工作流。

```python
list_workflows() -> List[str]
```

**返回**: 工作流名称列表

**示例**:
```python
workflows = manager.list_workflows()
print(workflows)  # ['workflow1', 'workflow2']
```

#### delete_workflow

删除工作流。

```python
delete_workflow(name: str) -> bool
```

**参数**:
- `name`: 工作流名称

**返回**: 成功返回 True，失败返回 False

**示例**:
```python
success = manager.delete_workflow("my_workflow")
```

#### get_available_templates

获取可用模板列表。

```python
get_available_templates() -> List[str]
```

**返回**: 模板名称列表

**示例**:
```python
templates = manager.get_available_templates()
print(templates)  # ['code_review', 'refactor', 'test_generation']
```

#### save_workflow

保存工作流到文件。

```python
save_workflow(
    name: str,
    output_path: Optional[str] = None
) -> str
```

**参数**:
- `name`: 工作流名称
- `output_path`: 输出文件路径（可选）

**返回**: 保存的文件路径

**示例**:
```python
path = manager.save_workflow("my_workflow")
```

#### load_workflow

从文件加载工作流。

```python
load_workflow(file_path: str) -> Workflow
```

**参数**:
- `file_path`: 工作流文件路径

**返回**: 加载的 Workflow 实例

**示例**:
```python
workflow = manager.load_workflow("workflows/my_workflow.json")
```

---

## Workflow

工作流类，表示一个包含多个任务的工作流。

### 属性

- `name`: 工作流名称
- `description`: 工作流描述
- `tasks`: 任务列表
- `created_at`: 创建时间
- `updated_at`: 更新时间
- `status`: 状态（created, running, completed）
- `results`: 执行结果

### 方法

#### add_task

添加任务到工作流。

```python
add_task(
    model: str,
    task_type: str,
    **kwargs
) -> Task
```

**参数**:
- `model`: 模型名称（claude 或 openai）
- `task_type`: 任务类型
- `**kwargs`: 其他任务参数

**返回**: 创建的 Task 实例

**示例**:
```python
task = workflow.add_task(
    model="claude",
    task_type="code_review",
    file_path="src/main.py",
    check_style=True
)
```

#### remove_task

从工作流中移除任务。

```python
remove_task(task_id: str) -> bool
```

**参数**:
- `task_id`: 任务 ID

**返回**: 成功返回 True，失败返回 False

**示例**:
```python
success = workflow.remove_task(task.id)
```

#### get_task

获取任务。

```python
get_task(task_id: str) -> Optional[Task]
```

**参数**:
- `task_id`: 任务 ID

**返回**: Task 实例或 None

**示例**:
```python
task = workflow.get_task(task_id)
```

#### list_tasks

列出所有任务 ID。

```python
list_tasks() -> List[str]
```

**返回**: 任务 ID 列表

**示例**:
```python
task_ids = workflow.list_tasks()
```

#### execute

执行工作流中的所有任务。

```python
execute() -> Dict[str, Any]
```

**返回**: 任务结果字典

**示例**:
```python
results = workflow.execute()
for task_id, result in results.items():
    print(f"Task {task_id}: {result}")
```

#### load_template

加载工作流模板。

```python
load_template(template_name: str) -> None
```

**参数**:
- `template_name`: 模板名称

**示例**:
```python
workflow.load_template("code_review")
```

#### save

保存工作流到文件。

```python
save(file_path: str) -> None
```

**参数**:
- `file_path`: 保存路径

**示例**:
```python
workflow.save("workflows/my_workflow.json")
```

#### to_dict

转换为字典。

```python
to_dict() -> Dict[str, Any]
```

**返回**: 字典表示

**示例**:
```python
data = workflow.to_dict()
```

---

## Task

任务类，表示工作流中的单个任务。

### 属性

- `id`: 任务 ID
- `model`: 使用的模型
- `task_type`: 任务类型
- `parameters`: 任务参数
- `created_at`: 创建时间
- `status`: 状态（pending, running, completed, failed）
- `result`: 执行结果
- `error`: 错误信息

### 方法

#### execute

执行任务。

```python
execute() -> Dict[str, Any]
```

**返回**: 任务结果

**示例**:
```python
result = task.execute()
```

#### to_dict

转换为字典。

```python
to_dict() -> Dict[str, Any]
```

**返回**: 字典表示

**示例**:
```python
data = task.to_dict()
```

---

## ModelConfig

模型配置类。

### 属性

- `api_key`: API 密钥
- `model`: 模型名称
- `max_tokens`: 最大 token 数
- `temperature`: 温度参数

### 示例

```python
from ai_coding_workflow.models import ModelConfig

config = ModelConfig(
    api_key="your-api-key",
    model="claude-3-opus-20240229",
    max_tokens=4096,
    temperature=0.7
)
```

---

## TaskResult

任务结果类。

### 属性

- `task_id`: 任务 ID
- `model`: 使用的模型
- `task_type`: 任务类型
- `status`: 任务状态
- `output`: 任务输出
- `error`: 错误信息
- `execution_time`: 执行时间

### 示例

```python
from ai_coding_workflow.models import TaskResult

result = TaskResult(
    task_id="123",
    model="claude",
    task_type="code_review",
    status="completed",
    output="Code review completed",
    execution_time=2.5
)
```

---

## WorkflowResult

工作流结果类。

### 属性

- `workflow_name`: 工作流名称
- `status`: 工作流状态
- `total_tasks`: 总任务数
- `completed_tasks`: 完成的任务数
- `failed_tasks`: 失败的任务数
- `results`: 任务结果
- `execution_time`: 总执行时间

### 示例

```python
from ai_coding_workflow.models import WorkflowResult

result = WorkflowResult(
    workflow_name="my_workflow",
    status="completed",
    total_tasks=3,
    completed_tasks=3,
    failed_tasks=0,
    results={},
    execution_time=7.5
)
```

---

## 错误处理

### 常见错误

#### ValueError

当工作流不存在或参数无效时抛出。

```python
try:
    workflow = manager.get_workflow("nonexistent")
except ValueError as e:
    print(f"Error: {e}")
```

#### FileNotFoundError

当文件不存在时抛出。

```python
try:
    workflow = manager.load_workflow("nonexistent.json")
except FileNotFoundError as e:
    print(f"Error: {e}")
```

---

## 完整示例

```python
from ai_coding_workflow import WorkflowManager

# 初始化管理器
manager = WorkflowManager()

# 创建工作流
workflow = manager.create_workflow(
    name="my_workflow",
    description="My first workflow"
)

# 添加任务
task1 = workflow.add_task(
    model="claude",
    task_type="code_review",
    file_path="src/main.py",
    check_style=True
)

task2 = workflow.add_task(
    model="openai",
    task_type="security_audit",
    file_path="src/main.py",
    deep_scan=True
)

# 执行工作流
results = workflow.execute()

# 保存工作流
manager.save_workflow("my_workflow")

# 加载工作流
loaded_workflow = manager.load_workflow("output/my_workflow.json")

# 列出所有工作流
workflows = manager.list_workflows()
print(f"Available workflows: {workflows}")
```

---

## 下一步

- 查看 [快速开始](quickstart.md) 快速上手
- 探索 [模板指南](templates.md) 了解可用模板
- 阅读 [最佳实践](best_practices.md) 提高效率
