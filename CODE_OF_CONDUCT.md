# Code of Conduct

## 1. Our Pledge

We as members, contributors, maintainers, and leaders of this project pledge to make participation in our community a harassment-free experience for everyone, regardless of age, body size, visible or invisible disability, ethnicity, sex characteristics, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, caste, color, religion, or sexual identity and orientation.

This commitment also applies regardless of level of technical experience, familiarity with machine learning or NLP, fluency in English, or access to compute or a GPU.

We pledge to act and interact in ways that contribute to an open, welcoming, diverse, inclusive, and healthy community.

## 2. Our Standards

Examples of behavior that contributes to a positive environment:

- Demonstrating empathy and kindness toward other people.
- Being respectful of differing opinions, viewpoints, and experiences.
- Giving and gracefully accepting constructive feedback.
- Accepting responsibility and apologizing to those affected by our mistakes, and learning from the experience.
- Focusing on what is best not just for us as individuals, but for the overall community.

Examples of unacceptable behavior:

- The use of sexualized language or imagery, and sexual attention or advances of any kind.
- Trolling, insulting or derogatory comments, and personal or political attacks.
- Public or private harassment.
- Publishing others' private information, such as a physical or email address, without their explicit permission.
- Other conduct which could reasonably be considered inappropriate in a professional setting.

## 3. Beginner safety

This project is explicitly for beginners. The most common harm in beginner open-source projects is not abuse — it is condescension. Contributors must be able to ask basic questions and learn without being mocked, dismissed, or made to feel that they do not belong.

Forbidden:

- Responding to a beginner's question with "just Google it", "read the docs", "this is obvious", or any equivalent dismissal. If you do not want to answer, say nothing and let someone else answer.
- Mocking code quality, commit history, branch names, or PR descriptions.
- Reviewing the person instead of the code. Critique the diff, never the contributor.
- Gatekeeping based on ML background. Nobody needs to have trained a transformer before to contribute here.
- Leaving a first-time contributor's PR without any response. Silence is a form of exclusion.

Required:

- Every code review comment must explain *why* the change is requested, not only *what* to change. Include the file, the line, and the reason.
- If you cannot explain why, do not request the change.
- If a first-time contributor's PR is out of scope, say so clearly and point to a stream or issue that fits their interests.

Bad review comment:
> "This is wrong. Read the PyTorch docs."

Good review comment:
> "Line 12 of `backend/model.py` calls `from_pretrained` on the base model ID. We need the fine-tuned one here. See `docs/interfaces.md` for the required model ID. Can you update it and push?"

Bad review comment:
> "Why would you write it like this? This is unreadable."

Good review comment:
> "This function has three nested conditionals. Could we split the validation into a helper? It would make the 400-handling path easier to test. Not blocking — your call."

## 4. Scope

This Code of Conduct applies in all project spaces and whenever an individual is officially representing the project in public spaces.

Project spaces include:

- The GitHub repository: issues, pull requests, reviews, comments, and commit messages.
- Hugging Face Hub: dataset repos, model repos, discussions, and model cards.
- Club communication channels: Discord, Slack, WhatsApp, email, or any channel the club uses for this project.
- In-person events: Hacktoberfest meetups, workshops, and club meetings related to this project.
- Any space where a contributor is acting as a representative of the project.

## 5. Enforcement Responsibilities

Community leaders (maintainers and the project owner) are responsible for clarifying and enforcing this Code of Conduct. They will take appropriate and fair corrective action in response to behavior they deem inappropriate, threatening, offensive, or harmful.

They have the right and responsibility to remove, edit, or reject comments, commits, code, issues, and other contributions that are not aligned with this Code of Conduct. They will communicate reasons for moderation decisions when appropriate.

## 6. Reporting

Primary contact for Code of Conduct reports:

`conduct@YOUR-CLUB.org`

<!-- conduct@YOUR-CLUB.org must be replaced before publishing. -->

If the report concerns a maintainer, an alternative contact is the club president or faculty advisor:

`[club president or faculty advisor contact]`

<!-- [club president or faculty advisor contact] must be replaced before publishing. -->

A report should include:

- What happened.
- Where it happened.
- When it happened.
- Who was involved.
- Links or screenshots, if available.

Reports are seen only by the maintainers handling the report. The reporter's identity is not shared with the reported party unless the reporter agrees.

Maintainers will acknowledge a report within 72 hours and provide a decision within 7 days.

Good-faith reports will never result in retaliation. Retaliation against someone who makes a good-faith report is itself a violation of this Code of Conduct.

## 7. Enforcement Guidelines

| Tier | Community Impact | Consequence |
|---|---|---|
| **Tier 1 — Correction** | Use of inappropriate language or other behavior deemed unprofessional or unwelcome in the community. | A private, written warning from community leaders, providing clarity around the nature of the violation and an explanation of why the behavior was inappropriate. A public apology may be requested. |
| **Tier 2 — Warning** | A violation through a single incident or series of actions. | A warning with consequences for continued behavior. No interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, for a specified period of time. This includes avoiding interactions in community spaces as well as external channels like social media. Violating these terms may lead to a temporary or permanent ban. |
| **Tier 3 — Temporary Ban** | A serious violation of community standards, including sustained inappropriate behavior. | A temporary ban from any sort of interaction or public communication with the community for a specified period of time. No public or private interaction with the people involved, including unsolicited interaction with those enforcing the Code of Conduct, is allowed during this period. Violating these terms may lead to a permanent ban. |
| **Tier 4 — Permanent Ban** | Demonstrating a pattern of violation of community standards, including sustained inappropriate behavior, harassment of an individual, or aggression toward or disparagement of classes of individuals. | A permanent ban from any sort of public interaction within the community. |

## 8. University policy

This project operates under the university's student code of conduct and applicable club rules. Violations may be escalated to the club's faculty advisor or the university's student affairs office. This Code of Conduct does not replace those policies; it supplements them for project-specific spaces.

## 9. Attribution

This Code of Conduct is adapted from the Contributor Covenant, version 2.1, available at https://www.contributor-covenant.org/version/2/1/code_of_conduct.html. Enforcement guidelines were inspired by Mozilla's code of conduct enforcement ladder.