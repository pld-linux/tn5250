Summary:	5250 Telnet protocol and Terminal
Summary(pl):	Obs³uga protoko³u i terminal Telnet 5250
Name:		tn5250
Version:	0.16.1
Release:	3
License:	GPL
Group:		Applications/Networking
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/tn5250/%{name}-%{version}.tar.gz
Patch0:		%{name}-updates_to_0.16.1.patch
Patch1:		%{name}-ncurses.patch
URL:		http://tn5250.sourceforge.net/
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
tn5250 to implementacja protoko³u Telnet 5250. Zawiera bibliotekê 5250
i emulator terminala 5250.

%package devel
Summary:	Development tools for 5250 protocol
Summary(pl):	Pakiet dla programisty protoko³u 5250
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files to use lib5250.

%description devel -l pl
Pliki nag³ówkowe do korzystania z lib5250.

%package static
Summary:	Static libraries for 5250 protocol
Summary(pl):	Statyczne biblioteki do protoko³u 5250
Group:		Development/Libraries
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
%{__libtoolize}
aclocal
autoheader
%{__automake}
%{__autoconf}
CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses"
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

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/bin/tic %{_datadir}/%{name}/5250.terminfo >/dev/null 2>&1
/sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog INSTALL NEWS README* TODO linux/README
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
%{_aclocaldir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
