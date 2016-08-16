Name: packer
Version: 0.10.2
Release: 1%{?dist}
Summary: Create machine and container images for multiple platforms
Group: Development/Tools
License: MPLv2.0
URL: https://www.packer.io/

# Taken from https://releases.hashicorp.com/packer/0.10.2/packer_0.10.2_linux_amd64.zip
Source0: packer_0.10.2_linux_amd64.zip

%description
Packer is a tool for creating machine and container images for
multiple platforms from a single source configuration. 

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

# Rename to packerio since packer conflicts with Fedora
pushd %{buildroot}%{_bindir}
  mv packer packerio
popd

%files
%{_bindir}/*

%changelog
* Mon Oct 10 2016 Allan Lewis <allanlewis99@gmail.com> - 0.10.2-1
- Update to 0.10.2

* Thu May 05 2016 Josef Strzibny <strzibny@strzibny.name> - 0.10.0-1
- Update to 0.10.0

* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.8.6-1
- Initial package
