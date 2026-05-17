import re
import spacy

class TextExtractor:
    def __init__(self):
        """Initialize the TextExtractor with a spaCy NLP model."""
        self.nlp = spacy.load("en_core_web_sm")
    
    def extract_name(self, text):
        """Extract name from text using NLP entity recognition."""
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                return ent.text
        return None

    def extract_email(self, text):
        """Extract email addresses using regular expression matching."""
        email = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', text)
        return email[0] if email else None

    def extract_mobile_number(self, text):
        """Extract mobile numbers using regular expression matching."""
        phone = re.findall(r'\+\d{1,3}\s?\d{5}\s?\d{5}', text)
        return phone[0] if phone else None

    def extract_degree(self, text):
        """Extract academic degrees from text by searching for specific keywords."""
        degrees = ["Bachelor", "Master", "Bachelor's", "Master's", "PhD"]
        found_degrees = [degree for degree in degrees if degree in text]
        return found_degrees

class ResumeAnalyzer:
    def __init__(self, domains, weights):
        """Initialize the ResumeAnalyzer with domain skills and weights configuration."""
        self.domains = domains
        self.weights = weights
    
    def extract_skills(self, text):
        """Extract skills from text based on domain configurations."""
        skills_found = {}
        for domain, sub_domains in self.domains.items():
            for sub_domain, details in sub_domains.items():
                found_skills = [skill for skill in details["expected"] if skill.lower() in text.lower()]
                if found_skills:
                    if domain not in skills_found:
                        skills_found[domain] = {}
                    skills_found[domain][sub_domain] = {
                        "found": found_skills,
                        "missing": [skill for skill in details["expected"] if skill not in found_skills]
                    }
        return skills_found

    def suggest_domain_and_subdomain(self, skills_found):
        """Suggest domain and sub-domain based on the extracted skills."""
        domain_strength = {domain: sum(len(details['found']) for sub_domain, details in sub_domains.items()) for domain, sub_domains in skills_found.items()}
        sorted_domains = sorted(domain_strength.items(), key=lambda item: item[1], reverse=True)
        top_domain = sorted_domains[0][0] if sorted_domains and sorted_domains[0][1] > 0 else "No clear domain fit"

        if top_domain == "No clear domain fit":
            return (top_domain, None)

        sub_domain_strength = {sub_domain: len(details['found']) for sub_domain, details in skills_found[top_domain].items()}
        sorted_sub_domains = sorted(sub_domain_strength.items(), key=lambda item: item[1], reverse=True)
        top_sub_domain = sorted_sub_domains[0][0] if sorted_sub_domains and sorted_sub_domains[0][1] > 0 else None

        return (top_domain, top_sub_domain)

    def score_resume(self, name, email, mobile_number, degrees, skills_found, domain, sub_domain):
        """Calculate a score for the resume based on extracted data and domain relevance."""
        score = 0
        max_score = 100  # Maximum achievable score
        deductions = max_score // 5  # Each critical section contributes equally

        if name:
            score += deductions
        if email:
            score += deductions
        if mobile_number:
            score += deductions
        if degrees:
            score += deductions
        if domain in skills_found and sub_domain in skills_found[domain]:
            if skills_found[domain][sub_domain]['found']:
                score += deductions
            else:
                score -= deductions
        return score
