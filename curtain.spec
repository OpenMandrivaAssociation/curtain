Summary:	Show a movable and resizable curtain on the desktop screen
Name:		curtain
Version:	0.3
Release:	4
License:	GPLv3+
Group:		Education
Url:		http://code.google.com/p/ardesia
Source:		http://ardesia.googlecode.com/files/%{name}-%{version}.tar.gz
Patch0:		curtain-desktop-file.patch
Patch1:		curtain-0.3-gtk3tests.patch
BuildRequires:	desktop-file-utils
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)

%description
Curtain is a tool that show a movable and resizable curtain on the desktop
screen. You can use this to hide and show objects on the desktop.

This program has been implemented for educational purposes.

%files -f %{name}.lang
%doc COPYING README NEWS ChangeLog AUTHORS
%{_bindir}/curtain
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/ui/%{name}.glade
%{_datadir}/%{name}/ui/icons/%{name}.*
%{_iconsdir}/%{name}.*
%{_datadir}/pixmaps/%{name}.*
%{_mandir}/man1/%{name}.1.*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
%patch1 -p1 -b .gtk3tests

%build
autoreconf -fi
%configure
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_datadir}/pixmaps
mv %{buildroot}%{_iconsdir}/%{name}.xpm %{buildroot}%{_datadir}/pixmaps/

desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}

