Summary:	5250 Telnet protocol and Terminal
Name:		tn5250
Version:	0.16.1
Release:	3
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
Url:		http://www.blarg.net/~mmadore/5250.html 
Source0:	http://www.nacs.net/~jasonf/%{name}-%{version}.tar.gz
Patch0:		%{name}-updates_to_0.16.1.patch
Patch1:		%{name}-ncurses.patch
BuildRequires:	ncurses-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tn5250 is an implementation of the 5250 Telnet protocol. It provide
5250 library and 5250 terminal emulation.

%package devel
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Summary:	development tools for 5250 protocol.

%description devel
Libraires and include to use lib5250.

%package static
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Summary:	static libraries for 5250 protocol.

%description static
Static libraires to use lib5250.

%prep
%setup -q 
%patch0 -p1
%patch1 -p1

%build
libtoolize -c -f
aclocal
autoheader
automake -a -c
autoconf
%define	rpmcflags	%{?debug:%debugcflags}%{!?debug:%optflags} -I/usr/include/ncurses
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install linux/5250.tcap $RPM_BUILD_ROOT%{_datadir}/%{name}
install linux/5250.terminfo $RPM_BUILD_ROOT%{_datadir}/%{name}
#install linux/*.map $RPM_BUILD_ROOT%{_datadir}/%{name}
#install Xdefaults $RPM_BUILD_ROOT%{_datadir}/%{name}/xt5250.keys

gzip -9nf AUTHORS ChangeLog INSTALL NEWS README* TODO linux/README

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/tic %{_datadir}/%{name}/5250.terminfo >/dev/null 2>&1 
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz linux/README.gz
%attr(755,root,root) %{_bindir}/*5250
%attr(755,root,root) %{_bindir}/*5250d
%attr(755,root,root) %{_bindir}/tn3270d
%attr(755,root,root) %{_bindir}/scs2ascii
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_bindir}/*-config
%{_includedir}/*
%{_datadir}/aclocal/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
