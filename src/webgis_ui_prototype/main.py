#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from pathlib import Path

from webgis_ui_prototype.crew import WebgisUiPrototype

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run():
    with open("inputs/project_plan.txt", "r", encoding="utf-8") as f:
        project_plan = f.read()

    with open("inputs/frontend_generation_constraints.md", "r", encoding="utf-8") as f:
        frontend_constraints = f.read()

    reference_image_path = "inputs/ui_reference.png"
    has_reference_image = Path(reference_image_path).exists()

    inputs = {
        "project_plan": project_plan,
        "frontend_constraints": frontend_constraints,
        "reference_image_path": reference_image_path if has_reference_image else "用户未提供参考图片",
        "has_reference_image": str(has_reference_image),
        "project_plan_path": "inputs/project_plan.txt",
        "current_year": str(datetime.now().year),
    }

    try:
        WebgisUiPrototype().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"运行 Crew 时发生错误: {e}")


def train():
    inputs = {
        "project_plan_path": "inputs/project_plan.txt",
        "current_year": str(datetime.now().year),
    }

    try:
        WebgisUiPrototype().crew().train(
            n_iterations=int(sys.argv[1]),
            filename=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"训练 Crew 时发生错误: {e}")


def replay():
    try:
        WebgisUiPrototype().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"重放 Crew 时发生错误: {e}")


def test():
    inputs = {
        "project_plan_path": "inputs/project_plan.txt",
        "current_year": str(datetime.now().year),
    }

    try:
        WebgisUiPrototype().crew().test(
            n_iterations=int(sys.argv[1]),
            eval_llm=sys.argv[2],
            inputs=inputs,
        )
    except Exception as e:
        raise Exception(f"测试 Crew 时发生错误: {e}")