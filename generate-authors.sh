#!/bin/bash
# see also ".mailmap" for how email addresses and names are deduplicated

set -e

SCRIPTDIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
ROOTDIR="$(git -C "$SCRIPTDIR" rev-parse --show-toplevel)"

{
  echo "# This file lists all individuals having contributed content to the repository."
  echo "# DO NOT EDIT"
  echo "# For how it is generated, see \`generate-authors.sh\`"
  echo
  git -C "$ROOTDIR" log --format='%aN <%aE>' | LC_ALL=C.UTF-8 sort -uf
} > "${ROOTDIR}/AUTHORS"

