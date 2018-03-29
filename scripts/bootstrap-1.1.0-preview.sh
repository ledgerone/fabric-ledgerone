#!/bin/bash
#
# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#

export VERSION=1.1.0-preview
export ARCH=$(echo "$(uname -s|tr '[:upper:]' '[:lower:]'|sed 's/mingw64_nt.*/windows/')-$(uname -m | sed 's/x86_64/amd64/g')" | awk '{print tolower($0)}')
#Set MARCH variable i.e ppc64le,s390x,x86_64,i386
MARCH=`uname -m`

dockerFabricPull() {
  local FABRIC_TAG=$1
  for IMAGES in peer orderer couchdb ccenv javaenv kafka zookeeper tools; do
      echo "==> FABRIC IMAGE: $IMAGES"
      echo
      docker pull ledgerone/fabric-$IMAGES:$FABRIC_TAG
      docker tag ledgerone/fabric-$IMAGES:$FABRIC_TAG ledgerone/fabric-$IMAGES
  done
}

dockerCaPull() {
      local CA_TAG=$1
      echo "==> FABRIC CA IMAGE"
      echo
      docker pull ledgerone/fabric-ca:$CA_TAG
      docker tag ledgerone/fabric-ca:$CA_TAG ledgerone/fabric-ca
}

: ${CA_TAG:="$MARCH-$VERSION"}
: ${FABRIC_TAG:="$MARCH-$VERSION"}

echo "===> Downloading platform binaries"
curl https://nexus.ledgerone.org/content/repositories/releases/org/ledgerone/fabric-ledgerone/ledgerone-fabric-ledgerone/${ARCH}-${VERSION}/ledgerone-fabric-${ARCH}-${VERSION}.tar.gz | tar xz

echo "===> Pulling fabric Images"
dockerFabricPull ${FABRIC_TAG}

echo "===> Pulling fabric ca Image"
dockerCaPull ${CA_TAG}
echo
echo "===> List out ledgerone docker images"
docker images | grep ledgerone*
