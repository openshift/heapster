%undefine _missing_build_ids_terminate_build
%define debug_package %{nil}

# %commit is intended to be set by tito. The values in this spec file will not be kept up to date.
%{!?commit:
%global commit 4a0e1af82ff19c1390d671eea1fec8f871d22c0d
}

Name:           heapster

# Version and release information will be automatically managed by CD --
# It will be kept in sync with OCP builds.
Version:        0.2
Release:        1%{?dist}
Summary:        Enables container cluster monitoring and performance analysis for Kubernetes

License:        ASL 2.0
URL:            https://github.com/openshift/heapster
Source0:        https://github.com/openshift/heapster/archive/%{commit}/%{name}-%{version}.tar.gz

BuildRequires:  golang >= %{golang_version}

%description
Heapster enables Container Cluster Monitoring and Performance Analysis for Kubernetes (versions v1.0.6 and higher), and platforms which include it.

%prep
%autosetup

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/bin
install -m 755 myutil $RPM_BUILD_ROOT%{_bindir}

%files
%{_bindir}/heapster

%changelog
