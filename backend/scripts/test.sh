#!/usr/bin/env bash

set -e
set -x

# Store the original GEL_BRANCH value if it exists
original_gel_branch="${GEL_BRANCH:-}"

branch_name="test-$(date +%s)"
gel branch create "$branch_name"

# n.b. Need to set this environment variable after creating the new branch so
# that the prior `gel branch` command runs on the "current" branch rather than
# the (not yet created) new branch.
export GEL_BRANCH="$branch_name"

# This is like a try/catch block
{
    set +e
    python -m app.configure_auth
    coverage run --source=app -m pytest "$@"
    #coverage report --show-missing
    #coverage html --title "${@-coverage}"
    test_status=$?
    set -e
}

# Restore the original GEL_BRANCH value
if [ -n "$original_gel_branch" ]; then
    export GEL_BRANCH="$original_gel_branch"
else
    unset GEL_BRANCH
fi

# By default, we always drop the branch after the tests run, but you can set
# the TEST_KEEP_TEMP_BRANCH environment variable to keep the branch around for
# debugging.
if [ -z "$TEST_KEEP_TEMP_BRANCH" ]; then
    gel branch drop "$branch_name" --non-interactive
fi

exit $test_status