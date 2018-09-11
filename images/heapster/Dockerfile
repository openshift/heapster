FROM openshift/origin-base

RUN INSTALL_PKGS="origin-heapster" && \
    yum --enablerepo=origin-local-release install -y ${INSTALL_PKGS} && \
    rpm -V ${INSTALL_PKGS} && \
    yum clean all

LABEL io.k8s.display-name="OpenShift Container Platform Heapster" \
      io.k8s.description="This is a component of OpenShift Container Platform which container cluster monitoring" \
      io.openshift.tags="openshift"

# heapster doesn't require root
USER 1001

ENTRYPOINT ["/usr/bin/heapster", "--logtostderr"]
