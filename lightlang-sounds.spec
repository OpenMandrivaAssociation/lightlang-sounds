%define version 0.0.1
%define	rel	1
%define release %mkrel %{rel}

Summary: Dictionary for LightLang
Name: lightlang-sounds
Version:	%{version}
Release:	%{release}
License: GPL2+
Group: Office
URL: http://lightlang.org.ru
Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: lightlang

%description
Sounds for LightLang Dictionary

%prep
%setup -q

%build

%install
%{__rm} -rf %{buildroot}

mkdir %{buildroot}
mkdir -p  %{buildroot}/%{_datadir}/sl
mkdir %{buildroot}/%{_datadir}/sl/sounds/
mkdir %{buildroot}/%{_datadir}/sl/sounds/en
cp -r ./en/* %{buildroot}/%{_datadir}/sl/sounds/en

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)

%{_datadir}/sl/sounds/en/*