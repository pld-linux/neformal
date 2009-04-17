Summary:	Neformal is a small Qt/Phonon-based player
Summary(hu.UTF-8):	Nefomral egy kicsi Qt/Phonon-alapú lejátszó
Name:		neformal
Version:	1.0.1
Release:	0.1
License:	GPL v3
Group:		X11/Applications/Sound
Source0:	http://dl.sourceforge.net/neformal/%{name}-%{version}.tar.bz2
# Source0-md5:	8650a876d948375e770f3c92c4c370a6
Patch0:		%{name}-icondir.patch
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
%patch0 -p1

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
%doc ChangeLog TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_iconsdir}/hicolor/scalable/apps/%{name}
