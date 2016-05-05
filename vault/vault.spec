Name: vault
Version: 0.5.2
Release: 1%{?dist}
Summary: Tool for securely accessing secrets
Group: Applications/Engineering
License: MPLv2.0
URL: https://vaultproject.io/

# Taken from https://releases.hashicorp.com/vault/0.5.2/vault_0.5.2_linux_amd64.zip
Source0: vault_0.5.2_linux_amd64.zip

%description
Vault secures, stores, and tightly controls access to tokens, passwords,
certificates, API keys, and other secrets in modern computing. 

%prep

%build

%install
mkdir -p %{buildroot}%{_bindir}
unzip -o %{SOURCE0} -d %{buildroot}%{_bindir}

%files
%{_bindir}/vault

%changelog
* Thu May 05 2016 Josef Strzibny <strzibny@strzibny.name> - 0.5.2-1
- Update to 0.5.2

* Tue Oct 27 2015 Josef Stribny <jstribny@redhat.com> - 0.3.1-1
- Initial package
