from pathlib import Path
from crewai.tools import BaseTool
from pydantic import BaseModel, Field


class WriteProjectFileInput(BaseModel):
    relative_path: str = Field(..., description="相对于 outputs/generated_frontend 的文件路径")
    content: str = Field(..., description="要写入文件的完整内容")


class WriteProjectFileTool(BaseTool):
    name: str = "write_project_file"
    description: str = (
        "Write a frontend project file into outputs/generated_frontend. "
        "Only files inside outputs/generated_frontend are allowed."
    )
    args_schema: type[BaseModel] = WriteProjectFileInput

    def _run(self, relative_path: str, content: str) -> str:
        base_dir = Path("outputs/generated_frontend").resolve()
        target_path = (base_dir / relative_path).resolve()

        if not str(target_path).startswith(str(base_dir)):
            raise ValueError("非法路径：禁止写入 outputs/generated_frontend 之外的目录")

        target_path.parent.mkdir(parents=True, exist_ok=True)
        target_path.write_text(content, encoding="utf-8")

        return f"文件已写入: {target_path}"