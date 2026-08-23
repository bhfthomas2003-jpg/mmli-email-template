#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MMLI Email Template Generator
Builds 22 table-based, inline-CSS, Outlook/Gmail-safe HTML email templates
from one shared skeleton, using per-template content dictionaries.
"""
import os

OUT_DIR = "/home/claude/mmli-email-system/templates"
os.makedirs(OUT_DIR, exist_ok=True)

# ---------------------------------------------------------------------------
# BRAND TOKENS (kept in sync with styles/mmli-design-system.css)
# ---------------------------------------------------------------------------
NAVY_DEEP   = "#0B2545"
NAVY        = "#123B70"
NAVY_LIGHT  = "#1F4E8C"
GOLD        = "#C9A227"
GOLD_LIGHT  = "#E8C860"
GOLD_PALE   = "#F6ECC9"
WHITE       = "#FFFFFF"
BG          = "#F4F6FA"
CARD_BG     = "#F8F9FC"
BORDER      = "#E3E7EF"
TEXT        = "#2B2F38"
TEXT_MUTED  = "#6B7280"

FONT_HEAD = "Georgia, 'Times New Roman', Times, serif"
FONT_BODY = "Arial, Helvetica, sans-serif"

GRADIENT_BAR = f"""
<table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
  <tr><td height="4" style="font-size:4px;line-height:4px;background:{NAVY};background-image:linear-gradient(90deg,{NAVY} 0%,{NAVY_LIGHT} 35%,{GOLD} 70%,{GOLD_LIGHT} 100%);">&nbsp;</td></tr>
</table>"""

def social_row():
    return f"""
              <tr>
                <td align="center" style="padding:18px 24px 0 24px;font-family:{FONT_BODY};font-size:12px;letter-spacing:1px;">
                  <a href="{{{{FACEBOOK_URL}}}}" style="color:{GOLD_LIGHT};text-decoration:none;text-transform:uppercase;">Facebook</a>
                  <span style="color:#4A6285;">&nbsp;|&nbsp;</span>
                  <a href="{{{{INSTAGRAM_URL}}}}" style="color:{GOLD_LIGHT};text-decoration:none;text-transform:uppercase;">Instagram</a>
                  <span style="color:#4A6285;">&nbsp;|&nbsp;</span>
                  <a href="{{{{WHATSAPP_URL}}}}" style="color:{GOLD_LIGHT};text-decoration:none;text-transform:uppercase;">WhatsApp</a>
                  <span style="color:#4A6285;">&nbsp;|&nbsp;</span>
                  <a href="{{{{WEBSITE}}}}" style="color:{GOLD_LIGHT};text-decoration:none;text-transform:uppercase;">Website</a>
                </td>
              </tr>"""

def footer_block():
    return f"""
        <!-- FOOTER -->
        <tr>
          <td>
            {GRADIENT_BAR}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{NAVY_DEEP};">
              <tr>
                <td align="center" style="padding:28px 24px 4px 24px;font-family:{FONT_HEAD};font-size:15px;color:{WHITE};letter-spacing:1px;">
                  MIND MASTERS LIBERIA INITIATIVE
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:2px 24px 0 24px;font-family:{FONT_BODY};font-size:11px;color:{GOLD_LIGHT};letter-spacing:2px;text-transform:uppercase;">
                  Home of the Serious Thinkers
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:14px 24px 0 24px;font-family:{FONT_BODY};font-size:12px;line-height:20px;color:#B9C6DC;">
                  {{{{CONTACT_ADDRESS}}}}<br>
                  <a href="mailto:{{{{CONTACT_EMAIL}}}}" style="color:#B9C6DC;text-decoration:underline;">{{{{CONTACT_EMAIL}}}}</a>
                  &nbsp;&middot;&nbsp;
                  <a href="tel:{{{{PHONE}}}}" style="color:#B9C6DC;text-decoration:none;">{{{{PHONE}}}}</a>
                </td>
              </tr>
              {social_row()}
              <tr>
                <td style="padding:20px 24px 0 24px;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td height="1" style="background-color:#22406B;font-size:1px;line-height:1px;">&nbsp;</td></tr></table>
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:16px 24px 28px 24px;font-family:{FONT_BODY};font-size:11px;line-height:18px;color:#7E8FAD;">
                  You are receiving this email because you are part of the MMLI community of educators, students, and partners.<br>
                  &copy; {{{{CURRENT_YEAR}}}} Mind Masters Liberia Initiative. All rights reserved.<br>
                  <a href="{{{{UNSUBSCRIBE_LINK}}}}" style="color:#7E8FAD;text-decoration:underline;">Unsubscribe</a>
                  &nbsp;&middot;&nbsp;
                  <a href="{{{{WEBSITE}}}}" style="color:#7E8FAD;text-decoration:underline;">{{{{WEBSITE}}}}</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>"""

def header_block(eyebrow, title):
    return f"""
        <!-- HEADER -->
        <tr>
          <td>
            {GRADIENT_BAR}
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{NAVY_DEEP};">
              <tr>
                <td align="center" style="padding:32px 24px 12px 24px;">
                  <img src="{{{{LOGO_URL}}}}" width="72" height="72" alt="MMLI Logo" style="display:block;border:0;outline:none;text-decoration:none;border-radius:50%;background-color:{WHITE};" />
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:0 24px;font-family:{FONT_BODY};font-size:11px;letter-spacing:3px;color:{GOLD_LIGHT};text-transform:uppercase;">
                  Mind Masters Liberia Initiative
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:6px 24px 0 24px;font-family:{FONT_BODY};font-size:10px;letter-spacing:2px;color:#8FA3C4;text-transform:uppercase;">
                  Unleashing the Genius Within
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:22px 30px 6px 30px;font-family:{FONT_BODY};font-size:11px;letter-spacing:3px;color:{GOLD};text-transform:uppercase;">
                  {eyebrow}
                </td>
              </tr>
              <tr>
                <td align="center" style="padding:2px 30px 30px 30px;font-family:{FONT_HEAD};font-size:26px;line-height:32px;color:{WHITE};">
                  {title}
                </td>
              </tr>
            </table>
            {GRADIENT_BAR}
          </td>
        </tr>"""

def info_card(rows, title="Details"):
    """rows: list of (label, placeholder) tuples"""
    tr = ""
    for label, ph in rows:
        tr += f"""
                    <tr>
                      <td style="padding:9px 0;font-family:{FONT_BODY};font-size:13px;color:{TEXT_MUTED};width:130px;vertical-align:top;">{label}</td>
                      <td style="padding:9px 0;font-family:{FONT_BODY};font-size:14px;color:{TEXT};font-weight:bold;vertical-align:top;">{ph}</td>
                    </tr>"""
    return f"""
              <tr>
                <td style="padding:4px 0 28px 0;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{CARD_BG};border:1px solid {BORDER};border-left:4px solid {GOLD};border-radius:6px;">
                    <tr>
                      <td style="padding:20px 24px;">
                        <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
                          <tr><td colspan="2" style="padding:0 0 10px 0;font-family:{FONT_BODY};font-size:11px;letter-spacing:2px;color:{NAVY};text-transform:uppercase;font-weight:bold;">{title}</td></tr>
                          {tr}
                        </table>
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>"""

def alert_box(text):
    return f"""
              <tr>
                <td style="padding:0 0 28px 0;">
                  <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:{GOLD_PALE};border:1px solid {GOLD_LIGHT};border-radius:6px;">
                    <tr>
                      <td style="padding:16px 20px;font-family:{FONT_BODY};font-size:13px;line-height:20px;color:{NAVY_DEEP};">
                        {text}
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>"""

def cta_button(label, link_ph, style="primary"):
    if style == "primary":
        bg, color, border = GOLD, NAVY_DEEP, GOLD
    else:
        bg, color, border = NAVY_DEEP, WHITE, GOLD
    return f"""
              <tr>
                <td align="center" style="padding:8px 0 30px 0;">
                  <!--[if mso]>
                  <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" xmlns:w="urn:schemas-microsoft-com:office:word" href="{link_ph}" style="height:48px;v-text-anchor:middle;width:260px;" arcsize="12%" strokecolor="{border}" fillcolor="{bg}">
                  <w:anchorlock/>
                  <center style="color:{color};font-family:{FONT_BODY};font-size:15px;font-weight:bold;">{label}</center>
                  </v:roundrect>
                  <![endif]-->
                  <!--[if !mso]><!-- -->
                  <a href="{link_ph}" target="_blank" style="background-color:{bg};color:{color};border:1px solid {border};font-family:{FONT_BODY};font-size:15px;font-weight:bold;text-decoration:none;padding:14px 36px;border-radius:6px;display:inline-block;">{label}</a>
                  <!--<![endif]-->
                </td>
              </tr>"""

def paragraphs(paras):
    out = ""
    for p in paras:
        out += f"""
              <tr>
                <td style="padding:0 0 18px 0;font-family:{FONT_BODY};font-size:15px;line-height:26px;color:{TEXT};">
                  {p}
                </td>
              </tr>"""
    return out

def signoff(name_ph="{{SENDER_NAME}}", title_ph="{{SENDER_TITLE}}"):
    return f"""
              <tr>
                <td style="padding:6px 0 0 0;font-family:{FONT_BODY};font-size:15px;line-height:24px;color:{TEXT};">
                  Warm regards,<br>
                  <strong>{name_ph}</strong><br>
                  <span style="color:{TEXT_MUTED};font-size:13px;">{title_ph}, Mind Masters Liberia Initiative</span>
                </td>
              </tr>"""

def build_html(preheader, eyebrow, title, greeting, body_rows, doctitle):
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta http-equiv="X-UA-Compatible" content="IE=edge">
<meta name="color-scheme" content="light">
<meta name="supported-color-schemes" content="light">
<title>{doctitle} | MMLI</title>
<!--[if mso]>
<noscript>
<xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml>
</noscript>
<![endif]-->
<style>
  body, table, td, a {{ -webkit-text-size-adjust:100%; -ms-text-size-adjust:100%; }}
  table, td {{ mso-table-lspace:0pt; mso-table-rspace:0pt; }}
  img {{ -ms-interpolation-mode:bicubic; border:0; height:auto; line-height:100%; outline:none; text-decoration:none; }}
  body {{ margin:0; padding:0; width:100% !important; height:100% !important; background-color:{BG}; }}
  a {{ color:{NAVY_LIGHT}; }}
  @media screen and (max-width: 600px) {{
    .mmli-container {{ width:100% !important; max-width:100% !important; }}
    .mmli-px {{ padding-left:20px !important; padding-right:20px !important; }}
    .mmli-stack {{ display:block !important; width:100% !important; }}
    .mmli-btn-full a {{ display:block !important; width:100% !important; text-align:center !important; box-sizing:border-box; }}
    .mmli-h1 {{ font-size:22px !important; line-height:28px !important; }}
  }}
</style>
</head>
<body style="margin:0;padding:0;background-color:{BG};">
<div style="display:none;max-height:0;overflow:hidden;mso-hide:all;font-size:1px;line-height:1px;color:{BG};">{preheader}&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;</div>
<center role="article" aria-roledescription="email" style="width:100%;background-color:{BG};">
<!--[if mso]>
<table role="presentation" width="600" align="center" cellpadding="0" cellspacing="0" border="0"><tr><td>
<![endif]-->
<table role="presentation" class="mmli-container" width="600" align="center" cellpadding="0" cellspacing="0" border="0" style="width:600px;max-width:600px;margin:0 auto;background-color:{WHITE};">
{header_block(eyebrow, title)}
        <!-- BODY -->
        <tr>
          <td class="mmli-px" style="padding:36px 40px 8px 40px;">
            <table role="presentation" width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td style="padding:0 0 18px 0;font-family:{FONT_BODY};font-size:15px;line-height:26px;color:{TEXT};">
                  {greeting}
                </td>
              </tr>
              {body_rows}
            </table>
          </td>
        </tr>
{footer_block()}
</table>
<!--[if mso]>
</td></tr></table>
<![endif]-->
</center>
</body>
</html>
"""

# ---------------------------------------------------------------------------
# TEMPLATE CONTENT DEFINITIONS
# ---------------------------------------------------------------------------
event_card = lambda extra_title="Event Details": info_card([
    ("Event", "{{EVENT_NAME}}"),
    ("Date", "{{EVENT_DATE}}"),
    ("Time", "{{EVENT_TIME}}"),
    ("Venue", "{{VENUE}}"),
], extra_title)

TEMPLATES = []

def add(filename, doctitle, eyebrow, title, preheader, greeting, blocks):
    TEMPLATES.append(dict(filename=filename, doctitle=doctitle, eyebrow=eyebrow, title=title,
                           preheader=preheader, greeting=greeting, blocks=blocks))

# 1. Master Newsletter
add("master-newsletter.html", "MMLI Newsletter", "MMLI Newsletter",
    "The Serious Thinkers Digest",
    "This week at MMLI: programs, results, and opportunities for serious thinkers.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "Welcome to the latest edition of the <strong>MMLI Newsletter</strong>, bringing you news from across our mathematics, science, and Olympiad training community in Liberia.",
        "This issue features program updates, upcoming competitions, and ways for your school or institution to get involved.",
    ]) + info_card([
        ("Featured Program", "{{PROGRAM_NAME}}"),
        ("Next Deadline", "{{DEADLINE_DATE}}"),
        ("Upcoming Event", "{{EVENT_NAME}}"),
    ], "This Issue") + alert_box("<strong>Did you know?</strong> {{FUN_FACT_OR_STAT}}") + cta_button("Read Full Newsletter", "{{WEBSITE}}") + signoff())

# 2. Official Announcement
add("official-announcement.html", "Official Announcement", "Official Announcement",
    "{{ANNOUNCEMENT_TITLE}}",
    "An official announcement from Mind Masters Liberia Initiative.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative (MMLI) is pleased to share the following official announcement with our community of students, educators, and partners.",
        "{{ANNOUNCEMENT_BODY}}",
    ]) + info_card([
        ("Effective Date", "{{EFFECTIVE_DATE}}"),
        ("Applies To", "{{AUDIENCE}}"),
    ], "Announcement Summary") + cta_button("Learn More", "{{WEBSITE}}") + signoff())

# 3. School Invitation
add("school-invitation.html", "School Invitation", "School Partnership",
    "An Invitation for {{SCHOOL_NAME}}",
    "MMLI invites {{SCHOOL_NAME}} to join our STEM and Olympiad training programs.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "On behalf of Mind Masters Liberia Initiative, I am delighted to invite <strong>{{SCHOOL_NAME}}</strong> to partner with us in nurturing mathematics, science, and academic excellence among your students.",
        "MMLI offers Olympiad training, quiz and debate coaching, and access to national and international competitions designed to unleash the genius within every student.",
    ]) + event_card("Invitation Details") + alert_box("Participation is open to schools with students in grades {{GRADE_RANGE}}.") + cta_button("Confirm Your School's Participation", "{{REGISTRATION_LINK}}") + signoff())

# 4. University/Institution Invitation
add("university-invitation.html", "Institution Invitation", "Institutional Partnership",
    "Partnering with {{INSTITUTION_NAME}}",
    "MMLI invites {{INSTITUTION_NAME}} to a strategic academic partnership.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative respectfully invites <strong>{{INSTITUTION_NAME}}</strong> to explore a partnership that advances mathematics, science, and innovation education across Liberia.",
        "We believe a collaboration between our organizations can create meaningful opportunities for students, researchers, and faculty alike.",
    ]) + info_card([
        ("Proposed Focus", "{{PARTNERSHIP_FOCUS}}"),
        ("Proposed Meeting", "{{EVENT_DATE}}"),
        ("Format", "{{MEETING_FORMAT}}"),
    ], "Partnership Overview") + cta_button("Schedule a Discussion", "{{REGISTRATION_LINK}}") + signoff())

# 5. Partnership Proposal
add("partnership.html", "Partnership Proposal", "Partnership Proposal",
    "Building the Future of STEM in Liberia — Together",
    "A formal partnership proposal from Mind Masters Liberia Initiative.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Thank you for your interest in the work of Mind Masters Liberia Initiative. We are writing to formally propose a partnership between <strong>{{ORGANIZATION_NAME}}</strong> and MMLI.",
        "Together, we can expand access to mathematics and science education, Olympiad training, and academic competitions for students across Liberia.",
    ]) + info_card([
        ("Proposed Partnership Type", "{{PARTNERSHIP_TYPE}}"),
        ("Proposed Term", "{{PARTNERSHIP_TERM}}"),
        ("Key Contact", "{{SENDER_NAME}}"),
    ], "Proposal Summary") + alert_box("A detailed partnership brief is attached / linked below for your review.") + cta_button("View Full Proposal", "{{WEBSITE}}") + signoff())

# 6. Sponsorship Request
add("sponsorship.html", "Sponsorship Request", "Sponsorship Request",
    "Invest in Liberia's Serious Thinkers",
    "Support MMLI's mission to unleash the genius within Liberia's youth.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is seeking sponsorship support for <strong>{{PROGRAM_OR_EVENT_NAME}}</strong>, a program designed to strengthen mathematics, science, and academic competition training for Liberian students.",
        "Your organization's support would directly fund training materials, competition travel, and mentorship for talented students who otherwise lack access to these opportunities.",
    ]) + info_card([
        ("Program/Event", "{{PROGRAM_OR_EVENT_NAME}}"),
        ("Funding Goal", "{{FUNDING_GOAL}}"),
        ("Sponsorship Deadline", "{{DEADLINE_DATE}}"),
    ], "Sponsorship Details") + cta_button("View Sponsorship Packages", "{{WEBSITE}}") + signoff())

# 7. Competition Announcement
add("competition.html", "Competition Announcement", "Competition Announcement",
    "{{COMPETITION_NAME}} is Here",
    "MMLI announces {{COMPETITION_NAME}} — register your team today.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is proud to announce <strong>{{COMPETITION_NAME}}</strong>, open to serious thinkers across Liberia.",
        "This competition will test skills in mathematics, science, and critical reasoning, with prizes and recognition for top performers.",
    ]) + event_card("Competition Details") + alert_box("Registration closes on <strong>{{DEADLINE_DATE}}</strong>. Spaces are limited.") + cta_button("Register Now", "{{REGISTRATION_LINK}}") + signoff())

# 8. Competition Registration Invitation
add("registration.html", "Registration Invitation", "Registration Open",
    "You're Invited to Register for {{EVENT_NAME}}",
    "Secure your spot for {{EVENT_NAME}} — registration is now open.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Registration is now open for <strong>{{EVENT_NAME}}</strong>, hosted by Mind Masters Liberia Initiative.",
        "We encourage you to register early, as spaces fill quickly among Liberia's serious thinkers.",
    ]) + event_card("Registration Details") + cta_button("Complete Registration", "{{REGISTRATION_LINK}}") + signoff())

# 9. Olympiad Training Announcement
add("olympiad-training.html", "Olympiad Training", "Olympiad Training Program",
    "{{PROGRAM_NAME}} Begins Soon",
    "Join MMLI's Olympiad training program and sharpen your competitive edge.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is launching <strong>{{PROGRAM_NAME}}</strong>, an intensive training program to prepare students for national and international Olympiad competitions.",
        "Sessions will cover advanced problem-solving in mathematics and science, led by experienced coaches and mentors.",
    ]) + info_card([
        ("Program", "{{PROGRAM_NAME}}"),
        ("Start Date", "{{EVENT_DATE}}"),
        ("Schedule", "{{EVENT_TIME}}"),
        ("Location", "{{VENUE}}"),
    ], "Training Details") + cta_button("Enroll in Training", "{{REGISTRATION_LINK}}") + signoff())

# 10. Teacher/Coach Recruitment
add("teacher-recruitment.html", "Coach Recruitment", "We're Hiring",
    "Become an MMLI Coach or Trainer",
    "MMLI is recruiting passionate teachers and coaches for our Olympiad programs.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is seeking passionate educators and coaches to join our team of trainers for <strong>{{PROGRAM_NAME}}</strong>.",
        "As an MMLI coach, you will mentor Liberia's brightest students in mathematics, science, and academic competition preparation.",
    ]) + info_card([
        ("Role", "{{ROLE_TITLE}}"),
        ("Commitment", "{{TIME_COMMITMENT}}"),
        ("Application Deadline", "{{DEADLINE_DATE}}"),
    ], "Opportunity Details") + cta_button("Apply to Coach", "{{REGISTRATION_LINK}}") + signoff())

# 11. Student Invitation
add("student-invitation.html", "Student Invitation", "You're Invited",
    "Join {{PROGRAM_OR_EVENT_NAME}}, {{FIRST_NAME}}!",
    "An invitation to unleash the genius within — join MMLI today.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "You are personally invited to take part in <strong>{{PROGRAM_OR_EVENT_NAME}}</strong>, hosted by Mind Masters Liberia Initiative.",
        "This is your opportunity to sharpen your skills in mathematics and science, meet fellow serious thinkers, and compete at the highest levels.",
    ]) + event_card("Program Details") + cta_button("Join Now", "{{REGISTRATION_LINK}}") + signoff())

# 12. Event Reminder
add("event-reminder.html", "Event Reminder", "Reminder",
    "{{EVENT_NAME}} is Coming Up",
    "Don't forget — {{EVENT_NAME}} is happening soon.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "This is a friendly reminder that <strong>{{EVENT_NAME}}</strong> is coming up soon. We look forward to your participation.",
    ]) + event_card("Event Reminder") + alert_box("Please arrive 15 minutes early for check-in.") + cta_button("View Event Details", "{{WEBSITE}}") + signoff())

# 13. Deadline Reminder
add("deadline-reminder.html", "Deadline Reminder", "Deadline Approaching",
    "{{DEADLINE_NAME}} Closes Soon",
    "Time is running out to complete {{DEADLINE_NAME}}.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "This is a reminder that the deadline for <strong>{{DEADLINE_NAME}}</strong> is approaching quickly.",
        "Please complete your submission before the deadline to avoid missing this opportunity.",
    ]) + info_card([
        ("Deadline", "{{DEADLINE_DATE}}"),
        ("Time Remaining", "{{TIME_REMAINING}}"),
    ], "Deadline Details") + cta_button("Complete It Now", "{{REGISTRATION_LINK}}") + signoff())

# 14. Program Launch
add("program-launch.html", "Program Launch", "Now Launching",
    "Introducing {{PROGRAM_NAME}}",
    "MMLI proudly launches {{PROGRAM_NAME}}.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is proud to launch <strong>{{PROGRAM_NAME}}</strong>, a new initiative designed to expand opportunities for serious thinkers across Liberia.",
        "{{PROGRAM_DESCRIPTION}}",
    ]) + info_card([
        ("Program", "{{PROGRAM_NAME}}"),
        ("Launch Date", "{{EVENT_DATE}}"),
        ("Who Can Join", "{{AUDIENCE}}"),
    ], "Launch Details") + cta_button("Learn More & Join", "{{REGISTRATION_LINK}}") + signoff())

# 15. Membership Welcome
add("membership-welcome.html", "Membership Welcome", "Welcome to MMLI",
    "Welcome to the MMLI Family, {{FIRST_NAME}}!",
    "Your MMLI membership is confirmed — welcome aboard.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Welcome to <strong>Mind Masters Liberia Initiative</strong>! We are thrilled to have you join our community of serious thinkers.",
        "As a member, you now have access to training programs, competitions, resources, and a network of mathematics and science enthusiasts across Liberia.",
    ]) + info_card([
        ("Membership Type", "{{MEMBERSHIP_TYPE}}"),
        ("Member ID", "{{MEMBER_ID}}"),
        ("Start Date", "{{EVENT_DATE}}"),
    ], "Your Membership") + cta_button("Access Your Member Portal", "{{WEBSITE}}") + signoff())

# 16. Congratulations/Achievement
add("congratulations.html", "Congratulations", "Congratulations",
    "Well Done, {{FIRST_NAME}}!",
    "Congratulations on your achievement with MMLI.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "On behalf of everyone at Mind Masters Liberia Initiative, congratulations on <strong>{{ACHIEVEMENT_DESCRIPTION}}</strong>!",
        "Your hard work and dedication reflect the very spirit of MMLI — unleashing the genius within.",
    ]) + alert_box("<strong>Achievement:</strong> {{ACHIEVEMENT_DESCRIPTION}}<br><strong>Date:</strong> {{EVENT_DATE}}") + cta_button("Share Your Achievement", "{{WEBSITE}}") + signoff())

# 17. Award/Recognition
add("award.html", "Award & Recognition", "Award & Recognition",
    "You Have Been Recognized, {{FIRST_NAME}}",
    "MMLI proudly recognizes your excellence.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "It is with great pride that Mind Masters Liberia Initiative presents you with the <strong>{{AWARD_NAME}}</strong>.",
        "This recognition celebrates your outstanding contribution and commitment to academic excellence.",
    ]) + info_card([
        ("Award", "{{AWARD_NAME}}"),
        ("Awarded For", "{{AWARD_REASON}}"),
        ("Presentation Date", "{{EVENT_DATE}}"),
    ], "Award Details") + cta_button("View Award Details", "{{WEBSITE}}") + signoff())

# 18. Thank You to Sponsors/Partners
add("thank-you.html", "Thank You", "With Gratitude",
    "Thank You, {{FIRST_NAME}} {{LAST_NAME}}",
    "MMLI thanks {{ORGANIZATION_NAME}} for their generous support.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "On behalf of Mind Masters Liberia Initiative, thank you for your generous support of <strong>{{PROGRAM_OR_EVENT_NAME}}</strong>.",
        "Because of partners like <strong>{{ORGANIZATION_NAME}}</strong>, we are able to unleash the genius within more students across Liberia.",
    ]) + alert_box("Your contribution helped us reach <strong>{{IMPACT_METRIC}}</strong> students this term.") + cta_button("See the Impact of Your Support", "{{WEBSITE}}") + signoff())

# 19. Monthly Newsletter
add("monthly-newsletter.html", "Monthly Newsletter", "Monthly Newsletter — {{MONTH_YEAR}}",
    "MMLI Monthly: {{MONTH_YEAR}}",
    "Your monthly round-up from Mind Masters Liberia Initiative.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "Here is your monthly round-up of everything happening at Mind Masters Liberia Initiative for <strong>{{MONTH_YEAR}}</strong>.",
    ]) + info_card([
        ("Students Trained", "{{STUDENTS_TRAINED}}"),
        ("Competitions Held", "{{COMPETITIONS_HELD}}"),
        ("New Partnerships", "{{NEW_PARTNERSHIPS}}"),
    ], "This Month at a Glance") + paragraphs(["<strong>Looking Ahead:</strong> {{UPCOMING_HIGHLIGHTS}}"]) + cta_button("Read the Full Update", "{{WEBSITE}}") + signoff())

# 20. Post-Event Report
add("event-report.html", "Post-Event Report", "Event Report",
    "{{EVENT_NAME}} — Highlights & Results",
    "See how {{EVENT_NAME}} went — highlights and results inside.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Thank you for being part of <strong>{{EVENT_NAME}}</strong>. Here is a summary of how the event unfolded.",
    ]) + info_card([
        ("Attendees", "{{ATTENDEE_COUNT}}"),
        ("Top Performer(s)", "{{TOP_PERFORMERS}}"),
        ("Date Held", "{{EVENT_DATE}}"),
    ], "Event Summary") + paragraphs(["{{EVENT_SUMMARY_TEXT}}"]) + cta_button("View Full Report & Photos", "{{WEBSITE}}") + signoff())

# 21. Academic Resource Announcement
add("academic-resource.html", "Academic Resource", "New Resource Available",
    "New Resource: {{RESOURCE_NAME}}",
    "A new academic resource from MMLI is now available.",
    "Dear {{FIRST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative is pleased to share a new academic resource: <strong>{{RESOURCE_NAME}}</strong>.",
        "{{RESOURCE_DESCRIPTION}}",
    ]) + info_card([
        ("Resource", "{{RESOURCE_NAME}}"),
        ("Subject Area", "{{SUBJECT_AREA}}"),
        ("Format", "{{RESOURCE_FORMAT}}"),
    ], "Resource Details") + cta_button("Access the Resource", "{{REGISTRATION_LINK}}") + signoff())

# 22. International Outreach
add("international-outreach.html", "International Outreach", "International Outreach",
    "MMLI on the Global Stage",
    "MMLI's international outreach and collaboration update.",
    "Dear {{FIRST_NAME}} {{LAST_NAME}},",
    paragraphs([
        "Mind Masters Liberia Initiative continues to build bridges with international partners in support of our mission to unleash the genius within Liberia's youth.",
        "{{OUTREACH_UPDATE_TEXT}}",
    ]) + info_card([
        ("Partner Organization", "{{INTL_PARTNER_NAME}}"),
        ("Country/Region", "{{INTL_PARTNER_REGION}}"),
        ("Collaboration Focus", "{{COLLAB_FOCUS}}"),
    ], "International Collaboration") + cta_button("Read About Our Global Reach", "{{WEBSITE}}") + signoff())

# ---------------------------------------------------------------------------
# RENDER + WRITE FILES
# ---------------------------------------------------------------------------
manifest = []
for t in TEMPLATES:
    html = build_html(t["preheader"], t["eyebrow"], t["title"], t["greeting"], t["blocks"], t["doctitle"])
    path = os.path.join(OUT_DIR, t["filename"])
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    manifest.append({"file": t["filename"], "name": t["doctitle"]})
    print("wrote", path, len(html), "bytes")

print(f"\nTotal templates generated: {len(TEMPLATES)}")
