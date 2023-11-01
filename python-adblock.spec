%global srcname adblock

Name:           python-%{srcname}
Version:        0.6.0
Release:        1%{?dist}
Summary:        Python wrapper for Brave's adblocking library

License:        MIT and ASL 2.0
URL:            https://pypi.org/project/adblock/
Source0:        %{pypi_source}

Patch0:         0.patch

BuildRequires:  python3-devel
BuildRequires:  cargo
BuildRequires:  rust
BuildRequires:  rust-std-static
BuildRequires:  maturin
BuildRequires:  unzip

%global _description Python wrapper for Brave's adblocking library, which is \
written in Rust.

%description
%{_description}

%package -n python3-%{srcname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%description -n python3-%{srcname}
%{_description}

%prep
%autosetup -n %{srcname}-%{version}

%build
maturin build --release
unzip -d target/wheels/ target/wheels/%{srcname}-%{version}-*.whl

%install
mkdir -p %{buildroot}/%{python3_sitelib}/
cp -r target/wheels/%{srcname} %{buildroot}/%{python3_sitelib}/
cp -r target/wheels/%{srcname}-%{version}.dist-info  %{buildroot}/%{python3_sitelib}/

%files -n python3-%{srcname}
%license LICENSE-MIT LICENSE-APACHE
%doc README.md CHANGELOG.md
%{python3_sitelib}/%{srcname}-%{version}.dist-info/
%{python3_sitelib}/%{srcname}/

%changelog
* Tue Oct 03 2023 Ismael Puerto <ipuertofreire@gmail.com> - 0.6.0-1
- New upstream release.

* Fri Aug 20 2021 Timothée Floure <fnux@fedoraproject.org> - 0.5.0-1
- New upstream release.

* Sun May 29 2021 Timothée Floure <fnux@fedoraproject.org> - 0.4.4-1
- New upstream release.

* Sun Mar 28 2021 Timothée Floure <fnux@fedoraproject.org> - 0.4.3-1
- Let there be package.
