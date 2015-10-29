Name: otto		
Version: 0.1.2
Release: 1%{?dist}
Summary: Development and deployment made easy
Group: Development/Tools
License: MPLv2.0
URL: https://ottoproject.io/
# Taken from https://releases.hashicorp.com/otto/0.1.2/otto_0.1.2_linux_amd64.zip	
Source0: otto_0.1.2_linux_amd64.zip

%description
otto is a successor to Vagrant, a tool for managing both development
and deployment environment.

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

%files
%{_bindir}/otto


%changelog
* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.1.2-1
- Initial package
