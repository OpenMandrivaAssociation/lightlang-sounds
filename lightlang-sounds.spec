Summary:	Sounds for LightLang Dictionary
Name:		lightlang-sounds
Version:	0.0.1
Release:	3
License:	GPLv2+
Group:		Office
Url:		http://lightlang.org.ru
Source0:	%{name}-%{version}.tar.bz2
Requires:	lightlang
BuildArch:	noarch

%description
Sounds for LightLang Dictionary.

%files
%{_datadir}/sl/sounds/en/*

#----------------------------------------------------------------------------

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}%{_datadir}/sl
mkdir %{buildroot}%{_datadir}/sl/sounds/
mkdir %{buildroot}%{_datadir}/sl/sounds/en
cp -r ./en/* %{buildroot}%{_datadir}/sl/sounds/en

