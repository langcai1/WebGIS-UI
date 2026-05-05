from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from webgis_ui_prototype.tools import WriteProjectFileTool



@CrewBase
class WebgisUiPrototype():
    """WebGIS UI 原型生成 Crew"""

    agents: list[BaseAgent]
    tasks: list[Task]

   
    @agent
    def ui_requirement_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["ui_requirement_analyst"],
            verbose=True,
        )

    @agent
    def style_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["style_analyst"],
            verbose=True,
        )

    @agent
    def layout_designer(self) -> Agent:
        return Agent(
            config=self.agents_config["layout_designer"],
            verbose=True,
        )

    @agent
    def vue_ui_generator(self) -> Agent:
         return Agent(
            config=self.agents_config["vue_ui_generator"],
            tools=[WriteProjectFileTool()],
            verbose=True,
    )

    @agent
    def ui_code_reviewer(self) -> Agent:
        return Agent(
            config=self.agents_config["ui_code_reviewer"],
            verbose=True,
        )

    @agent
    def codex_prompt_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["codex_prompt_writer"],
            verbose=True,
        )

    

    @task
    def analyze_ui_requirement_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_ui_requirement_task"],
            output_file="outputs/ui_requirement_analysis.md",
        )

    @task
    def analyze_style_task(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_style_task"],
            output_file="outputs/ui_style_analysis.md",
        )

    @task
    def design_layout_task(self) -> Task:
        return Task(
            config=self.tasks_config["design_layout_task"],
            output_file="outputs/layout_plan.md",
        )

    @task
    def generate_vue_ui_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_vue_ui_task"],
        )

    @task
    def review_generated_frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config["review_generated_frontend_task"],
            output_file="outputs/vue_ui_review_report.md",
        )

    @task
    def generate_codex_prompt_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_codex_prompt_task"],
            output_file="outputs/codex_prompts/codex_next_steps.md",
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )