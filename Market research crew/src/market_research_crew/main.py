
import warnings
from market_research_crew.crew import MarketResearchCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")



def run():
    """
    Run the crew.
    """
    inputs = {
        "product_idea" : "An AI powered tool that summraizes youtube videos on my channel and post the summary on various social media platforms like linkedin, intsagram, facebook , X , whatsapp "
    }

    try:
        MarketResearchCrew().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


