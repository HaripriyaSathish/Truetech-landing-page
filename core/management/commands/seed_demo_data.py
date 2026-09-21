from django.core.management.base import BaseCommand

from core.models import (
    AutomationSection,
    BpoFeature,
    BpoSection,
    CommitmentStep,
    CommitmentsSection,
    ContactSection,
    CtaBanner,
    FaqItem,
    FaqSection,
    FooterLink,
    HeroFeature,
    HeroSection,
    InfoStripItem,
    NavLink,
    Office,
    OfficesSection,
    ProcessSection,
    ProcessStep,
    Service,
    ServiceLine,
    ServiceLinesSection,
    SiteSettings,
    WhyUsFeature,
    WhyUsSection,
)


class Command(BaseCommand):
    help = "Seeds the database with the real copy from the TrueTechs Figma screenshots (no images — upload those yourself in the admin)."

    def handle(self, *args, **options):
        self.stdout.write("Seeding TrueTechs demo content...")

        site, _ = SiteSettings.objects.get_or_create(
            defaults=dict(
                site_name="TrueTechs",
                logo_subtitle="IT · AUTOMATION · BPO",
                header_cta_label="Get a quote",
                header_cta_url="#contact",
                footer_description="IT infrastructure, automation and business process operations — delivered from Dubai and Chennai.",
                footer_tagline="24/7 monitoring and service desk",
            )
        )

        nav_items = ["Home", "Services", "Why us", "Process", "Offices", "FAQ", "Contact"]
        for i, label in enumerate(nav_items):
            NavLink.objects.get_or_create(label=label, defaults=dict(url="#" + label.lower().replace(" ", "-"), order=i))

        hero, _ = HeroSection.objects.get_or_create(
            heading="Keep your systems running",
            defaults=dict(
                eyebrow_text="IT INFRASTRUCTURE SUPPORT",
                heading_highlight="day and night.",
                description="A 24/7 NOC and service desk watching networks, servers and cloud — so problems get caught on our shift, not in your inbox on Monday morning.",
                primary_cta_label="Get a quote", primary_cta_url="#contact",
                secondary_cta_label="View services", secondary_cta_url="#services",
                stat_value="99.97%", stat_caption="uptime",
            ),
        )
        for i, label in enumerate(["24/7 NOC", "Cloud & M365", "Backup & DR", "Endpoint support"]):
            HeroFeature.objects.get_or_create(label=label, defaults=dict(order=i))

        AutomationSection.objects.get_or_create(
            heading="Put the repetitive work on autopilot.",
            defaults=dict(
                eyebrow_text="AI & AUTOMATION",
                description="Chatbots, RPA, document processing and workflow automation built into the systems your team already uses — not another platform they have to learn.",
                badge_label="Live automation running", badge_tags="AI, RPA, DOC, CRM",
                badge2_title="Workflows automated", badge2_subtitle="Across 4 service lines",
            ),
        )
        services = [
            ("AI chatbots", "monitor", "blue", "Intelligent virtual assistants that handle queries around the clock"),
            ("RPA", "refresh", "orange", "Robotic process automation for repetitive rule-based tasks"),
            ("Document processing", "document", "blue", "Intelligent extraction and classification of unstructured documents"),
            ("CRM automation", "grid", "orange", "Automated lead nurturing, data enrichment and sales workflows"),
        ]
        for i, (title, icon, color, desc) in enumerate(services):
            Service.objects.get_or_create(title=title, defaults=dict(icon_key=icon, icon_color=color, description=desc, order=i))

        CtaBanner.objects.get_or_create(
            heading="Ready to automate?",
            defaults=dict(subheading="We build around your existing systems.", button_label="Get started"),
        )

        BpoSection.objects.get_or_create(
            heading="Give your customers a",
            defaults=dict(
                eyebrow_text="BUSINESS PROCESS OUTSOURCING",
                heading_highlight="team that answers.",
                description="Voice, email, chat and WhatsApp support with the back-office processing behind it — trained people, your scripts, your quality standards.",
                stat_value="24/7", stat_caption="Support coverage",
                badge_label="ACTIVE CHANNELS", badge_value="Voice · Chat · Email",
                tags="Voice, Email, Chat, WhatsApp, 24/7",
            ),
        )
        bpo_features = [
            ("01", "Customer support", "mic", "Voice, email, chat and WhatsApp support teams trained to your standards."),
            ("02", "Back office", "briefcase", "Data processing, document handling and operational administration."),
            ("03", "Claims & billing", "document", "Claims management, invoicing, AP & AR and financial processing."),
            ("04", "Lead generation", "user-plus", "Outbound prospecting, appointment setting and pipeline development."),
        ]
        for i, (num, title, icon, desc) in enumerate(bpo_features):
            BpoFeature.objects.get_or_create(title=title, defaults=dict(number=num, icon_key=icon, description=desc, order=i))

        OfficesSection.objects.get_or_create(
            heading="Dubai for the relationship, Chennai for the engineering.",
            defaults=dict(
                eyebrow_text="WHERE WE WORK FROM",
                description="A working day long enough to cover clients in both directions, and a desk that stays staffed after both offices close.",
                highlight_title="Around the clock",
                highlight_description="Monitoring and the service desk run continuously; project and back-office work follow the shared Dubai–Chennai day.",
                highlight_channels="Voice, Chat, Email",
            ),
        )
        offices = [
            ("HEAD OFFICE", "orange", "Dubai, UAE", "0C40, 1st Floor, Waterfront Market, Al Khaleej Street, Corniche Deira, Dubai, UAE", "GST · UTC+4", "1234567890", "DUBAI"),
            ("DELIVERY CENTRE", "blue", "Chennai, India", "57, 1st floor, Estate main road, Industrial estate, Perungudi 600096", "IST · UTC+5:30", "1234567890", "CHENNAI"),
        ]
        for i, (label, color, city, address, tz, phone, toggle) in enumerate(offices):
            Office.objects.get_or_create(city=city, defaults=dict(label=label, label_color=color, address=address, timezone_label=tz, phone=phone, toggle_label=toggle, order=i))

        WhyUsSection.objects.get_or_create(
            heading="Support measured by what it changes in your operation.",
            defaults=dict(
                eyebrow_text="WHY WORK WITH US",
                description="Technology and process support designed to improve efficiency, productivity and long-term growth.",
                badge_label="One partner", badge_value="8 service lines",
            ),
        )
        whyus_features = [
            ("Reliable expertise", "shield", "blue", "left", "Experienced professionals delivering dependable business and technology support, aligned to your operational goals."),
            ("Cost efficiency", "dollar", "orange", "right", "Lower operational overhead, less manual work and better use of the people you already have."),
            ("Technology-driven", "bolt", "blue", "left", "Modern infrastructure, automation tooling and AI applied where a process is measurably better."),
            ("Faster operations", "clock", "orange", "right", "Streamlined processes and intelligent automation that shorten turnaround across the whole workflow."),
            ("Scalable delivery", "trending-up", "blue", "left", "Add seats, shifts or service lines as you grow, without renegotiating the whole arrangement each time."),
            ("Dedicated support", "users", "orange", "right", "Named contacts, responsive service and a long-term working relationship rather than a ticket queue."),
        ]
        for i, (title, icon, color, col, desc) in enumerate(whyus_features):
            WhyUsFeature.objects.get_or_create(title=title, defaults=dict(icon_key=icon, icon_color=color, column=col, description=desc, order=i))

        CommitmentsSection.objects.get_or_create(
            heading="Three commitments we hold to on every engagement.",
            defaults=dict(eyebrow_text="HOW WE WORK"),
        )
        commitments = [
            ("01", "Scoped, not templated", "Built around your processes, quality standards and systems."),
            ("02", "One point of contact", "Several service lines, one agreement, one accountable team."),
            ("03", "Cover that never sleeps", "Monitoring and service desk run on shift, through the night."),
        ]
        for i, (num, title, desc) in enumerate(commitments):
            CommitmentStep.objects.get_or_create(title=title, defaults=dict(number=num, description=desc, order=i))

        ProcessSection.objects.get_or_create(
            heading="From first assessment to steady state.",
            defaults=dict(eyebrow_text="OUR PROCESS", description="The same six steps whether we take one service line or several."),
        )
        process_steps = [
            ("01", "target", "Assess", "Understand your infrastructure, systems, volumes and the problems you actually want solved."),
            ("02", "nodes", "Plan", "Build a practical solution around those needs — scope, staffing, tooling and service levels."),
            ("03", "link", "Implement", "Deploy the technology and support processes, and run the handover from your team."),
            ("04", "grid", "Monitor", "Watch systems and queues continuously, so issues surface before they reach your customers."),
            ("05", "headset", "Support", "Ongoing assistance across the agreed channels and hours, with named points of contact."),
            ("06", "sparkles", "Optimise", "Improve performance, security and reliability over time — and automate what repetition exposes."),
        ]
        for i, (num, icon, title, desc) in enumerate(process_steps):
            ProcessStep.objects.get_or_create(title=title, defaults=dict(number=num, icon_key=icon, description=desc, order=i))

        ServiceLinesSection.objects.get_or_create(
            heading="Eight service lines, one point of contact.",
            defaults=dict(eyebrow_text="WHAT WE DO", description="Take a single line, or run several under one agreement with the same team behind them."),
        )
        service_lines = [
            ("01", "24/7 IT Infrastructure Support", "grid", "Proactive monitoring and management of your entire IT estate.",
             "24/7 NOC and service desk\nNetwork, server and system monitoring\nAzure, AWS and Google Cloud support\nMicrosoft 365, Exchange, Active Directory\nBackup, disaster recovery, continuity"),
            ("02", "Cyber Security", "shield", "Layered defence for systems, data and uptime.",
             "Endpoint, network and email security\nFirewall management and threat monitoring\nVulnerability assessment and audits\nIdentity and access management, zero trust\nIncident response and compliance support"),
            ("03", "AI & Automation", "grid", "Practical AI built into the systems your teams already use.",
             "AI chatbots and virtual assistants\nRPA and business process automation\nIntelligent document processing\nAI lead qualification and ticket routing\nCRM, sales and marketing automation"),
            ("04", "Technology Services", "monitor", "Broader technology delivery beyond day-to-day IT support.",
             "Cloud migration and architecture\nNetwork design and implementation\nIT strategy and roadmap consulting\nVendor and licence management"),
            ("05", "Application Development", "document", "Custom software built around your existing workflows.",
             "Web and mobile application development\nAPI design and integrations\nLegacy system modernisation\nOngoing maintenance and support"),
            ("06", "HR Solutions", "users", "People operations support that scales with your team.",
             "Recruitment and onboarding support\nPayroll and benefits administration\nHR compliance and documentation\nEmployee helpdesk"),
            ("07", "Financial Solutions", "dollar", "Back-office finance processing handled end to end.",
             "Accounts payable and receivable\nBookkeeping and reconciliation\nInvoicing and collections\nFinancial reporting support"),
            ("08", "BPO Services", "briefcase", "The full business-process outsourcing service line.",
             "Customer support across voice, chat and email\nBack-office data processing\nClaims and billing administration\nLead generation and outbound"),
        ]
        for i, (num, title, icon, desc, bullets) in enumerate(service_lines):
            ServiceLine.objects.get_or_create(title=title, defaults=dict(number=num, icon_key=icon, description=desc, bullets=bullets, order=i))

        faq, _ = FaqSection.objects.get_or_create(
            heading="What clients ask before they start.",
            defaults=dict(
                eyebrow_text="QUESTIONS",
                quote_text="One point of contact for your core operational needs, with consistent quality and measurable results.",
                quote_author="TrueTechs",
            ),
        )
        faq_items = [
            ("How can TrueTechs help my business?", "We combine BPO operations, AI automation and 24/7 IT infrastructure support into one accountable partnership — one point of contact for your core operational needs, with consistent quality and measurable results."),
            ("What BPO services do you offer?", "Customer support (voice, chat, email, WhatsApp), back-office processing, claims and billing, and lead generation — scoped to your standards."),
            ("Do you provide 24/7 customer support?", "Yes — our NOC and service desk run continuously across the shared Dubai–Chennai day, with named points of contact."),
            ("Can you provide customised solutions?", "Every engagement is scoped to your processes, quality standards and technology environment rather than a one-size template."),
            ("What IT support services do you provide?", "24/7 infrastructure monitoring, cyber security, cloud support, Microsoft 365/Active Directory administration, and backup & disaster recovery."),
            ("Do you offer AI automation?", "Yes — AI chatbots, RPA, intelligent document processing, and AI-assisted lead qualification and CRM automation."),
        ]
        for i, (q, a) in enumerate(faq_items):
            FaqItem.objects.get_or_create(question=q, defaults=dict(answer=a, order=i))

        ContactSection.objects.get_or_create(
            heading="Tell us what your operation needs.",
            defaults=dict(
                eyebrow_text="GET IN TOUCH",
                description="Describe the work and we'll come back with scope, staffing and a price.",
                bullets="One point of contact across all service lines\nScoped to your processes and quality standards\n24/7 coverage, no gaps in monitoring",
            ),
        )

        info_strip = [
            ("Dubai — Head Office", "map-pin", "orange", "0C40, 1st Floor, Waterfront Market, Al Khaleej Street, Corniche Deira, Dubai, UAE"),
            ("Chennai — Delivery Centre", "map-pin", "blue", "57, 1st floor, Estate main road, Industrial estate, Perungudi 600096"),
            ("Email", "mail", "blue", "To be confirmed"),
            ("Hours", "clock", "orange", "Service desk 24/7 · Office hours GST and IST"),
        ]
        for i, (title, icon, color, desc) in enumerate(info_strip):
            InfoStripItem.objects.get_or_create(title=title, defaults=dict(icon_key=icon, icon_color=color, description=desc, order=i))

        for i, label in enumerate(["About us", "Services", "Our process", "Offices", "FAQ"]):
            FooterLink.objects.get_or_create(column="quick_links", label=label, defaults=dict(order=i))
        for i, label in enumerate(["IT Infrastructure Support", "Cyber Security", "AI & Automation", "Application Development", "BPO Services"]):
            FooterLink.objects.get_or_create(column="services", label=label, defaults=dict(order=i))

        self.stdout.write(self.style.SUCCESS(
            "Done. All text content is seeded — go to /admin/ to upload the photos for each section "
            "(Hero background, Automation image, BPO image, Office photos, Why Us image, Commitment/Process step "
            "photos, Service Line photos, FAQ image, Contact background) since those weren't included in the zip."
        ))
