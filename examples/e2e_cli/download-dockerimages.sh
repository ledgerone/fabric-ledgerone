#!/bin/bash -eu
#
# Copyright IBM Corp. All Rights Reserved.
#
# SPDX-License-Identifier: Apache-2.0
#


##################################################
# This script pulls docker images from ledgerone
# docker hub repository and Tag it as
# ledgerone/fabric-<image> latest tag
##################################################

#Set ARCH variable i.e ppc64le,s390x,x86_64,i386
ARCH=`uname -m`

dockerFabricPull() {
  local FABRIC_TAG=$1
  for IMAGES in peer orderer couchdb ccenv javaenv kafka tools zookeeper; do
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
usage() {
      echo "Description "
      echo
      echo "Pulls docker images from ledgerone dockerhub repository"
      echo "tag as ledgerone/fabric-<image>:latest"
      echo
      echo "USAGE: "
      echo
      echo "./download-dockerimages.sh [-c <fabric-ca tag>] [-f <fabric tag>]"
      echo "      -c fabric-ca docker image tag"
      echo "      -f fabric docker image tag"
      echo
      echo
      echo "EXAMPLE:"
      echo "./download-dockerimages.sh -c x86_64-1.0.0-beta -f x86_64-1.0.0-beta"
      echo
      echo "By default, pulls fabric-ca and fabric 1.0.0-beta docker images"
      echo "from ledgerone dockerhub"
      exit 0
}

while getopts "\?hc:f:" opt; do
  case "$opt" in
     c) CA_TAG="$OPTARG"
        echo "Pull CA IMAGES"
        ;;

     f) FABRIC_TAG="$OPTARG"
        echo "Pull FABRIC TAG"
        ;;
     \?|h) usage
        echo "Print Usage"
        ;;
  esac
done

: ${CA_TAG:="$ARCH-1.0.0-beta"}
: ${FABRIC_TAG:="$ARCH-1.0.0-beta"}

echo "===> Pulling fabric Images"
dockerFabricPull ${FABRIC_TAG}

echo "===> Pulling fabric ca Image"
dockerCaPull ${CA_TAG}
echo
echo "===> List out ledgerone docker images"
docker images | grep ledgerone*
