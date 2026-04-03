"""
高级使用案例 - Advanced Usage Examples

本文件展示了AI编码工作流管理器的更高级使用方法。
"""

from ai_coding_workflow import WorkflowManager, Task, Workflow
from ai_coding_workflow.models import ModelConfig, TaskPriority

# ============================================================================
# 案例1: 多阶段代码审查工作流
# ============================================================================

def multi_stage_code_review(file_path: str):
    """多阶段代码审查：静态分析 + 模型审查 + 人工审查"""

    manager = WorkflowManager(
        claude_api_key="your-claude-api-key",
        openai_api_key="your-openai-api-key"
    )

    workflow = manager.create_workflow("code_review")

    # 阶段1: 静态代码分析（使用基础工具）
    workflow.add_task(
        model="openai",
        task="static_analysis",
        file_path=file_path,
        priority=TaskPriority.HIGH,
        context="Perform static code analysis without AI assistance"
    )

    # 阶段2: AI初步审查
    workflow.add_task(
        model="claude",
        task="review_code",
        file_path=file_path,
        priority=TaskPriority.HIGH,
        context="Focus on code quality, maintainability, and best practices"
    )

    # 阶段3: AI深度分析（安全性和性能）
    workflow.add_task(
        model="openai",
        task="deep_analysis",
        file_path=file_path,
        priority=TaskPriority.MEDIUM,
        context="Analyze security vulnerabilities and performance issues"
    )

    # 阶段4: 生成审查报告
    workflow.add_task(
        model="claude",
        task="generate_report",
        file_path=file_path,
        priority=TaskPriority.LOW,
        context="Generate comprehensive code review report"
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例2: 渐进式重构工作流
# ============================================================================

def progressive_refactor(file_path: str):
    """渐进式重构：逐步优化，避免破坏性变更"""

    manager = WorkflowManager(openai_api_key="your-openai-api-key")

    workflow = manager.create_workflow("refactor")

    # 第1步：分析当前代码
    workflow.add_task(
        model="openai",
        task="analyze_code",
        file_path=file_path,
        context="Analyze current code structure and identify refactoring opportunities"
    )

    # 第2步：制定重构计划
    workflow.add_task(
        model="openai",
        task="create_refactor_plan",
        file_path=file_path,
        context="Create detailed refactoring plan with priorities"
    )

    # 第3步：执行重构（小步快跑）
    workflow.add_task(
        model="openai",
        task="refactor_code",
        file_path=file_path,
        context="Apply refactoring changes incrementally"
    )

    # 第4步：验证重构结果
    workflow.add_task(
        model="claude",
        task="verify_refactor",
        file_path=file_path,
        context="Verify that refactoring didn't introduce bugs"
    )

    # 第5步：运行测试
    workflow.add_task(
        model="openai",
        task="run_tests",
        file_path=file_path,
        context="Run tests to ensure code still works correctly"
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例3: 自动化测试生成工作流
# ============================================================================

def automated_test_generation(file_path: str, test_framework: str = "pytest"):
    """自动化测试生成：根据代码自动生成全面的测试套件"""

    manager = WorkflowManager(claude_api_key="your-claude-api-key")

    workflow = manager.create_workflow("test_generation")

    # 第1步：分析代码结构和功能
    workflow.add_task(
        model="claude",
        task="analyze_code",
        file_path=file_path,
        context=f"Analyze code structure and identify testable components for {test_framework}"
    )

    # 第2步：生成单元测试
    workflow.add_task(
        model="claude",
        task="generate_unit_tests",
        file_path=file_path,
        test_framework=test_framework,
        coverage_target=85
    )

    # 第3步：生成集成测试
    workflow.add_task(
        model="claude",
        task="generate_integration_tests",
        file_path=file_path,
        test_framework=test_framework
    )

    # 第4步：生成端到端测试
    workflow.add_task(
        model="claude",
        task="generate_e2e_tests",
        file_path=file_path,
        test_framework=test_framework
    )

    # 第5步：生成测试数据
    workflow.add_task(
        model="claude",
        task="generate_test_data",
        file_path=file_path,
        test_framework=test_framework
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例4: 智能代码补全工作流
# ============================================================================

def intelligent_code_completion(file_path: str, context: str):
    """智能代码补全：根据上下文智能生成代码"""

    manager = WorkflowManager(claude_api_key="your-claude-api-key")

    workflow = manager.create_workflow("code_completion")

    # 第1步：分析上下文
    workflow.add_task(
        model="claude",
        task="analyze_context",
        file_path=file_path,
        context=context,
        priority=TaskPriority.HIGH
    )

    # 第2步：生成代码建议
    workflow.add_task(
        model="claude",
        task="generate_code",
        file_path=file_path,
        context=context,
        code_style="modern_python"
    )

    # 第3步：验证代码正确性
    workflow.add_task(
        model="openai",
        task="validate_code",
        file_path=file_path,
        context=context
    )

    # 第4步：生成代码文档
    workflow.add_task(
        model="claude",
        task="generate_documentation",
        file_path=file_path,
        context=context
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例5: 代码审查自动化工作流
# ============================================================================

def automated_code_review(file_path: str):
    """自动化代码审查：集成多个工具和AI模型"""

    manager = WorkflowManager(
        claude_api_key="your-claude-api-key",
        openai_api_key="your-openai-api-key"
    )

    workflow = manager.create_workflow("code_review")

    # 阶段1: 静态分析
    workflow.add_task(
        model="openai",
        task="static_analysis",
        file_path=file_path,
        context="Static code analysis using linters and formatters"
    )

    # 阶段2: 代码质量检查
    workflow.add_task(
        model="claude",
        task="check_quality",
        file_path=file_path,
        context="Check code quality against best practices"
    )

    # 阶段3: 安全审计
    workflow.add_task(
        model="openai",
        task="security_audit",
        file_path=file_path,
        context="Identify security vulnerabilities and risks"
    )

    # 阶段4: 性能分析
    workflow.add_task(
        model="claude",
        task="performance_analysis",
        file_path=file_path,
        context="Analyze code performance and suggest optimizations"
    )

    # 阶段5: 生成审查报告
    workflow.add_task(
        model="openai",
        task="generate_report",
        file_path=file_path,
        context="Generate comprehensive code review report with actionable recommendations"
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例6: 代码重构与优化工作流
# ============================================================================

def refactor_and_optimize(file_path: str):
    """代码重构与优化：结合重构和性能优化"""

    manager = WorkflowManager(
        claude_api_key="your-claude-api-key",
        openai_api_key="your-openai-api-key"
    )

    workflow = manager.create_workflow("refactor")

    # 阶段1: 代码分析
    workflow.add_task(
        model="claude",
        task="analyze_code",
        file_path=file_path,
        context="Comprehensive code analysis for refactoring opportunities"
    )

    # 阶段2: 重构计划
    workflow.add_task(
        model="openai",
        task="create_refactor_plan",
        file_path=file_path,
        context="Create detailed refactoring plan with priorities and risks"
    )

    # 阶段3: 重构执行
    workflow.add_task(
        model="claude",
        task="apply_refactoring",
        file_path=file_path,
        context="Apply refactoring changes while maintaining functionality"
    )

    # 阶段4: 性能优化
    workflow.add_task(
        model="openai",
        task="optimize_performance",
        file_path=file_path,
        context="Optimize code performance and reduce computational complexity"
    )

    # 阶段5: 代码审查
    workflow.add_task(
        model="claude",
        task="review_refactored_code",
        file_path=file_path,
        context="Review refactored code for quality and correctness"
    )

    # 阶段6: 测试验证
    workflow.add_task(
        model="openai",
        task="verify_changes",
        file_path=file_path,
        context="Run tests to verify all changes work correctly"
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例7: 文档自动生成工作流
# ============================================================================

def auto_documentation_generation(file_path: str):
    """文档自动生成：从代码生成完整的文档"""

    manager = WorkflowManager(claude_api_key="your-claude-api-key")

    workflow = manager.create_workflow("documentation")

    # 第1步：分析代码
    workflow.add_task(
        model="claude",
        task="analyze_code",
        file_path=file_path,
        context="Analyze code structure and identify all components"
    )

    # 第2步：生成API文档
    workflow.add_task(
        model="claude",
        task="generate_api_docs",
        file_path=file_path,
        format="markdown"
    )

    # 第3步：生成用户文档
    workflow.add_task(
        model="claude",
        task="generate_user_docs",
        file_path=file_path,
        target_audience="developers"
    )

    # 第4步：生成代码示例
    workflow.add_task(
        model="claude",
        task="generate_examples",
        file_path=file_path,
        num_examples=5
    )

    # 第5步：生成README
    workflow.add_task(
        model="claude",
        task="generate_readme",
        file_path=file_path,
        include_examples=True
    )

    results = workflow.execute()
    return results


# ============================================================================
# 案例8: Bug修复工作流
# ============================================================================

def bug_fix_workflow(bug_report: str, file_path: str):
    """Bug修复工作流：从bug报告到修复验证"""

    manager = WorkflowManager(
        claude_api_key="your-claude-api-key",
        openai_api_key="your-openai-api-key"
    )

    workflow = manager.create_workflow("bug_fix")

    # 第1步：分析bug报告
    workflow.add_task(
        model="claude",
        task="analyze_bug",
        file_path=file_path,
        bug_report=bug_report,
        priority=TaskPriority.HIGH
    )

    # 第2步：定位问题代码
    workflow.add_task(
        model="openai",
        task="locate_issue",
        file_path=file_path,
        bug_report=bug_report
    )

    # 第3步：生成修复方案
    workflow.add_task(
        model="claude",
        task="generate_fix",
        file_path=file_path,
        bug_report=bug_report
    )

    # 第4步：应用修复
    workflow.add_task(
        model="openai",
        task="apply_fix",
        file_path=file_path,
        bug_report=bug_report
    )

    # 第5步：验证修复
    workflow.add_task(
        model="claude",
        task="verify_fix",
        file_path=file_path,
        bug_report=bug_report
    )

    # 第6步：运行测试
    workflow.add_task(
        model="openai",
        task="run_tests",
        file_path=file_path,
        bug_report=bug_report
    )

    results = workflow.execute()
    return results


if __name__ == "__main__":
    print("高级使用案例示例")
    print("=" * 50)

    # 示例：自动化代码审查
    print("\n示例1: 自动化代码审查")
    print("-" * 50)
    # results = multi_stage_code_review("src/main.py")
    # print(f"审查完成: {len(results['tasks'])} 个子任务")

    # 示例：渐进式重构
    print("\n示例2: 渐进式重构")
    print("-" * 50)
    # results = progressive_refactor("src/legacy_code.py")
    # print(f"重构完成: {results['success']}")

    # 示例：自动化测试生成
    print("\n示例3: 自动化测试生成")
    print("-" * 50)
    # results = automated_test_generation("src/calculator.py")
    # print(f"测试生成完成: {len(results['test_cases'])} 个测试用例")

    # 示例：Bug修复工作流
    print("\n示例4: Bug修复工作流")
    print("-" * 50)
    # bug_report = "Memory leak in the data processing function"
    # results = bug_fix_workflow(bug_report, "src/data_processor.py")
    # print(f"Bug修复完成: {results['success']}")

    print("\n所有示例已准备就绪，取消注释代码以运行")
