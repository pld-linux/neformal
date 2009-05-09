Summary:	Neformal is a small Qt/Phonon-based player
Summary(hu.UTF-8):	Neformal egy kicsi Qt/Phonon-alapú lejátszó
Name:		neformal
Version:	3.0.0
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/neformal/%{name}-%{version}.tar.bz2
# Source0-md5:	731a67018559a3f1ef50237b39c404e3
URL:		http://neformal.sourceforge.net/
BuildRequires:	QtGui-devel
BuildRequires:	QtSvg-devel
BuildRequires:	libpng-devel
BuildRequires:	phonon-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Neformal is a small Qt/Phonon-based player without any playlist or
collection support. It provides a useful file manager with the ability
to play file by file. Neformal can keep the bookmarks for the
favourities directories.

%description -l hu.UTF-8
Neformal egy apró Qt/Phonon-alapú lejátszó lejátszási lista és
gyűjtemény nélkül. Egy hasznos fájlkezelőt is biztosít, fájlról fájlra
történő lejátszáshoz. A Neformal képes könyvjelzők nyilvántartására is
a kedvenc könyvtárakról.

%prep
%setup -q
%{__sed} -i 's@\":/icons\/\([^"]*\)@"/usr/share/icons/hicolor/scalable/apps/neformal/\1@' mainwindow.cpp
%{__sed} -i 's@std::\([^(]*\)@\1@' metainf.cpp

%build
qmake-qt4
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir} $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/%{name}
install bin/%{name} $RPM_BUILD_ROOT%{_bindir}
install icons/* $RPM_BUILD_ROOT%{_iconsdir}/hicolor/scalable/apps/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS REDME TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}
