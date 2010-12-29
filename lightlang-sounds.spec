# $Id: lightlang.spec $
# Authority: akdengi
# Upstream: lightlang.org.ru

%define version 0.0.1
%define	rel	1
%define release %mkrel %{rel}

%{?dist: %{expand: %%define %dist 1}}

Summary: Dictionary for LightLang
Name: lightlang-sounds
Version:	%{version}
Release:	%{release}
License: GPL
Group: Applications/Office
URL: http://lightlang.org.ru

Packager: Alexander Kazantcev <kazancas@mandriva.ru>
Vendor: EduMandriva <www.edumandriva.ru>

Source: %{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: lightlang

%description
Sounds for LightLang
Звуки для LightLang

%prep
%setup

%{__rm} -rf %{buildroot}

mkdir %{buildroot}
mkdir %{buildroot}/usr
mkdir %{buildroot}/usr/share
mkdir %{buildroot}/usr/share/sl
mkdir %{buildroot}/usr/share/sl/sounds/
mkdir %{buildroot}/usr/share/sl/sounds/en
cp -r ./en/* %{buildroot}/usr/share/sl/sounds/en

%build


%clean
%{__rm} -rf %{buildroot}



%files
%defattr(-, root, root, 0755)

%{_datadir}/sl/sounds/en/*

