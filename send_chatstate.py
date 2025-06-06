import requests
import json

def create_sample_chatstate():
    """Create a sample ChatState instance with all fields filled"""
    chatstate_data = {
        # Original attributes
        "stage": "complete",
        "original_request": "Need comprehensive market analysis for expanding our AI-powered fitness app",
        "questions": [
            "What is your primary target market?",
            "Who are your main competitors?",
            "What marketing channels are you currently using?",
            "What are your key performance indicators?"
        ],
        "answers": [
            "Health-conscious millennials aged 25-40",
            "MyFitnessPal, Strava, and Nike Training Club",
            "Social media, Google Ads, and influencer partnerships",
            "User acquisition cost, monthly active users, retention rate"
        ],
        "search_plan": "Comprehensive market research for fitness app industry",
        "search_results": [],
        "intro_methodology_plan": "Industry overview and research methodology",
        "intro_methodology_results": [],
        "industry_market_plan": "Fitness app market analysis",
        "industry_market_results": [],
        "competitor_plan": "Competitive landscape analysis",
        "competitor_results": [],
        "comparative_analysis_plan": "Feature and pricing comparison",
        "comparative_analysis_results": [],
        "strategic_analysis_plan": "Strategic recommendations and action plan",
        "strategic_analysis_results": [],
        "recommendations_action_plan_chapter": "Strategic recommendations chapter",
        "gaps_opportunities_plan": "Market gaps and opportunities identification",
        "gaps_opportunities_results": [],
        "marketing_strategic_plan": "Marketing strategy development",
        "marketing_strategic_results": [],
        "marketing_strategic_chapter": "Marketing strategy chapter",
        "emerging_trends_future_outlook_plan": "Future trends analysis",
        "emerging_trends_future_outlook_results": [],
        "emerging_trends_future_outlook_chapter": "Future outlook chapter",
        "appendix_plan": "Supporting data and references",
        "appendix_results": [],
        "appendix_chapter": "Appendix chapter",
        "discovered_competitors": [
            "Fitbit Premium",
            "Apple Fitness+",
            "Peloton Digital"
        ],
        
        # Business information
        "language": "English",
        "business": {
            "name": "FitAI Pro",
            "topic_description": "AI-powered personalized fitness and nutrition app",
            "products_services": "Mobile app with AI personal trainer, nutrition tracking, workout plans, and community features"
        },
        
        # Industry information
        "industry": {
            "primary": "Health & Fitness Technology",
            "niche": "AI-powered fitness applications",
            "secondary_industries": ["Mobile App Development", "Health Tech", "Wellness"]
        },
        
        # Geography
        "geography": {
            "country": "United States",
            "state": "California",
            "city": "San Francisco",
            "market_scope": "North America with plans for global expansion"
        },
        
        # Target audience
        "target_audience": {
            "demographics": "Ages 25-45, household income $50k+, urban/suburban, college-educated",
            "psychographics": "Health-conscious, tech-savvy, goal-oriented, busy professionals",
            "type": "B2C - Individual consumers"
        },
        
        # Customer pain points
        "customer_pain_points": [
            "Lack of personalized workout plans",
            "Difficulty staying motivated",
            "Inconsistent nutrition tracking",
            "Generic fitness advice",
            "Expensive personal trainers"
        ],
        
        # Competitor analysis goals
        "competitor_analysis_goals": {
            "objectives": [
                "Identify market positioning opportunities",
                "Analyze pricing strategies",
                "Understand feature gaps",
                "Assess marketing approaches"
            ],
            "details": "Comprehensive analysis to inform product development and go-to-market strategy"
        },
        
        # KPIs and metrics
        "kpis_metrics": [
            "Monthly Active Users (MAU)",
            "Customer Acquisition Cost (CAC)",
            "Lifetime Value (LTV)",
            "Retention Rate",
            "App Store Rating",
            "Revenue per User"
        ],
        
        # Competitors
        "competitors": {
            "direct": [
                "MyFitnessPal",
                "Strava",
                "Nike Training Club",
                "Fitbit Premium"
            ],
            "indirect": [
                "YouTube Fitness Channels",
                "Local Gyms",
                "Personal Trainers",
                "Nutrition Apps"
            ],
            "aspirational": [
                "Peloton",
                "Apple Fitness+",
                "Mirror Home Gym"
            ]
        },
        
        # Unique value proposition
        "unique_value_proposition": "AI-powered personal trainer that adapts to your fitness level, schedule, and preferences, providing personalized workouts and nutrition plans at a fraction of the cost of traditional personal training",
        
        # Marketing strategy
        "marketing_strategy": {
            "channels": {
                "seo": True,
                "social_media": True,
                "paid_ads": True,
                "email_marketing": True,
                "other": "Influencer partnerships, fitness blogger collaborations"
            },
            "what_is_working": "Instagram and TikTok content marketing, Google Ads for fitness keywords, email nurture campaigns",
            "what_is_not_working": "Facebook ads have low conversion rates, LinkedIn advertising not effective for B2C audience"
        }
    }
    
    return chatstate_data

def send_chatstate_to_render(url, chatstate_data):
    """Send ChatState data to the Render application"""
    try:
        print("Sending ChatState data to Render...")
        print(f"URL: {url}")
        print(f"Data size: {len(json.dumps(chatstate_data))} characters")
        
        response = requests.post(
            url,
            json=chatstate_data,
            headers={'Content-Type': 'application/json'},
            timeout=30  # 30 second timeout (app needs 20 seconds + processing time)
        )
        
        if response.status_code == 200:
            result = response.json()
            print("\n" + "="*50)
            print("SUCCESS! Response received:")
            print("="*50)
            print(f"Status: {result.get('status')}")
            print(f"Message: {result.get('message')}")
            print(f"Timestamp: {result.get('timestamp')}")
            print("\nSummary:")
            print(result.get('summary', 'No summary provided'))
            print("="*50)
        else:
            print(f"Error: HTTP {response.status_code}")
            print(f"Response: {response.text}")
            
    except requests.exceptions.Timeout:
        print("Request timed out - this is expected due to the 20-second delay")
    except Exception as e:
        print(f"Error sending request: {str(e)}")

if __name__ == "__main__":
    # Your Render app URL
    render_url = "https://deepresearcher-6ro6.onrender.com/chatstate"
    
    # Create sample ChatState data
    chatstate_data = create_sample_chatstate()
    
    # Send to Render
    send_chatstate_to_render(render_url, chatstate_data)
