from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai.llm import LLM
from dotenv import load_dotenv
load_dotenv()


#defining the class for crew
@CrewBase
class ResearchAndBlogCrew():

    agents: list[BaseAgent]
    tasks: list[Task]

    # define the paths of config files

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"
    
    # ============= agents =====
    @agent
    def report_generator(self) -> Agent:
        return Agent(
            config= self.agents_config["report_generator"]
        )
    
    @agent
    def blog_writer(self) -> Agent :
        return Agent(
            config = self.agents_config["blog_writer"]
        )
    
    # +++++++++++++++++ taks ++++++++++++
    # order of task definition matters
    @task
    def report_task(self) -> Task:
        return Task(
            config = self.tasks_config["report_task"]
        )
    
    @task
    def blog_writing_task(self) -> Task:
        return Task(
            config= self.tasks_config["blog_writing_task"],
            output_file="blogs/blog.md"
        )
    
    # ================== crew ========================
    @crew
    def crew(self) ->Crew:
        return Crew(
            agents=self.agents,
            tasks= self.tasks,
            process= Process.sequential,
            verbose=True
        )