%define	name	emusic
%define	version	0.0.1
%define release %mkrel 1

%define major 0
%define libname %mklibname %{name} %major
%define libnamedev %mklibname %{name} %major -d

Summary: 	Emusic
Name: 		%{name}
Version: 	%{version}
Release: 	%{release}
License: 	BSD
Group: 		Applications/Music
URL: 		http://www.digital-corner.org/
Source: 	%{name}-%{version}.tar.bz2
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	evas-devel >= 0.9.9.038
BuildRequires:	ecore-devel >= 0.9.9.038, edje-devel >= 0.5.0.038
BuildRequires:	edje >= 0.5.0.038, etk-devel >= 0.1.0.003
Buildrequires:	%{mklibname cdda0}-devel
Buildrequires:	%{mklibname xmms2_0}-devel
Buildrequires:  %{mklibname gstreamer-plugins0.8}-devel, gstreamer0.10-plugins-good
requires: xmms2, edje

%description
Ephoto is an ewl app that is used for sophisticate image viewing.
This package is part of the Enlightenment DR17 desktop shell.

%package -n %libname
Summary: Emusic headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description -n %libname
Headers, static libraries, test programs and documentation for Emotion

%package -n %libnamedev
Summary: Emusic headers, static libraries, documentation and test programs
Group: System Environment/Libraries
Requires: %{name} = %{version}

%description -n %libnamedev
Headers, static libraries, test programs and documentation for Emotion


%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build
./autogen.sh
%configure2_5x --disable-etk
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING NEWS README TODO
%{_bindir}/*

%files -n %libnamedev
%{_libdir}/emusic/*.la
%{_libdir}/emusic/*.a
%{_libdir}/*.a
%{_libdir}/*.la
%{_includedir}/Emusic.h
%{_libdir}/pkgconfig/emusic.pc

%files -n %libname
%defattr(-, root, root)
%{_libdir}/*.so*
%{_libdir}/emusic/*.so

