Summary:	5250 Telnet protocol and Terminal
Summary(pl):	Obs�uga protoko�u i terminal Telnet 5250
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
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
Requires(post):	/sbin/ldconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
tn5250 is an implementation of the 5250 Telnet protocol. It provide
5250 library and 5250 terminal emulation.

%description -l pl
tn5250 to implementacja protoko�u Telnet 5250. Zawiera bibliotek� 5250
i emulator terminala 5250.

%package devel
Summary:	Development tools for 5250 protocol
Summary(pl):	Pakiet dla programisty protoko�u 5250
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name} = %{version}

%description devel
Header files to use lib5250.

%description devel -l pl
Pliki nag��wkowe do korzystania z lib5250.

%package static
Summary:	Static libraries for 5250 protocol
Summary(pl):	Statyczne biblioteki do protoko�u 5250
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	����������/����������
Group(uk):	��������/��̦�����
Requires:	%{name}-devel = %{version}

%description static
Static libraries to use lib5250.

%description static -l pl
Statyczne biblioteki lib5250.

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
CFLAGS="%{rpmcflags} -I/usr/include/ncurses"
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
