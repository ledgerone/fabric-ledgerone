#!/bin/bash -e
#
# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#

# regexes for packages to exclude from unit test
excluded_packages=(
    "github.com/ledgerone/fabric-ledgerone/bccsp/factory" # this package's tests need to be mocked
    "github.com/ledgerone/fabric-ledgerone/bccsp/mocks"
    "github.com/ledgerone/fabric-ledgerone/bddtests"
    "github.com/ledgerone/fabric-ledgerone/build/"
    "github.com/ledgerone/fabric-ledgerone/common/ledger/testutil"
    "github.com/ledgerone/fabric-ledgerone/common/mocks"
    "github.com/ledgerone/fabric-ledgerone/core/chaincode/platforms/car/test" # until FAB-7629 is resolved
    "github.com/ledgerone/fabric-ledgerone/core/deliverservice/mocks"
    "github.com/ledgerone/fabric-ledgerone/core/ledger/kvledger/example"
    "github.com/ledgerone/fabric-ledgerone/core/ledger/kvledger/marble_example"
    "github.com/ledgerone/fabric-ledgerone/core/ledger/testutil"
    "github.com/ledgerone/fabric-ledgerone/core/mocks"
    "github.com/ledgerone/fabric-ledgerone/core/testutil"
    "github.com/ledgerone/fabric-ledgerone/examples"
    "github.com/ledgerone/fabric-ledgerone/orderer/mocks"
    "github.com/ledgerone/fabric-ledgerone/orderer/sample_clients"
    "github.com/ledgerone/fabric-ledgerone/test"
    "github.com/ledgerone/fabric-ledgerone/vendor/"
)

# regexes for packages that must be run serially
serial_packages=(
    "github.com/ledgerone/fabric-ledgerone/gossip"
)

# packages which need to be tested with build tag pluginsenabled
plugin_packages=(
    "github.com/ledgerone/fabric-ledgerone/core/scc"
)

# obtain packages changed since some git refspec
packages_diff() {
    git -C "${GOPATH}/src/github.com/ledgerone/fabric-ledgerone" diff --no-commit-id --name-only -r "${1:-HEAD}" |
        grep '.go$' | grep -Ev '^vendor/|^build/' | \
        sed 's%/[^/]*$%/%' | sort -u | \
        awk '{print "github.com/ledgerone/fabric-ledgerone/"$1"..."}'
}

# "go list" packages and filter out excluded packages
list_and_filter() {
    go list $@ 2>/dev/null | grep -Ev $(local IFS='|' ; echo "${excluded_packages[*]}") || true
}

# remove packages that must be tested serially
parallel_test_packages() {
    echo "$@" | grep -Ev $(local IFS='|' ; echo "${serial_packages[*]}") || true
}

# get packages that must be tested serially
serial_test_packages() {
    echo "$@" | grep -E $(local IFS='|' ; echo "${serial_packages[*]}") || true
}

# "go test" the provided packages. Packages that are not prsent in the serial package list
# will be tested in parallel
run_tests() {
    echo ${GO_TAGS}
    flags="-cover"
    if [ -n "${VERBOSE}" ]; then
      flags="-v -cover"
    fi

    local parallel=$(parallel_test_packages "$@")
    if [ -n "${parallel}" ]; then
        time go test ${flags} -tags "$GO_TAGS" -ldflags "$GO_LDFLAGS" ${parallel[@]} -short -timeout=20m
    fi

    local serial=$(serial_test_packages "$@")
    if [ -n "${serial}" ]; then
        time go test ${flags} -tags "$GO_TAGS" -ldflags "$GO_LDFLAGS" ${serial[@]} -short -p 1 -timeout=20m
    fi
}

# "go test" the provided packages and generate code coverage reports. Until go 1.10 is released,
# profile reports can only be generated one package at a time.
run_tests_with_coverage() {
    # Initialize profile.cov
    for pkg in $@; do
        :> profile_tmp.cov
        go test -cover -coverprofile=profile_tmp.cov -tags "$GO_TAGS" -ldflags "$GO_LDFLAGS" $pkg -timeout=20m
        tail -n +2 profile_tmp.cov >> profile.cov || echo "Unable to append coverage for $pkg"
    done

    # convert to cobertura format
    gocov convert profile.cov | gocov-xml > report.xml
}

main() {
    # default behavior is to run all tests
    local package_spec=${TEST_PKGS:-github.com/ledgerone/fabric-ledgerone/...}

    # extra exclusions for ppc and s390x
    local arch=`uname -m`
    if [ x${arch} == xppc64le -o x${arch} == xs390x ]; then
        excluded_packages+=("github.com/ledgerone/fabric-ledgerone/core/chaincode/platforms/java")
    fi

    # when running a "verify" job, only test packages that have changed
    if [ "${JOB_TYPE}" = "VERIFY" ]; then
        # first check for uncommitted changes
        package_spec=$(packages_diff HEAD)
        if [ -z "${package_spec}" ]; then
            # next check for changes in the latest commit - typically this will
            # be for CI only, but could also handle a committed change before
            # pushing to Gerrit
            package_spec=$(packages_diff HEAD^)
        fi
    fi

    # expand the package spec into an array of packages
    local -a packages=$(list_and_filter ${package_spec})

    if [ -z "${packages}" ]; then
        echo "Nothing to test!!!"
    elif [ "${JOB_TYPE}" = "PROFILE" ]; then
        echo "mode: set" > profile.cov
        run_tests_with_coverage "${packages[@]}"
        GO_TAGS="${GO_TAGS} pluginsenabled" run_tests_with_coverage "${plugin_packages[@]}"
    else
        run_tests "${packages[@]}"
        GO_TAGS="${GO_TAGS} pluginsenabled" run_tests "${plugin_packages[@]}"
    fi
}

main
