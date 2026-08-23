#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Builds preview/templates-data.js — embeds every template's raw HTML
(for "Copy HTML" / "Open file") plus a sample-data-filled version
(for the live preview iframe), so the dashboard needs no backend and
no fetch() calls (which fail under file:// CORS rules on phones).
"""
import os, json, re

TPL_DIR = "/home/claude/mmli-email-system/templates"
OUT_JS = "/home/claude/mmli-email-system/preview/templates-data.js"

# Human-readable name + one-line purpose for the dashboard cards
CATALOG = [
    ("master-newsletter.html", "Master MMLI Newsletter", "Flagship newsletter template covering multiple stories in one send."),
    ("official-announcement.html", "Official Announcement", "Formal organization-wide announcements and policy updates."),
    ("school-invitation.html", "School Invitation", "Invite a school to partner with MMLI's programs."),
    ("university-invitation.html", "University/Institution Invitation", "Invite a university or institution into a strategic partnership."),
    ("partnership.html", "Partnership Proposal", "Formal proposal to a prospective partner organization."),
    ("sponsorship.html", "Sponsorship Request", "Request funding or in-kind sponsorship for a program or event."),
    ("competition.html", "Competition Announcement", "Announce a new academic competition and open registration."),
    ("registration.html", "Competition Registration Invitation", "Invite recipients to register for a specific event."),
    ("olympiad-training.html", "Olympiad Training Announcement", "Announce a new Olympiad training program/cohort."),
    ("teacher-recruitment.html", "Teacher/Coach Recruitment", "Recruit teachers and coaches to lead MMLI programs."),
    ("student-invitation.html", "Student Invitation", "Personal invitation for a student to join a program or event."),
    ("event-reminder.html", "Event Reminder", "Reminder email for an upcoming event."),
    ("deadline-reminder.html", "Deadline Reminder", "Reminder that a registration/submission deadline is approaching."),
    ("program-launch.html", "Program Launch", "Announce the launch of a brand-new MMLI program."),
    ("membership-welcome.html", "Membership Welcome", "Welcome new members immediately after signup."),
    ("congratulations.html", "Congratulations / Achievement", "Congratulate a student or partner on an achievement."),
    ("award.html", "Award / Recognition", "Formally recognize an individual or institution with an award."),
    ("thank-you.html", "Thank You to Sponsors/Partners", "Thank sponsors and partners for their support."),
    ("monthly-newsletter.html", "Monthly MMLI Newsletter", "Recurring monthly round-up of MMLI activity and metrics."),
    ("event-report.html", "Post-Event Report", "Summarize results and highlights after an event concludes."),
    ("academic-resource.html", "Academic Resource Announcement", "Announce a new study guide, resource, or material."),
    ("international-outreach.html", "International Outreach", "Update on MMLI's international partnerships and collaborations."),
]

SAMPLE_DATA = {
    "FIRST_NAME": "Josephine",
    "LAST_NAME": "Kollie",
    "EMAIL": "josephine.kollie@example.com",
    "EVENT_NAME": "MMLI National Mathematics Olympiad",
    "EVENT_DATE": "Saturday, October 17, 2026",
    "EVENT_TIME": "9:00 AM – 1:00 PM GMT",
    "VENUE": "University of Liberia, Fendall Campus, Monrovia",
    "REGISTRATION_LINK": "https://mmli.org/register",
    "WEBSITE": "https://mmli.org",
    "CONTACT_EMAIL": "info@mmli.org",
    "CONTACT_ADDRESS": "Tubman Boulevard, Congo Town, Monrovia, Liberia",
    "PHONE": "+231-770-000-000",
    "FACEBOOK_URL": "https://facebook.com/mmliberia",
    "INSTAGRAM_URL": "https://instagram.com/mmliberia",
    "WHATSAPP_URL": "https://wa.me/231770000000",
    "LOGO_URL": "../assets/logo/mmli-logo.png",
    "CURRENT_YEAR": "2026",
    "UNSUBSCRIBE_LINK": "https://mmli.org/unsubscribe",
    "SENDER_NAME": "Emmanuel B. Boafo",
    "SENDER_TITLE": "Executive Director",
    "SCHOOL_NAME": "B.W. Harris Episcopal School",
    "INSTITUTION_NAME": "University of Liberia",
    "ORGANIZATION_NAME": "Atlas Education Foundation",
    "GRADE_RANGE": "7–12",
    "PARTNERSHIP_FOCUS": "Joint Olympiad training and teacher development",
    "MEETING_FORMAT": "Virtual (Zoom) or in-person in Monrovia",
    "PARTNERSHIP_TYPE": "Program Co-Delivery Partnership",
    "PARTNERSHIP_TERM": "2026 – 2027 Academic Year",
    "PROGRAM_OR_EVENT_NAME": "MMLI Olympiad Training Program",
    "FUNDING_GOAL": "$15,000 USD",
    "DEADLINE_DATE": "September 30, 2026",
    "COMPETITION_NAME": "MMLI National Science Quiz Championship",
    "PROGRAM_NAME": "MMLI Elite Olympiad Track",
    "ROLE_TITLE": "Mathematics Olympiad Coach",
    "TIME_COMMITMENT": "6 hours/week, evenings and weekends",
    "DEADLINE_NAME": "Olympiad Training Enrollment",
    "TIME_REMAINING": "5 days left",
    "PROGRAM_DESCRIPTION": "The program combines weekly problem-solving labs with mentorship from experienced coaches and alumni of past national teams.",
    "AUDIENCE": "Students in grades 7–12 nationwide",
    "MEMBERSHIP_TYPE": "Student Member",
    "MEMBER_ID": "MMLI-2026-04821",
    "ACHIEVEMENT_DESCRIPTION": "placing 1st at the West African Regional Mathematics Olympiad",
    "AWARD_NAME": "MMLI Excellence in Mathematics Award",
    "AWARD_REASON": "Outstanding performance in the 2026 National Science Quiz",
    "IMPACT_METRIC": "2,400+",
    "MONTH_YEAR": "September 2026",
    "STUDENTS_TRAINED": "1,180",
    "COMPETITIONS_HELD": "6",
    "NEW_PARTNERSHIPS": "3 schools, 1 university",
    "UPCOMING_HIGHLIGHTS": "The National Mathematics Olympiad and our first International Outreach Summit are both coming up next month.",
    "ATTENDEE_COUNT": "312 students from 28 schools",
    "TOP_PERFORMERS": "Josephine Kollie (Grade 11), Samuel Toe (Grade 12)",
    "EVENT_SUMMARY_TEXT": "The event featured written and oral rounds across mathematics and physical sciences, closing with an awards ceremony recognizing our top 10 finishers.",
    "RESOURCE_NAME": "MMLI Olympiad Problem Set Vol. 3",
    "RESOURCE_DESCRIPTION": "A curated set of 60 practice problems spanning algebra, geometry, and combinatorics, with full worked solutions.",
    "SUBJECT_AREA": "Mathematics",
    "RESOURCE_FORMAT": "PDF Download",
    "OUTREACH_UPDATE_TEXT": "This quarter, MMLI formalized a new exchange partnership supporting joint training sessions and a shared problem-writing workshop.",
    "INTL_PARTNER_NAME": "Global Quantum Mechanics Challenge",
    "INTL_PARTNER_REGION": "Hamburg, Germany",
    "COLLAB_FOCUS": "Joint Olympiad problem design and ambassador exchange",
    "ANNOUNCEMENT_TITLE": "2026–2027 Academic Calendar Released",
    "ANNOUNCEMENT_BODY": "The full calendar of MMLI programs, training sessions, and competitions for the 2026–2027 academic year is now available.",
    "EFFECTIVE_DATE": "September 1, 2026",
    "FUN_FACT_OR_STAT": "MMLI-trained students have represented Liberia at 3 international Olympiads since 2023.",
}

def fill(html: str) -> str:
    def repl(m):
        key = m.group(1)
        return SAMPLE_DATA.get(key, m.group(0))
    return re.sub(r"\{\{([A-Z0-9_]+)\}\}", repl, html)

entries = []
for filename, name, purpose in CATALOG:
    path = os.path.join(TPL_DIR, filename)
    raw = open(path, encoding="utf-8").read()
    preview_html = fill(raw)
    entries.append({
        "id": filename.replace(".html", ""),
        "file": filename,
        "name": name,
        "purpose": purpose,
        "raw": raw,
        "preview": preview_html,
    })

with open(OUT_JS, "w", encoding="utf-8") as f:
    f.write("// Auto-generated by build_preview_data.py — do not hand-edit.\n")
    f.write("const MMLI_TEMPLATES = ")
    f.write(json.dumps(entries, ensure_ascii=False))
    f.write(";\n")

print(f"Wrote {OUT_JS} ({os.path.getsize(OUT_JS)/1024:.1f} KB) with {len(entries)} templates.")
