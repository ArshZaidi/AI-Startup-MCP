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


#Validate startup ideas  -->

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


#Competitor Analysis -->

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

#Pricing Suggestions  -->

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

#Landing Page Audits  -->

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

#Suggested Features  -->

@mcp.tool(
    name="Suggested Features",
    description="Provides suggestions for features to include in a given startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers"),
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip(),
    ]):

        raise ValueError("All fields are required.")

    prompt = f"""
        You are a senior product manager, startup advisor, SaaS architect, and AI consultant.

        Analyze the following startup idea and suggest features that would maximize user value, engagement, retention, and monetization.

        Evaluate the startup from a product perspective and recommend features based on current market trends, user expectations, and competitor standards.

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Generate:

        - Core MVP features
        - Advanced/Premium features
        - AI-powered feature suggestions
        - Features that differentiate the startup from competitors
        - User engagement & retention features
        - Revenue-generating features
        - Future roadmap features
        - Technical complexity (Low/Medium/High) for each feature
        - Priority (Must Have / Nice to Have / Future)

        Return ONLY a JSON object with these fields:

        Core Features
        Premium Features
        AI Features
        Competitive Advantages
        Feature Roadmap
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

#Investor's POV  -->

@mcp.tool(
    name="Investor's POV",
    description="Provides an insight to the investor's perspective on a given startup idea."
)
def validate_startup_idea(
    name: str = Field(description="Startup name"),
    idea: str = Field(description="Startup idea"),
    potential_customers: str = Field(description="Target customers"),
):
    if not all([
        name.strip(),
        idea.strip(),
        potential_customers.strip(),
    ]):

        raise ValueError("All fields are required.")

    prompt = f"""
        You are a senior venture capitalist, startup advisor, angel investor, and business strategist.

        Evaluate the following startup from an investor's perspective.

        Analyze whether this startup would be attractive for Pre-Seed, Seed, or Series A funding.

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Evaluate based on:

        - Market Opportunity
        - Problem-Solution Fit
        - Product Differentiation
        - Competitive Advantage (Moat)
        - Scalability
        - Business Model
        - Revenue Potential
        - Customer Acquisition Potential
        - Team Requirements (if inferable)
        - Market Risks
        - Execution Risks
        - Funding Readiness

        Score the startup from low to high based on:

        - Innovation
        - Market Size
        - Scalability
        - Investment Potential
        - Risk Level

        Also provide:

        - Strengths
        - Weaknesses
        - Biggest Risks
        - Investor Concerns
        - Questions an investor would ask
        - Recommendations before raising funds

        Return ONLY a JSON object with these fields:

        Investment Score
        Funding Stage
        Strengths
        Weaknesses
        Risks
        Investor Questions
        Recommendations
        Overall Verdict
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

#Complete All-In-One Startup Report  -->

@mcp.tool(
    name="All-In-One Startup Report",
    description="Provides a comprehensive evaluation of a given startup idea."
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

    prompt = f"""
        You are a senior startup advisor, venture capitalist, product strategist, market analyst, pricing consultant, UX expert, and business consultant.

        Perform a comprehensive evaluation of the following startup.

        Startup Name:
        {name}

        Startup Idea:
        {idea}

        Target Customers:
        {potential_customers}

        Website:
        {website_link}

        Provide a concise but comprehensive report covering:

        Business Analysis
        - Startup validation
        - Problem-Solution Fit
        - Uniqueness
        - Innovation Score

        Market Research
        - Market Opportunity
        - Industry Trends
        - Target Audience
        - Growth Potential

        Competitor Analysis
        - Major Competitors
        - Competitive Advantages
        - Weaknesses Compared to Competitors

        Pricing Analysis
        - Recommended Pricing
        - Competitor Pricing
        - Freemium/Premium Suggestions

        Product Strategy
        - Core Features
        - Premium Features
        - AI Opportunities
        - Future Roadmap

        Website Audit (if website is accessible)
        - UX
        - Design
        - Navigation
        - Conversion Optimization
        - SEO
        - Branding

        Investor Perspective
        - Investment Readiness
        - Scalability
        - Risks
        - Funding Potential

        Marketing Strategy
        - Go-To-Market Strategy
        - Customer Acquisition Channels
        - SEO Opportunities
        - Social Media Strategy

        Score the startup from low to high based on:

        - Innovation
        - Market Potential
        - Product Quality
        - Business Model
        - Scalability
        - Investment Potential
        - Website Quality (if applicable)

        Finally provide:

        - Top Strengths
        - Top Weaknesses
        - Biggest Opportunities
        - Biggest Threats
        - Immediate Next Steps
        - Long-Term Recommendations

        Return ONLY a JSON object with these fields:

        Startup Validation
        Market Analysis
        Competitor Analysis
        Pricing Analysis
        Suggested Features
        Website Audit
        Investor Analysis
        Marketing Strategy
        Scores
        Recommendations
        Executive Summary
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

if __name__ == "__main__":
    mcp.run(transport="stdio")