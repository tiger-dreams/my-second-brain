#!/bin/bash

# Read blog article using Selenium

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
source "${SCRIPT_DIR}/common.sh"

# Check arguments
if [ $# -lt 1 ]; then
    log_error "Usage: $0 <blog_url>"
    exit 1
fi

URL="$1"

# Validate URL format
if [[ ! "$URL" =~ ^https?:// ]]; then
    log_error "URL must be a valid HTTP/HTTPS URL"
    exit 1
fi

log_info "Reading blog article: $URL"

# Run Python script
python3 "${SCRIPT_DIR}/read_medium.py" "$URL"

if [ $? -eq 0 ]; then
    log_info "✅ Article read successfully" >&2
else
    log_error "❌ Failed to read article" >&2
    exit 1
fi
