
import streamlit as st

st.set_page_config(page_title="LumelaWeb Tier Picker", layout="centered")

# --- Custom CSS ---
st.markdown(
    """
    <style>
        div[data-baseweb="radio"] > div {
            gap: 0.75rem;
        }
        input[type="radio"]:checked + div > div {
            background-color: #105489 !important;
            border-color: #105489 !important;
        }
        [data-baseweb="radio"] label span {
            font-size: 1rem;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("✨ LumelaWeb Tier Picker Quiz")
st.subheader("Find your perfect Website Blueprint tier in 60 seconds.")
st.markdown("Answer a few quick questions and we’ll match you with the best package for where you are in business.")

# --- Questions ---
score = {"Tier 1": 0, "Tier 2": 0, "Tier 3": 0}

q1 = st.radio("1. Where are you in your business journey?", [
    "Just starting or launching something new",
    "I have a website but it’s not really working",
    "I’m growing fast and need systems to keep up"
])
if "starting" in q1:
    score["Tier 1"] += 1
elif "not really working" in q1:
    score["Tier 2"] += 1
else:
    score["Tier 3"] += 1

q2 = st.radio("2. What’s your biggest priority right now?", [
    "Getting a clean, professional site live",
    "Improving performance + making the site work harder",
    "Scaling my business with automation and better systems"
])
if "clean" in q2:
    score["Tier 1"] += 1
elif "performance" in q2:
    score["Tier 2"] += 1
else:
    score["Tier 3"] += 1

q3 = st.radio("3. Do you currently have a CRM, lead magnet, or email marketing?", [
    "Not yet",
    "Some—but it’s disorganized",
    "Yes—but I want it all integrated"
])
if "Not yet" in q3:
    score["Tier 1"] += 1
elif "disorganized" in q3:
    score["Tier 2"] += 1
else:
    score["Tier 3"] += 1

q4 = st.radio("4. What kind of support are you looking for?", [
    "Just need help getting launched",
    "Strategy + guidance post-launch",
    "A partner to walk with me through growth + optimization"
])
if "launched" in q4:
    score["Tier 1"] += 1
elif "guidance" in q4:
    score["Tier 2"] += 1
else:
    score["Tier 3"] += 1

# --- Recommendation Logic ---
if st.button("🔍 Show My Result"):
    best_fit = max(score, key=score.get)

    st.success(f"🎯 Your Recommended Tier: {best_fit}")

    if best_fit == "Tier 1":
        st.markdown("""
        **🪴 Tier 1: Foundation**  
        For new businesses or first-time founders. Launch a clean, strategic site with confidence.

        - Messaging & branding starter kit  
        - Copy for 4 pages  
        - Booking or email integration  
        - SEO-ready WordPress site  
        💸 *Starting at $2,000*  
        ⏳ *2–3 week build*
        """)
    elif best_fit == "Tier 2":
        st.markdown("""
        **🔧 Tier 2: Fix & Focus**  
        Already have a site? Let’s redesign it with better strategy and tools to grow your leads.

        - Includes everything in Tier 1  
        - Website audit + refined messaging  
        - AI lead magnet + email sequence  
        - Booking, CRM or donation tools  
        💸 *Starting at $4,500*  
        ⏳ *4–6 week build*
        """)
    else:
        st.markdown("""
        **🚀 Tier 3: Fuel & Scale**  
        You’re scaling—let’s add automation, a CRM, and AI tools that support your growth.

        - Everything in Tier 2  
        - Funnel & dashboard setup  
        - Client onboarding system + CRM  
        - 90-day post-launch support  
        💸 *$5,500 or 3 x $2,000*  
        ⏳ *6-week build + optimization*
        """)

    # Action Buttons
    st.markdown("### 📎 Next Steps")
    st.markdown("[🌐 Explore All Tiers](https://lumelaweb.com/services/)")
    st.markdown("[📅 Book a Free Strategy Call](https://calendly.com/lumelaweb/30min)")
