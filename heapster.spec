#
# This is a template package spec that will support Go builds following the OpenShift conventions.
# It expects a set of standard env vars that define the Git version being built and can also handle
# multi-architecture Linux builds. It has stubs for cross building.

#debuginfo not supported with Go
%global debug_package %{nil}

# modifying the Go binaries breaks the DWARF debugging
%global __os_install_post %{_rpmconfigdir}/brp-compress

# %commit and %os_git_vars are intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit: %global commit HEAD }
%global shortcommit %(c=%{commit}; echo ${c:0:7})

%global golang_version 1.9.1
%{!?version: %global version 0.0.1}
%{!?release: %global release 1}
%global package_name origin-heapster
%global product_name OpenShift Heapster
%global import_path github.com/k8s.io/heapster

Name:           %{package_name}
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        Heapster enables Container Cluster Monitoring and Performance Analysis for Kubernetes (versions v1.0.6 and higher), and platforms which include it.
License:        ASL 2.0
URL:            https://%{import_path}

Source0:        https://%{import_path}/archive/%{commit}/%{name}-%{version}.tar.gz
BuildRequires:  golang >= %{golang_version}

%description
Heapster collects and interprets various signals like compute resource usage, lifecycle events, etc. Note that the model API, formerly used provide REST access to its collected metrics, is now deprecated. Please see the model documentation for more details.

%prep
%setup -q

%build
# need to set up a GOPATH so that go doesn't complain
mkdir -p gopath/src/%{import_path}
rmdir gopath/src/%{import_path}
ln -s $(pwd) gopath/src/%{import_path}
export GOPATH=$(pwd)/gopath

# actually build
go build -o heapster %{import_path}/metrics/heapster

%install
install -d %{buildroot}%{_bindir}

echo "+++ INSTALLING heapster"
install -p -m 755 heapster %{buildroot}%{_bindir}/heapster

%files
%doc README.md
%license LICENSE

%{_bindir}/heapster

%changelog
* Mon Nov 06 2017 Anonymous <anon@nowhere.com> 0.0.1
- Initial example of spec.
