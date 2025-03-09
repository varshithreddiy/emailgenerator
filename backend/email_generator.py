import random

TEMPLATES = {
    "job_application": [
        {
            "subject": "Application for {position} at {company}",
            "body": """Dear {recipient},

I hope this email finds you well. I am writing to express my strong interest in the {position} position at {company}. With a proven track record in {skills}, I am confident that my expertise and enthusiasm would make a significant contribution to your team.

Throughout my career, I have successfully led multiple projects that required {skills}. My ability to adapt to dynamic challenges, collaborate effectively with teams, and continuously improve my skills has helped me achieve meaningful results. I am particularly drawn to {company} because of its innovative work culture and commitment to excellence.

I am eager to bring my experience and dedication to your organization. I would love the opportunity to discuss my qualifications further and learn more about how I can contribute to {company}. Please let me know a convenient time for us to connect.

Looking forward to your response.

Best regards,  
{sender}
            """
        }
    ],
    "meeting_request": [
        {
            "subject": "Request for a Meeting Regarding {topic}",
            "body": """Dear {recipient},

I hope you are doing well. I am reaching out to request a meeting to discuss {topic}, as I believe it is crucial to align our strategies and ensure effective collaboration moving forward.

The purpose of this meeting is to address key concerns, share relevant updates, and explore potential solutions that will help us streamline our efforts. I would appreciate your insights on the matter and believe that a discussion would be beneficial for both of us.

Please let me know your availability, and I will do my best to accommodate your schedule. I look forward to a productive conversation.

Best regards,  
{sender}
            """
        }
    ],
    "leave_request": [
        {
            "subject": "Request for Leave on {date}",
            "body": """Dear {recipient},

I am writing to formally request leave on {date} due to {reason}. I understand the importance of maintaining a smooth workflow, and I have made necessary arrangements to ensure that my responsibilities are managed in my absence.

I have delegated urgent tasks to my colleagues and have provided them with all necessary instructions. Additionally, I am available to address any concerns before my leave begins.

I sincerely appreciate your consideration of this request and hope for your approval. Please let me know if any further information is required.

Thank you for your time and understanding.

Best regards,  
{sender}
            """
        }
    ],
    "follow_up": [
        {
            "subject": "Following Up on Our Discussion Regarding {topic}",
            "body": """Dear {recipient},

I hope you are doing well. I am writing to follow up on our recent conversation regarding {topic}. I greatly appreciate the time you took to discuss this matter, and I wanted to check if there are any updates or decisions made.

I understand that you may have a busy schedule, but I would love to continue our discussion and explore possible next steps. If there is any additional information you need from my side, please let me know, and I will be happy to provide it.

Looking forward to hearing from you soon.

Best regards,  
{sender}
            """
        }
    ],
    "thank_you": [
        {
            "subject": "Sincere Thanks for Your Support",
            "body": """Dear {recipient},

I wanted to take a moment to express my sincere gratitude for your support and guidance regarding {topic}. Your assistance has been invaluable to me, and I truly appreciate the time and effort you have dedicated.

Your advice has helped me gain new perspectives and approach challenges with greater confidence. I feel fortunate to have had the opportunity to learn from you and collaborate with you on this matter.

I look forward to staying connected and hope to work together again in the future. Once again, thank you for everything.

Best regards,  
{sender}
            """
        }
    ],
    "apology": [
        {
            "subject": "Sincere Apology for {reason}",
            "body": """Dear {recipient},

I want to extend my sincere apologies for {reason}. It was never my intention to cause any inconvenience, and I deeply regret the situation.

I acknowledge that my actions may have led to difficulties, and I take full responsibility for any misunderstanding or disruption. Please know that I am committed to making things right and ensuring that such incidents do not happen again in the future.

If there is anything I can do to address the issue or make amends, please do not hesitate to let me know. I truly value our relationship and appreciate your understanding.

Best regards,  
{sender}
            """
        }
    ],
    "introduction": [
        {
            "subject": "Introduction: {sender}",
            "body": """Dear {recipient},

I hope this email finds you well. My name is {sender}, and I wanted to take a moment to introduce myself.

I am currently working as a {role} at {company}, specializing in {skills}. I have a passion for innovation and problem-solving, and I am always eager to explore new opportunities for collaboration.

I believe that our interests align, and I would love to connect with you to exchange ideas and insights. Please let me know if you would be open to a conversation.

Looking forward to hearing from you.

Best regards,  
{sender}
            """
        }
    ],
    "invitation": [
        {
            "subject": "You’re Invited to {event}!",
            "body": """Dear {recipient},

I am excited to invite you to {event}, which is scheduled for {date} at {location}. This event promises to be a valuable experience, featuring insightful discussions, networking opportunities, and engaging activities.

Your presence would mean a lot, and I believe you will find the event both enjoyable and beneficial. Please let me know if you can attend, and feel free to reach out if you have any questions.

Looking forward to your response.

Best regards,  
{sender}
            """
        }
    ],
    "recommendation": [
        {
            "subject": "Strong Recommendation for {person}",
            "body": """Dear {recipient},

I am pleased to write this recommendation for {person} regarding {opportunity}. Having worked closely with {person}, I have witnessed their exceptional skills, dedication, and professionalism.

{person} has consistently demonstrated a strong work ethic and an ability to handle complex challenges with ease. Their contributions have been instrumental in achieving remarkable results, and I have no doubt that they will bring the same level of excellence to {opportunity}.

Please feel free to contact me if you require any additional information.

Best regards,  
{sender}
            """
        }
    ],
    "friendly": [
        {
            "subject": "Catching Up – Let’s Connect!",
            "body": """Hey {recipient},

It’s been a while, and I just wanted to check in to see how you’re doing! I hope everything is going great with you.

Life has been busy on my end, but I’ve been meaning to catch up. Let’s plan a time to meet up soon—it would be great to hear about everything you’ve been up to!

Let me know when you’re free, and we’ll set something up.

Take care,  
{sender}
            """
        }
    ]
}

def generate_email(template_type, recipient, sender, **kwargs):
    if template_type not in TEMPLATES:
        return {"subject": "Invalid Email Type", "body": "The selected email type is not available."}
    
    template = random.choice(TEMPLATES[template_type])
    
    return {
        "subject": template["subject"].format(recipient=recipient, sender=sender, **kwargs),
        "body": template["body"].format(recipient=recipient, sender=sender, **kwargs)
    }
