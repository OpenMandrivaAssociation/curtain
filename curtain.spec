Name:		curtain
Summary:	Resizable curtain on the desktop screen
Version:	0.3
Release:	%mkrel 1
Source0:	http://ardesia.googlecode.com/files/%{name}-%{version}.tar.gz
URL:		http://code.google.com/p/ardesia
Group:		Education
License:	GPLv3
BuildRequires:	gcc make automake libtool
BuildRequires:	freetype intltool
BuildRequires:	gtk+3-devel
Requires:	freetype gtk+2.0


%description
Curtain is a tool that show a movable and resizable curtain
on the desktop screen
You can use this to hide and show objects on the desktop
This program has been implemented for educational purposes

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std XDG_UTILS=""
%find_lang %{name}

%files -f %{name}.lang
%doc AUTHORS README COPYING NEWS
%{_bindir}/%name
%{_datadir}/%{name}/ui/*.glade
%{_datadir}/%{name}/ui/icons/*
%{_datadir}/icons/%name.xpm
%{_datadir}/icons/%name.ico
%{_datadir}/applications/%name.desktop
#% {_datadir}/locale/*
%{_mandir}/man1/%name.*
