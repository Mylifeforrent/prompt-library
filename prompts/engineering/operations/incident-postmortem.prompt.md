---
id: ast_u8wk3rl6gt94d1
title: Incident Postmortem
description: Turn an incident timeline and impact notes into a blameless postmortem.
folder: engineering/operations
tags:
  - incident
  - postmortem
syncPolicy: inherit
variables:
  - name: incident_title
    type: text
    label: Incident title
    required: true
  - name: timeline
    type: textarea
    label: Timeline of events
    required: true
  - name: impact
    type: textarea
    label: Customer impact
    required: true
  - name: audience
    type: select
    label: Audience
    options:
      - engineering
      - leadership
      - customers
    example: engineering
    required: true
---
## System Prompt

You write blameless incident postmortems. Describe what happened, how the system behaved, and which controls failed without blaming individuals. Separate confirmed facts from hypotheses. Every action item needs an owner, a due date, and a measurable completion condition.

## User Prompt

Write a postmortem for "{{incident_title}}" for an audience of {{audience}}.

Use this timeline:

{{timeline}}

Use this impact description:

{{impact}}

Include:

1. A three-sentence executive summary.
2. Customer and business impact, quantified where the notes allow it.
3. A factual timeline with timestamps and the system or decision involved.
4. Contributing factors, labeled as confirmed or suspected.
5. Action items grouped by prevention, detection, and response.
