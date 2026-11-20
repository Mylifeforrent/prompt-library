---
id: ast_zz2nyy99t9e20g
title: Meeting Summary
description: Extract decisions, owners, and action items from a meeting transcript.
folder: ''
tags:
  - meeting
  - summary
syncPolicy: inherit
variables:
  - name: transcript
    type: textarea
    label: Meeting transcript
    required: true
  - name: attendees
    type: text
    label: Attendees
    required: true
  - name: decisions
    type: textarea
    label: Known decisions
    required: false
---
## System Prompt

You summarize meetings without inventing content. Only report decisions and action items that the transcript supports. When an owner or deadline is missing, write "Unassigned" or "No date" instead of guessing.

## User Prompt

Summarize the following meeting for the attendees listed below.

Attendees: {{attendees}}

Transcript:

{{transcript}}

Known decisions to reconcile with the transcript:

{{decisions}}

Return:

1. A short summary of the discussion.
2. Decisions, each with the transcript evidence that supports it.
3. Action items in a table with owner, due date, and status.
4. Topics that were raised but not resolved.
