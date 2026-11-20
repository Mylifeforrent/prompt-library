#!/bin/sh
# Validate a Conventional Commit subject supplied as the first argument.
set -eu

subject=${1:-}
if [ -z "$subject" ]; then
  printf '%s\n' 'usage: validate-subject.sh "type(scope): subject"' >&2
  exit 2
fi

pattern='^(feat|fix|docs|refactor|test|chore|perf|build|ci)(\([a-z0-9._/-]+\))?!?: .+'
if ! printf '%s\n' "$subject" | grep -Eq "$pattern"; then
  printf '%s\n' 'error: subject must match type(scope): summary' >&2
  exit 1
fi

if [ "${#subject}" -gt 72 ]; then
  printf '%s\n' 'error: subject exceeds 72 characters' >&2
  exit 1
fi

case "$subject" in
  *.)
    printf '%s\n' 'error: subject must not end with a period' >&2
    exit 1
    ;;
esac

printf '%s\n' 'ok'
