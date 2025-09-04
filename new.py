from flask import Flask, render_template, request, jsonify
import io
import contextlib
import webbrowser as _webbrowser
import webbrowser


app = Flask(__name__)  

# =========================
# LINKS 
# =========================
samta_foundation_url = "https://www.samtafoundation.org"
facebook_url = "https://www.facebook.com/Samta-Foundation-157548568218711/"
instagram_url = "https://www.instagram.com/samta_foundation/"
twitter_url = "https://twitter.com/samta_fdn"
linkedin_url = "https://www.linkedin.com/company/72699630"
youtube_url = "https://youtube.com/@samtafoundation813"
upi_url = "https://samtafoundation.org/contact/"

# =========================
# YOUR ORIGINAL FUNCTION DEFINITIONS
# =========================

#Code of "Courses" Below
def courses(text):

    if any(word in text for word in ["duration", "length", "time required", "how long", "course length","time","timing"]):
        print("SamtaSaathi: Most of our courses last between 3 to 4 Months depending on the subject. You can also learn at your own pace.")

    elif any(word in text for word in ["fee","fees", "cost", "price", "charge"]):
        print("SamtaSaathi: Our All Courses Are Mostly 300rs Only.")

    elif any(word in text for word in ["age","requirement"]):
        print("SamtaSaathi: > - Minimum age: 10 years or 5th grade")
    
    elif any(word in text for word in ["online", "offline", "class mode", "attend", "mode", "from home", "physical class"]):
        print("SamtaSaathi: We offer both online and offline classes. You can attend from home or visit our local training centers depending on availability.\n")

    elif any(word in text for word in["certificate"]):
        print("SamtaSaathi: Yes, you will receive a course completion certificate after successfully completing the course.")
    
    elif any(word in text for word in ["exam", "exams", "test", "paper", "assessment"]):
        print("SamtaSaathi: Exams are usually conducted at the end of the course. You’ll be informed about the schedule via email or WhatsApp. Let us know if you want help registering.")

    elif any(word in text for word in["programming language","1","power","power point","point","word","excel","outlook","c language","c ","python","java","html","programming", "accounting", "electronic","electronics","robotics","robotic","robot","ms","office","ms office","basic","computer","tally","tailoring","dress","designing"]):
        programming_lang(text)

    elif any(word in text for word in ["admission", "enroll", "registration", "join", "apply", "register"]):
        print("SamtaSaathi: You can join easily by filling out the admission form online or visiting one of our centers.\n" \
        "> - Minimum age: 10 years or 5th grade")
        
    elif any(word in text for word in ["course","courses"]):
        print("SamtaSaathi: ---> We Provide Various Courses : ")
        print("1) Programming Languages")
        print("2) Electronics & Robotics")
        print("3) MS OFFICE")
        print("4) Tally")
        print("5) Basic Computer")
        print("6) Tailoring & Dress Designing")
    

    else :
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")

def programming_lang(text):

    if any(word in text for word in["c language","c ","python","java","html","programming"]):
        print("SamtaSaathi: ---> In Programming Languages We Teach : ")
        print("\n> C,C++ and C# \n> Python \n> Java \n> HTML\n ")

    elif any(word in text for word in ["electronic","electronics","robotics","robotic","robot"]):
        print("SamtaSaathi: ---> In Electronics & Robotics We Teach :")
        print("\n> Basic Robotics \n> Adv Robotics \n> Arduino IDE \n> Basic Electronics")

    elif any(word in text for word in["ms","office","ms office","power","power point","point","word","excel","outlook"]):
        print("\nSamtaSaathi: ---> In MS OFFICE We Teach : ")
        print("\n> Power Point \n> Word \n> Excel \n> Outlook")

    elif any(word in text for word in["basic","computer","basic computer"]):
        print("\nSamtaSaathi: ---> In Basic Computer We Teach : ")
        print("\n> Paint \n> Notepad \n> Typing \n> About Computer")

    elif 'tally' in text or 'accounting' in text:
        print("\nSamtaSaathi: --->In Tally We Teach : ")
        print("\n> Accounting and Managment")

    elif any(word in text for word in["tailoring","dress","designing"]):
        print("\nSamtaSaathi: ---> In Tailoring & Dress Designing We Teach : ")
        print("\n> Basic Tailoring \n> Dress Designing \n> Fashion Designing \n")

    elif 'course' in text or 'courses' in text :
        courses(text)

    else :
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
#End of "Courses" Code 

# Code of "Risod" Below
def risod(text):
    if any(word in text for word in ["about","masti"]):
        print("\nAbout Risod Institute (MASTI):")
        print("The Mannalal Agrawal Skill & Technical Institute, started in 2018 by Samta Foundation, provides free or low-cost vocational training in rural areas.\n" \
        "It offers courses like computers, robotics, AI/ML, web development, Tally, IoT, and more, with modern labs and facilities to empower students with technical skills.")

    elif any(word in text for word in ["contact"]):
        contact(text)

    elif any(word in text for word in ["address","where is risod institute","where is"]):
        print("> Samta Foundation Institute – Risod")
        print("Location: Risod (44506), Maharashtra, India\n")

    elif any(word in text for word in ["institute", "samta institute", "samta foundation institute", "college", "center", "campus"]):
        print("Samta Foundation Institute – Risod\n"
            "The Samta Foundation Institute located in Risod, Maharashtra, is an educational and training center established by the Samta Foundation.\n"
            "It aims to provide skill development, digital education, and empowerment opportunities to youth in rural areas.\n"
            "The institute focuses on practical learning, community upliftment, and creating pathways to employment through quality training and awareness programs.")

    else :
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
# End of "Risod" Code

# Code of "Foundation" Below
def foundation(text):
    
    if any(word in text for word in ["founder", "who started", "who founded", "purushottam", "agrawal", "about founder"]):
        print("\nSamtaSaathi: The Samta Foundation was founded by **Shri Purushottam Agrawal**, a visionary dedicated "
            "to uplifting underprivileged communities.")
        print("He is a respected social worker and entrepreneur, known for his deep commitment to equality and education.")
        print("Through his leadership and compassion, Samta Foundation has grown into a trusted NGO "
            "working in education, women's empowerment, digital literacy, and community welfare.")
    
    elif any(phrase in text for phrase in ["where is samta foundation", "samta foundation location", "address of samta foundation", "samta foundation situated", "samta foundation located"]):
        print ("Samta Foundation is headquartered in Risod, Maharashtra, India.\n"
            "It serves surrounding rural and urban communities through various educational, social, and empowerment programs.")

    elif any(word in text for word in ["purpose", "mission", "organization","tell me about samta foundation","about samta foundation","about foundation"]):
        print("\nSamtaSaathi: Samta Foundation is a non-profit organization committed to promoting equality, education, and empowerment—")
        print("especially for underprivileged communities. We strive to create opportunities, raise awareness, and support individuals.")
        print("---> Our Core Focus Areas:\n"
            "> Bridging the Education Gap\n"
            "> Skill Development & Training\n"
            "> Empowerment of Women & Minorities\n"
            "> Building a Fair and Inclusive Society\n"
            "> Promoting Digital Awareness & Literacy")
        
    elif any(word in text for word in ["establish", "established", "founded"]):
        print("\nSamtaSaathi: Samta Foundation was established with the goal of empowering underprivileged communities through education and equality.")
        print("It was founded by Shri Purushottam Agrawal, a visionary who dedicated his efforts to social upliftment and equal opportunity for all.")

    elif any(word in text for word in ["branch","branches","location","address","where"]):
        print("Samta Foundation – Branches, Locations & Institute:\n")
        print("> Mumbai (Head Office): Level 7, Gala Impecca, Andheri-Kurla Road, Andheri East, Mumbai.\n")
        print("> Aurangabad (Branch): Office in Aurangabad, Maharashtra.\n")
        print("> Samta Institute : (Risod, Maharashtra)\n")

    elif any(word in text for word in["samta"]):
        samta(text)

    elif any(word in text for word in["course","courses"]):
        courses(text)
    
    elif any(word in text for word in["location","address"]):
        location(text)

    elif any(word in text for word in["group"]):
        group(text)

    elif any(word in text for word in ["institute", "mode", "samta institute","samta foundation institute", "college", "center", "campus","risod","masti","conatact","address","history","establishment","establish","when started","how started","institute history","team", "faculty", "teachers", "staff","risod team", "team risod","trainer","people","environment", "labs", "infrastructure", "institute", "facilities", "training center", "training institute"]):
        institute(text)

    elif any(word in text for word in ["story","history"]):
        print("\nSamtaSaathi: ---> Our Story\n")
        print("Samta Foundation was established with a vision to create an inclusive and " \
        "empowered society.\nWhat began as a small group of passionate individuals has grown " \
        "into a dedicated organization working towards education,\ncommunity welfare, health, and arts. " \
        "Through innovative programs and grassroots efforts,\nwe continue to bring positive change to " \
        "lives across India.\n")

    else : 
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
# End of "Foundation" Code

# Code of "Samta Group" Below
def group(text):

    if any(word in text for word in ["who runs samta group", "owner of samta group", "head of samta group","founder"]):
        print("The Samta Group was founded by Shri Purushottam Agrawal, "
            "a visionary entrepreneur and social worker committed to education, equality, and community welfare.")

    elif any(word in text for word in ["who runs samta group", "owner of samta group", "head of samta group"]):
        print("SamtaSaathi: Samta Group is led by **Purushottam Agrawal**, the visionary founder of the Samta ecosystem.")
        print("He guides both the social and business wings with a mission to uplift and empower communities.\n")

    elif any(word in text for word in ["location of samta group", "where is samta group", "head office of samta group"]):
        print("SamtaSaathi: Samta Group operates across India and Uganda, with major activities based in Maharashtra and Mumbai.")
        print("The exact head office location may vary depending on the business vertical.\n")
    
    elif any(word in text for word in ["what is samta group", "about samta group", "samta business", "samta ventures", "samta group"]):
        print("SamtaSathi : Samta Group is a multinational Indian conglomerate founded by Shri Purushottam Agrawal.\n" \
        "Headquartered in Mumbai, the group is built on the principles of sustainability, innovation, and social responsibility.")
        print("It operates across 4 major business sectors and also runs the Samta Foundation,\n" \
        "a large-scale NGO working in rural and tribal Maharashtra.")

        print("\nKey Business Verticals of Samta Group :\n")
        print("1. Mines & Minerals \n" \
        "→ Company: Samta Mines & Minerals Ltd.\n" \
        "→ Operations in India, Congo, Uganda, Morocco\n" \
        "→ CEO & Head of Operations: Vinod Wagh\n" \
        "→ Board Chairman of Samta Group: Purushottam Agrawal\n")
        print("2. Renewable Energy\n" \
        "→ Company: Samta Energy Pvt. Ltd.\n" \
        "→ Focus on solar and green energy solutions\n" \
        "→ Board Chairman of Samta Group: Purushottam Agrawal\n")
        print("3. Biotechnology\n" \
        "→ Companies: Gencrest Pvt. Ltd., QuantumZyme, PhylloZyme\n" \
        "→ Specializing in enzyme engineering and sustainable biotech\n" \
        "→ CEO (Gencrest & Biotech vertical): Vinay Gupta\n" \
        "→ Board Chairman of Samta Group: Purushottam Agrawal\n")
        print("4. Fintech\n" \
        "→ Company: Infinichains (based in the USA)\n" \
        "→ Works in digital finance and supply chain solutions\n" \
        "→ Managing Director (Samta Group) : Ravi Agrawal\n" \
        "→ Board Chairman of Samta Group: Purushottam Agrawal\n")

    elif any(word in text for word in["samta"]):
        samta(text)

    else :
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
# End of "Samta Group" Code

# *Samta* Code Below
def samta(text):
    if any(word in text for word in ["why named", "name", "named after", "his wife", "her name"]):
        print("SamtaSaathi: The name 'Samta' carries both personal and symbolic meaning.")
        print("It represents the Hindi word for 'equality', aligning with the foundation's mission.")
        print("Additionally, it is a heartfelt tribute to the founder's wife, whose name was Samta.")
        print("Her values and support deeply influenced the organization's purpose and spirit.")

    
    elif any(word in text for word in ["who was samta", "about samta", "samta person", "samta lady"]):
        print("About Samta:\n"
            "Samta was the beloved wife of Shri Purushottam Agrawal, the founder of Samta Foundation. "
            "She was known for her kindness, compassion, and dedication to helping others. "
            "In her honor, the foundation was named 'Samta Foundation', symbolizing her values of equality, care, and service to the community.")


    elif any(word in text for word in ["reason", "why started", "why it was started", "motive", "vision"]):
        print("SamtaSaathi: The foundation was started to address the social inequality in education and opportunity.")
        print("The vision was to bridge the digital divide, uplift rural talent, and create a just society through skill-building and awareness.")

    elif any(word in text for word in["story "]):
        print("SamtaSaathi: ---> Our Story\n")
        print("Samta Foundation was established with a vision to create an inclusive and " \
        "empowered society.\nWhat began as a small group of passionate individuals has grown " \
        "into a dedicated organization working towards education,\ncommunity welfare, health, and arts. " \
        "Through innovative programs and grassroots efforts,\nwe continue to bring positive change to " \
        "lives across India.\n")
# End of "Samta" Code    

# Code of "Instiute" Below
def institute(text):
    
    if any(word in text for word in["history","establishment","establish","when started","how started","institute history"]):
        print("History & Establishment of Samta Institute\n"
            "The Samta Foundation Institute was established with a vision to uplift rural communities through quality education and skills training.\n"
            "It was founded by Purushottam Agrawal, driven by the belief that every student, regardless of their background, deserves access to practical and digital education.\n\n"
            "Since its inception, the institute has focused on creating equal opportunities by offering various development programs tailored for youth and women.")
    
    elif any(word in text for word in ["team", "faculty", "teachers", "staff","risod team", "team risod","trainer","people"]):
        print("SamtaSaathi: Risod Team Members:\n\n> - Ravindra Garje: Principal\n"
        "> - Amol Kalmbe: Vice Principal\n> - Aditya Ukhalkar: Admin\n> - Prakash Khilare: Marketing Officer\n---\n"
        "> - Mayur Aher: AI & ML Trainer\n> - Karan Giri: C/C++ Trainer\n        > - Rushup Sirnaik: Robotics Trainer\n> - Avinash Kamble: Robotics Trainer\n"
        "> - Abhishek Nirban: Tally Trainer\n> - Sanika Deshmukh: Basic Computer Teacher")

    elif any(word in text for word in ["environment", "labs", "infrastructure", "facilities", "training center", "training institute"]):
        print("SamtaSaathi: The Risod Institute provides: \n> - Comfortable AC environment\n"
        "> - 80+ Windows computers\n> - 3+ Dedicated labs\n> - Fire safety protocols\n"
        "> - Meditation Hall (Sundays)\n> - Robotics competition practice hub\n> - Class strength: 5 to 25 students")
    
    elif any(word in text for word in["risod","conatact","address","masti"]):
        risod(text)

    elif any(word in text for word in["course","courses"]):
        courses(text)

    elif any(word in text for word in ["founder","who", "who started", "who founded", "purushottam", "agrawal", "about founder","samta", "foundation", "purpose", "mission", "organization","establish", "established", "founded","branch","branches","location","address","where","story","history"]):
        foundation(text)
    
    elif any(word in text for word in["samta"]):
        samta(text)

    else :
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
# End of "Institue" Code

# *Location* Code Below
def location(text):
    if any(word in text for word in ["location","locations","address","located","where is your office", "what is the address"]):
        print("SamtaSaathi: ---> LOCATIONS : \n")
        print("Risod - 444506 (At, Mannalal Agrawal - Training Institute, Nizampur, Risod)")
        print("Mumbai - 400001 (7th Floor, Gala Impecca, Andheri Kurla Road, Andheri East, Mumbai)")
        print("Sambhaji Nagar - 431001 ( Gangotri, Plot No.3-4, N-5, Cidco,Chh. Sambhajinagar)\n")
# End of *Location* Code

# *Social Media* Code Below
def social(text):
    if any(word in text for word in ["open facebook"]):
        webbrowser.open(facebook_url)   

    elif any(word in text for word in ["open instagram"]):
        webbrowser.open(instagram_url) 

    elif any(word in text for word in ["open twitter"]):
        webbrowser.open(twitter_url)   
    
    elif any(word in text for word in ["open linked","open linked in"]):
        webbrowser.open(linkedin_url)   
    
    elif any(word in text for word in ["open youtube"]):
        webbrowser.open(youtube_url)   

    elif any(word in text for word in ["social", "media", "connect", "follow", "platforms", "instagram", "twitter", "facebook", "linkedin"]):
        print("SamtaSaathi: ---> SOCIAL MEDIA : \n")
        print("Instagram")
        print("Twitter")
        print("Facebook")
        print("Linked In\n")
        print("Type 'open <platform>'") 
# End of *Social Media* Code

# *Contact* Code Below
def contact(text):
    if any(word in text for word in ["contact","contacts","call","email","gmail","phone","reach","get in touch","whatsapp"]):
        print("SamtaSaathi: ---> CONTACT US : \n")
        print("Phone no : +91 22 69693200")
        print("Phone no : +91 8181814884")
        print("Email us : Samta@samtafoundation.org\n")
# End of *Contact* Code

# "Donate" Code Below
def donate(text):
    if  any(word in text for word in ["donate", "support", "contribute", "funds", "financial", "donate computers", "donate laptops", "donate clothes", "donate money", "donate goods"]):
        print("\nSamtaSaathi: ---> DONATE & SUPPORT : \n")
        print("# Your contribution can empower lives and bring real change to underserved communities.\n" \
        "  Every donation supports: \n")
        print("> Education for rural children\n> Skill development for youth and women\n> Health and hygiene drives in villages\n> Creative programs like Art & Masti for kids\n")
        print("# Ways You Can Support: \n")
        print("> Monetary Donation (UPI, Bank Transfer, Paytm, etc.)\n> Sponsor a Workshop or Student\n> Donate Goods – Books, clothes, laptops, sewing machines, etc.\n> Corporate Partnerships for CSR collaboration\n")
        print("TO DONATE : \n1) UPI & QR \n2) Netbanking \n3) Credit Card & Debit Card\n")
    
    elif any(word in text for word in["upi","qr","netbanking","credit","debit"]):
        print("\nSamtaSaathi: Loading Link......\n")
        webbrowser.open(upi_url)

    elif any(word in text for word in["receipt","certificate","donation"]):
        print("\nSamtaSaathi: YES, Samta Foundation provides an official receipt and donation certificate when you : \n> Donate.\n> Complete Course\n> Participate in Events\n")

    else : 
        print("SamtaSaathi: I'm here to help! Could you please clarify your query?")
# End of "Donate" Code

def show_help():
    print("\nSamtaSaathi Help — things I can do (ask in simple words):\n")
    print("Courses & Study:")
    print(" - List courses (e.g. 'courses', 'what courses')")
    print(" - Duration / timing (e.g. 'duration', 'how long')")
    print(" - Fees (e.g. 'fees', 'price')")
    print(" - Age / eligibility (e.g. 'age requirement')")
    print(" - Admission / register (e.g. 'admission', 'register')")
    print(" - Online / offline classes (e.g. 'online', 'offline')")
    print(" - Certificates & exams (e.g. 'certificate', 'exam')\n")

    print("Risod Institute:")
    print(" - General info (e.g. 'risod', 'institute')")
    print(" - Address (e.g. 'where is risod', 'risod address')")
    print(" - History & establishment (e.g. 'history', 'established')")
    print(" - Facilities & environment (e.g. 'labs', 'facilities')\n")

    print("Samta Foundation & Group:")
    print(" - Founder info (e.g. 'founder', 'who started')")
    print(" - Mission / purpose / story (e.g. 'purpose', 'mission', 'story')")
    print(" - Branches & locations (e.g. 'branches', 'locations')")
    print(" - Samta Group / business info (e.g. 'samta group', 'ventures')\n")

    print("Donations & Volunteering:")
    print(" - How to donate (e.g. 'donate', 'upi', 'netbanking')")
    print(" - Donation receipt (e.g. 'receipt', 'certificate')")
    print(" - Volunteer (e.g. 'volunteer', 'join')\n")

    print("Contact & Social:")
    print(" - Phone / email / WhatsApp (e.g. 'contact', 'phone', 'email')")
    print(" - Open website (e.g. 'site')")
    print(" - Open social pages (e.g. 'open facebook', 'open instagram')\n")

    print("General:")
    print(" - Greetings (e.g. 'hi', 'hello')")
    print(" - Ask for help (e.g. 'help', 'assist')")
    print(" - Exit (type 'exit' or 'quit')\n")

def main():
    print("Namaste! I'm SamtaSaathi 😊 How can I assist you today? (type 'exit' to quit & 'help' for help)")
    while True:
        text = input("\nYOU: ").strip().lower()
        print("") # JUST A BLANK SPACE FOR A SPACE IN CHAT >>>
        
        if text in ["exit", "quit"]:
            print("SamtaSaathi: Thank you for visiting Samta Foundation. Have a great day!")
            break

        # Custom replies
        if "who are you" in text or "what is your name" in text:
            print("SamtaSaathi: I am SamtaSaathi, your virtual assistant for Samta Foundation!")
            continue

        elif text.startswith(("my name is", "myself", "im", "i am")):
            for x in ["my name is", "myself", "im", "i am"]:
                if text.startswith(x):
                    name = text[len(x):].strip().title()
                    print(f"SamtaSaathi: Nice to meet you, {name}! How can I help you today?")
                    break
            continue

        elif any(phrase in text for phrase in ["how you can help","how can you help","what can you do"]):
            print("SamtaSaathi: I can provide information about our courses, branches, admission process, donation options, and more. Just ask!")
            continue

        # Hierarchical intent handling
        if any(word in text for word in ["courses","mode", "age","requirement","course","duration", "length", "time required", "how long", "course length","time","timing","admission", "enroll", "registration", "join", "apply", "register","fee","fees", "cost", "price", "charge","online", "offline", "class mode", "attend", "from home", "physical class","certificate","exam", "exams", "test", "paper", "assessment","accounting"]):
            courses(text)

        elif any(word in text for word in ["group","what is samta group", "about samta group", "samta business", "samta ventures", "samta group","who runs samta group", "owner of samta group", "head of samta group","location of samta group", "where is samta group", "head office of samta group"]):
            group(text)

        elif any(word in text for word in ["institute", "mode", "samta institute", "college", "center", "campus","risod","where is risod institute","where is","masti","conatact","address","history","establishment","establish","when started","how started","institute history","team", "faculty", "teachers", "staff","risod team", "team risod","trainer","people","environment", "labs", "infrastructure", "institute", "facilities", "training center", "training institute"]):
            institute(text)

        elif any(word in text for word in ["who was samta", "about samta", "samta person", "samta lady","founder","who", "who started", "who founded", "purushottam", "agrawal", "about founder","samta", "foundation", "purpose", "mission", "organization","establish", "established", "founded","branch","branches","where is samta foundation", "samta foundation location", "address of samta foundation", "samta foundation situated", "samta foundation located","location","address","where","story","history"]):
            foundation(text)

        elif any(word in text for word in ["power","power point","point","word","excel","outlook","c language","c ","python","java","html","programming", "accounting","electronic","electronics","robotics","robotic","robot","ms","office","ms office","basic","computer","basic computer","tally","tailoring","dress","designing"]):
            programming_lang(text)

        elif any(word in text for word in ["location","address","where"]):
            location(text)

        elif any(word in text for word in ["social","facebook","instagram","twitter","linkedin","youtube"]):
            social(text)

        elif any(word in text for word in ["contact","call","email","whatsapp"]):
            contact(text)

        elif any(word in text for word in ["donate", "support", "contribute", "funds", "financial", "donate computers", "donate laptops", "donate clothes", "donate money", "donate goods","upi","qr","netbanking","credit","debit","receipt","certificate","donation"]):
            donate(text)

        elif "more help" in text or "help more" in text :
            show_help()

        elif "help" in text or "what can you do" in text:
            print("SamtaSaathi — I can help with:")
            print("- Courses (duration, fees, admission)")
            print("- Institute & locations (Risod)")
            print("- Founder & foundation info")
            print("- Donate / Volunteer")
            print("- Contact & social links")
            print("Type 'more help' for more options")
            print("Type 'exit' to quit.\n")
        
        else:
            print("SamtaSaathi: I'm here to help! Could you please clarify your query?")

# =========================
# HELPER UTILS
# =========================
def capture_printed_output(func, *args, **kwargs):
    buf = io.StringIO()
    original_open = _webbrowser.open
    try:
        _webbrowser.open = lambda url, *a, **k: print(f"[OPEN LINK] {url}")
        with contextlib.redirect_stdout(buf):
            func(*args, **kwargs)
    finally:
        _webbrowser.open = original_open
    return buf.getvalue().strip()

def matches_any(text, words):
    txt = text.lower()
    return any(w in txt for w in words)

# =========================
# REAL process_text_and_capture
# =========================
def process_text_and_capture(text):
    """Runs your original routing logic and returns list of reply lines."""
    t = (text or "").strip().lower()
    if not t:
        return ["Please type something."]
    if t in ["exit", "quit"]:
        return ["SamtaSaathi: Thank you for visiting Samta Foundation. Have a great day!", "__exit__"]

    if "who are you" in t or "what is your name" in t:
        return ["SamtaSaathi: I am SamtaSaathi, your virtual assistant for Samta Foundation!"]

    prefixes = ("my name is", "myself", "im", "i am")
    for p in prefixes:
        if t.startswith(p):
            name = text[len(p):].strip().title()
            if name:
                return [f"SamtaSaathi: Nice to meet you, {name}! How can I help you today?"]
            else:
                return ["SamtaSaathi: Nice to meet you! How can I help you today?"]
    
    # in process_text_and_capture()
    if matches_any(t, ["facebook", "instagram", "twitter", "linkedin", "youtube","upi"]):
        if "facebook" in t:
            return ["__openlink__", facebook_url]
        elif "instagram" in t:
            return ["__openlink__", instagram_url]
        elif "twitter" in t:
            return ["__openlink__", twitter_url]
        elif "linkedin" in t:
            return ["__openlink__", linkedin_url]
        elif "youtube" in t:
            return ["__openlink__", youtube_url]
        elif "upi" in t:
            return ["__openlink__", upi_url]

    if matches_any(t, ["social", "media", "connect", "follow", "platforms"]):
        out = capture_printed_output(social, text)
        return out.splitlines()


    # --- ROUTING ---
    if matches_any(t, ["courses","mode","age","requirement","course","duration","length","time required","how long","course length","time","timing","admission","enroll","registration","join","apply","register","fee","fees","cost","price","charge","online","offline","class mode","attend","from home","physical class","certificate","exam","exams","test","paper","assessment","accounting"]):
        out = capture_printed_output(courses, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["group","what is samta group","about samta group","samta business","samta ventures","samta group","who runs samta group","owner of samta group","head of samta group","location of samta group","where is samta group","head office of samta group"]):
        out = capture_printed_output(group, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["institute","mode","samta institute","college","center","campus","risod","where is risod institute","where is","masti","conatact","address","history","establishment","establish","when started","how started","institute history","team","faculty","teachers","staff","risod team","team risod","trainer","people","environment","labs","infrastructure","institute","facilities","training center","training institute"]):
        out = capture_printed_output(institute, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["who was samta","about samta","tell me about samta foundation","about samta foundation","about foundation","samta person","samta lady","founder","who","who started","who founded","purushottam","agrawal","about founder","samta","foundation","purpose","mission","organization","establish","established","founded","branch","branches","where is samta foundation","samta foundation location","address of samta foundation","samta foundation situated","samta foundation located","location","address","where","story","history"]):
        out = capture_printed_output(foundation, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["power","power point","point","word","excel","outlook","c language","c ","python","java","html","programming","accounting","electronic","electronics","robotics","robotic","robot","ms","office","ms office","basic","computer","basic computer","tally","tailoring","dress","designing"]):
        out = capture_printed_output(programming_lang, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["location","address","where"]):
        out = capture_printed_output(location, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["social","facebook","instagram","twitter","linkedin","youtube"]):
        out = capture_printed_output(social, text)
        return out.splitlines() if out else ["[ACTION] Open social links"]

    if matches_any(t, ["contact","call","email","whatsapp"]):
        out = capture_printed_output(contact, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if matches_any(t, ["donate","support","contribute","funds","financial","donate computers","donate laptops","donate clothes","donate money","donate goods","upi","qr","netbanking","credit","debit","receipt","certificate","donation"]):
        out = capture_printed_output(donate, text)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if "more help" in t or "help more" in t:
        out = capture_printed_output(show_help)
        return out.splitlines() if out else ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

    if "help" in t or "what can you do" in t:
        return [
            "SamtaSaathi — I can help with:",
            "- Courses (duration, fees, admission)",
            "- Institute & locations (Risod)",
            "- Founder & foundation info",
            "- Donate / Volunteer",
            "- Contact & social links",
            "Type 'more help' for more options",
            "Type 'exit' to quit."
        ]

    return ["SamtaSaathi: I'm here to help! Could you please clarify your query?"]

# =========================
# FLASK ROUTES
# =========================
@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/start-chat")
def start_chat():
    # Define the initial message
    bot_message = "Hello! I'm SamtaSaathi. How can I assist you today?"
    return render_template("start_chat.html", initial_message=bot_message)
@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact_page():
    return render_template("contact.html")

@app.route("/help")
def help_page():
    return render_template("help.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    data = request.get_json(force=True, silent=True) or {}
    text = data.get("message") or data.get("text") or ""
    replies = process_text_and_capture(text)
    big = "\n".join([r for r in replies if r != "__exit__"]).strip().lower()
    exit_triggered = "__exit__" in replies
    return jsonify({"reply": big, "replies": replies, "exit": exit_triggered})

if __name__ == "__main__":
    print("Starting SamtaSaathi Flask server on http://127.0.0.1:5000")
    app.run(debug=True)
