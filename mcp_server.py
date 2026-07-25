from pydantic import Field
from groq import Groq
from dotenv import load_dotenv
import os
from mcp.server.fastmcp import FastMCP
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

mcp = FastMCP ("DocumentMCP", log_level="ERROR")


#Validate startup ideas  --

@mcp.tool(
    name="Validation of Startup Idea",
    description="Performs a basic validation of a startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers")
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip()
    ]):
        raise ValueError("All fields are required.")

    prompt = f""" You are a senior startup advisor and venture capitalist.
        Evaluate the following startup idea which has been proposed to you
        keep everything concise and to the point

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Score the startup from 0 to 10 based on:
        - Market demand
        - Problem significance
        - Customer clarity
        - Scalability
        - Branding (startup name)

        Return ONLY a JSON object with these fields:

        Startup
        Idea
        Validation Score
        Strengths
        Weaknesses
        Recommendations
        Whether to proceed with the idea or not
    """


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert startup advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    try:
        result = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON.")

    return result


#Competitor Analysis --

@mcp.tool(
    name="Competitor Analysis",
    description="Analyzes the competitive landscape for a given startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers")
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip()
    ]):
        raise ValueError("All fields are required.")

    prompt = f""" You are a senior startup advisor and venture capitalist.
        Evaluate the following startup idea and check who the competitors are, properly analyse the market and give a detailed report on the competitive landscape
        also search for similar startups and provide a list of competitors existing in the market
        keep everything concise and to the point

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Score the competitiveness from low to high based on:
        - Market demand
        - Customer amount
        - Scalability

        Return ONLY a JSON object with these fields:

        Competitiveness
        Competitors
        Market Demand
        Scalability 

    """


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert startup advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    try:
        result = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON.")

    return result

#TODO: Pricing Suggestions

@mcp.tool(
    name="Pricing Suggestions",
    description="Provides pricing recommendations for a given startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers"),
    payment_model: str = Field(description="Payment model (e.g., subscription, one-time purchase, freemium)")
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip(),
        payment_model.strip()
    ]):

        raise ValueError("All fields are required.")

    prompt = f""" You are a senior startup advisor and venture capitalist.
        Evaluate the following startup idea and check who the competitors are, properly analyse the market and give a detailed report on the pricing landscapein USD and INR
        also search for similar startups and provide a list of competitors existing in the market and compare the prices with them in USD and INR
        keep everything concise and to the point

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Pricing Model preference;
        {payment_model}

        Score the pricing from low to high based on:
        - Market demand
        - Customer amount
        - Scalability

        Return ONLY a JSON object with these fields:

        Pricing (USD and INR)
        Competitors Pricing
        Recommended Payment Model
    """


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert startup advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    try:
        result = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON.")

    return result

#TODO: landing page audits

@mcp.tool(
    name="Landing Page Audit",
    description="Audits the landing page for a given startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers"),
    website_link: str = Field(description="Website link for the landing page"),
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip(),
        website_link.strip()
    ]):

        raise ValueError("All fields are required.")

    prompt = f""" You are a senior startup advisor and venture capitalist.
        Evaluate the following website or landing page as an experienced UX designer, CRO (Conversion Rate Optimization) specialist, SEO consultant, and startup advisor.

        Analyze the website thoroughly and provide a concise, actionable report covering:

        - Overall website quality and user experience
        - Clarity of the value proposition
        - Headline and messaging effectiveness
        - Visual hierarchy and layout
        - Navigation and user flow
        - Call-to-Action (CTA) placement, clarity, and effectiveness
        - Trust signals (testimonials, reviews, certifications, security badges, etc.)
        - Conversion optimization opportunities
        - Mobile responsiveness (if inferable)
        - Page readability and content quality
        - SEO fundamentals (titles, headings, keyword usage, metadata, internal linking, image alt text, etc.)
        - Website performance issues (if inferable)
        - Accessibility concerns
        - Branding consistency and professionalism

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Website Link:
        {website_link}

        Score the landing page from low to high based on:
        - Visual appeal
        - User experience
        - Conversion optimization
        - Scalability

        Return ONLY a JSON object with these fields:

        Landing Page Evaluation
        Visual Appeal
        User Experience
        Conversion Optimization
        Competitors Analysis
        Recommendations
    """


    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": "You are an expert startup advisor."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3,
        response_format={"type": "json_object"},
    )

    try:
        result = json.loads(response.choices[0].message.content)
    except json.JSONDecodeError:
        raise ValueError("LLM returned invalid JSON.")

    return result

#TODO: SEO keyword research
#TODO: investor readiness
#TODO: estimate TAM/SAM/SOM
#TODO: generate customer personas

if __name__ == "__main__":
    mcp.run(transport="stdio")